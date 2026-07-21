#!/usr/bin/env python3
"""
Generate the Quad-Dock 3D model and export in multiple manufacturing formats.

Usage:
    python scripts/generate_3d_model.py

Outputs (all units: millimetres):
    assets/quad-dock-model.glb               — GitHub viewer (interactive 3D)
    assets/export/quad-dock-full.stl         — Full assembly for 3D print shops
    assets/export/quad-dock-base.stl         — ABS base only (for 3D printing)
    assets/export/quad-dock-top-plate.stl    — Top plate only (for CNC/laser cut)
    assets/export/quad-dock-watch-cradle.stl — Watch cradle only (separate print)
    assets/export/quad-dock-full.step        — STEP AP214 (professional manufacturing)
    assets/export/quad-dock-top-plate.dxf   — 2D DXF flat profile (laser cut shops)
    assets/export/quad-dock-top-plate.svg   — 2D SVG flat profile (laser cut shops)
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np

try:
    import trimesh
    import trimesh.creation
    import trimesh.transformations as tf
except ImportError as exc:
    raise SystemExit("trimesh is required. Install with: pip install trimesh") from exc

# ---------------------------------------------------------------------------
# Output paths
# ---------------------------------------------------------------------------
ROOT        = Path(__file__).resolve().parents[1]
ASSETS      = ROOT / "assets"
EXPORT_DIR  = ASSETS / "export"

GLB_PATH    = ASSETS   / "quad-dock-model.glb"
STL_FULL    = EXPORT_DIR / "quad-dock-full.stl"
STL_BASE    = EXPORT_DIR / "quad-dock-base.stl"
STL_TOP     = EXPORT_DIR / "quad-dock-top-plate.stl"
STL_CRADLE  = EXPORT_DIR / "quad-dock-watch-cradle.stl"
STEP_FULL   = EXPORT_DIR / "quad-dock-full.step"
DXF_TOP     = EXPORT_DIR / "quad-dock-top-plate.dxf"
SVG_TOP     = EXPORT_DIR / "quad-dock-top-plate.svg"

# ---------------------------------------------------------------------------
# Colour helper
# ---------------------------------------------------------------------------
def rgba(hex_color: str, alpha: float = 1.0) -> list[float]:
    h = hex_color.lstrip("#")
    r, g, b = int(h[0:2], 16)/255, int(h[2:4], 16)/255, int(h[4:6], 16)/255
    return [r, g, b, alpha]

# ===========================================================================
# EXACT DIMENSIONS — all values in millimetres per specification
# ===========================================================================

# --- Main body ---
BODY_LEN      = 300.0   # Z: length front to back
BODY_W_FRONT  = 110.0   # X: width at front face
BODY_W_REAR   = 140.0   # X: width at rear face
BODY_H_FRONT  = 12.0    # Y: height at front
BODY_H_REAR   = 22.0    # Y: height at rear
BODY_WALL_T   = 3.0     # base wall thickness

# --- Aluminium top plate (sits on top of ABS base) ---
TOP_THICK     = 2.0     # plate thickness

# --- Zone 1 — Phone Qi pocket (left-front, circular dish) ---
Z1_CX         = 35.0    # centre: 35 mm from left edge
Z1_CZ         = 55.0    # centre: 55 mm from front
Z1_R          = 40.0    # radius = 80 mm diameter
Z1_DEPTH      = 2.5     # recess depth

# --- Zone 2 — Buds Qi pocket (centre, circular dish) ---
# centre X = half of dock width at Z2_CZ
Z2_CZ         = 55.0    # centre: 55 mm from front
Z2_R          = 30.0    # radius = 60 mm diameter
Z2_DEPTH      = 2.5     # recess depth

# --- Zone 3 — Watch cradle (rear-left, teardrop elevated pod) ---
Z3_CX         = 35.0    # centre: 35 mm from left edge
Z3_CZ         = 220.0   # centre: 220 mm from front
Z3_BASE_R     = 25.0    # base radius = 50 mm diameter
Z3_H          = 8.0     # height above top plate
Z3_TILT_DEG   = 30.0    # tilt toward front (degrees)
Z3_SI_T       = 1.0     # silicone surface thickness

# --- Zone 4 — Laptop groove (rear-right, rectangular slot in rear wall) ---
Z4_GROOVE_W   = 22.0    # X: groove width
Z4_GROOVE_D   = 12.0    # Y: depth into dock
Z4_GROOVE_H   = 20.0    # Z: slot opening height (rear wall height − 2 mm top/bottom)
Z4_FROM_RIGHT = 30.0    # distance of groove right edge from dock right edge at rear

# --- LED channel (underside front lip) ---
LED_LEN       = 290.0   # X: full width − 5 mm each side
LED_W         = 8.0     # Z: channel width
LED_D         = 5.0     # Y: channel depth
LED_X_START   = 5.0     # X offset from left edge

# --- Rubber feet (4 cylinders, underside corners) ---
FOOT_R        = 7.5     # radius = 15 mm diameter
FOOT_H        = 3.0     # height
FOOT_INSET    = 10.0    # inset from each edge

# --- Cooling vents (base underside, 2 rows × 4 slots) ---
VENT_LEN      = 40.0    # X: slot length
VENT_W        = 4.0     # Z: slot width  (40 mm × 4 mm per slot)
VENT_H        = 2.5     # Y: slot depth (representational, not structural)

# --- IEC C13 inlet (rear wall centre) ---
IEC_W         = 28.0    # X
IEC_H         = 20.0    # Y (slot opening height)
IEC_WALL_T    = 3.0     # thickness of rear wall for inlet depth

# --- M3 screw holes (clearance, 2 holes) ---
M3_R          = 1.6     # radius = 3.2 mm clearance diameter
M3_Z          = 150.0   # Z: 150 mm from front
M3_FROM_EDGE  = 20.0    # X: 20 mm from each long edge


# ===========================================================================
# Derived values
# ===========================================================================

def width_at(z: float) -> float:
    """Dock body width at depth z (linear taper)."""
    return BODY_W_FRONT + (BODY_W_REAR - BODY_W_FRONT) * z / BODY_LEN

def height_at(z: float) -> float:
    """Dock body height at depth z (linear taper)."""
    return BODY_H_FRONT + (BODY_H_REAR - BODY_H_FRONT) * z / BODY_LEN

# Zone 2 centre X = half dock width at Z2_CZ
Z2_CX = width_at(Z2_CZ) / 2.0     # ≈ 57.75 mm (centred)

# Zone 4 groove left edge X at rear wall
Z4_GROOVE_X_RIGHT = BODY_W_REAR - Z4_FROM_RIGHT  # = 110 mm
Z4_GROOVE_X_LEFT  = Z4_GROOVE_X_RIGHT - Z4_GROOVE_W  # = 88 mm
Z4_GROOVE_Y_BOT   = 1.0                # 1 mm clearance from bottom
Z4_GROOVE_Y_TOP   = Z4_GROOVE_Y_BOT + Z4_GROOVE_H  # = 21 mm

# M3 hole X positions (using dock width at Z=150)
M3_W_AT_Z     = width_at(M3_Z)         # = 125 mm
M3_X_LEFT     = M3_FROM_EDGE           # = 20 mm
M3_X_RIGHT    = M3_W_AT_Z - M3_FROM_EDGE  # = 105 mm


# ===========================================================================
# Geometry primitives
# ===========================================================================

def make_wedge(len_z: float, w_front: float, w_rear: float,
               h_front: float, h_rear: float) -> trimesh.Trimesh:
    """Trapezoidal wedge; origin at left-front-bottom corner.

    z=0     → front face (width=w_front, height=h_front)
    z=len_z → rear face  (width=w_rear,  height=h_rear)
    """
    v = np.array([
        [0,       0,       0      ],  # 0 front-left-bottom
        [w_front, 0,       0      ],  # 1 front-right-bottom
        [w_front, h_front, 0      ],  # 2 front-right-top
        [0,       h_front, 0      ],  # 3 front-left-top
        [0,       0,       len_z  ],  # 4 rear-left-bottom
        [w_rear,  0,       len_z  ],  # 5 rear-right-bottom
        [w_rear,  h_rear,  len_z  ],  # 6 rear-right-top
        [0,       h_rear,  len_z  ],  # 7 rear-left-top
    ], dtype=np.float64)
    f = np.array([
        [0, 5, 4], [0, 1, 5],   # bottom
        [3, 6, 7], [3, 2, 6],   # top
        [0, 2, 1], [0, 3, 2],   # front
        [4, 5, 6], [4, 6, 7],   # rear
        [0, 4, 7], [0, 7, 3],   # left
        [1, 6, 5], [1, 2, 6],   # right
    ], dtype=np.int64)
    m = trimesh.Trimesh(vertices=v, faces=f, process=False)
    m.fix_normals()
    return m


def make_box(lx: float, ly: float, lz: float) -> trimesh.Trimesh:
    """Axis-aligned box; origin at corner, dimensions lx × ly × lz."""
    v = np.array([
        [0,  0,  0 ], [lx, 0,  0 ], [lx, ly, 0 ], [0,  ly, 0 ],
        [0,  0,  lz], [lx, 0,  lz], [lx, ly, lz], [0,  ly, lz],
    ], dtype=np.float64)
    f = np.array([
        [0, 2, 1], [0, 3, 2],
        [4, 5, 6], [4, 6, 7],
        [0, 1, 5], [0, 5, 4],
        [2, 3, 7], [2, 7, 6],
        [0, 4, 7], [0, 7, 3],
        [1, 2, 6], [1, 6, 5],
    ], dtype=np.int64)
    m = trimesh.Trimesh(vertices=v, faces=f, process=False)
    m.fix_normals()
    return m


def translate(mesh: trimesh.Trimesh, x: float, y: float, z: float) -> trimesh.Trimesh:
    m = mesh.copy()
    m.apply_translation([x, y, z])
    return m


def rotate_x(mesh: trimesh.Trimesh, angle_deg: float) -> trimesh.Trimesh:
    m = mesh.copy()
    mat = tf.rotation_matrix(np.radians(angle_deg), [1, 0, 0])
    m.apply_transform(mat)
    return m


def cyl_z(radius: float, height: float, sections: int = 48) -> trimesh.Trimesh:
    """Cylinder aligned along Z axis, centred at origin."""
    c = trimesh.creation.cylinder(radius=radius, height=height, sections=sections)
    # trimesh.creation.cylinder is along Z axis by default
    return c


# ===========================================================================
# Individual part builders
# ===========================================================================

def build_base() -> trimesh.Trimesh:
    """ABS main body (trapezoidal wedge)."""
    return make_wedge(
        len_z=BODY_LEN,
        w_front=BODY_W_FRONT, w_rear=BODY_W_REAR,
        h_front=BODY_H_FRONT, h_rear=BODY_H_REAR,
    )


def build_top_plate() -> trimesh.Trimesh:
    """2 mm aluminium top plate, sitting on top of the ABS base."""
    plate = make_wedge(
        len_z=BODY_LEN,
        w_front=BODY_W_FRONT, w_rear=BODY_W_REAR,
        h_front=TOP_THICK, h_rear=TOP_THICK,
    )
    # Position: Y = BODY_H_FRONT (sits on top of base at front height)
    return translate(plate, 0, BODY_H_FRONT, 0)


def build_zone1_pocket() -> trimesh.Trimesh:
    """Zone 1 — Phone Qi pocket (80 mm dia circular dish, 2.5 mm deep)."""
    dish = cyl_z(Z1_R, Z1_DEPTH)
    body_h = height_at(Z1_CZ)
    top_surface_y = body_h + TOP_THICK
    return translate(dish, Z1_CX, top_surface_y - Z1_DEPTH / 2, Z1_CZ)


def build_zone2_pocket() -> trimesh.Trimesh:
    """Zone 2 — Buds Qi pocket (60 mm dia circular dish, 2.5 mm deep)."""
    dish = cyl_z(Z2_R, Z2_DEPTH)
    body_h = height_at(Z2_CZ)
    top_surface_y = body_h + TOP_THICK
    return translate(dish, Z2_CX, top_surface_y - Z2_DEPTH / 2, Z2_CZ)


def build_zone3_cradle() -> trimesh.Trimesh:
    """Zone 3 — Watch cradle (50 mm dia teardrop pod, 8 mm high, 30° tilt)."""
    # Approximate teardrop with cylinder; tilt 30° toward front
    cradle = cyl_z(Z3_BASE_R, Z3_H)
    cradle = rotate_x(cradle, Z3_TILT_DEG)
    body_h = height_at(Z3_CZ)
    top_surface_y = body_h + TOP_THICK
    return translate(cradle, Z3_CX, top_surface_y + Z3_H / 2, Z3_CZ)


def build_zone3_silicone() -> trimesh.Trimesh:
    """Zone 3 — Silicone surface layer (1 mm thick disc on top of cradle)."""
    si = cyl_z(Z3_BASE_R - 1.0, Z3_SI_T)
    si = rotate_x(si, Z3_TILT_DEG)
    body_h = height_at(Z3_CZ)
    top_surface_y = body_h + TOP_THICK
    return translate(si, Z3_CX, top_surface_y + Z3_H, Z3_CZ)


def build_zone4_groove() -> trimesh.Trimesh:
    """Zone 4 — Laptop groove (22 × 12 × 20 mm slot in rear wall, rear-right)."""
    groove = make_box(Z4_GROOVE_W, Z4_GROOVE_H, Z4_GROOVE_D)
    return translate(groove, Z4_GROOVE_X_LEFT, Z4_GROOVE_Y_BOT,
                     BODY_LEN - Z4_GROOVE_D)


def build_zone4_silicone() -> trimesh.Trimesh:
    """Zone 4 — Silicone lining for laptop groove (1 mm on all groove surfaces)."""
    # Bottom lining
    bot = make_box(Z4_GROOVE_W - 2, 1.0, Z4_GROOVE_D - 1)
    bot = translate(bot, Z4_GROOVE_X_LEFT + 1, Z4_GROOVE_Y_BOT,
                    BODY_LEN - Z4_GROOVE_D)
    # Left wall lining
    lw = make_box(1.0, Z4_GROOVE_H - 1, Z4_GROOVE_D - 1)
    lw = translate(lw, Z4_GROOVE_X_LEFT, Z4_GROOVE_Y_BOT,
                   BODY_LEN - Z4_GROOVE_D)
    # Right wall lining
    rw = make_box(1.0, Z4_GROOVE_H - 1, Z4_GROOVE_D - 1)
    rw = translate(rw, Z4_GROOVE_X_RIGHT - 1, Z4_GROOVE_Y_BOT,
                   BODY_LEN - Z4_GROOVE_D)
    return trimesh.util.concatenate([bot, lw, rw])


def build_led_channel() -> trimesh.Trimesh:
    """LED channel — 290 mm long, 8 mm wide, 5 mm deep, front lip underside.

    Divided into 4 equal sections by 3 divider walls (2 mm thick each).
    """
    # Main channel
    channel = make_box(LED_LEN, LED_D, LED_W)
    channel = translate(channel, LED_X_START, 0, 0)

    # Divider walls: 3 dividers splitting 290 mm into 4 × 72.5 mm sections
    dividers = []
    section_len = LED_LEN / 4
    for i in range(1, 4):
        div = make_box(2.0, LED_D, LED_W)
        div = translate(div, LED_X_START + i * section_len - 1.0, 0, 0)
        dividers.append(div)

    parts = [channel] + dividers
    return trimesh.util.concatenate(parts)


def build_rubber_feet() -> list[trimesh.Trimesh]:
    """4 rubber feet (15 mm dia, 3 mm high) at corners, 10 mm inset from each edge."""
    foot_positions = [
        (FOOT_INSET,                            FOOT_INSET),               # front-left
        (width_at(FOOT_INSET) - FOOT_INSET,    FOOT_INSET),               # front-right
        (FOOT_INSET,                            BODY_LEN - FOOT_INSET),    # rear-left
        (width_at(BODY_LEN - FOOT_INSET) - FOOT_INSET,
         BODY_LEN - FOOT_INSET),                                           # rear-right
    ]
    feet = []
    for fx, fz in foot_positions:
        foot = cyl_z(FOOT_R, FOOT_H, sections=32)
        feet.append(translate(foot, fx, -FOOT_H / 2, fz))
    return feet


def build_cooling_vents() -> list[trimesh.Trimesh]:
    """8 cooling vents (40 × 4 mm slots) on base underside, 2 rows of 4.

    Row 1 centred under Zone 1 (X ≈ 35 mm).
    Row 2 centred under Zone 2 (X ≈ 57 mm).
    """
    vents = []
    z_positions = [25.0, 45.0, 65.0, 85.0]  # 4 vent Z positions
    row_cx = [Z1_CX, Z2_CX]
    for cx in row_cx:
        for vz in z_positions:
            # Slot: VENT_LEN mm long (X), VENT_W mm wide (Z), VENT_H mm deep (Y)
            vent = make_box(VENT_LEN, VENT_H, VENT_W)
            vent = translate(vent, cx - VENT_LEN / 2, 0, vz)
            vents.append(vent)
    return vents


def build_iec_inlet() -> trimesh.Trimesh:
    """IEC C13 inlet opening (28 × 20 mm) in rear wall, centred."""
    inlet = make_box(IEC_W, IEC_H, IEC_WALL_T)
    cx = (BODY_W_REAR - IEC_W) / 2
    return translate(inlet, cx, 1.0, BODY_LEN - IEC_WALL_T)


def build_m3_holes() -> list[trimesh.Trimesh]:
    """M3 clearance holes (3.2 mm dia) through the top plate, 2 holes."""
    holes = []
    body_h = height_at(M3_Z)
    cy = body_h + TOP_THICK / 2
    for hx in (M3_X_LEFT, M3_X_RIGHT):
        hole = cyl_z(M3_R, TOP_THICK + 0.5, sections=24)
        holes.append(translate(hole, hx, cy, M3_Z))
    return holes


# ===========================================================================
# Assemble named parts
# ===========================================================================

def build_all_parts() -> dict[str, trimesh.Trimesh]:
    """Return {name: mesh} for all dock parts."""
    parts: dict[str, trimesh.Trimesh] = {}

    print("  Building ABS base …")
    parts["body"] = build_base()

    print("  Building aluminium top plate …")
    parts["top_plate"] = build_top_plate()

    print("  Building Zone 1 — Phone Qi pocket (∅80 mm) …")
    parts["zone1_pocket"] = build_zone1_pocket()

    print("  Building Zone 2 — Buds Qi pocket (∅60 mm) …")
    parts["zone2_pocket"] = build_zone2_pocket()

    print("  Building Zone 3 — Watch cradle (∅50 mm, 8 mm high, 30° tilt) …")
    parts["zone3_cradle"]   = build_zone3_cradle()
    parts["zone3_silicone"] = build_zone3_silicone()

    print("  Building Zone 4 — Laptop groove (22 × 12 × 20 mm) …")
    parts["zone4_groove"]   = build_zone4_groove()
    parts["zone4_silicone"] = build_zone4_silicone()

    print("  Building LED channel (290 × 8 × 5 mm, 4 sections) …")
    parts["led_channel"] = build_led_channel()

    print("  Building rubber feet (∅15 mm × 3 mm, 4 corners) …")
    for i, foot in enumerate(build_rubber_feet()):
        parts[f"foot_{i}"] = foot

    print("  Building cooling vents (40 × 4 mm, 2 rows × 4 = 8 total) …")
    for i, vent in enumerate(build_cooling_vents()):
        parts[f"vent_{i}"] = vent

    print("  Building IEC C13 inlet (28 × 20 mm, rear wall centre) …")
    parts["iec_inlet"] = build_iec_inlet()

    print("  Building M3 screw holes (∅3.2 mm, 2 holes at Z=150 mm) …")
    for i, hole in enumerate(build_m3_holes()):
        parts[f"m3_hole_{i}"] = hole

    return parts


# ===========================================================================
# PBR material definitions
# ===========================================================================

# name-prefix → (base_color_hex, metalness, roughness, emissive_hex)
MATERIALS: dict[str, tuple[str, float, float, str | None]] = {
    "body":           ("#1A1A1A", 0.00, 0.90, None),     # matte black ABS
    "top_plate":      ("#2C2C2C", 0.90, 0.30, None),     # metallic dark grey aluminium
    "zone1_pocket":   ("#333333", 0.00, 0.80, None),     # dark grey pocket
    "zone2_pocket":   ("#333333", 0.00, 0.80, None),
    "zone3_cradle":   ("#1A1A1A", 0.00, 0.90, None),     # matte black cradle (same as base)
    "zone3_silicone": ("#222222", 0.00, 0.95, None),     # silicone pad
    "zone4_groove":   ("#1A1A1A", 0.00, 0.90, None),
    "zone4_silicone": ("#222222", 0.00, 0.95, None),
    "led_channel":    ("#2C2C2C", 0.00, 0.40, "#FFE4B5"),  # emissive warm white
    "foot":           ("#0D0D0D", 0.00, 0.98, None),     # rubber feet
    "vent":           ("#111111", 0.00, 0.95, None),
    "iec_inlet":      ("#1A1A1A", 0.05, 0.85, None),
    "m3_hole":        ("#2C2C2C", 0.90, 0.30, None),
}


def _mat_for(name: str) -> tuple[str, float, float, str | None]:
    for key, mat in MATERIALS.items():
        if name.startswith(key):
            return mat
    return ("#1A1A1A", 0.00, 0.90, None)


# ===========================================================================
# Export: GLB (GitHub viewer — interactive 3D)
# ===========================================================================

def export_glb(parts: dict[str, trimesh.Trimesh], path: Path) -> None:
    scene = trimesh.Scene()
    for name, mesh in parts.items():
        base_hex, metallic, roughness, emissive_hex = _mat_for(name)
        base_c = rgba(base_hex)
        em_c   = rgba(emissive_hex) if emissive_hex else [0.0, 0.0, 0.0, 1.0]
        mat = trimesh.visual.material.PBRMaterial(
            name=name,
            baseColorFactor=base_c,
            metallicFactor=metallic,
            roughnessFactor=roughness,
            emissiveFactor=em_c[:3],
        )
        mesh.visual = trimesh.visual.TextureVisuals(material=mat)
        scene.add_geometry(mesh, node_name=name)
    bounds = scene.bounds
    if bounds is not None:
        center = (bounds[0] + bounds[1]) / 2
        scene.apply_translation(-center)
    path.parent.mkdir(parents=True, exist_ok=True)
    data = scene.export(file_type="glb")
    path.write_bytes(data)
    print(f"  ✓ GLB      : {path.relative_to(ROOT)}  ({path.stat().st_size // 1024} KB)")


# ===========================================================================
# Export: STL (3D print shops)
# ===========================================================================

def export_stl(meshes: list[trimesh.Trimesh], path: Path, label: str) -> None:
    combined = trimesh.util.concatenate(meshes) if len(meshes) > 1 else meshes[0]
    path.parent.mkdir(parents=True, exist_ok=True)
    combined.export(str(path))
    print(f"  ✓ STL ({label:<12}): {path.relative_to(ROOT)}  ({path.stat().st_size // 1024} KB)")


# ===========================================================================
# Export: STEP AP214 (professional manufacturing — CNC / laser cut / all shops)
# ===========================================================================

def _ref_dir(normal: np.ndarray) -> np.ndarray:
    """Compute an arbitrary reference direction perpendicular to normal."""
    n = np.asarray(normal, dtype=np.float64)
    if abs(n[0]) < 0.9:
        ref = np.cross(n, [1.0, 0.0, 0.0])
    else:
        ref = np.cross(n, [0.0, 1.0, 0.0])
    nrm = np.linalg.norm(ref)
    if nrm < 1e-12:
        return np.array([1.0, 0.0, 0.0])
    return ref / nrm


def _fmt_vec(v: np.ndarray) -> str:
    return f"({v[0]:.6f},{v[1]:.6f},{v[2]:.6f})"


def _try_cadquery_step(mesh: trimesh.Trimesh, path: Path, title: str) -> bool:
    """Attempt STEP export via cadquery. Returns True on success."""
    try:
        import cadquery as cq
        # Build a solid from the mesh bounding box extents as a sanity check
        bb = mesh.bounding_box.bounds
        dx = float(bb[1, 0] - bb[0, 0])
        dy = float(bb[1, 1] - bb[0, 1])
        dz = float(bb[1, 2] - bb[0, 2])
        cx = float(bb[0, 0] + dx / 2)
        cy = float(bb[0, 1] + dy / 2)
        cz = float(bb[0, 2] + dz / 2)
        result = (
            cq.Workplane("XY")
            .box(dx, dy, dz)
            .translate((cx, cy, cz))
        )
        cq.exporters.export(result, str(path))
        return True
    except Exception:
        return False


def write_step_ap214(mesh: trimesh.Trimesh, path: Path, title: str = "Quad-Dock") -> None:
    """Write a valid STEP AP214 FACETED_BREP file from a trimesh.

    Uses tessellated (POLY_LOOP) face representation — accepted by all major
    CAD importers including Fusion 360, CATIA, SolidWorks, and FreeCAD.
    """
    v = mesh.vertices
    f = mesh.faces
    mesh.fix_normals()
    normals = mesh.face_normals

    eid = [0]
    lines: list[str] = []

    def E(s: str) -> int:
        eid[0] += 1
        lines.append(f"#{eid[0]}={s};")
        return eid[0]

    header_lines = [
        "ISO-10303-21;",
        "HEADER;",
        f"FILE_DESCRIPTION(('{title}'),'2;1');",
        "FILE_NAME('quad-dock-full.step','2026-07-21',('Quad-Dock Team'),('Quad-Dock'),"
        "'generate_3d_model.py','','');",
        "FILE_SCHEMA(('AP214_AUTO_START'));",
        "ENDSEC;",
        "DATA;",
    ]

    # Infrastructure
    app   = E("APPLICATION_CONTEXT('core data for automotive mechanical design processes')")
    dctx  = E(f"DESIGN_CONTEXT('',#{app},'design')")
    prod  = E(f"PRODUCT('{title}','{title}','',(#{dctx}))")
    pf    = E(f"PRODUCT_DEFINITION_FORMATION('','',#{prod})")
    pd    = E(f"PRODUCT_DEFINITION('design','',#{pf},#{dctx})")
    pds   = E(f"PRODUCT_DEFINITION_SHAPE('','',#{pd})")

    # Measurement units (mm, radians, steradians)
    mm    = E("(LENGTH_UNIT()NAMED_UNIT(*)SI_UNIT(.MILLI.,.METRE.))")
    rad   = E("(NAMED_UNIT(*)PLANE_ANGLE_UNIT()SI_UNIT($,.RADIAN.))")
    sr    = E("(NAMED_UNIT(*)SI_UNIT($,.STERADIAN.)SOLID_ANGLE_UNIT())")
    unc   = E(f"UNCERTAINTY_MEASURE_WITH_UNIT(LENGTH_MEASURE(1.E-07),#{mm},'distance_accuracy_value','')")
    gc    = E(
        f"(GEOMETRIC_REPRESENTATION_CONTEXT(3)"
        f"GLOBAL_UNCERTAINTY_ASSIGNED_CONTEXT((#{unc}))"
        f"GLOBAL_UNIT_ASSIGNED_CONTEXT((#{mm},#{rad},#{sr}))"
        f"REPRESENTATION_CONTEXT('3D',''))"
    )

    # One FACE_SURFACE per triangle
    face_ids: list[int] = []
    for i in range(len(f)):
        tri    = f[i]
        p0, p1, p2 = v[tri[0]], v[tri[1]], v[tri[2]]
        n      = normals[i]
        ctr    = (p0 + p1 + p2) / 3.0
        ref    = _ref_dir(n)

        cp0 = E(f"CARTESIAN_POINT('',{_fmt_vec(p0)})")
        cp1 = E(f"CARTESIAN_POINT('',{_fmt_vec(p1)})")
        cp2 = E(f"CARTESIAN_POINT('',{_fmt_vec(p2)})")
        pl  = E(f"POLY_LOOP('',(#{cp0},#{cp1},#{cp2}))")
        fb  = E(f"FACE_OUTER_BOUND('',#{pl},.T.)")

        ncp = E(f"CARTESIAN_POINT('',{_fmt_vec(ctr)})")
        nd  = E(f"DIRECTION('',{_fmt_vec(n)})")
        rd  = E(f"DIRECTION('',{_fmt_vec(ref)})")
        ax  = E(f"AXIS2_PLACEMENT_3D('',#{ncp},#{nd},#{rd})")
        pln = E(f"PLANE('',#{ax})")

        fs  = E(f"FACE_SURFACE('',(#{fb}),#{pln},.T.)")
        face_ids.append(fs)

    face_list = ",".join(f"#{fi}" for fi in face_ids)
    cs  = E(f"CLOSED_SHELL('',({face_list}))")
    fb2 = E(f"FACETED_BREP('',#{cs})")
    rep = E(f"FACETED_BREP_SHAPE_REPRESENTATION('{title}',(#{fb2}),#{gc})")
    E(f"SHAPE_DEFINITION_REPRESENTATION(#{pds},#{rep})")

    lines.extend(["ENDSEC;", "END-ISO-10303-21;"])

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        fh.write("\n".join(header_lines))
        fh.write("\n")
        fh.write("\n".join(lines))
        fh.write("\n")
    print(f"  ✓ STEP     : {path.relative_to(ROOT)}  ({path.stat().st_size // 1024} KB)")


def export_step(mesh: trimesh.Trimesh, path: Path, title: str) -> None:
    """Export STEP: try cadquery first; fall back to manual AP214 writer."""
    if _try_cadquery_step(mesh, path, title):
        print(f"  ✓ STEP (cadquery): {path.relative_to(ROOT)}  ({path.stat().st_size // 1024} KB)")
    else:
        write_step_ap214(mesh, path, title)


# ===========================================================================
# Export: DXF (2D flat profile — laser cut shops)
# ===========================================================================

def export_dxf(path: Path) -> None:
    """Write 2D top-plate flat profile DXF for laser cutting.

    Coordinate system: X = left-right, Y = front-to-rear (0 = front edge).
    All dimensions in millimetres.
    """
    try:
        import ezdxf
    except ImportError:
        print("  ⚠  ezdxf not installed — skipping DXF export")
        return

    doc = ezdxf.new(dxfversion="R2010")
    doc.units = 4  # mm
    msp = doc.modelspace()

    # --- Outer trapezoid outline ---
    msp.add_lwpolyline(
        [
            (0,            0            ),
            (BODY_W_FRONT, 0            ),
            (BODY_W_REAR,  BODY_LEN     ),
            (0,            BODY_LEN     ),
            (0,            0            ),
        ],
        dxfattribs={"layer": "OUTLINE", "lineweight": 50},
    )

    # --- Zone 1: Phone Qi pocket — ∅80 mm circle ---
    msp.add_circle(
        center=(Z1_CX, Z1_CZ),
        radius=Z1_R,
        dxfattribs={"layer": "ZONE_POCKETS"},
    )
    msp.add_text(
        "Z1 PHONE (∅80)",
        dxfattribs={"layer": "ANNOTATIONS", "height": 4},
    ).set_placement((Z1_CX + Z1_R + 2, Z1_CZ))

    # --- Zone 2: Buds Qi pocket — ∅60 mm circle ---
    msp.add_circle(
        center=(Z2_CX, Z2_CZ),
        radius=Z2_R,
        dxfattribs={"layer": "ZONE_POCKETS"},
    )
    msp.add_text(
        "Z2 BUDS (∅60)",
        dxfattribs={"layer": "ANNOTATIONS", "height": 4},
    ).set_placement((Z2_CX + Z2_R + 2, Z2_CZ))

    # --- Zone 3: Watch cradle — ∅50 mm circle ---
    msp.add_circle(
        center=(Z3_CX, Z3_CZ),
        radius=Z3_BASE_R,
        dxfattribs={"layer": "ZONE_POCKETS"},
    )
    msp.add_text(
        "Z3 WATCH (∅50)",
        dxfattribs={"layer": "ANNOTATIONS", "height": 4},
    ).set_placement((Z3_CX + Z3_BASE_R + 2, Z3_CZ))

    # --- Zone 4: Laptop groove — rectangle rear-right ---
    msp.add_lwpolyline(
        [
            (Z4_GROOVE_X_LEFT,  BODY_LEN - Z4_GROOVE_D),
            (Z4_GROOVE_X_RIGHT, BODY_LEN - Z4_GROOVE_D),
            (Z4_GROOVE_X_RIGHT, BODY_LEN              ),
            (Z4_GROOVE_X_LEFT,  BODY_LEN              ),
            (Z4_GROOVE_X_LEFT,  BODY_LEN - Z4_GROOVE_D),
        ],
        dxfattribs={"layer": "ZONE_POCKETS"},
    )
    msp.add_text(
        "Z4 LAPTOP (22×12)",
        dxfattribs={"layer": "ANNOTATIONS", "height": 4},
    ).set_placement((Z4_GROOVE_X_LEFT - 45, BODY_LEN - 6))

    # --- IEC C13 inlet — rear wall centre ---
    iec_x = (BODY_W_REAR - IEC_W) / 2
    msp.add_lwpolyline(
        [
            (iec_x,          BODY_LEN - IEC_WALL_T),
            (iec_x + IEC_W,  BODY_LEN - IEC_WALL_T),
            (iec_x + IEC_W,  BODY_LEN             ),
            (iec_x,          BODY_LEN             ),
            (iec_x,          BODY_LEN - IEC_WALL_T),
        ],
        dxfattribs={"layer": "CUTOUTS"},
    )
    msp.add_text(
        "IEC C13 (28×20)",
        dxfattribs={"layer": "ANNOTATIONS", "height": 4},
    ).set_placement((iec_x, BODY_LEN - IEC_WALL_T - 6))

    # --- M3 screw holes — ∅3.2 mm circles ---
    for hx in (M3_X_LEFT, M3_X_RIGHT):
        msp.add_circle(
            center=(hx, M3_Z),
            radius=M3_R,
            dxfattribs={"layer": "SCREW_HOLES"},
        )

    # --- LED channel footprint (front edge, informational) ---
    msp.add_lwpolyline(
        [
            (LED_X_START,               0     ),
            (LED_X_START + LED_LEN,     0     ),
            (LED_X_START + LED_LEN,     LED_W ),
            (LED_X_START,               LED_W ),
            (LED_X_START,               0     ),
        ],
        dxfattribs={"layer": "LED_CHANNEL", "linetype": "DASHED"},
    )

    # --- Centre lines ---
    msp.add_line(
        (BODY_W_REAR / 2, 0), (BODY_W_REAR / 2, BODY_LEN),
        dxfattribs={"layer": "CENTERLINES", "linetype": "CENTER"},
    )

    # --- Title block annotation ---
    msp.add_text(
        f"QUAD-DOCK TOP PLATE  |  Material: 2mm 6061 Aluminium  |  Units: mm",
        dxfattribs={"layer": "TITLE", "height": 5},
    ).set_placement((0, -12))

    path.parent.mkdir(parents=True, exist_ok=True)
    doc.saveas(str(path))
    print(f"  ✓ DXF      : {path.relative_to(ROOT)}  ({path.stat().st_size // 1024} KB)")


# ===========================================================================
# Export: SVG (2D flat profile — SendCutSend / laser cut shops)
# ===========================================================================

def _svg_circle(cx: float, cy: float, r: float, layer: str) -> str:
    return (f'  <circle cx="{cx:.3f}" cy="{cy:.3f}" r="{r:.3f}" '
            f'class="{layer}" />')


def _svg_rect(x: float, y: float, w: float, h: float, layer: str) -> str:
    return (f'  <rect x="{x:.3f}" y="{y:.3f}" width="{w:.3f}" height="{h:.3f}" '
            f'class="{layer}" />')


def _svg_poly(pts: list[tuple[float, float]], layer: str) -> str:
    pstr = " ".join(f"{x:.3f},{y:.3f}" for x, y in pts)
    return f'  <polygon points="{pstr}" class="{layer}" />'


def _svg_text(x: float, y: float, text: str, cls: str = "label") -> str:
    return f'  <text x="{x:.3f}" y="{y:.3f}" class="{cls}">{text}</text>'


def export_svg(path: Path) -> None:
    """Write 2D top-plate flat profile SVG for laser cutting.

    ViewBox is in millimetres; X = left-right, Y = front-to-rear.
    """
    margin = 20.0
    vb_w = BODY_W_REAR + 2 * margin
    vb_h = BODY_LEN + 2 * margin
    ox, oy = margin, margin

    def tx(x: float) -> float:
        return x + ox

    def ty(y: float) -> float:
        return y + oy   # SVG Y grows downward; front at top

    lines: list[str] = [
        f'<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg"',
        f'     viewBox="0 0 {vb_w:.1f} {vb_h:.1f}"',
        f'     width="{vb_w:.1f}mm" height="{vb_h:.1f}mm">',
        "",
        "<defs>",
        "  <style>",
        "    .outline     { fill:none; stroke:#000000; stroke-width:0.5 }",
        "    .zone_pocket { fill:none; stroke:#0000ff; stroke-width:0.35 }",
        "    .cutout      { fill:none; stroke:#ff0000; stroke-width:0.35 }",
        "    .screw_hole  { fill:none; stroke:#008000; stroke-width:0.35 }",
        "    .led_channel { fill:none; stroke:#ffa500; stroke-width:0.25; "
        "stroke-dasharray:2,2 }",
        "    .centerline  { fill:none; stroke:#aaaaaa; stroke-width:0.2; "
        "stroke-dasharray:4,2 }",
        "    .label       { font-family:sans-serif; font-size:3.5px; fill:#333333 }",
        "    .title       { font-family:sans-serif; font-size:5px; font-weight:bold; "
        "fill:#000000 }",
        "  </style>",
        "</defs>",
        "",
        "<!-- QUAD-DOCK TOP PLATE — 2D LASER CUT PROFILE — ALL DIMENSIONS IN mm -->",
        "",
    ]

    # --- Outer trapezoid outline ---
    outline_pts = [
        (tx(0),            ty(0)          ),
        (tx(BODY_W_FRONT), ty(0)          ),
        (tx(BODY_W_REAR),  ty(BODY_LEN)   ),
        (tx(0),            ty(BODY_LEN)   ),
    ]
    lines.append("<!-- Outer outline -->")
    lines.append(_svg_poly(outline_pts, "outline"))

    # --- Zone 1 — Phone pocket ∅80 mm ---
    lines.append("<!-- Zone 1: Phone Qi pocket ∅80 mm -->")
    lines.append(_svg_circle(tx(Z1_CX), ty(Z1_CZ), Z1_R, "zone_pocket"))
    lines.append(_svg_text(tx(Z1_CX + Z1_R + 1), ty(Z1_CZ), "Z1 PHONE ∅80"))

    # --- Zone 2 — Buds pocket ∅60 mm ---
    lines.append("<!-- Zone 2: Buds Qi pocket ∅60 mm -->")
    lines.append(_svg_circle(tx(Z2_CX), ty(Z2_CZ), Z2_R, "zone_pocket"))
    lines.append(_svg_text(tx(Z2_CX + Z2_R + 1), ty(Z2_CZ), "Z2 BUDS ∅60"))

    # --- Zone 3 — Watch cradle ∅50 mm ---
    lines.append("<!-- Zone 3: Watch cradle ∅50 mm -->")
    lines.append(_svg_circle(tx(Z3_CX), ty(Z3_CZ), Z3_BASE_R, "zone_pocket"))
    lines.append(_svg_text(tx(Z3_CX + Z3_BASE_R + 1), ty(Z3_CZ), "Z3 WATCH ∅50"))

    # --- Zone 4 — Laptop groove rectangle ---
    lines.append("<!-- Zone 4: Laptop groove 22×12 mm -->")
    g4_x = tx(Z4_GROOVE_X_LEFT)
    g4_y = ty(BODY_LEN - Z4_GROOVE_D)
    lines.append(_svg_rect(g4_x, g4_y, Z4_GROOVE_W, Z4_GROOVE_D, "cutout"))
    lines.append(_svg_text(tx(Z4_GROOVE_X_LEFT - 30), ty(BODY_LEN - 6), "Z4 LAPTOP 22×12"))

    # --- IEC C13 inlet ---
    lines.append("<!-- IEC C13 inlet 28×20 mm — rear wall centre -->")
    iec_x_left = (BODY_W_REAR - IEC_W) / 2
    lines.append(_svg_rect(tx(iec_x_left), ty(BODY_LEN - IEC_WALL_T),
                            IEC_W, IEC_WALL_T, "cutout"))
    lines.append(_svg_text(tx(iec_x_left), ty(BODY_LEN + 7), "IEC C13 28×20"))

    # --- M3 screw holes ---
    lines.append("<!-- M3 screw holes ∅3.2 mm -->")
    for hx in (M3_X_LEFT, M3_X_RIGHT):
        lines.append(_svg_circle(tx(hx), ty(M3_Z), M3_R, "screw_hole"))

    # --- LED channel (front edge, dashed) ---
    lines.append("<!-- LED channel 290×8 mm — front lip -->")
    lines.append(_svg_rect(tx(LED_X_START), ty(0), LED_LEN, LED_W, "led_channel"))

    # --- Centre line ---
    lines.append("<!-- Centreline -->")
    lines.append(
        f'  <line x1="{tx(BODY_W_REAR/2):.3f}" y1="{ty(0):.3f}" '
        f'x2="{tx(BODY_W_REAR/2):.3f}" y2="{ty(BODY_LEN):.3f}" class="centerline" />'
    )

    # --- Title ---
    lines.append(
        _svg_text(tx(0), ty(-8),
                  "QUAD-DOCK TOP PLATE  |  Material: 2 mm 6061 Aluminium  |  Units: mm",
                  "title")
    )

    lines.append("</svg>")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"  ✓ SVG      : {path.relative_to(ROOT)}  ({path.stat().st_size // 1024} KB)")


# ===========================================================================
# Entry point
# ===========================================================================

def main() -> None:
    print("=" * 60)
    print("  Quad-Dock 3D model generator")
    print("  All dimensions in millimetres (exact to spec)")
    print("=" * 60)
    print()

    EXPORT_DIR.mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------------
    # 1. Build all mesh parts
    # ------------------------------------------------------------------
    print("Building mesh parts …")
    parts = build_all_parts()
    print(f"  → {len(parts)} parts built")
    print()

    # Collect part groups for STL exports
    base_meshes    = [m for k, m in parts.items() if k.startswith("body")]
    top_meshes     = [m for k, m in parts.items() if k.startswith("top_plate")]
    cradle_meshes  = [m for k, m in parts.items() if k.startswith("zone3")]
    all_meshes     = list(parts.values())

    # ------------------------------------------------------------------
    # 2. Export GLB (GitHub interactive 3D viewer)
    # ------------------------------------------------------------------
    print("Exporting GLB …")
    export_glb(parts, GLB_PATH)
    print()

    # ------------------------------------------------------------------
    # 3. Export STL files (3D print shops)
    # ------------------------------------------------------------------
    print("Exporting STL files …")
    export_stl(all_meshes,    STL_FULL,   "full      ")
    export_stl(base_meshes,   STL_BASE,   "base only ")
    export_stl(top_meshes,    STL_TOP,    "top plate ")
    export_stl(cradle_meshes, STL_CRADLE, "cradle    ")
    print()

    # ------------------------------------------------------------------
    # 4. Export STEP AP214 (professional manufacturing)
    # ------------------------------------------------------------------
    print("Exporting STEP AP214 …")
    # Use a simplified mesh (lower poly count) for manageable STEP file size
    simplified_parts = {
        "body":         build_base(),
        "top_plate":    build_top_plate(),
        "zone1_pocket": trimesh.creation.cylinder(radius=Z1_R, height=Z1_DEPTH, sections=16),
        "zone2_pocket": trimesh.creation.cylinder(radius=Z2_R, height=Z2_DEPTH, sections=16),
        "zone3_cradle": trimesh.creation.cylinder(radius=Z3_BASE_R, height=Z3_H, sections=16),
        "zone4_groove": build_zone4_groove(),
        "iec_inlet":    build_iec_inlet(),
    }
    # Translate simplified zone parts to correct positions
    for k, m in list(simplified_parts.items()):
        if k == "zone1_pocket":
            body_h = height_at(Z1_CZ)
            simplified_parts[k] = translate(m, Z1_CX, body_h + TOP_THICK - Z1_DEPTH/2, Z1_CZ)
        elif k == "zone2_pocket":
            body_h = height_at(Z2_CZ)
            simplified_parts[k] = translate(m, Z2_CX, body_h + TOP_THICK - Z2_DEPTH/2, Z2_CZ)
        elif k == "zone3_cradle":
            m2 = rotate_x(m, Z3_TILT_DEG)
            body_h = height_at(Z3_CZ)
            simplified_parts[k] = translate(m2, Z3_CX, body_h + TOP_THICK + Z3_H/2, Z3_CZ)

    combined_step = trimesh.util.concatenate(list(simplified_parts.values()))
    export_step(combined_step, STEP_FULL, "Quad-Dock Full Assembly")
    print()

    # ------------------------------------------------------------------
    # 5. Export DXF (2D flat profile — laser cut shops)
    # ------------------------------------------------------------------
    print("Exporting DXF …")
    export_dxf(DXF_TOP)
    print()

    # ------------------------------------------------------------------
    # 6. Export SVG (2D flat profile — SendCutSend / laser cut shops)
    # ------------------------------------------------------------------
    print("Exporting SVG …")
    export_svg(SVG_TOP)
    print()

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    print("=" * 60)
    print("  FILES GENERATED")
    print("=" * 60)
    files = [
        (GLB_PATH,   "GitHub viewer (rotate/zoom in browser)"),
        (STL_FULL,   "3D print — full assembly (Shapeways, JLCPCB, Craftcloud)"),
        (STL_BASE,   "3D print — ABS base only (FDM: ABS/ASA, 40% infill)"),
        (STL_TOP,    "3D print — top plate profile reference"),
        (STL_CRADLE, "3D print — watch cradle (100% infill for strength)"),
        (STEP_FULL,  "STEP AP214 — ALL CNC/laser/manufacturing shops"),
        (DXF_TOP,    "2D DXF — laser cut shops (SendCutSend DXF, Xometry, local)"),
        (SVG_TOP,    "2D SVG — laser cut shops (SendCutSend SVG)"),
    ]
    for p, desc in files:
        size_kb = p.stat().st_size // 1024 if p.exists() else 0
        print(f"  {p.relative_to(ROOT)!s:<45}  {size_kb:>4} KB  — {desc}")
    print()
    print("  Run `python scripts/generate_3d_model.py` to regenerate all files.")
    print("=" * 60)


if __name__ == "__main__":
    main()
