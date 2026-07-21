#!/usr/bin/env python3
"""
generate_render.py — Investor-ready photorealistic Blender render of Quad-Device Dock.

Run with:
    blender --background --python scripts/generate_render.py
Output: assets/quad-dock-render.png
"""
from __future__ import annotations

import math
from pathlib import Path

import bpy
from mathutils import Euler, Vector

ROOT        = Path(__file__).resolve().parents[1]
OUTPUT_PATH = ROOT / "assets" / "quad-dock-render.png"

# ─── unit helper ─────────────────────────────────────────────────────────────
MM = 0.001   # 1 mm expressed in Blender metre units

# =============================================================================
# EXACT DIMENSIONS — spec-accurate to 0.01 mm
# =============================================================================

# Enclosure body  (front = Y=0, rear = Y=LENGTH in Blender coords)
LENGTH   = 300 * MM     # Y axis: 0 → 300 mm
FRONT_W  = 110 * MM     # X width at front  (−55 mm … +55 mm, centred at 0)
REAR_W   = 140 * MM     # X width at rear   (−70 mm … +70 mm)
FRONT_H  =  12 * MM     # Z top-surface height at front
REAR_H   =  22 * MM     # Z top-surface height at rear
TOP_T    =   1.5 * MM   # aluminium top-plate thickness
CORNER_R =  20 * MM     # plan-view corner radius
CORNER_SEGS = 8         # arc segments per corner

# Zone 1 — Phone Qi dish (front-left)
# CX spec: "35 mm from left edge → X = −55 + 35 = −20 mm from centre"
# Using front-width reference, not the tapered width at the zone Y-position.
Z1_CX_MM  = -20.0   # fixed X from centre (mm)
Z1_Y_MM   =  57.5   # centre Y from front (mm)
Z1_W_MM   =  80.0   # pocket width  (X)
Z1_H_MM   =  55.0   # pocket height (Y)
Z1_R_MM   =  10.0   # pocket corner radius
Z1_D_MM   =   2.5   # recess depth into top plate

# Zone 2 — Buds Qi dish (front-centre)
Z2_CX_MM  =   0.0   # centred on dock width
Z2_Y_MM   =  57.5
Z2_W_MM   =  65.0
Z2_H_MM   =  55.0
Z2_R_MM   =  10.0
Z2_D_MM   =   2.5

# Zone 3 — Watch Cradle (rear-left)
# Same X reference convention as Zone 1.
Z3_CX_MM    = -20.0   # fixed X from centre (mm)
Z3_Y_MM     = 220.0   # centre Y from front (mm)
Z3_DIAM_MM  =  50.0   # pod cylinder diameter
Z3_CYL_H_MM =  12.0   # cylinder height
Z3_CONE_H_MM=   6.0   # cone height
Z3_TIP_D_MM =  10.0   # cone tip diameter
Z3_TILT_DEG =  30.0   # tilt toward front (degrees, positive = top leans to −Y)

# Zone 4 — Laptop Groove (rear-right)
# Right edge: 110 mm from left at rear = 70 − (70−40) = +40 mm from centre
Z4_R_X_MM  = +40.0   # right edge X from centre
Z4_L_X_MM  = +18.0   # left  edge X from centre  (groove width = 22 mm)
Z4_W_MM    =  22.0
Z4_D_MM    =  12.0   # groove depth (Y)
Z4_H_MM    =  20.0   # groove height (Z)

# LED bar — 4 sections under front lip
LED_SPAN_MM  = 290.0
LED_W_MM     =   8.0
LED_H_MM     =   3.0
LED_SECTIONS =   4
LED_GAP_MM   =   2.0

# Rubber feet ×4
FOOT_R_MM     =  7.5    # radius (15 mm dia)
FOOT_H_MM     =  3.0
FOOT_INSET_MM = 15.0    # inset from each edge (spec: 15 mm)

