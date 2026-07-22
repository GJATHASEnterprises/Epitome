#!/usr/bin/env python3
"""Generate manufacturing exports for Quad-Dock."""
from __future__ import annotations

import math
from pathlib import Path

import numpy as np

try:
    import trimesh
except ImportError as exc:
    raise SystemExit("trimesh is required: pip install trimesh") from exc

try:
    import ezdxf  # type: ignore
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

Z1 = dict(cx=-20.0, cy=70.0, w=80.0, d=55.0, r=10.0, depth=2.5)
Z2 = dict(cx=+20.0, cy=70.0, w=65.0, d=55.0, r=10.0, depth=2.5)
Z3 = dict(cx=-22.0, cy=225.0, d=50.0)
Z4 = dict(x0=18.0, x1=40.0, y0=288.0, y1=300.0, depth=12.0)
IEC = dict(w=28.0, h=20.0, x=0.0, y=298.5, z_bottom=1.0)
M3S = [(-35.0, 150.0), (30.0, 150.0), (-35.0, 230.0), (30.0, 230.0)]
FEET = [(-39.17, 15.0), (39.17, 15.0), (-53.5, 285.0), (53.5, 285.0)]
VENTS = [(-20.0, 25.0), (-20.0, 45.0), (-20.0, 65.0), (-20.0, 85.0), (20.0, 25.0), (20.0, 45.0), (20.0, 65.0), (20.0, 85.0)]


def h(y: float) -> float:
    return FRONT_H + (REAR_H - FRONT_H) * (y / LENGTH)


def rounded_outline_40() -> list[tuple[float, float]]:
    corners = [(-FRONT_W / 2, 0.0), (FRONT_W / 2, 0.0), (REAR_W / 2, LENGTH), (-REAR_W / 2, LENGTH)]

    def norm(dx, dy):
        mag = math.hypot(dx, dy)
        return (dx / mag, dy / mag)

    coarse = []
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

    out = []
    boundaries = {8, 17, 26, 35}
    for i, p in enumerate(coarse):
        out.append(p)
        if i in boundaries:
            q = coarse[(i + 1) % len(coarse)]
            out.append(((p[0] + q[0]) / 2.0, (p[1] + q[1]) / 2.0))
    return out


def rounded_rect_pts(w, d, r, seg=16):
    hw, hd = w / 2, d / 2
    pts = []
    for cx, cy, a0, a1 in [
        (hw - r, -hd + r, -math.pi / 2, 0),
        (hw - r, hd - r, 0, math.pi / 2),
        (-hw + r, hd - r, math.pi / 2, math.pi),
        (-hw + r, -hd + r, math.pi, 3 * math.pi / 2),
    ]:
        for i in range(seg):
            t = i / max(1, seg - 1)
            a = a0 + (a1 - a0) * t
            pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


def circle_pts(r, n=48):
    return [(r * math.cos(2 * math.pi * i / n), r * math.sin(2 * math.pi * i / n)) for i in range(n)]


def prism_from_outline(outline, z0_fn, z1_fn):
    n = len(outline)
    verts = np.array([(x, y, z0_fn(y)) for x, y in outline] + [(x, y, z1_fn(y)) for x, y in outline], dtype=float)
    faces: list[list[int]] = []
    for i in range(n):
        j = (i + 1) % n
        faces += [[i, j, n + j], [i, n + j, n + i]]
    # bottom cap (faces down)
    for i in range(1, n - 1):
        faces.append([0, i + 1, i])
    # top cap (faces up)
    for i in range(1, n - 1):
        faces.append([n, n + i, n + i + 1])
    mesh = trimesh.Trimesh(vertices=verts, faces=np.array(faces, dtype=int), process=True)
    mesh.update_faces(mesh.nondegenerate_faces())
    mesh.update_faces(mesh.unique_faces())
    mesh.remove_unreferenced_vertices()
    return mesh


