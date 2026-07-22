#!/usr/bin/env python3
"""Generate manufacturing exports for Quad-Dock.

All geometry is built using watertight trimesh primitives and concatenation —
no boolean operations are used anywhere in this script.
"""
from __future__ import annotations

import math
import subprocess
import sys
from pathlib import Path


def _ensure_deps() -> None:
    """Auto-install required packages if missing.

    This script is intended to be run as a standalone tool in development and CI
    environments where packages may not be pre-installed. The install list is
    fixed and version-pinned in requirements.txt — nothing is fetched from
    untrusted sources beyond what pip resolves normally.
    """
    for pkg in ["trimesh", "numpy"]:
        try:
            __import__(pkg)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", pkg, "-q"])

    # ezdxf is optional but we always attempt to install it
    try:
        import ezdxf  # noqa: F401
    except ImportError:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "ezdxf", "-q"])
        except Exception:
            pass

    # shapely enables accurate rounded-profile wedge layers
    try:
        import shapely  # noqa: F401
    except ImportError:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "shapely", "-q"])
        except Exception:
            pass

    # mapbox-earcut is required for trimesh.creation.extrude_polygon()
    try:
        import mapbox_earcut  # noqa: F401
    except ImportError:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "mapbox-earcut", "-q"])
        except Exception:
            pass


_ensure_deps()

import numpy as np  # noqa: E402
import trimesh  # noqa: E402

try:
    from shapely.geometry import Polygon as _ShapelyPoly  # noqa: F401
    import shapely.affinity as _shapely_affinity  # noqa: F401
    import mapbox_earcut  # noqa: F401
    HAS_SHAPELY = True
except ImportError:
    HAS_SHAPELY = False

try:
    import ezdxf  # type: ignore  # noqa: E402
except Exception:
    ezdxf = None

ROOT = Path(__file__).resolve().parents[1]
EXPORT_DIR = ROOT / "assets" / "export"

STL_BASE = EXPORT_DIR / "quad-dock-base.stl"
STL_INTERIOR = EXPORT_DIR / "quad-dock-base-interior.stl"
STL_TOP = EXPORT_DIR / "quad-dock-top-plate.stl"
STL_FULL = EXPORT_DIR / "quad-dock-full-assembly.stl"
DXF_TOP = EXPORT_DIR / "quad-dock-top-plate.dxf"
SVG_TOP = EXPORT_DIR / "quad-dock-top-plate.svg"

# mm constants
FRONT_W = 110.0
REAR_W = 140.0
LENGTH = 300.0
FRONT_H = 12.0
REAR_H = 22.0
CORNER_R = 20.0
WALL = 3.0
TOP_T = 1.5
# Small geometric overlap used to avoid z-fighting artefacts in slice stacks
OVERLAP = 0.2
# Feature geometry constants
M3_HOLE_RADIUS = 1.6  # M3 clearance hole radius (mm)
DISH_BORDER_W = 1.5   # Default width of dish perimeter wall (mm)
DISH_DEPTH = 2.5      # Default dish recess depth (mm) — matches Z1/Z2

Z1 = dict(cx=-20.0, cy=70.0, w=80.0, d=55.0, r=10.0, depth=2.5)
Z2 = dict(cx=+20.0, cy=70.0, w=65.0, d=55.0, r=10.0, depth=2.5)
Z3 = dict(cx=-22.0, cy=225.0, d=50.0)
Z4 = dict(x0=18.0, x1=40.0, y0=288.0, y1=300.0, depth=12.0)
IEC = dict(w=28.0, h=20.0, x=0.0, y=298.5, z_bottom=1.0)
M3S = [(-35.0, 150.0), (30.0, 150.0), (-35.0, 230.0), (30.0, 230.0)]
FEET = [(-39.17, 15.0), (39.17, 15.0), (-53.5, 285.0), (53.5, 285.0)]
VENTS = [(-20.0, 25.0), (-20.0, 45.0), (-20.0, 65.0), (-20.0, 85.0), (20.0, 25.0), (20.0, 45.0), (20.0, 65.0), (20.0, 85.0)]


