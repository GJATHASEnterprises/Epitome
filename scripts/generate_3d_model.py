#!/usr/bin/env python3
"""Generate visual-reference STL/DXF/SVG exports for the Penta Dock.

All geometry is generated from watertight trimesh primitives and concatenation.
"""
from __future__ import annotations

import math
import shutil
import subprocess
import sys
from pathlib import Path


def _ensure_deps() -> None:
    """Auto-install required packages if missing."""
    for pkg in ["trimesh", "numpy"]:
        try:
            __import__(pkg)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", pkg, "-q"])

    try:
        import ezdxf  # noqa: F401
    except ImportError:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "ezdxf", "-q"])
        except Exception:
            pass


_ensure_deps()

import numpy as np  # noqa: E402
import trimesh  # noqa: E402

try:
    import ezdxf  # type: ignore  # noqa: E402
except Exception:
    ezdxf = None


ROOT = Path(__file__).resolve().parents[1]
EXPORT_DIR = ROOT / "assets" / "export"

STL_BASE = EXPORT_DIR / "penta-dock-base.stl"
STL_INTERIOR = EXPORT_DIR / "penta-dock-base-interior.stl"
STL_TOP = EXPORT_DIR / "penta-dock-top-plate.stl"
STL_FULL = EXPORT_DIR / "penta-dock-full-assembly.stl"
DXF_TOP = EXPORT_DIR / "penta-dock-top-plate.dxf"
SVG_TOP = EXPORT_DIR / "penta-dock-top-plate.svg"

# Backwards-compat copies under old quad-dock-* names
_COMPAT = {
    STL_BASE:     EXPORT_DIR / "quad-dock-base.stl",
    STL_INTERIOR: EXPORT_DIR / "quad-dock-base-interior.stl",
    STL_TOP:      EXPORT_DIR / "quad-dock-top-plate.stl",
    STL_FULL:     EXPORT_DIR / "quad-dock-full-assembly.stl",
    DXF_TOP:      EXPORT_DIR / "quad-dock-top-plate.dxf",
    SVG_TOP:      EXPORT_DIR / "quad-dock-top-plate.svg",
}

# New dock geometry — compact rectangular design
DOCK_W = 250.0
DOCK_D = 100.0
WALL_T = 3.0

# Slot dimensions
LAPTOP_SLOT_W = 35.0
LAPTOP_SLOT_L = 400.0
LAPTOP_SLOT_H = 95.0
TABLET_SLOT_W = 20.0
TABLET_SLOT_L = 290.0
TABLET_SLOT_H = 75.0

# Centre platform
PLATFORM_W = 180.0
PLATFORM_D = 110.0
RISER_H = 50.0
STEP_H = 15.0
STEP_TAPER = 40.0

# PSU cavity
PSU_W = 199.0
PSU_D = 98.0
PSU_H = 30.0

# Rear rail and front fascia
REAR_RAIL_H = 25.0
FASCIA_H = 20.0
CORNER_R = 10.0

# Base and detailing
BASE_T = 3.0
FRONT_STRIP_D = 3.0
REAR_STRIP_D = 3.0
M3_HOLE_R = 1.6


# ---------------------------------------------------------------------------
# Primitive helpers
# ---------------------------------------------------------------------------

def _box(center: tuple[float, float, float], size: tuple[float, float, float]) -> trimesh.Trimesh:
    mesh = trimesh.creation.box(extents=size)
    mesh.apply_translation(center)
    return mesh


def _cyl(radius: float, height: float, center: tuple[float, float, float], sections: int = 48) -> trimesh.Trimesh:
    mesh = trimesh.creation.cylinder(radius=radius, height=height, sections=sections)
    mesh.apply_translation(center)
    return mesh


def _rounded_plate(w: float, d: float, t: float, r: float) -> trimesh.Trimesh:
    """Rounded rectangle from overlapping watertight primitives (no booleans)."""
    parts = [
        _box((w / 2.0, d / 2.0, t / 2.0), (w - 2.0 * r, d, t)),
        _box((w / 2.0, d / 2.0, t / 2.0), (w, d - 2.0 * r, t)),
    ]
    for cx, cy in [
        (r, r),
        (w - r, r),
        (w - r, d - r),
        (r, d - r),
    ]:
        parts.append(_cyl(r, t, (cx, cy, t / 2.0), sections=40))
    return trimesh.util.concatenate(parts)