def extruded_shape(points, z0, z1, cx=0.0, cy=0.0):
    n = len(points)
    pts = [(x + cx, y + cy) for x, y in points]
    verts = np.array([(x, y, z0) for x, y in pts] + [(x, y, z1) for x, y in pts], dtype=float)
    faces: list[list[int]] = []
    for i in range(n):
        j = (i + 1) % n
        faces += [[i, j, n + j], [i, n + j, n + i]]
    for i in range(1, n - 1):
        faces.append([0, i + 1, i])  # bottom cap
        faces.append([n, n + i, n + i + 1])  # top cap
    mesh = trimesh.Trimesh(vertices=verts, faces=np.array(faces, dtype=int), process=True)
    mesh.update_faces(mesh.nondegenerate_faces())
    mesh.update_faces(mesh.unique_faces())
    mesh.remove_unreferenced_vertices()
    return mesh


def safe_diff(mesh, cutter, label):
    try:
        out = trimesh.boolean.difference([mesh, cutter])
        if out is None:
            raise RuntimeError("difference returned None")
        if isinstance(out, list):
            out = trimesh.util.concatenate(out)
        return out
    except Exception as exc:
        print(f"[warn] boolean difference failed ({label}): {exc}")
        return mesh


def safe_union(meshes, label):
    try:
        out = trimesh.boolean.union(meshes)
        if out is None:
            raise RuntimeError("union returned None")
        if isinstance(out, list):
            out = trimesh.util.concatenate(out)
        return out
    except Exception as exc:
        print(f"[warn] boolean union failed ({label}): {exc}")
        return trimesh.util.concatenate(meshes)


def box(center, size):
    m = trimesh.creation.box(extents=size)
    m.apply_translation(center)
    return m


def cyl(radius, height, center):
    m = trimesh.creation.cylinder(radius=radius, height=height, sections=64)
    m.apply_translation(center)
    return m


def build_base():
    outline = rounded_outline_40()
    outer = prism_from_outline(outline, lambda _y: 0.0, h)

    inner_outline = [
        (x * ((FRONT_W - 2 * WALL) / FRONT_W if y < 1e-6 else (REAR_W - 2 * WALL) / REAR_W), y)
        for x, y in outline
    ]
    inner = prism_from_outline(inner_outline, lambda _y: WALL, lambda y: max(WALL + 0.1, h(y) - WALL))
    base = safe_diff(outer, inner, "outer-inner shell")

    # top features
    for z in (Z1, Z2):
        pocket = extruded_shape(rounded_rect_pts(z["w"], z["d"], z["r"], 20), h(z["cy"]) - z["depth"], h(z["cy"]) + 2.0, z["cx"], z["cy"])
        base = safe_diff(base, pocket, f"dish_{z['cx']}")

    watch_hole = cyl(Z3["d"] / 2.0, 30.0, (Z3["cx"], Z3["cy"], h(Z3["cy"]) - 5.0))
    base = safe_diff(base, watch_hole, "watch hole")

    groove = box(((Z4["x0"] + Z4["x1"]) / 2.0, (Z4["y0"] + Z4["y1"]) / 2.0, h(294.0) / 2.0), (Z4["x1"] - Z4["x0"], Z4["y1"] - Z4["y0"], 20.0))
    base = safe_diff(base, groove, "laptop groove")

    iec = box((IEC["x"], IEC["y"], IEC["z_bottom"] + IEC["h"] / 2.0), (IEC["w"], 6.0, IEC["h"]))
    base = safe_diff(base, iec, "iec")

    led = box((0.0, -2.0, 2.5), (290.0, 8.0, 5.0))
    base = safe_diff(base, led, "led channel")

    for x, y in FEET:
        base = safe_diff(base, cyl(7.5, 2.0, (x, y, -1.0)), f"foot recess {x},{y}")

    for x, y in M3S:
        boss = cyl(3.0, 8.0, (x, y, h(y) - 4.0))
        hole = cyl(1.6, 20.0, (x, y, h(y) - 4.0))
        base = safe_union([base, boss], f"boss {x},{y}")
        base = safe_diff(base, hole, f"m3 hole {x},{y}")

    for x, y in VENTS:
        vent = box((x, y, -1.25), (40.0, 4.0, 2.5))
        base = safe_diff(base, vent, f"vent {x},{y}")

    usbc = box((29.0, 298.0, 8.0), (10.0, 4.0, 4.0))
    base = safe_diff(base, usbc, "usb-c")
    return base