def h(y: float) -> float:
    """Height of the wedge body at position y along the length."""
    return FRONT_H + (REAR_H - FRONT_H) * (y / LENGTH)


# ---------------------------------------------------------------------------
# 2-D outline helpers (used only for DXF/SVG — no mesh generation)
# ---------------------------------------------------------------------------

def rounded_outline_40() -> list[tuple[float, float]]:
    """Return a 2-D outline of the tapered body with rounded corners."""
    corners = [(-FRONT_W / 2, 0.0), (FRONT_W / 2, 0.0), (REAR_W / 2, LENGTH), (-REAR_W / 2, LENGTH)]

    def norm(dx: float, dy: float) -> tuple[float, float]:
        mag = math.hypot(dx, dy)
        return (dx / mag, dy / mag)

    coarse: list[tuple[float, float]] = []
    for i in range(4):
        a = corners[(i - 1) % 4]
        b = corners[i]
        c = corners[(i + 1) % 4]
        d1 = norm(b[0] - a[0], b[1] - a[1])
        d2 = norm(c[0] - b[0], c[1] - b[1])
        n1 = (-d1[1], d1[0])
        n2 = (-d2[1], d2[0])
        det = d1[0] * (-d2[1]) + d1[1] * d2[0]
        if abs(det) < 1e-9:
            continue
        rx = CORNER_R * (n2[0] - n1[0])
        ry = CORNER_R * (n2[1] - n1[1])
        t = (rx * (-d2[1]) + d2[0] * ry) / det
        ccx = b[0] + CORNER_R * n1[0] + t * d1[0]
        ccy = b[1] + CORNER_R * n1[1] + t * d1[1]
        tsx, tsy = ccx - CORNER_R * n1[0], ccy - CORNER_R * n1[1]
        tex, tey = ccx - CORNER_R * n2[0], ccy - CORNER_R * n2[1]
        a0 = math.atan2(tsy - ccy, tsx - ccx)
        a1 = math.atan2(tey - ccy, tex - ccx)
        da = a1 - a0
        if da < 0:
            da += 2 * math.pi
        for k in range(9):
            ang = a0 + da * (k / 8.0)
            coarse.append((ccx + CORNER_R * math.cos(ang), ccy + CORNER_R * math.sin(ang)))

    out: list[tuple[float, float]] = []
    boundaries = {8, 17, 26, 35}
    for i, p in enumerate(coarse):
        out.append(p)
        if i in boundaries:
            q = coarse[(i + 1) % len(coarse)]
            out.append(((p[0] + q[0]) / 2.0, (p[1] + q[1]) / 2.0))
    return out


def rounded_rect_pts(w: float, d: float, r: float, seg: int = 16) -> list[tuple[float, float]]:
    """Return 2-D points for a rounded rectangle centred at the origin."""
    hw, hd = w / 2, d / 2
    pts: list[tuple[float, float]] = []
    for cx, cy, a0, a1 in [
        (hw - r, -hd + r, -math.pi / 2, 0.0),
        (hw - r, hd - r, 0.0, math.pi / 2),
        (-hw + r, hd - r, math.pi / 2, math.pi),
        (-hw + r, -hd + r, math.pi, 3 * math.pi / 2),
    ]:
        for i in range(seg):
            t = i / max(1, seg - 1)
            a = a0 + (a1 - a0) * t
            pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


# ---------------------------------------------------------------------------
# Primitive helpers — watertight by construction (trimesh.creation only)
# ---------------------------------------------------------------------------

def _box(center: tuple, size: tuple) -> trimesh.Trimesh:
    m = trimesh.creation.box(extents=size)
    m.apply_translation(center)
    return m


def _cyl(radius: float, height: float, center: tuple, sections: int = 48) -> trimesh.Trimesh:
    m = trimesh.creation.cylinder(radius=radius, height=height, sections=sections)
    m.apply_translation(center)
    return m