# =============================================================================
# Material colours  (linear sRGB)
# =============================================================================
_C_ABS      = (0.102, 0.102, 0.102, 1.0)   # #1A1A1A  matte black ABS
_C_ALUM     = (0.172, 0.172, 0.172, 1.0)   # #2C2C2C  brushed gunmetal aluminium
_C_SILICONE = (0.165, 0.165, 0.165, 1.0)   # #2A2A2A  dark silicone
_C_RUBBER   = (0.051, 0.051, 0.051, 1.0)   # #0D0D0D  near-black rubber
_C_LED      = (1.000, 0.894, 0.710, 1.0)   # #FFE4B5  warm-white LED
_C_ETCHED   = (0.133, 0.133, 0.133, 1.0)   # #222222  laser-etched text
_C_GROUND   = (0.973, 0.973, 0.973, 1.0)   # #F8F8F8  studio white ground


def log(msg: str) -> None:
    print(f"[quad-dock-render] {msg}")


# =============================================================================
# Coordinate helpers
# =============================================================================

def width_at_y(y: float) -> float:
    """Dock width (m) at Y-depth y (m)."""
    return FRONT_W + (REAR_W - FRONT_W) * y / LENGTH


def height_at_y(y: float) -> float:
    """Top-surface Z (m) at Y-depth y (m)."""
    return FRONT_H + (REAR_H - FRONT_H) * y / LENGTH


def look_at(obj: bpy.types.Object, target: Vector) -> None:
    """Point obj's local −Z axis at target."""
    direction = target - Vector(obj.location)
    obj.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


# =============================================================================
# Mesh helpers
# =============================================================================

def _norm2(dx: float, dy: float) -> tuple[float, float]:
    L = math.sqrt(dx * dx + dy * dy)
    return (dx / L, dy / L) if L > 1e-10 else (0.0, 1.0)


def rounded_polygon_outline(
    corners: list[tuple[float, float]],
    radius: float,
    n_segs: int,
) -> list[tuple[float, float]]:
    """
    2-D CCW rounded-corner outline of a convex polygon.

    Each sharp corner is replaced by a circular arc of (n_segs + 1) points.
    """
    n = len(corners)
    pts: list[tuple[float, float]] = []
    for i in range(n):
        A = corners[(i - 1) % n]
        B = corners[i]
        C = corners[(i + 1) % n]
        d1 = _norm2(B[0] - A[0], B[1] - A[1])
        d2 = _norm2(C[0] - B[0], C[1] - B[1])
        n1 = (-d1[1],  d1[0])
        n2 = (-d2[1],  d2[0])
        rx  = radius * (n2[0] - n1[0])
        ry  = radius * (n2[1] - n1[1])
        det = d1[0] * (-d2[1]) + d2[0] * d1[1]
        if abs(det) < 1e-9:
            pts.append(B)
            continue
        t      = (rx * (-d2[1]) + d2[0] * ry) / det
        cx_arc = B[0] + radius * n1[0] + t * d1[0]
        cy_arc = B[1] + radius * n1[1] + t * d1[1]
        ts_x   = cx_arc - radius * n1[0]
        ts_y   = cy_arc - radius * n1[1]
        te_x   = cx_arc - radius * n2[0]
        te_y   = cy_arc - radius * n2[1]
        a0 = math.atan2(ts_y - cy_arc, ts_x - cx_arc)
        a1 = math.atan2(te_y - cy_arc, te_x - cx_arc)
        da = a1 - a0
        if da < 0.0:
            da += 2.0 * math.pi
        for k in range(n_segs + 1):
            a = a0 + da * k / n_segs
            pts.append((cx_arc + radius * math.cos(a),
                        cy_arc + radius * math.sin(a)))
    return pts


def _rrect_pts(
    w: float, h: float, r: float, n_segs: int = 8,
) -> list[tuple[float, float]]:
    """CCW rounded-rectangle 2-D outline, centred at origin."""
    hw, hh = w / 2.0, h / 2.0
    pts: list[tuple[float, float]] = []
    for cx_a, cy_a, a_s, a_e in (
        ( hw - r, -hh + r, -math.pi / 2,  0.0          ),
        ( hw - r,  hh - r,  0.0,           math.pi / 2 ),
        (-hw + r,  hh - r,  math.pi / 2,   math.pi     ),
        (-hw + r, -hh + r,  math.pi,    3 * math.pi / 2 ),
    ):
        for k in range(n_segs + 1):
            a = a_s + (a_e - a_s) * k / n_segs
            pts.append((cx_a + r * math.cos(a), cy_a + r * math.sin(a)))
    return pts