def _u_slot(x0: float, x1: float, y0: float, y1: float, h: float, wall_t: float) -> trimesh.Trimesh:
    """Create a U-channel slot: bottom + two side walls + rear wall (front and top open)."""
    w = x1 - x0
    d = y1 - y0
    parts = []

    # Floor liner
    parts.append(_box(((x0 + x1) / 2.0, (y0 + y1) / 2.0, BASE_T + wall_t / 2.0), (w, d, wall_t)))

    wall_h = max(0.0, h - BASE_T)
    zc = BASE_T + wall_h / 2.0

    # Left wall
    parts.append(_box((x0 + wall_t / 2.0, (y0 + y1) / 2.0, zc), (wall_t, d, wall_h)))
    # Right wall
    parts.append(_box((x1 - wall_t / 2.0, (y0 + y1) / 2.0, zc), (wall_t, d, wall_h)))
    # Rear wall
    parts.append(_box(((x0 + x1) / 2.0, y1 - wall_t / 2.0, zc), (w, wall_t, wall_h)))

    return trimesh.util.concatenate(parts)


# ---------------------------------------------------------------------------
# Geometry builders
# ---------------------------------------------------------------------------

def build_base() -> trimesh.Trimesh:
    parts = [_rounded_plate(DOCK_W, DOCK_D, BASE_T, CORNER_R)]

    # Front fascia strip (full width, low strip at front)
    parts.append(
        _box((DOCK_W / 2.0, FRONT_STRIP_D / 2.0, FASCIA_H / 2.0), (DOCK_W, FRONT_STRIP_D, FASCIA_H))
    )

    # Rear rail (full width, low rail at rear)
    parts.append(
        _box((DOCK_W / 2.0, DOCK_D - REAR_STRIP_D / 2.0, REAR_RAIL_H / 2.0), (DOCK_W, REAR_STRIP_D, REAR_RAIL_H))
    )
    return trimesh.util.concatenate(parts)


def build_interior_features() -> trimesh.Trimesh:
    parts: list[trimesh.Trimesh] = []

    laptop_slot_d = min(DOCK_D - 10.0, LAPTOP_SLOT_L)   # 90 mm rendered depth, 400 mm device-length reference
    tablet_slot_d = min(DOCK_D - 30.0, TABLET_SLOT_L)   # 70 mm rendered depth, 290 mm device-length reference

    # Left laptop slot box 35×90×95
    parts.append(_u_slot(0.0, LAPTOP_SLOT_W, 5.0, 5.0 + laptop_slot_d, LAPTOP_SLOT_H, WALL_T))

    # Right tablet slot box 20×70×75
    parts.append(_u_slot(DOCK_W - TABLET_SLOT_W, DOCK_W, 15.0, 15.0 + tablet_slot_d, TABLET_SLOT_H, WALL_T))

    # Centre riser base (solid for STL reference)
    step1_x0 = (DOCK_W - PLATFORM_W) / 2.0
    step1_x1 = step1_x0 + PLATFORM_W
    # PLATFORM_D is 110 mm by design; we center it against the 100 mm body envelope
    # so the overhang is symmetric (+/-5 mm) rather than only rearward.
    step1_y0 = (DOCK_D - PLATFORM_D) / 2.0
    step1_y1 = step1_y0 + PLATFORM_D
    parts.append(
        _box(((step1_x0 + step1_x1) / 2.0, (step1_y0 + step1_y1) / 2.0, RISER_H / 2.0), (PLATFORM_W, PLATFORM_D, RISER_H))
    )

    # Step 1
    parts.append(
        _box(((step1_x0 + step1_x1) / 2.0, (step1_y0 + step1_y1) / 2.0, RISER_H + STEP_H / 2.0), (PLATFORM_W, PLATFORM_D, STEP_H))
    )

    # Step 2
    step2_w = PLATFORM_W - STEP_TAPER
    step2_d = 100.0
    step2_x0 = (DOCK_W - step2_w) / 2.0
    parts.append(
        _box((step2_x0 + step2_w / 2.0, step2_d / 2.0, RISER_H + STEP_H + STEP_H / 2.0), (step2_w, step2_d, STEP_H))
    )

    # Step 3
    step3_w = PLATFORM_W - 2.0 * STEP_TAPER
    step3_d = 80.0
    step3_x0 = (DOCK_W - step3_w) / 2.0
    parts.append(
        _box((step3_x0 + step3_w / 2.0, step3_d / 2.0, RISER_H + 2.0 * STEP_H + STEP_H / 2.0), (step3_w, step3_d, STEP_H))
    )

    return trimesh.util.concatenate(parts)