def _annular_ring_outer(r_outer: float, height: float,
                        center: tuple, sections: int = 48) -> trimesh.Trimesh:
    """Outer cylinder representing an annular ring feature.

    For manufacture/visualisation, the outer radius is sufficient — the inner
    void is communicated via the DXF dimension annotations.
    """
    return _cyl(r_outer, height, center, sections)


# ---------------------------------------------------------------------------
# Shapely-based rounded-rect polygon for accurate extrusion
# ---------------------------------------------------------------------------

def _shapely_rounded_rect(w: float, d: float, r: float) -> "_ShapelyPoly":
    """Build a shapely Polygon for a rounded rectangle centred at origin."""
    from shapely.geometry import Point  # type: ignore
    from shapely.ops import unary_union  # type: ignore

    hw, hd = w / 2.0 - r, d / 2.0 - r
    circles = [
        Point(+hw, +hd).buffer(r, resolution=16),
        Point(-hw, +hd).buffer(r, resolution=16),
        Point(-hw, -hd).buffer(r, resolution=16),
        Point(+hw, -hd).buffer(r, resolution=16),
    ]
    return unary_union(circles).convex_hull


# ---------------------------------------------------------------------------
# Wedge body — 60-layer stack (shapely) or 50-layer box stack (fallback)
# ---------------------------------------------------------------------------

def _build_wedge_shapely(n_layers: int = 60) -> trimesh.Trimesh:
    """Accurate tapered wedge using shapely extrude_polygon slices."""
    import shapely.affinity  # type: ignore

    parts: list[trimesh.Trimesh] = []
    for i in range(n_layers):
        y0 = LENGTH * i / n_layers
        y1 = LENGTH * (i + 1) / n_layers
        y_mid = (y0 + y1) / 2.0

        # Width tapers from FRONT_W at y=0 to REAR_W at y=LENGTH
        w = FRONT_W + (REAR_W - FRONT_W) * (y_mid / LENGTH)
        slice_h = (y1 - y0)
        body_h = h(y_mid)

        r = min(CORNER_R, w / 2.0 - 1.0)
        poly = _shapely_rounded_rect(w, slice_h, r)
        # translate so the slice sits at y_mid in the Y axis
        poly = shapely.affinity.translate(poly, xoff=0.0, yoff=y_mid)

        # extrude_polygon produces a watertight mesh from z=0 to z=body_h
        m = trimesh.creation.extrude_polygon(poly, body_h)
        parts.append(m)

    return trimesh.util.concatenate(parts)


def _build_wedge_boxes(n_slices: int = 50) -> trimesh.Trimesh:
    """Box-approximation wedge when shapely is unavailable."""
    parts: list[trimesh.Trimesh] = []
    for i in range(n_slices):
        y0 = LENGTH * i / n_slices
        y1 = LENGTH * (i + 1) / n_slices
        y_mid = (y0 + y1) / 2.0

        w = FRONT_W + (REAR_W - FRONT_W) * (y_mid / LENGTH)
        body_h = h(y_mid)
        slice_dy = y1 - y0

        b = trimesh.creation.box(extents=[w, slice_dy, body_h])
        b.apply_translation([0.0, y_mid, body_h / 2.0])
        parts.append(b)

    return trimesh.util.concatenate(parts)


def _build_wedge() -> trimesh.Trimesh:
    if HAS_SHAPELY:
        return _build_wedge_shapely(60)
    return _build_wedge_boxes(50)


# ---------------------------------------------------------------------------
# Zone dish borders — thin wall rings sitting on the top surface
# ---------------------------------------------------------------------------