def _build_prism(
    name: str,
    outline: list[tuple[float, float]],
    z_bot_fn,
    z_top_fn,
) -> bpy.types.Object:
    """
    Closed prism from 2-D CCW XY outline.

    z_bot_fn(y) / z_top_fn(y) return the Z coordinate for bottom/top rings.
    Face normals are outward (−Z bottom, +Z top, outward sides).
    """
    N = len(outline)
    verts: list[tuple] = []
    for x, y in outline:
        verts.append((x, y, z_bot_fn(y)))
    for x, y in outline:
        verts.append((x, y, z_top_fn(y)))
    faces: list[list[int]] = []
    faces.append(list(range(N - 1, -1, -1)))    # bottom  (CW from above)
    faces.append(list(range(N, 2 * N)))          # top     (CCW from above)
    for i in range(N):
        j = (i + 1) % N
        faces.append([i, j, N + j, N + i])      # sides
    mesh = bpy.data.meshes.new(name)
    obj  = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    mesh.from_pydata(verts, [], faces)
    mesh.validate(verbose=False)
    mesh.update()
    return obj


def _rrect_prism(
    name: str,
    cx: float, cy: float,
    w: float, h: float, r: float,
    z_bot: float, z_top: float,
    n_segs: int = 8,
) -> bpy.types.Object:
    """Flat-topped rounded-rectangle prism centred at (cx, cy)."""
    pts = [(cx + px, cy + py) for px, py in _rrect_pts(w, h, r, n_segs)]
    return _build_prism(name, pts, lambda _: z_bot, lambda _: z_top)


def _bool_diff(
    target: bpy.types.Object,
    cutter: bpy.types.Object,
) -> None:
    """Boolean difference (EXACT solver); removes cutter from scene."""
    cutter.hide_viewport = False
    cutter.hide_render   = True
    mod = target.modifiers.new(f"Bool_{cutter.name}", "BOOLEAN")
    mod.operation = "DIFFERENCE"
    mod.solver    = "EXACT"
    mod.object    = cutter
    bpy.context.view_layer.objects.active = target
    try:
        bpy.ops.object.modifier_apply(modifier=mod.name)
    except RuntimeError as exc:
        log(f"Boolean apply warning ({cutter.name}): {exc}")
    bpy.data.objects.remove(cutter, do_unlink=True)


def _add_bevel(
    obj: bpy.types.Object,
    width_mm: float,
    segs: int,
) -> None:
    """Angle-limited bevel for outer-edge softening (45° limit)."""
    mod = obj.modifiers.new("Bevel", "BEVEL")
    mod.limit_method = "ANGLE"
    mod.angle_limit  = math.radians(45.0)
    mod.width        = width_mm * MM
    mod.segments     = segs
    mod.profile      = 0.7


def _assign_mat(
    obj: bpy.types.Object,
    mat: bpy.types.Material,
) -> None:
    if obj.data.materials:
        obj.data.materials[0] = mat
    else:
        obj.data.materials.append(mat)


# =============================================================================
# Scene / render setup
# =============================================================================

def clear_scene() -> None:
    log("Clearing scene")
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for db in (bpy.data.meshes, bpy.data.materials, bpy.data.lights,
               bpy.data.curves, bpy.data.cameras):
        for blk in list(db):
            if blk.users == 0:
                db.remove(blk)