def build_top_plate() -> trimesh.Trimesh:
    """Top-surface features STL (kept output path for compatibility)."""
    parts: list[trimesh.Trimesh] = []

    # Watch cradle pod as a raised oval on step 3
    pod = trimesh.creation.icosphere(subdivisions=2, radius=1.0)
    pod.apply_scale([25.0, 17.5, 4.0])
    pod.apply_translation([DOCK_W / 2.0, 58.0, RISER_H + 3.0 * STEP_H + 4.0])
    parts.append(pod)

    # Silicone pad guides (thin raised references)
    parts.append(_box((DOCK_W / 2.0, 52.0, RISER_H + STEP_H + 0.4), (160.0, 90.0, 0.8)))
    parts.append(_box((DOCK_W / 2.0, 50.0, RISER_H + 2.0 * STEP_H + 0.4), (120.0, 80.0, 0.8)))

    # Slot cable grommet collars (top cap references)
    parts.append(_cyl(4.0, 2.0, (LAPTOP_SLOT_W / 2.0, 84.0, LAPTOP_SLOT_H + 1.0), sections=30))
    parts.append(_cyl(3.5, 2.0, (DOCK_W - TABLET_SLOT_W / 2.0, 74.0, TABLET_SLOT_H + 1.0), sections=30))

    return trimesh.util.concatenate(parts)