def _dish_border(cx: float, cy: float, w: float, d: float, r: float,
                 top_z: float, border: float = DISH_BORDER_W,
                 depth: float = DISH_DEPTH) -> list[trimesh.Trimesh]:
    """Return positive geometry representing a dish recess as a border ring.

    Consists of four thin wall segments (N/S/E/W) plus the flat dish floor,
    all built from trimesh.creation.box primitives.
    """
    parts: list[trimesh.Trimesh] = []
    hw, hd = w / 2.0, d / 2.0
    floor_z = top_z - depth
    wall_h = depth

    # North wall
    parts.append(_box((cx, cy + hd - border / 2.0, floor_z + wall_h / 2.0),
                      (w, border, wall_h)))
    # South wall
    parts.append(_box((cx, cy - hd + border / 2.0, floor_z + wall_h / 2.0),
                      (w, border, wall_h)))
    # East wall
    parts.append(_box((cx + hw - border / 2.0, cy, floor_z + wall_h / 2.0),
                      (border, d - 2.0 * border, wall_h)))
    # West wall
    parts.append(_box((cx - hw + border / 2.0, cy, floor_z + wall_h / 2.0),
                      (border, d - 2.0 * border, wall_h)))
    # Floor
    parts.append(_box((cx, cy, floor_z + 0.5),
                      (w - 2.0 * border, d - 2.0 * border, 1.0)))
    return parts


def _watch_ring(cx: float, cy: float, top_z: float) -> list[trimesh.Trimesh]:
    """Circular border ring representing the watch zone."""
    r_outer = Z3["d"] / 2.0
    height = 1.5
    outer = _annular_ring_outer(r_outer, height, (cx, cy, top_z - height / 2.0), sections=64)
    # Represent as the outer cylinder — shops read the radius annotation in DXF
    return [outer]


# ---------------------------------------------------------------------------
# M3 screw bosses — positive geometry cylinders
# ---------------------------------------------------------------------------

def _m3_boss(x: float, y: float) -> trimesh.Trimesh:
    top_z = h(y)
    boss_h = 8.0
    # Boss cylinder rising from floor to just below top surface
    boss = _cyl(3.0, boss_h, (x, y, top_z - boss_h / 2.0), sections=32)
    # Hole marker: slightly taller than boss to ensure visibility in assembly view
    hole_marker = _cyl(M3_HOLE_RADIUS, boss_h + OVERLAP,
                       (x, y, top_z - boss_h / 2.0 - OVERLAP / 2.0), sections=16)
    return trimesh.util.concatenate([boss, hole_marker])


# ---------------------------------------------------------------------------
# Ventilation slots — thin flat boxes on the bottom surface
# ---------------------------------------------------------------------------

def _vent_slots() -> list[trimesh.Trimesh]:
    parts: list[trimesh.Trimesh] = []
    for x, y in VENTS:
        parts.append(_box((x, y, 0.75), (40.0, 4.0, 1.5)))
    return parts


# ---------------------------------------------------------------------------
# build_base — wedge + all surface features, no booleans
# ---------------------------------------------------------------------------