def setup_cycles() -> None:
    log("Configuring Cycles  —  192 samples, 3200 × 2133 px")
    scene = bpy.context.scene
    scene.render.engine        = "CYCLES"
    scene.cycles.samples       = 192

    # OIDN not available in apt Blender 4.0 — disable denoising
    scene.cycles.use_denoising = False
    try:
        scene.cycles.denoiser  = "NONE"
    except (AttributeError, TypeError):
        pass

    scene.render.resolution_x  = 3200
    scene.render.resolution_y  = 2133
    scene.render.image_settings.file_format = "PNG"
    scene.render.filepath      = str(OUTPUT_PATH)
    scene.unit_settings.system = "METRIC"
    scene.unit_settings.scale_length = 1.0

    # GPU selection
    cp = bpy.context.preferences.addons.get("cycles")
    if cp is None:
        scene.cycles.device = "CPU"
        log("GPU addon unavailable — CPU render")
        return
    prefs = cp.preferences
    for dtype in ("CUDA", "OPTIX", "HIP", "METAL", "ONEAPI"):
        try:
            prefs.compute_device_type = dtype
            prefs.get_devices()
            if any(d.type != "CPU" for d in prefs.devices):
                for d in prefs.devices:
                    if d.type != "CPU":
                        d.use = True
                scene.cycles.device = "GPU"
                log(f"GPU: {dtype}")
                return
        except Exception:
            continue
    scene.cycles.device = "CPU"
    log("No compatible GPU — CPU render")


# =============================================================================
# Materials  (PBR, spec-accurate)
# =============================================================================

