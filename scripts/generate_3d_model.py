#!/usr/bin/env python3
"""
Generate a 3D model of the Quad-Dock and export it as a GLB file.

Usage:
    python scripts/generate_3d_model.py

Output:
    assets/quad-dock-model.glb
"""
from __future__ import annotations

import struct
import json
from pathlib import Path

import numpy as np

try:
    import trimesh
    import trimesh.creation
    import trimesh.transformations as tf
except ImportError as exc:
    raise SystemExit(
        "trimesh is required. Install with: pip install trimesh"
    ) from exc

# ---------------------------------------------------------------------------
# Output path
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = ROOT / "assets" / "quad-dock-model.glb"

# ---------------------------------------------------------------------------
# Colour helpers
# ---------------------------------------------------------------------------

def rgba(hex_color: str, alpha: float = 1.0) -> list[float]:
    """Convert #rrggbb hex to [r, g, b, a] list (0–1 range)."""
    h = hex_color.lstrip("#")
    r, g, b = int(h[0:2], 16) / 255, int(h[2:4], 16) / 255, int(h[4:6], 16) / 255
    return [r, g, b, alpha]


# ---------------------------------------------------------------------------
# Geometry helpers
# ---------------------------------------------------------------------------

def make_wedge(
    len_z: float,
    width_front: float,
    width_rear: float,
    height_front: float,
    height_rear: float,
) -> trimesh.Trimesh:
    """
    Build a trapezoidal wedge (tapered box) as a watertight mesh.

    The wedge spans:
      z = 0  → front  (width_front wide, height_front tall)
      z = len_z → rear (width_rear wide, height_rear tall)

    Origin at the left-front-bottom corner.
    """
    # 8 corners
    v = np.array([
        # Front face (z=0)
        [0,           0,            0],   # 0 front-left-bottom
        [width_front, 0,            0],   # 1 front-right-bottom
        [width_front, height_front, 0],   # 2 front-right-top
        [0,           height_front, 0],   # 3 front-left-top
        # Rear face (z=len_z)
        [0,           0,            len_z],   # 4 rear-left-bottom
        [width_rear,  0,            len_z],   # 5 rear-right-bottom
        [width_rear,  height_rear,  len_z],   # 6 rear-right-top
        [0,           height_rear,  len_z],   # 7 rear-left-top
    ], dtype=np.float64)

    # 12 triangles (6 faces × 2 triangles each), winding order: CCW for outward normals
    f = np.array([
        # Bottom
        [0, 5, 4], [0, 1, 5],
        # Top
        [3, 6, 7], [3, 2, 6],
        # Front
        [0, 2, 1], [0, 3, 2],
        # Rear
        [4, 5, 6], [4, 6, 7],
        # Left
        [0, 4, 7], [0, 7, 3],
        # Right
        [1, 6, 5], [1, 2, 6],
    ], dtype=np.int64)

    mesh = trimesh.Trimesh(vertices=v, faces=f, process=False)
    mesh.fix_normals()
    return mesh


def make_cylinder_z(radius: float, height: float, sections: int = 32) -> trimesh.Trimesh:
    """Cylinder aligned along the Z axis, centred at origin."""
    cyl = trimesh.creation.cylinder(radius=radius, height=height, sections=sections)
    return cyl


def make_box(lx: float, ly: float, lz: float) -> trimesh.Trimesh:
    """
    Axis-aligned box with corner at origin, dimensions lx × ly × lz.
    """
    v = np.array([
        [0,  0,  0],
        [lx, 0,  0],
        [lx, ly, 0],
        [0,  ly, 0],
        [0,  0,  lz],
        [lx, 0,  lz],
        [lx, ly, lz],
        [0,  ly, lz],
    ], dtype=np.float64)
    f = np.array([
        [0, 2, 1], [0, 3, 2],  # bottom (-y)
        [4, 5, 6], [4, 6, 7],  # top    (+y)
        [0, 1, 5], [0, 5, 4],  # front  (-z)
        [2, 3, 7], [2, 7, 6],  # rear   (+z)
        [0, 4, 7], [0, 7, 3],  # left   (-x)
        [1, 2, 6], [1, 6, 5],  # right  (+x)
    ], dtype=np.int64)
    mesh = trimesh.Trimesh(vertices=v, faces=f, process=False)
    mesh.fix_normals()
    return mesh


def translate(mesh: trimesh.Trimesh, x: float, y: float, z: float) -> trimesh.Trimesh:
    """Return a new mesh translated by (x, y, z)."""
    m = mesh.copy()
    m.apply_translation([x, y, z])
    return m


def rotate_x(mesh: trimesh.Trimesh, angle_deg: float) -> trimesh.Trimesh:
    """Return a new mesh rotated around the X axis."""
    m = mesh.copy()
    mat = tf.rotation_matrix(np.radians(angle_deg), [1, 0, 0])
    m.apply_transform(mat)
    return m


# ---------------------------------------------------------------------------
# Dock dimensions (millimetres)
# ---------------------------------------------------------------------------