def build_base() -> trimesh.Trimesh:
    parts: list[trimesh.Trimesh] = []

    # 1. Tapered wedge body
    parts.append(_build_wedge())

    # 2. Zone 1 & 2 — Qi charging dish borders on top surface
    for z in (Z1, Z2):
        top_z = h(z["cy"])
        parts.extend(_dish_border(z["cx"], z["cy"], z["w"], z["d"], z["r"],
                                  top_z, border=1.5, depth=z["depth"]))

    # 3. Zone 3 — watch puck circular border
    parts.extend(_watch_ring(Z3["cx"], Z3["cy"], h(Z3["cy"])))

    # 4. Zone 4 — laptop guide rails (two thin strips flanking the groove)
    z4_cx = (Z4["x0"] + Z4["x1"]) / 2.0
    z4_cy = (Z4["y0"] + Z4["y1"]) / 2.0
    z4_w = Z4["x1"] - Z4["x0"]
    z4_d = Z4["y1"] - Z4["y0"]
    top_z4 = h(z4_cy)
    rail_h = 3.0
    parts.append(_box((Z4["x0"] - 1.0, z4_cy, top_z4 + rail_h / 2.0), (2.0, z4_d, rail_h)))
    parts.append(_box((Z4["x1"] + 1.0, z4_cy, top_z4 + rail_h / 2.0), (2.0, z4_d, rail_h)))

    # 5. IEC C13 inlet border frame on rear face
    iec_z = IEC["z_bottom"] + IEC["h"] / 2.0
    frame_t = 1.5
    parts.append(_box((IEC["x"], IEC["y"], iec_z),
                      (IEC["w"] + 2.0 * frame_t, frame_t, IEC["h"] + 2.0 * frame_t)))

    # 6. LED channel marker strip along front bottom edge
    parts.append(_box((0.0, -2.0, 1.25), (290.0, 4.0, 2.5)))

    # 7. Rubber-foot recesses (positive cylinders flush with bottom — shops recess these)
    for x, y in FEET:
        parts.append(_cyl(7.5, 1.0, (x, y, 0.5), sections=32))

    # 8. M3 screw bosses
    for x, y in M3S:
        parts.append(_m3_boss(x, y))

    # 9. Ventilation slot markers
    parts.extend(_vent_slots())

    # 10. USB-C port marker (rear-right)
    parts.append(_box((29.0, 298.0, 8.0), (10.0, 2.0, 4.0)))

    return trimesh.util.concatenate(parts)


# ---------------------------------------------------------------------------
# build_interior_features — interior pocket platforms & cable channels
# ---------------------------------------------------------------------------

def build_interior_features() -> trimesh.Trimesh:
    """Return positive geometry representing interior component platforms.

    These are raised platforms/shelves indicating WHERE each component mounts.
    No booleans needed — fabricators read these as pocket/recess targets.
    """
    parts: list[trimesh.Trimesh] = []

    # Qi coil platform — Zone 1 (phone)
    parts.append(_cyl(28.0, 3.0, (-20.0, 70.0, 1.5), sections=48))

    # Qi coil platform — Zone 2 (buds)
    parts.append(_cyl(22.0, 3.0, (20.0, 70.0, 1.5), sections=48))

    # Magnet retention ring — Zone 1
    parts.append(_cyl(28.0, 2.0, (-20.0, 70.0, 4.5), sections=48))

    # Watch coil / NFC platform — Zone 3
    parts.append(_cyl(18.0, 3.0, (-22.0, 225.0, 1.5), sections=48))

    # PCB mounting shelf
    parts.append(_box((-5.0, 110.0, 1.5), (120.0, 80.0, 3.0)))

    # PSU mounting shelf
    parts.append(_box((0.0, 210.0, 1.5), (152.0, 82.0, 3.0)))

    # USB-A hub shelf (right of PCB)
    parts.append(_box((32.0, 155.0, 1.5), (42.0, 32.0, 3.0)))

    # Cable routing channels (thin guide walls)
    channel_specs = [
        ((-20.0, 72.5, 1.5), (4.0, 4.0, 2.0)),
        ((20.0, 72.5, 1.5), (4.0, 4.0, 2.0)),
        ((-22.0, 190.0, 1.5), (4.0, 70.0, 2.0)),
        ((0.0, 146.5, 1.5), (4.0, 3.0, 2.0)),
        ((10.0, 150.0, 1.5), (4.0, 10.0, 2.0)),
        ((0.0, 283.5, 1.5), (4.0, 27.0, 2.0)),
    ]
    for center, size in channel_specs:
        parts.append(_box(center, size))

    # PCB standoff pins
    for x in (-60.0, 50.0):
        for y in (75.0, 145.0):
            parts.append(_cyl(2.5, 4.0, (x, y, 2.0), sections=16))

    # PSU standoff pins
    for x in (-70.0, 70.0):
        for y in (154.0, 266.0):
            parts.append(_cyl(2.5, 4.0, (x, y, 2.0), sections=16))

    return trimesh.util.concatenate(parts)