def _pbsdf(name: str):
    mat  = bpy.data.materials.new(name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    return mat, bsdf


def _mat_abs():
    mat, b = _pbsdf("ABS_Matte_Black")
    b.inputs["Base Color"].default_value = _C_ABS
    b.inputs["Roughness"].default_value  = 0.90
    b.inputs["Metallic"].default_value   = 0.00
    return mat


def _mat_aluminum():
    """Brushed aluminium with noise-based anisotropic streaks."""
    mat, b = _pbsdf("Aluminum_Brushed")
    b.inputs["Base Color"].default_value  = _C_ALUM
    b.inputs["Metallic"].default_value    = 0.95
    b.inputs["Roughness"].default_value   = 0.15
    b.inputs["Anisotropic"].default_value = 0.70
    nt   = mat.node_tree
    tc   = nt.nodes.new("ShaderNodeTexCoord");  tc.location   = (-800, 200)
    mp   = nt.nodes.new("ShaderNodeMapping");   mp.location   = (-620, 200)
    ns   = nt.nodes.new("ShaderNodeTexNoise");  ns.location   = (-440, 200)
    ramp = nt.nodes.new("ShaderNodeValToRGB");  ramp.location = (-250, 200)
    mp.inputs["Scale"].default_value     = (220.0, 1.2, 1.2)
    ns.inputs["Scale"].default_value     = 340.0
    ns.inputs["Detail"].default_value    = 2.0
    ns.inputs["Roughness"].default_value = 0.3
    ramp.color_ramp.elements[0].position = 0.35
    ramp.color_ramp.elements[1].position = 0.70
    nt.links.new(tc.outputs["Object"],   mp.inputs["Vector"])
    nt.links.new(mp.outputs["Vector"],   ns.inputs["Vector"])
    nt.links.new(ns.outputs["Fac"],      ramp.inputs["Fac"])
    nt.links.new(ramp.outputs["Color"],  b.inputs["Roughness"])
    return mat


def _mat_silicone():
    mat, b = _pbsdf("Silicone_Dark")
    b.inputs["Base Color"].default_value = _C_SILICONE
    b.inputs["Roughness"].default_value  = 0.95
    b.inputs["Metallic"].default_value   = 0.00
    return mat


def _mat_rubber():
    mat, b = _pbsdf("Rubber_Black")
    b.inputs["Base Color"].default_value = _C_RUBBER
    b.inputs["Roughness"].default_value  = 1.00
    b.inputs["Metallic"].default_value   = 0.00
    return mat


def _mat_led():
    mat, b = _pbsdf("LED_Diffuser")
    b.inputs["Base Color"].default_value        = _C_LED
    b.inputs["Roughness"].default_value         = 0.45
    b.inputs["Emission Color"].default_value    = _C_LED
    b.inputs["Emission Strength"].default_value = 4.0
    return mat


def _mat_etched():
    mat, b = _pbsdf("Etched_Text")
    b.inputs["Base Color"].default_value = _C_ETCHED
    b.inputs["Roughness"].default_value  = 0.30
    b.inputs["Metallic"].default_value   = 0.50
    return mat


def _mat_ground():
    mat, b = _pbsdf("Studio_Ground")
    b.inputs["Base Color"].default_value = _C_GROUND
    b.inputs["Roughness"].default_value  = 0.05
    # specular (Blender 4.x uses 'Specular IOR Level' or 'Specular')
    for spec_key in ("Specular IOR Level", "Specular"):
        if spec_key in b.inputs:
            b.inputs[spec_key].default_value = 0.5
            break
    return mat


# =============================================================================
# Lighting  — Apple-style product photography
# =============================================================================

def _hex_rgb(h: str) -> tuple:
    h = h.lstrip("#")
    return (int(h[0:2], 16) / 255.0,
            int(h[2:4], 16) / 255.0,
            int(h[4:6], 16) / 255.0, 1.0)


def _area_light(
    name: str,
    location: tuple,
    size_x: float,
    size_y: float,
    energy: float,
    color: tuple,
    target: Vector,
) -> None:
    data = bpy.data.lights.new(name=name, type="AREA")
    data.shape  = "RECTANGLE"
    data.size   = size_x
    data.size_y = size_y
    data.energy = energy
    data.color  = color[:3]
    obj = bpy.data.objects.new(name=name, object_data=data)
    bpy.context.collection.objects.link(obj)
    obj.location = location
    look_at(obj, target)


# =============================================================================
# Zone labels  (laser-etched text, converted to mesh)
# =============================================================================

def _zone_label(
    label: str,
    location: tuple,
    size_mm: float,
    mat,
) -> None:
    bpy.ops.object.text_add(location=location)
    t = bpy.context.active_object
    t.data.body    = label
    t.data.size    = size_mm * MM
    t.data.extrude = 0.2 * MM
    t.data.align_x = "CENTER"
    bpy.ops.object.convert(target="MESH")
    m = bpy.context.active_object
    m.name = f"Text_{label}"
    _assign_mat(m, mat)


# =============================================================================
# Main
# =============================================================================

def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    clear_scene()
    setup_cycles()

    log("Creating materials")
    m_abs = _mat_abs()
    m_al  = _mat_aluminum()
    m_sil = _mat_silicone()
    m_rub = _mat_rubber()
    m_led = _mat_led()
    m_eth = _mat_etched()
    m_gnd = _mat_ground()

    # Dock scene centre — used for light targeting
    dock_centre = Vector((0.0, LENGTH / 2, FRONT_H / 2))

    # ── Rounded-trapezoid footprint ───────────────────────────────────────────
    # CCW corners: front-left → front-right → rear-right → rear-left
    trap_corners = [
        (-FRONT_W / 2, 0.0    ),
        ( FRONT_W / 2, 0.0    ),
        ( REAR_W  / 2, LENGTH ),
        (-REAR_W  / 2, LENGTH ),
    ]
    outline = rounded_polygon_outline(trap_corners, CORNER_R, CORNER_SEGS)

    # ── ABS base — proper wedge prism ─────────────────────────────────────────
    log("Building ABS base wedge")
    base = _build_prism(
        "Base_ABS", outline,
        z_bot_fn=lambda y: 0.0,
        z_top_fn=lambda y: height_at_y(y),
    )
    _assign_mat(base, m_abs)

    # ── Zone 4 — Laptop groove (rear-right) ───────────────────────────────────
    log("Cutting Zone 4 laptop groove")
    z4_cx = (Z4_L_X_MM + Z4_R_X_MM) / 2.0 * MM
    z4_cy = LENGTH - Z4_D_MM * MM / 2.0 + 0.5 * MM
    zone4_cut = _rrect_prism(
        "Zone4_Cutter", z4_cx, z4_cy,
        Z4_W_MM * MM, (Z4_D_MM + 1.0) * MM, 0.5 * MM,
        z_bot=-0.5 * MM, z_top=REAR_H + 0.5 * MM,
    )
    _bool_diff(base, zone4_cut)

    z4_sil = _rrect_prism(
        "Zone4_Silicone", z4_cx, LENGTH - Z4_D_MM * MM / 2.0,
        (Z4_W_MM - 2.0) * MM, Z4_D_MM * MM, 0.3 * MM,
        z_bot=0.5 * MM, z_top=REAR_H - 0.5 * MM,
    )
    _assign_mat(z4_sil, m_sil)

    # Small edge bevel on base outer geometry
    _add_bevel(base, 0.8, 3)

    # ── Aluminium top plate ───────────────────────────────────────────────────
    log("Building aluminium top plate (1.50 mm)")
    top_plate = _build_prism(
        "Top_Plate", outline,
        z_bot_fn=lambda y: height_at_y(y),
        z_top_fn=lambda y: height_at_y(y) + TOP_T,
    )
    _assign_mat(top_plate, m_al)

    # ── Zone 1 — Phone Qi dish  (front-left, rounded rectangle, 80 × 55 mm) ──
    log("Cutting Zone 1 phone dish  (−20 mm, Y = 57.5 mm)")
    z1_cx   = Z1_CX_MM * MM          # −20 mm from centre
    z1_y    = Z1_Y_MM  * MM          # 57.5 mm from front
    z1_ztop = height_at_y(z1_y) + TOP_T

    z1_cut = _rrect_prism(
        "Zone1_Cutter", z1_cx, z1_y,
        Z1_W_MM * MM, Z1_H_MM * MM, Z1_R_MM * MM,
        z_bot=z1_ztop - Z1_D_MM * MM,
        z_top=z1_ztop + 0.5 * MM,
    )
    _bool_diff(top_plate, z1_cut)

    z1_sil = _rrect_prism(
        "Zone1_Silicone", z1_cx, z1_y,
        (Z1_W_MM - 2.0) * MM, (Z1_H_MM - 2.0) * MM,
        max((Z1_R_MM - 1.0) * MM, 0.5 * MM),
        z_bot=z1_ztop - Z1_D_MM * MM,
        z_top=z1_ztop - Z1_D_MM * MM + 0.3 * MM,
    )
    _assign_mat(z1_sil, m_sil)

    # ── Zone 2 — Buds Qi dish  (front-centre, rounded rectangle, 65 × 55 mm) ─
    log("Cutting Zone 2 buds dish  (centred, Y = 57.5 mm)")
    z2_cx   = Z2_CX_MM * MM          # 0 — centred
    z2_y    = Z2_Y_MM  * MM
    z2_ztop = height_at_y(z2_y) + TOP_T

    z2_cut = _rrect_prism(
        "Zone2_Cutter", z2_cx, z2_y,
        Z2_W_MM * MM, Z2_H_MM * MM, Z2_R_MM * MM,
        z_bot=z2_ztop - Z2_D_MM * MM,
        z_top=z2_ztop + 0.5 * MM,
    )
    _bool_diff(top_plate, z2_cut)

    z2_sil = _rrect_prism(
        "Zone2_Silicone", z2_cx, z2_y,
        (Z2_W_MM - 2.0) * MM, (Z2_H_MM - 2.0) * MM,
        max((Z2_R_MM - 1.0) * MM, 0.5 * MM),
        z_bot=z2_ztop - Z2_D_MM * MM,
        z_top=z2_ztop - Z2_D_MM * MM + 0.3 * MM,
    )
    _assign_mat(z2_sil, m_sil)

    _add_bevel(top_plate, 0.5, 3)

    # ── Zone 3 — Watch cradle  (rear-left, teardrop pod, 30° tilt) ────────────
    log("Building Zone 3 watch cradle  (teardrop: cyl ∅50×12 mm + cone ∅50→∅10×6 mm)")
    z3_cx     = Z3_CX_MM * MM          # −20 mm from centre
    z3_y      = Z3_Y_MM  * MM
    z3_base_z = height_at_y(z3_y) + TOP_T
    cyl_r     = Z3_DIAM_MM / 2.0 * MM
    cyl_h     = Z3_CYL_H_MM  * MM
    cone_h    = Z3_CONE_H_MM * MM
    tip_r     = Z3_TIP_D_MM  / 2.0 * MM

    bpy.ops.mesh.primitive_cylinder_add(
        vertices=48, radius=cyl_r, depth=cyl_h,
        location=(z3_cx, z3_y, z3_base_z + cyl_h / 2.0),
    )
    cyl_obj = bpy.context.active_object
    cyl_obj.name = "_Z3_Cyl"

    bpy.ops.mesh.primitive_cone_add(
        vertices=48, radius1=cyl_r, radius2=tip_r, depth=cone_h,
        location=(z3_cx, z3_y, z3_base_z + cyl_h + cone_h / 2.0),
    )
    cone_obj = bpy.context.active_object
    cone_obj.name = "_Z3_Cone"

    bpy.ops.object.select_all(action="DESELECT")
    cyl_obj.select_set(True)
    cone_obj.select_set(True)
    bpy.context.view_layer.objects.active = cyl_obj
    bpy.ops.object.join()
    pod = bpy.context.active_object
    pod.name = "Zone3_Watch_Pod"

    # Tilt: pivot at pod base centre, top leans toward Y=0 (front)
    bpy.context.scene.cursor.location = (z3_cx, z3_y, z3_base_z)
    bpy.ops.object.origin_set(type="ORIGIN_CURSOR")
    pod.rotation_euler = Euler((math.radians(Z3_TILT_DEG), 0.0, 0.0), "XYZ")
    _assign_mat(pod, m_abs)

    # ── LED bar — 4 sections under front lip ──────────────────────────────────
    log("Adding LED bar (4 sections, warm white emissive)")
    section_len_mm = (LED_SPAN_MM - (LED_SECTIONS - 1) * LED_GAP_MM) / LED_SECTIONS
    # 290 − 3 × 2 = 284 mm total content → 284/4 = 71.0 mm per section (matches spec)
    x_start_mm = -LED_SPAN_MM / 2.0 + section_len_mm / 2.0

    led_y = -2.0 * MM            # peeks from under the front lip
    led_z =  LED_H_MM / 2.0 * MM

    for idx in range(LED_SECTIONS):
        sec_cx = (x_start_mm + idx * (section_len_mm + LED_GAP_MM)) * MM
        bpy.ops.mesh.primitive_cube_add(size=1.0, location=(sec_cx, led_y, led_z))
        sec = bpy.context.active_object
        sec.name = f"LED_Section_{idx + 1}"
        sec.scale = (section_len_mm * MM, LED_W_MM * MM, LED_H_MM * MM)
        bpy.ops.object.transform_apply(scale=True)
        _assign_mat(sec, m_led)

    # ── Rubber feet ×4 ────────────────────────────────────────────────────────
    log("Adding rubber feet (∅15 mm, 15 mm corner inset)")
    y_front = FOOT_INSET_MM * MM
    y_rear  = LENGTH - FOOT_INSET_MM * MM
    # Spec: X = left_at(Y) + 15mm  or  right_at(Y) − 15mm  (using tapered width)
    foot_positions = [
        (-width_at_y(y_front) / 2.0 + FOOT_INSET_MM * MM, y_front),   # front-left
        ( width_at_y(y_front) / 2.0 - FOOT_INSET_MM * MM, y_front),   # front-right
        (-width_at_y(y_rear)  / 2.0 + FOOT_INSET_MM * MM, y_rear ),   # rear-left
        ( width_at_y(y_rear)  / 2.0 - FOOT_INSET_MM * MM, y_rear ),   # rear-right
    ]
    for idx, (fx, fy) in enumerate(foot_positions, start=1):
        bpy.ops.mesh.primitive_cylinder_add(
            vertices=32, radius=FOOT_R_MM * MM, depth=FOOT_H_MM * MM,
            location=(fx, fy, -FOOT_H_MM * MM / 2.0),
        )
        foot = bpy.context.active_object
        foot.name = f"Foot_{idx}"
        _assign_mat(foot, m_rub)

    # ── Zone labels (laser-etched text) ───────────────────────────────────────
    log("Adding zone labels and wordmark")
    dz = 0.15 * MM   # slight Z offset above top surface

    _zone_label("PHONE",
                (z1_cx,
                 z1_y + Z1_H_MM * MM / 2.0 + 4 * MM,
                 height_at_y(z1_y) + TOP_T + dz),
                6.0, m_eth)
    _zone_label("BUDS",
                (z2_cx,
                 z2_y + Z2_H_MM * MM / 2.0 + 4 * MM,
                 height_at_y(z2_y) + TOP_T + dz),
                6.0, m_eth)
    _zone_label("WATCH",
                (z3_cx,
                 z3_y - 32 * MM,
                 height_at_y(z3_y) + TOP_T + dz),
                6.0, m_eth)
    z4_lbl_y = 250 * MM
    z4_lbl_x = (Z4_L_X_MM + Z4_R_X_MM) / 2.0 * MM
    _zone_label("LAPTOP",
                (z4_lbl_x, z4_lbl_y,
                 height_at_y(z4_lbl_y) + TOP_T + dz),
                6.0, m_eth)
    wm_y = 270 * MM
    _zone_label("Quad-Dock",
                (0.0, wm_y, height_at_y(wm_y) + TOP_T + dz),
                9.0, m_eth)

    # ── Studio ground plane (6 m × 6 m, near-white) ───────────────────────────
    log("Building studio ground")
    bpy.ops.mesh.primitive_plane_add(size=6.0, location=(0.0, LENGTH / 2, 0.0))
    gnd = bpy.context.active_object
    gnd.name = "Studio_Ground"
    _assign_mat(gnd, m_gnd)

    # ── World environment: pure white studio ──────────────────────────────────
    world = bpy.data.worlds["World"]
    world.use_nodes = True
    bg = world.node_tree.nodes["Background"]
    bg.inputs["Color"].default_value    = (1.0, 1.0, 1.0, 1.0)
    bg.inputs["Strength"].default_value = 1.0   # bright studio feel

    # ── Apple-style product photography lighting ──────────────────────────────
    log("Setting up studio lights (key / fill / rim / top-bounce)")

    # Key light: large upper-left softbox
    _area_light("Key_Light",
                location=(-0.8, -0.6, 0.9),
                size_x=2.0, size_y=2.0,
                energy=800.0,
                color=_hex_rgb("#FFF5E6"),
                target=dock_centre)

    # Fill light: right-side softer light
    _area_light("Fill_Light",
                location=(0.9, 0.2, 0.5),
                size_x=1.5, size_y=1.5,
                energy=300.0,
                color=_hex_rgb("#EAF4FF"),
                target=dock_centre)

    # Rim light: behind, separates product from background
    _area_light("Rim_Light",
                location=(0.0, 0.8, 0.6),
                size_x=0.5, size_y=0.5,
                energy=200.0,
                color=(1.0, 1.0, 1.0, 1.0),
                target=dock_centre)

    # Top bounce: simulates studio ceiling reflection
    _area_light("Top_Bounce",
                location=(0.0, LENGTH / 2, 1.2),
                size_x=3.0, size_y=2.0,
                energy=150.0,
                color=(1.0, 1.0, 1.0, 1.0),
                target=dock_centre)

    # ── Camera — zoomed out, full-product view ─────────────────────────────────
    log("Configuring camera  (−550 / −550 / 450 mm, 85 mm lens)")
    cam_loc    = Vector((-0.55, -0.55, 0.45))
    cam_target = Vector(( 0.00,  0.15, 0.015))
    bpy.ops.object.camera_add(location=cam_loc)
    cam = bpy.context.active_object
    cam.name      = "Product_Camera"
    cam.data.lens = 85.0   # mm, telephoto for compression
    look_at(cam, cam_target)
    bpy.context.scene.camera = cam

    # ── Render ─────────────────────────────────────────────────────────────────
    log(f"Rendering → {OUTPUT_PATH}")
    try:
        result = bpy.ops.render.render(write_still=True)
        if "FINISHED" in result:
            log("Render complete")
            log(f"Output: {OUTPUT_PATH}")
        else:
            log(f"Render returned: {result}")
    except Exception as exc:
        log(f"Render exception: {exc!r}")
        ri = bpy.data.images.get("Render Result")
        if ri is not None:
            ri.save_render(str(OUTPUT_PATH))
            log(f"Partial render saved: {OUTPUT_PATH}")
        else:
            raise


if __name__ == "__main__":
    main()