def write_top_plate_dxf_and_svg() -> None:
    if ezdxf is None:
        print("[warn] ezdxf unavailable; skipping DXF/SVG export")
        return

    doc = ezdxf.new("R2018")
    msp = doc.modelspace()
    layers = {
        "OUTLINE": 7,
        "OPENINGS": 1,
        "STEPS": 5,
        "HOLES": 3,
        "ANNOTATIONS": 4,
        "CENTER": 8,
        "TITLE": 6,
    }
    for name, color in layers.items():
        if name not in doc.layers:
            doc.layers.new(name, dxfattribs={"color": color})

    # Outer rectangle
    outline = [(0, 0), (DOCK_W, 0), (DOCK_W, DOCK_D), (0, DOCK_D), (0, 0)]
    msp.add_lwpolyline(outline, dxfattribs={"layer": "OUTLINE"})

    # Slot openings (top-view references)
    msp.add_lwpolyline([(0, 5), (LAPTOP_SLOT_W, 5), (LAPTOP_SLOT_W, 95), (0, 95), (0, 5)], dxfattribs={"layer": "OPENINGS"})
    msp.add_lwpolyline([
        (DOCK_W - TABLET_SLOT_W, 15),
        (DOCK_W, 15),
        (DOCK_W, 85),
        (DOCK_W - TABLET_SLOT_W, 85),
        (DOCK_W - TABLET_SLOT_W, 15),
    ], dxfattribs={"layer": "OPENINGS"})

    # Step outlines
    c = DOCK_W / 2.0
    step1 = [(c - 90, 0), (c + 90, 0), (c + 90, 100), (c - 90, 100), (c - 90, 0)]
    step2 = [(c - 70, 0), (c + 70, 0), (c + 70, 100), (c - 70, 100), (c - 70, 0)]
    step3 = [(c - 50, 0), (c + 50, 0), (c + 50, 80), (c - 50, 80), (c - 50, 0)]
    msp.add_lwpolyline(step1, dxfattribs={"layer": "STEPS"})
    msp.add_lwpolyline(step2, dxfattribs={"layer": "STEPS"})
    msp.add_lwpolyline(step3, dxfattribs={"layer": "STEPS"})

    # IEC C13 cutout on rear rail (28×20, centred)
    iec_x0 = DOCK_W / 2.0 - 14.0
    iec_x1 = DOCK_W / 2.0 + 14.0
    msp.add_lwpolyline([(iec_x0, 80), (iec_x1, 80), (iec_x1, 100), (iec_x0, 100), (iec_x0, 80)], dxfattribs={"layer": "OPENINGS"})

    # Cable grommet holes
    msp.add_circle(center=(LAPTOP_SLOT_W / 2.0, 84.0), radius=4.0, dxfattribs={"layer": "HOLES"})
    msp.add_circle(center=(DOCK_W - TABLET_SLOT_W / 2.0, 74.0), radius=3.5, dxfattribs={"layer": "HOLES"})

    # M3 mounting holes
    m3_pts = [(18.0, 18.0), (DOCK_W - 18.0, 18.0), (18.0, DOCK_D - 18.0), (DOCK_W - 18.0, DOCK_D - 18.0)]
    for x, y in m3_pts:
        msp.add_circle(center=(x, y), radius=M3_HOLE_R, dxfattribs={"layer": "HOLES"})

    # Dimension/center annotations
    msp.add_line((DOCK_W / 2.0, -12), (DOCK_W / 2.0, DOCK_D + 12), dxfattribs={"layer": "CENTER"})
    msp.add_line((-12, DOCK_D / 2.0), (DOCK_W + 12, DOCK_D / 2.0), dxfattribs={"layer": "CENTER"})
    msp.add_text("250.0 mm overall width", dxfattribs={"height": 3.8, "layer": "ANNOTATIONS"}).set_placement((80, -16))
    msp.add_text("100.0 mm overall depth", dxfattribs={"height": 3.8, "layer": "ANNOTATIONS"}).set_placement((DOCK_W + 8, 45))
    msp.add_text("L Slot 35 mm", dxfattribs={"height": 3.2, "layer": "ANNOTATIONS"}).set_placement((4, 2))
    msp.add_text("R Slot 20 mm", dxfattribs={"height": 3.2, "layer": "ANNOTATIONS"}).set_placement((DOCK_W - 38, 2))
    msp.add_text("Step widths: 180 / 140 / 100 mm", dxfattribs={"height": 3.2, "layer": "ANNOTATIONS"}).set_placement((65, 108))

    # Title block (updated)
    tx = DOCK_W + 24
    ty = 96
    title_lines = [
        "PENTA DOCK TOP VIEW",
        "Material: Full ABS (Matte Black)",
        "Outer: 250 x 100 mm | Corner R10",
        "IEC C13 cutout: 28 x 20 mm centered (rear rail)",
        "M3 mounting holes and slot grommets shown",
        "Rev: 2.0 | Date: 2026-08-25",
    ]
    for i, line in enumerate(title_lines):
        msp.add_text(line, dxfattribs={"height": 3.4, "layer": "TITLE"}).set_placement((tx, ty - i * 6))

    doc.saveas(DXF_TOP)

    # Simple SVG companion
    svg = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="-20 -30 390 180" width="390mm" height="180mm">',
        '<rect x="-20" y="-30" width="390" height="180" fill="white"/>',
        f'<rect x="0" y="0" width="{DOCK_W}" height="{DOCK_D}" fill="none" stroke="black" stroke-width="0.8"/>',
        f'<rect x="0" y="5" width="{LAPTOP_SLOT_W}" height="90" fill="none" stroke="red" stroke-width="0.6"/>',
        f'<rect x="{DOCK_W - TABLET_SLOT_W}" y="15" width="{TABLET_SLOT_W}" height="70" fill="none" stroke="red" stroke-width="0.6"/>',
        f'<rect x="{DOCK_W / 2.0 - 90}" y="0" width="180" height="100" fill="none" stroke="blue" stroke-width="0.5"/>',
        f'<rect x="{DOCK_W / 2.0 - 70}" y="0" width="140" height="100" fill="none" stroke="blue" stroke-width="0.5"/>',
        f'<rect x="{DOCK_W / 2.0 - 50}" y="0" width="100" height="80" fill="none" stroke="blue" stroke-width="0.5"/>',
        f'<rect x="{DOCK_W / 2.0 - 14}" y="80" width="28" height="20" fill="none" stroke="purple" stroke-width="0.6"/>',
        '</svg>',
    ]
    SVG_TOP.write_text("\n".join(svg), encoding="utf-8")


def kb(path: Path) -> int:
    return int(round(path.stat().st_size / 1024.0)) if path.exists() else 0


def main() -> None:
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)

    base = build_base()
    interior = build_interior_features()
    top = build_top_plate()
    full = trimesh.util.concatenate([base, interior, top])

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

    # Write backwards-compat copies under quad-dock-* names
    for src, dst in _COMPAT.items():
        if src.exists():
            shutil.copy2(src, dst)


if __name__ == "__main__":
    main()