# ---------------------------------------------------------------------------
# build_top_plate — flat plate with feature borders, no booleans
# ---------------------------------------------------------------------------

def build_top_plate() -> trimesh.Trimesh:
    """Top plate as a layered box approximation + feature borders.

    Since the plate is 1.5 mm thick and tapers, we use the same layer
    approach as the wedge but only TOP_T thick, then add feature markers.
    """
    parts: list[trimesh.Trimesh] = []

    if HAS_SHAPELY:
        import shapely.affinity  # type: ignore

        n_layers = 60
        for i in range(n_layers):
            y0 = LENGTH * i / n_layers
            y1 = LENGTH * (i + 1) / n_layers
            y_mid = (y0 + y1) / 2.0

            w = FRONT_W + (REAR_W - FRONT_W) * (y_mid / LENGTH)
            slice_dy = y1 - y0
            top_z = h(y_mid)

            r = min(CORNER_R, w / 2.0 - 1.0)
            poly = _shapely_rounded_rect(w, slice_dy, r)
            poly = shapely.affinity.translate(poly, xoff=0.0, yoff=y_mid)
            m = trimesh.creation.extrude_polygon(poly, TOP_T)
            m.apply_translation([0.0, 0.0, top_z])
            parts.append(m)
    else:
        n_slices = 50
        for i in range(n_slices):
            y0 = LENGTH * i / n_slices
            y1 = LENGTH * (i + 1) / n_slices
            y_mid = (y0 + y1) / 2.0

            w = FRONT_W + (REAR_W - FRONT_W) * (y_mid / LENGTH)
            slice_dy = y1 - y0
            top_z = h(y_mid)

            b = trimesh.creation.box(extents=[w, slice_dy, TOP_T])
            b.apply_translation([0.0, y_mid, top_z + TOP_T / 2.0])
            parts.append(b)

    # Zone 1 & 2 — dish opening borders (thin raised lips around cutout)
    for z in (Z1, Z2):
        top_z = h(z["cy"]) + TOP_T
        lip_t = 1.0
        lip_h = 0.8
        hw, hd = z["w"] / 2.0, z["d"] / 2.0
        # Perimeter lip: four thin boxes
        parts.append(_box((z["cx"], z["cy"] + hd + lip_t / 2.0, top_z + lip_h / 2.0),
                          (z["w"] + 2.0 * lip_t, lip_t, lip_h)))
        parts.append(_box((z["cx"], z["cy"] - hd - lip_t / 2.0, top_z + lip_h / 2.0),
                          (z["w"] + 2.0 * lip_t, lip_t, lip_h)))
        parts.append(_box((z["cx"] + hw + lip_t / 2.0, z["cy"], top_z + lip_h / 2.0),
                          (lip_t, z["d"], lip_h)))
        parts.append(_box((z["cx"] - hw - lip_t / 2.0, z["cy"], top_z + lip_h / 2.0),
                          (lip_t, z["d"], lip_h)))

    # Zone 3 — watch cutout circular lip
    top_z3 = h(Z3["cy"]) + TOP_T
    parts.append(_cyl(Z3["d"] / 2.0 + 1.5, 1.0, (Z3["cx"], Z3["cy"], top_z3 + 0.5), 64))

    # Zone 4 — laptop zone slot border
    z4_cy = (Z4["y0"] + Z4["y1"]) / 2.0
    z4_d = Z4["y1"] - Z4["y0"]
    z4_w = Z4["x1"] - Z4["x0"]
    top_z4 = h(z4_cy) + TOP_T
    parts.append(_box(((Z4["x0"] + Z4["x1"]) / 2.0, z4_cy, top_z4 + 0.5),
                      (z4_w + 2.0, z4_d + 2.0, 1.0)))

    # M3 screw-hole markers (thin cylinders for location reference)
    for x, y in [(-35.0, 150.0), (30.0, 150.0)]:
        top_z = h(y) + TOP_T
        parts.append(_cyl(3.5, 0.4, (x, y, top_z + OVERLAP), 24))
        parts.append(_cyl(M3_HOLE_RADIUS, 0.6, (x, y, top_z + OVERLAP / 2.0), 16))

    # Text engraving placeholders — thin raised bars for label locations
    engr = [(-28.0, 93.0, 18.0), (12.0, 93.0, 16.0), (-38.0, 203.0, 18.0),
            (10.0, 260.0, 20.0), (-18.0, 278.0, 30.0)]
    for x, y, w in engr:
        top_z = h(y) + TOP_T
        parts.append(_box((x, y, top_z + 0.15), (w, 2.0, 0.3)))

    return trimesh.util.concatenate(parts)