def build_interior_features(mesh):
    features = []
    features.append(cyl(28.0, 6.0, (-20.0, 70.0, 3.0)))
    features.append(cyl(28.0, 6.0, (20.0, 70.0, 3.0)))
    ring_outer = cyl(28.0, 3.0, (-20.0, 70.0, 6.5))
    ring_inner = cyl(25.0, 5.0, (-20.0, 70.0, 6.5))
    ring = safe_diff(ring_outer, ring_inner, "magnet ring")
    features.append(ring)
    features.append(cyl(18.0, 6.0, (-22.0, 225.0, 3.0)))
    features.append(box((-5.0, 110.0, 2.0), (120.0, 80.0, 4.0)))
    features.append(box((0.0, 210.0, 18.0), (152.0, 82.0, 36.0)))
    features.append(box((32.0, 155.0, 2.0), (42.0, 32.0, 4.0)))

    # cable channels
    channels = [
        box((-20.0, 72.5, 1.5), (5.0, 5.0, 3.0)),
        box((20.0, 72.5, 1.5), (5.0, 5.0, 3.0)),
        box((-22.0, 190.0, 1.5), (5.0, 70.0, 3.0)),
        box((0.0, 146.5, 1.5), (5.0, 3.0, 3.0)),
        box((10.0, 150.0, 1.5), (5.0, 10.0, 3.0)),
        box((0.0, 283.5, 1.5), (5.0, 27.0, 3.0)),
    ]
    for ch in channels:
        features.append(ch)

    out = mesh
    for i, f in enumerate(features):
        out = safe_diff(out, f, f"interior feature {i}")

    # PCB holes
    for x in (-60.0, 50.0):
        for y in (75.0, 145.0):
            out = safe_diff(out, cyl(1.6, 12.0, (x, y, 2.0)), f"pcb hole {x},{y}")

    # PSU holes
    for x in (-70.0, 70.0):
        for y in (154.0, 266.0):
            out = safe_diff(out, cyl(1.6, 12.0, (x, y, 2.0)), f"psu hole {x},{y}")

    return out


def build_top_plate():
    outline = rounded_outline_40()
    top = prism_from_outline(outline, h, lambda y: h(y) + TOP_T)

    # cuts
    for z in (Z1, Z2):
        cut = extruded_shape(rounded_rect_pts(z["w"], z["d"], z["r"], 20), h(z["cy"]) - 5.0, h(z["cy"]) + TOP_T + 2.0, z["cx"], z["cy"])
        top = safe_diff(top, cut, f"top cut {z['cx']}")
    top = safe_diff(top, cyl(25.0, 30.0, (-22.0, 225.0, h(225.0))), "z3 through")
    top = safe_diff(top, box((29.0, 294.0, h(294.0)), (22.0, 12.0, 20.0)), "z4 slot")
    top = safe_diff(top, box((0.0, 298.5, 11.0), (28.0, 6.0, 20.0)), "iec top")
    for x, y in [(-35.0, 150.0), (30.0, 150.0)]:
        top = safe_diff(top, cyl(1.6, 20.0, (x, y, h(y))), "m3 through")

    # simple text engraving placeholders (0.3 deep) as small bars
    engr = [(-28.0, 93.0, 18.0), (12.0, 93.0, 16.0), (-38.0, 203.0, 18.0), (10.0, 260.0, 20.0), (-18.0, 278.0, 30.0)]
    for x, y, w in engr:
        cut = box((x, y, h(y) + TOP_T - 0.15), (w, 2.2, 0.3))
        top = safe_diff(top, cut, f"engrave {x},{y}")
    return top


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


def save_stl(mesh, path):
    mesh.export(path)


def kb(path: Path) -> int:
    return int(round(path.stat().st_size / 1024.0)) if path.exists() else 0


def main():
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)

    base = build_base()
    interior = build_interior_features(base.copy())
    top = build_top_plate()

    full = safe_union([base.copy(), top.copy()], "full assembly")

    save_stl(base, STL_BASE)
    save_stl(interior, STL_INTERIOR)
    save_stl(top, STL_TOP)
    save_stl(full, STL_FULL)

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