DL          = 300.0   # length (Z)
DW_FRONT    = 110.0   # width at front
DW_REAR     = 140.0   # width at rear
DH_FRONT    = 12.0    # height at front
DH_REAR     = 22.0    # height at rear
TP_THICK    = 2.5     # top-plate thickness
TP_INSET    = 4.0     # top-plate inset from body edges

# Zone pocket radii & positions (x = left-right, z = front-rear on top surface)
Z1_X, Z1_Z = 30.0,  70.0   # Zone 1 — Phone (left-front)
Z2_X, Z2_Z = 75.0,  70.0   # Zone 2 — Buds  (centre-front)
Z3_X, Z3_Z = 32.0, 220.0   # Zone 3 — Watch  (rear-left)
Z4_X, Z4_Z = 95.0, 235.0   # Zone 4 — Laptop (rear-right)

QI_R       = 35.0   # Qi pad dish radius
QI_DEPTH   = 2.5    # Qi pad dish depth

# Laptop groove
LAP_W = 22.0    # groove width
LAP_D = 12.0    # groove depth
LAP_L = 64.0    # groove length (front-back)

# Watch cradle elevation
WATCH_ELEV = 5.0    # mm above top plate

# Rubber feet
FOOT_R  = 6.0   # foot radius
FOOT_H  = 2.0   # foot height

# LED channel (underside of front lip)
LED_W  = DW_FRONT - 6.0
LED_H  = 3.5
LED_D  = 8.0

# Vent slots on underside
VENT_W  = 18.0
VENT_H  = 2.0
VENT_D  = 40.0

# ---------------------------------------------------------------------------
# Build scene
# ---------------------------------------------------------------------------

def build_model() -> dict[str, trimesh.Trimesh]:
    """Return a dict of {name: mesh} for all dock parts."""

    parts: dict[str, trimesh.Trimesh] = {}

    # ---- 1. ABS main body ------------------------------------------------
    print("  Building ABS main body …")
    body = make_wedge(
        len_z=DL,
        width_front=DW_FRONT,
        width_rear=DW_REAR,
        height_front=DH_FRONT,
        height_rear=DH_REAR,
    )
    parts["body"] = body

    # ---- 2. Aluminium top plate ------------------------------------------
    print("  Building top plate …")
    # Interpolate width/height at front and rear of top plate region
    tp_wf = DW_FRONT - TP_INSET * 2
    tp_wr = DW_REAR  - TP_INSET * 2
    top_plate = make_wedge(
        len_z=DL - TP_INSET * 2,
        width_front=tp_wf,
        width_rear=tp_wr,
        height_front=TP_THICK,
        height_rear=TP_THICK,
    )
    # Position on top of the body
    top_plate = translate(top_plate, TP_INSET, DH_FRONT, TP_INSET)
    parts["top_plate"] = top_plate

    # ---- 3. Zone 1 — Phone Qi pocket (circular dish) ----------------------
    print("  Building Zone 1 — Phone Qi pocket …")
    z1_dish = trimesh.creation.cylinder(
        radius=QI_R, height=QI_DEPTH, sections=48
    )
    # Cylinder is centred at origin; translate to correct position on top surface
    z1_y = DH_FRONT + TP_THICK / 2
    # Interpolate dock height at z=Z1_Z
    z1_body_h = DH_FRONT + (DH_REAR - DH_FRONT) * Z1_Z / DL
    z1_dish = translate(z1_dish, Z1_X, z1_body_h + TP_THICK - QI_DEPTH / 2, Z1_Z)
    parts["zone1_pocket"] = z1_dish

    # ---- 4. Zone 2 — Buds Qi pocket (circular dish) -----------------------
    print("  Building Zone 2 — Buds Qi pocket …")
    z2_body_h = DH_FRONT + (DH_REAR - DH_FRONT) * Z2_Z / DL
    z2_dish = trimesh.creation.cylinder(
        radius=QI_R - 4, height=QI_DEPTH, sections=48
    )
    z2_dish = translate(z2_dish, Z2_X, z2_body_h + TP_THICK - QI_DEPTH / 2, Z2_Z)
    parts["zone2_pocket"] = z2_dish

    # ---- 5. Zone 3 — Watch cradle (elevated teardrop pod, 30° tilt) -------
    print("  Building Zone 3 — Watch cradle …")
    # Teardrop approximation: elongated cylinder
    cradle_base = trimesh.creation.cylinder(radius=18, height=WATCH_ELEV, sections=48)
    # Scale to teardrop (taller than wide)
    scale_mat = np.eye(4)
    scale_mat[0, 0] = 0.75   # narrow x axis
    scale_mat[2, 2] = 1.30   # elongate z axis
    cradle_base.apply_transform(scale_mat)
    # Tilt 30° forward (rotate around X axis so it tips toward front)
    cradle_base = rotate_x(cradle_base, 30)
    z3_body_h = DH_FRONT + (DH_REAR - DH_FRONT) * Z3_Z / DL
    cradle_base = translate(cradle_base, Z3_X, z3_body_h + TP_THICK + WATCH_ELEV / 2, Z3_Z)
    parts["zone3_cradle"] = cradle_base

    # Inductive watch charging puck (small disc on top of cradle)
    watch_puck = trimesh.creation.cylinder(radius=14, height=2.5, sections=36)
    watch_puck = translate(watch_puck, Z3_X, z3_body_h + TP_THICK + WATCH_ELEV, Z3_Z)
    parts["zone3_puck"] = watch_puck

    # ---- 6. Zone 4 — Laptop groove (rectangular slot) --------------------
    print("  Building Zone 4 — Laptop groove …")
    lap_groove = make_box(LAP_W, LAP_D, LAP_L)
    z4_body_h = DH_FRONT + (DH_REAR - DH_FRONT) * Z4_Z / DL
    # Position groove: centred at Z4_X, Z4_Z on top surface, sinking downward
    lap_groove = translate(
        lap_groove,
        Z4_X - LAP_W / 2,
        z4_body_h + TP_THICK - LAP_D,
        Z4_Z - LAP_L / 2,
    )
    parts["zone4_groove"] = lap_groove

    # ---- 7. LED bar channel (underside front lip) -------------------------
    print("  Building LED bar channel …")
    led_channel = make_box(LED_W, LED_H, LED_D)
    # Centred on the front lip, underneath
    led_channel = translate(led_channel, (DW_FRONT - LED_W) / 2, 0, 0)
    parts["led_channel"] = led_channel

    # ---- 8. Rubber feet (4 cylinders, underside corners) ------------------
    print("  Building rubber feet …")
    foot_positions = [
        (10,            10),             # front-left
        (DW_FRONT - 10, 10),             # front-right
        (10,            DL - 10),        # rear-left
        (DW_REAR  - 10, DL - 10),        # rear-right
    ]
    for i, (fx, fz) in enumerate(foot_positions):
        foot = trimesh.creation.cylinder(radius=FOOT_R, height=FOOT_H, sections=24)
        foot = translate(foot, fx, -FOOT_H / 2, fz)
        parts[f"foot_{i}"] = foot

    # ---- 9. Cooling vents (6 rectangular slots on underside) --------------
    print("  Building cooling vents …")
    vent_z_start = 60.0
    for i in range(6):
        vent = make_box(VENT_W, VENT_H, VENT_D)
        vx = 15.0 + i * 22.0
        vent = translate(vent, vx, 0, vent_z_start + i * 32.0)
        parts[f"vent_{i}"] = vent

    return parts