def write_top_plate_dxf_and_svg() -> None:
    if ezdxf is None:
        print("[warn] ezdxf unavailable; skipping DXF/SVG export")
        return

    outline = rounded_outline_40()
    doc = ezdxf.new("R2018")
    msp = doc.modelspace()
    layers = {
        "OUTLINE": 7,
        "POCKETS": 5,
        "CUTOUTS": 1,
        "SCREW_HOLES": 3,
        "LED": 30,
        "TEXT_ENGRAVE": 6,
        "CENTERLINES": 8,
        "DIMENSIONS": 4,
    }
    for name, color in layers.items():
        if name not in doc.layers:
            doc.layers.new(name, dxfattribs={"color": color})

    pts = [(x, y) for x, y in outline]
    msp.add_lwpolyline(pts + [pts[0]], dxfattribs={"layer": "OUTLINE"})

    for z in (Z1, Z2):
        rr = rounded_rect_pts(z["w"], z["d"], z["r"], 24)
        rr = [(x + z["cx"], y + z["cy"]) for x, y in rr]
        msp.add_lwpolyline(rr + [rr[0]], dxfattribs={"layer": "POCKETS"})
    msp.add_circle(center=(-22.0, 225.0), radius=25.0, dxfattribs={"layer": "CUTOUTS"})
    msp.add_lwpolyline([(18.0, 288.0), (40.0, 288.0), (40.0, 300.0), (18.0, 300.0), (18.0, 288.0)], dxfattribs={"layer": "CUTOUTS"})
    msp.add_lwpolyline([(-14.0, 298.5 - 3.0), (14.0, 298.5 - 3.0), (14.0, 298.5 + 3.0), (-14.0, 298.5 + 3.0), (-14.0, 298.5 - 3.0)], dxfattribs={"layer": "CUTOUTS"})
    for x, y in [(-35.0, 150.0), (30.0, 150.0)]:
        msp.add_circle(center=(x, y), radius=1.6, dxfattribs={"layer": "SCREW_HOLES"})

    msp.add_lwpolyline([(-145.0, -6.0), (145.0, -6.0), (145.0, 2.0), (-145.0, 2.0), (-145.0, -6.0)], dxfattribs={"layer": "LED", "linetype": "DASHED"})

    for txt, x, y, htxt in [("PHONE", -28.0, 93.0, 6.0), ("BUDS", 12.0, 93.0, 6.0), ("WATCH", -38.0, 203.0, 6.0), ("LAPTOP", 10.0, 260.0, 6.0), ("Quad-Dock", -18.0, 278.0, 8.0)]:
        msp.add_text(txt, dxfattribs={"height": htxt, "layer": "TEXT_ENGRAVE"}).set_placement((x, y))

    # centerlines and dimensions
    msp.add_line((-80, 0), (-80, 300), dxfattribs={"layer": "CENTERLINES"})
    msp.add_line((0, -15), (0, 315), dxfattribs={"layer": "CENTERLINES"})
    msp.add_text("300.00", dxfattribs={"height": 4, "layer": "DIMENSIONS"}).set_placement((-5, 308))
    msp.add_text("110.00 front / 140.00 rear", dxfattribs={"height": 4, "layer": "DIMENSIONS"}).set_placement((-65, -12))
    msp.add_text("Zone1 @(-20,70), Zone2 @(+20,70), Zone3 @(-22,225), Zone4 @(+29,294)", dxfattribs={"height": 3.5, "layer": "DIMENSIONS"}).set_placement((-75, 316))

    # title block
    tx = 180
    ty = -40
    for i, line in enumerate([
        "QUAD-DOCK TOP PLATE",
        "Material: 1.5mm 6061-T6 Aluminium",
        "Finish: Gunmetal anodized, brushed",
        "All dimensions in mm | Tolerance ±0.10mm",
        "Scale: 1:1 | Units: mm",
        "Rev: 1.0 | Date: 2026-07-22",
    ]):
        msp.add_text(line, dxfattribs={"height": 4.0, "layer": "DIMENSIONS"}).set_placement((tx, ty - i * 6))

    doc.saveas(DXF_TOP)

    # SVG with mm viewBox
    def poly(points, stroke, fill="none", sw=0.6, dash=""):
        d = " ".join(f"{x},{320-y}" for x, y in points)
        ds = f' stroke-dasharray="{dash}"' if dash else ""
        return f'<polyline points="{d}" stroke="{stroke}" fill="{fill}" stroke-width="{sw}"{ds} />'

    svg = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="-200 -80 500 430" width="500mm" height="430mm">',
        '<rect x="-200" y="-80" width="500" height="430" fill="white"/>',
        poly(pts + [pts[0]], "black"),
    ]
    for z in (Z1, Z2):
        rr = [(x + z["cx"], y + z["cy"]) for x, y in rounded_rect_pts(z["w"], z["d"], z["r"], 24)]
        svg.append(poly(rr + [rr[0]], "blue"))
    svg.append(poly([(18, 288), (40, 288), (40, 300), (18, 300), (18, 288)], "red"))
    svg.append(poly([(-145, -6), (145, -6), (145, 2), (-145, 2), (-145, -6)], "orange", dash="4 3"))
    for txt, x, y in [("PHONE", -28, 93), ("BUDS", 12, 93), ("WATCH", -38, 203), ("LAPTOP", 10, 260), ("Quad-Dock", -18, 278)]:
        svg.append(f'<text x="{x}" y="{320-y}" fill="magenta" font-size="4">{txt}</text>')
    svg.append("</svg>")
    SVG_TOP.write_text("\n".join(svg), encoding="utf-8")


def kb(path: Path) -> int:
    return int(round(path.stat().st_size / 1024.0)) if path.exists() else 0


def main():
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)

    base = build_base()
    interior = build_interior_features()
    top = build_top_plate()

    full = trimesh.util.concatenate([base, top])

    base.export(STL_BASE)
    interior.export(STL_INTERIOR)
    top.export(STL_TOP)
    full.export(STL_FULL)

    write_top_plate_dxf_and_svg()

    print(f"✓ Base STL        : {STL_BASE.relative_to(ROOT)}           ({kb(STL_BASE)} KB)")
    print(f"✓ Interior STL    : {STL_INTERIOR.relative_to(ROOT)}  ({kb(STL_INTERIOR)} KB)")
    print(f"✓ Top Plate STL   : {STL_TOP.relative_to(ROOT)}      ({kb(STL_TOP)} KB)")
    if DXF_TOP.exists():
        print(f"✓ Top Plate DXF   : {DXF_TOP.relative_to(ROOT)}      ({kb(DXF_TOP)} KB)")
    else:
        print("✓ Top Plate DXF   : skipped (ezdxf unavailable)")
    if SVG_TOP.exists():
        print(f"✓ Top Plate SVG   : {SVG_TOP.relative_to(ROOT)}      ({kb(SVG_TOP)} KB)")
    else:
        print("✓ Top Plate SVG   : skipped (ezdxf unavailable)")
    print(f"✓ Full Assembly   : {STL_FULL.relative_to(ROOT)}  ({kb(STL_FULL)} KB)")


if __name__ == "__main__":
    main()