# ---------------------------------------------------------------------------
# Assign PBR materials and export GLB
# ---------------------------------------------------------------------------

# Material definitions: name → (base_color_hex, metallic, roughness, emissive_hex)
MATERIALS: dict[str, tuple[str, float, float, str | None]] = {
    "body":         ("#1a1d22", 0.05, 0.85, None),       # matte black ABS
    "top_plate":    ("#2d3240", 0.80, 0.30, None),       # brushed aluminium (dark)
    "zone1_pocket": ("#1c2028", 0.05, 0.70, None),       # silicone pad
    "zone2_pocket": ("#1c2028", 0.05, 0.70, None),
    "zone3_cradle": ("#1a1d22", 0.05, 0.75, None),
    "zone3_puck":   ("#252a30", 0.10, 0.65, None),
    "zone4_groove": ("#151820", 0.05, 0.80, None),
    "led_channel":  ("#2a2010", 0.05, 0.50, "#ffcc44"),  # emissive warm amber
}


def _mat_for(name: str) -> tuple[str, float, float, str | None]:
    """Return material definition for the given part name, with sensible defaults."""
    for key, mat in MATERIALS.items():
        if name.startswith(key):
            return mat
    # Default: matte black
    return ("#1a1d22", 0.05, 0.85, None)


def export_glb(parts: dict[str, trimesh.Trimesh], output_path: Path) -> None:
    """Combine all parts into a single trimesh scene and export as GLB."""
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

    # Center scene at origin
    bounds = scene.bounds
    if bounds is not None:
        center = (bounds[0] + bounds[1]) / 2
        scene.apply_translation(-center)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    print(f"  Exporting scene with {len(parts)} parts …")
    exported = scene.export(file_type="glb")
    output_path.write_bytes(exported)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    print("Quad-Dock 3D model generator starting …")
    print(f"Output: {OUTPUT_PATH}")
    print()

    parts = build_model()
    print()
    print(f"Built {len(parts)} mesh parts.")

    print("Exporting GLB …")
    export_glb(parts, OUTPUT_PATH)

    size_kb = OUTPUT_PATH.stat().st_size // 1024
    print(f"\n✓  Saved {OUTPUT_PATH}  ({size_kb} KB)")
    print("    Open on GitHub to view the interactive 3D model.")


if __name__ == "__main__":
    main()
