#!/usr/bin/env python3
"""
generate_render.py — Photorealistic Blender render of Quad-Device Dock.

Complete spec-accurate rewrite.  Run with:
    blender --background --python scripts/generate_render.py
Output: assets/quad-dock-render.png
"""
from __future__ import annotations

import math
from pathlib import Path

import bpy
from mathutils import Euler, Vector

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = ROOT / "assets" / "quad-dock-render.png"

# ---------------------------------------------------------------------------
# Unit conversions & body constants
# ---------------------------------------------------------------------------
MM = 0.001  # 1 mm expressed in Blender's metre units

# Enclosure body (front = Y=0, rear = Y=LENGTH)
LENGTH    = 300 * MM
FRONT_W   = 110 * MM   # width at front
REAR_W    = 140 * MM   # width at rear
FRONT_H   =  12 * MM   # base height at front edge
REAR_H    =  22 * MM   # base height at rear edge
TOP_T     = 1.5 * MM   # top aluminium plate thickness

# Plan-view corner rounding — baked into mesh geometry, NOT a modifier
CORNER_R    = 20 * MM
CORNER_SEGS =  8        # arc segments per corner

# Zone 1 — Phone Qi dish (front-left)
Z1_Y_MM         = 60.0
Z1_FROM_LEFT_MM = 35.0
Z1_W_MM         = 80.0   # X extent
Z1_H_MM         = 55.0   # Y extent
Z1_CORNER_MM    = 10.0
Z1_DEPTH_MM     =  2.5

# Zone 2 — Buds Qi dish (front-centre)
Z2_Y_MM      = 60.0
Z2_W_MM      = 65.0
Z2_H_MM      = 55.0
Z2_CORNER_MM = 10.0
Z2_DEPTH_MM  =  2.5

# Zone 3 — Watch cradle (rear-left)
Z3_Y_MM         = 220.0
Z3_FROM_LEFT_MM =  35.0
Z3_DIAM_MM      =  50.0
Z3_HEIGHT_MM    =  18.0
Z3_TILT_DEG     =  30.0

# Zone 4 — Laptop groove (rear-right)
Z4_W_MM            = 22.0
Z4_GROOVE_DEPTH_MM = 12.0
Z4_FROM_RIGHT_MM   = 30.0

# LED bar — runs along underside of front lip
LED_SPAN_MM  = 290.0
LED_SECTIONS =   4
LED_GAP_MM   =   2.0
LED_W_MM     =   8.0
LED_H_MM     =   3.0

# Rubber feet
FOOT_R_MM     =  7.5   # radius (15 mm diameter)
FOOT_H_MM     =  3.0
FOOT_INSET_MM = 15.0

# ---------------------------------------------------------------------------
# Exact material colours from design-spec.md
# ---------------------------------------------------------------------------
_C_ABS      = (0.102, 0.102, 0.102, 1.0)  # #1A1A1A  matte black ABS
_C_ALUM     = (0.172, 0.172, 0.172, 1.0)  # #2C2C2C  brushed gunmetal aluminium
_C_SILICONE = (0.165, 0.165, 0.165, 1.0)  # #2A2A2A  dark grey silicone
_C_RUBBER   = (0.051, 0.051, 0.051, 1.0)  # #0D0D0D  near-black rubber
_C_LED      = (1.000, 0.894, 0.710, 1.0)  # #FFE4B5  warm-white emissive
_C_ETCHED   = (0.133, 0.133, 0.133, 1.0)  # #222222  laser-etched text
_C_GROUND   = (0.960, 0.960, 0.960, 1.0)  # studio white ground

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

def log(msg: str) -> None:
    print(f"[quad-dock-render] {msg}")

# ---------------------------------------------------------------------------
# Coordinate helpers
# ---------------------------------------------------------------------------

def _lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t


def width_at_y(y: float) -> float:
    """Dock width in metres at Y-depth y (metres)."""
    return _lerp(FRONT_W, REAR_W, y / LENGTH)


def height_at_y(y: float) -> float:
    """Base-top Z in metres at Y-depth y (metres)."""
    return _lerp(FRONT_H, REAR_H, y / LENGTH)


def x_from_left(y: float, dist_mm: float) -> float:
    return -width_at_y(y) / 2.0 + dist_mm * MM


def x_from_right(y: float, dist_mm: float) -> float:
    return width_at_y(y) / 2.0 - dist_mm * MM


def look_at(obj: bpy.types.Object, target: Vector) -> None:
    direction = target - Vector(obj.location)
    obj.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()

# ---------------------------------------------------------------------------
# Mesh helpers
# ---------------------------------------------------------------------------

def _norm2(dx: float, dy: float) -> tuple[float, float]:
    L = math.sqrt(dx * dx + dy * dy)
    return (dx / L, dy / L) if L > 1e-10 else (0.0, 1.0)


def rounded_polygon_outline(
    corners: list[tuple[float, float]],
    radius: float,
    n_segs: int,
) -> list[tuple[float, float]]:
    """
    2-D CCW outline of a convex polygon with rounded corners.

    Each corner is replaced by a circular arc of (n_segs+1) points
    (both tangent endpoints included).  Between consecutive arcs the
    polygon edge is the straight section of the original side.

    Total vertices = len(corners) * (n_segs + 1).
    """
    n = len(corners)
    pts: list[tuple[float, float]] = []

    for i in range(n):
        A = corners[(i - 1) % n]
        B = corners[i]
        C = corners[(i + 1) % n]

        d1 = _norm2(B[0] - A[0], B[1] - A[1])   # incoming edge direction
        d2 = _norm2(C[0] - B[0], C[1] - B[1])   # outgoing edge direction

        # Inward normals for a CCW polygon: rotate 90° CCW → (−dy, dx)
        n1 = (-d1[1], d1[0])
        n2 = (-d2[1], d2[0])

        # Arc centre = intersection of the two offset lines
        # L1: B + R·n1 + t·d1
        # L2: B + R·n2 + s·d2
        # → t·d1 − s·d2 = R·(n2 − n1)
        rx = radius * (n2[0] - n1[0])
        ry = radius * (n2[1] - n1[1])
        det = d1[0] * (-d2[1]) + d2[0] * d1[1]   # det of [d1 | -d2]

        if abs(det) < 1e-9:          # nearly parallel edges – keep sharp corner
            pts.append(B)
            continue

        t = (rx * (-d2[1]) + d2[0] * ry) / det   # Cramer

        cx_arc = B[0] + radius * n1[0] + t * d1[0]
        cy_arc = B[1] + radius * n1[1] + t * d1[1]

        # Tangent points on the two edges
        ts_x = cx_arc - radius * n1[0];  ts_y = cy_arc - radius * n1[1]
        te_x = cx_arc - radius * n2[0];  te_y = cy_arc - radius * n2[1]

        a0 = math.atan2(ts_y - cy_arc, ts_x - cx_arc)
        a1 = math.atan2(te_y - cy_arc, te_x - cx_arc)

        # Arc sweeps CCW (positive Δθ) for a convex corner on a CCW polygon
        da = a1 - a0
        if da < 0.0:
            da += 2.0 * math.pi

        for k in range(n_segs + 1):          # include both tangent endpoints
            a = a0 + da * k / n_segs
            pts.append((cx_arc + radius * math.cos(a),
                        cy_arc + radius * math.sin(a)))

    return pts


def _rrect_pts(
    w: float, h: float, r: float, n_segs: int = 8,
) -> list[tuple[float, float]]:
    """CCW 2-D rounded-rectangle outline centred at the origin."""
    hw, hh = w / 2.0, h / 2.0
    pts: list[tuple[float, float]] = []
    for cx_a, cy_a, a_s, a_e in (
        ( hw - r, -hh + r, -math.pi / 2,  0.0           ),
        ( hw - r,  hh - r,  0.0,           math.pi / 2  ),
        (-hw + r,  hh - r,  math.pi / 2,   math.pi      ),
        (-hw + r, -hh + r,  math.pi,    3 * math.pi / 2  ),
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
    Build a closed prism from a 2-D CCW outline.

    z_bot_fn(y) and z_top_fn(y) return the Z coordinate for the bottom
    and top ring respectively.  Face normals are outward (−Z bottom,
    +Z top, outward sides).
    """
    N = len(outline)
    verts: list[tuple] = []
    for x, y in outline:                           # ring 0 = bottom
        verts.append((x, y, z_bot_fn(y)))
    for x, y in outline:                           # ring 1 = top
        verts.append((x, y, z_top_fn(y)))

    faces: list[list[int]] = []
    faces.append(list(range(N - 1, -1, -1)))       # bottom: CW from above → −Z normal
    faces.append(list(range(N, 2 * N)))            # top:    CCW from above → +Z normal
    for i in range(N):                             # sides:  outward normals
        j = (i + 1) % N
        faces.append([i, j, N + j, N + i])

    mesh = bpy.data.meshes.new(name)
    obj = bpy.data.objects.new(name, mesh)
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
    """Flat-topped rounded-rectangle prism, centred at (cx, cy)."""
    pts = [(cx + px, cy + py) for px, py in _rrect_pts(w, h, r, n_segs)]
    return _build_prism(name, pts, lambda _: z_bot, lambda _: z_top)


def _bool_diff(target: bpy.types.Object, cutter: bpy.types.Object) -> None:
    """Apply Boolean Difference (EXACT solver) and remove the cutter object."""
    cutter.hide_viewport = False
    cutter.hide_render = True
    mod = target.modifiers.new(f"Bool_{cutter.name}", "BOOLEAN")
    mod.operation = "DIFFERENCE"
    mod.solver = "EXACT"
    mod.object = cutter
    bpy.context.view_layer.objects.active = target
    try:
        bpy.ops.object.modifier_apply(modifier=mod.name)
    except RuntimeError as exc:
        log(f"Boolean apply warning ({cutter.name}): {exc}")
    bpy.data.objects.remove(cutter, do_unlink=True)


def _add_bevel(obj: bpy.types.Object, width_mm: float, segs: int) -> None:
    """Small angle-limited bevel for outer-edge smoothing only."""
    mod = obj.modifiers.new("Bevel", "BEVEL")
    mod.limit_method = "ANGLE"
    mod.angle_limit = math.radians(45.0)
    mod.width = width_mm * MM
    mod.segments = segs
    mod.profile = 0.7


def _assign_mat(obj: bpy.types.Object, mat: bpy.types.Material) -> None:
    if obj.data.materials:
        obj.data.materials[0] = mat
    else:
        obj.data.materials.append(mat)

# ---------------------------------------------------------------------------
# Scene / render setup
# ---------------------------------------------------------------------------

def clear_scene() -> None:
    log("Clearing existing scene")
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for db in (bpy.data.meshes, bpy.data.materials, bpy.data.lights,
               bpy.data.curves, bpy.data.cameras):
        for blk in list(db):
            if blk.users == 0:
                db.remove(blk)


def setup_cycles() -> None:
    log("Configuring Cycles render settings")
    scene = bpy.context.scene
    scene.render.engine = "CYCLES"
    scene.cycles.samples = 128

    # Denoising disabled — OIDN not available in apt Blender 4.0
    scene.cycles.use_denoising = False
    try:
        scene.cycles.denoiser = "NONE"
    except (AttributeError, TypeError):
        pass

    scene.render.resolution_x = 2400
    scene.render.resolution_y = 1600
    scene.render.image_settings.file_format = "PNG"
    scene.render.filepath = str(OUTPUT_PATH)
    scene.unit_settings.system = "METRIC"
    scene.unit_settings.scale_length = 1.0

    # Attempt GPU selection
    cp = bpy.context.preferences.addons.get("cycles")
    if cp is None:
        scene.cycles.device = "CPU"
        log("No GPU backend available; falling back to CPU")
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
                log(f"Using GPU device type: {dtype}")
                return
        except Exception:
            continue
    scene.cycles.device = "CPU"
    log("No GPU backend available; falling back to CPU")

# ---------------------------------------------------------------------------
# Materials
# ---------------------------------------------------------------------------

def _pbsdf(name: str) -> tuple[bpy.types.Material,
                                bpy.types.ShaderNodeBsdfPrincipled]:
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    return mat, bsdf


def _mat_abs() -> bpy.types.Material:
    mat, b = _pbsdf("ABS_Matte_Black")
    b.inputs["Base Color"].default_value = _C_ABS
    b.inputs["Roughness"].default_value = 0.9
    b.inputs["Metallic"].default_value = 0.0
    return mat


def _mat_aluminum() -> bpy.types.Material:
    mat, b = _pbsdf("Aluminum_Brushed")
    b.inputs["Base Color"].default_value = _C_ALUM
    b.inputs["Metallic"].default_value = 0.95
    b.inputs["Roughness"].default_value = 0.15
    b.inputs["Anisotropic"].default_value = 0.6

    nt = mat.node_tree
    tc   = nt.nodes.new("ShaderNodeTexCoord");  tc.location   = (-800, 200)
    mp   = nt.nodes.new("ShaderNodeMapping");   mp.location   = (-620, 200)
    ns   = nt.nodes.new("ShaderNodeTexNoise");  ns.location   = (-440, 200)
    ramp = nt.nodes.new("ShaderNodeValToRGB");  ramp.location = (-250, 200)
    mp.inputs["Scale"].default_value = (220.0, 1.2, 1.2)
    ns.inputs["Scale"].default_value = 340.0
    ns.inputs["Detail"].default_value = 2.0
    ns.inputs["Roughness"].default_value = 0.3
    ramp.color_ramp.elements[0].position = 0.35
    ramp.color_ramp.elements[1].position = 0.70
    nt.links.new(tc.outputs["Object"],   mp.inputs["Vector"])
    nt.links.new(mp.outputs["Vector"],   ns.inputs["Vector"])
    nt.links.new(ns.outputs["Fac"],      ramp.inputs["Fac"])
    nt.links.new(ramp.outputs["Color"],  b.inputs["Roughness"])
    return mat


def _mat_silicone() -> bpy.types.Material:
    mat, b = _pbsdf("Silicone_Dark")
    b.inputs["Base Color"].default_value = _C_SILICONE
    b.inputs["Roughness"].default_value = 0.95
    b.inputs["Metallic"].default_value = 0.0
    return mat


def _mat_rubber() -> bpy.types.Material:
    mat, b = _pbsdf("Rubber_Black")
    b.inputs["Base Color"].default_value = _C_RUBBER
    b.inputs["Roughness"].default_value = 1.0
    return mat


def _mat_led() -> bpy.types.Material:
    mat, b = _pbsdf("LED_Diffuser")
    b.inputs["Base Color"].default_value = _C_LED
    b.inputs["Roughness"].default_value = 0.45
    b.inputs["Emission Color"].default_value = _C_LED
    b.inputs["Emission Strength"].default_value = 4.0
    return mat


def _mat_etched() -> bpy.types.Material:
    mat, b = _pbsdf("Etched_Text")
    b.inputs["Base Color"].default_value = _C_ETCHED
    b.inputs["Roughness"].default_value = 0.3
    b.inputs["Metallic"].default_value = 0.5
    return mat


def _mat_ground() -> bpy.types.Material:
    mat, b = _pbsdf("Studio_Ground")
    b.inputs["Base Color"].default_value = _C_GROUND
    b.inputs["Roughness"].default_value = 0.12
    return mat

# ---------------------------------------------------------------------------
# Lighting
# ---------------------------------------------------------------------------

def _area_light(
    name: str,
    location: tuple,
    rotation: tuple,
    size_x: float,
    size_y: float,
    energy: float,
    color: tuple,
) -> None:
    data = bpy.data.lights.new(name=name, type="AREA")
    data.shape = "RECTANGLE"
    data.size   = size_x
    data.size_y = size_y
    data.energy = energy
    data.color  = color[:3]
    obj = bpy.data.objects.new(name=name, object_data=data)
    bpy.context.collection.objects.link(obj)
    obj.location       = location
    obj.rotation_euler = Euler(rotation, "XYZ")

# ---------------------------------------------------------------------------
# Text labels
# ---------------------------------------------------------------------------

def _zone_label(
    label: str,
    location: tuple,
    size_mm: float,
    mat: bpy.types.Material,
) -> None:
    bpy.ops.object.text_add(location=location)
    t = bpy.context.active_object
    t.data.body    = label
    t.data.size    = size_mm * MM
    t.data.extrude = 0.2 * MM
    bpy.ops.object.convert(target="MESH")
    m = bpy.context.active_object
    m.name = f"Text_{label}"
    _assign_mat(m, mat)

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    clear_scene()
    setup_cycles()

    log("Creating materials")
    m_abs  = _mat_abs()
    m_al   = _mat_aluminum()
    m_sil  = _mat_silicone()
    m_rub  = _mat_rubber()
    m_led  = _mat_led()
    m_eth  = _mat_etched()
    m_gnd  = _mat_ground()

    # ── Shared rounded-trapezoid XY outline ──────────────────────────────────
    # Corners in CCW order (front-left → front-right → rear-right → rear-left)
    trap_corners = [
        (-FRONT_W / 2, 0.0),
        ( FRONT_W / 2, 0.0),
        ( REAR_W  / 2, LENGTH),
        (-REAR_W  / 2, LENGTH),
    ]
    outline = rounded_polygon_outline(trap_corners, CORNER_R, CORNER_SEGS)

    # ── Base — proper trapezoid prism, NO large bevel modifier ───────────────
    log("Building base trapezoidal wedge")
    base = _build_prism(
        "Base_ABS",
        outline,
        z_bot_fn=lambda y: 0.0,
        z_top_fn=lambda y: height_at_y(y),
    )
    _assign_mat(base, m_abs)

    # ── Zone 4 — laptop groove (rear-right, cut into base rear wall) ─────────
    log("Cutting Zone 4 laptop groove")
    z4_x_right = REAR_W / 2 - Z4_FROM_RIGHT_MM * MM   # right edge of groove
    z4_x_left  = z4_x_right - Z4_W_MM * MM             # left edge
    z4_cx      = (z4_x_left + z4_x_right) / 2.0
    # Cutter spans from (LENGTH − groove_depth) to slightly past rear face
    z4_cutter_cy = LENGTH - Z4_GROOVE_DEPTH_MM * MM / 2.0 + 0.5 * MM
    z4_cutter_hy = (Z4_GROOVE_DEPTH_MM + 1.0) * MM

    zone4_cut = _rrect_prism(
        "Zone4_Cutter",
        z4_cx, z4_cutter_cy,
        Z4_W_MM * MM, z4_cutter_hy,
        0.5 * MM,
        z_bot=-0.5 * MM, z_top=REAR_H + 0.5 * MM,
    )
    _bool_diff(base, zone4_cut)

    # Zone 4 silicone lining inside groove (1 mm thick on 3 sides)
    z4_sil = _rrect_prism(
        "Zone4_Silicone",
        z4_cx, LENGTH - Z4_GROOVE_DEPTH_MM * MM / 2.0,
        (Z4_W_MM - 2.0) * MM, Z4_GROOVE_DEPTH_MM * MM,
        0.3 * MM,
        z_bot=0.5 * MM, z_top=REAR_H - 0.5 * MM,
    )
    _assign_mat(z4_sil, m_sil)

    # Small bevel on base outer edges only
    _add_bevel(base, 1.5, 4)

    # ── Top aluminium plate ───────────────────────────────────────────────────
    log("Building top aluminium plate")
    top_plate = _build_prism(
        "Top_Plate",
        outline,
        z_bot_fn=lambda y: height_at_y(y),
        z_top_fn=lambda y: height_at_y(y) + TOP_T,
    )
    _assign_mat(top_plate, m_al)

    # ── Zone 1 — Phone Qi dish (front-left, rounded rectangle) ───────────────
    log("Cutting Zone 1 phone dish")
    z1_y    = Z1_Y_MM * MM
    z1_cx   = x_from_left(z1_y, Z1_FROM_LEFT_MM)
    z1_ztop = height_at_y(z1_y) + TOP_T

    z1_cut = _rrect_prism(
        "Zone1_Cutter",
        z1_cx, z1_y,
        Z1_W_MM * MM, Z1_H_MM * MM,
        Z1_CORNER_MM * MM,
        z_bot=z1_ztop - Z1_DEPTH_MM * MM,
        z_top=z1_ztop + 0.5 * MM,
    )
    _bool_diff(top_plate, z1_cut)

    # Zone 1 silicone lining (1 mm inset, thin pad at dish floor)
    z1_sil = _rrect_prism(
        "Zone1_Silicone",
        z1_cx, z1_y,
        (Z1_W_MM - 2.0) * MM, (Z1_H_MM - 2.0) * MM,
        max((Z1_CORNER_MM - 1.0) * MM, 0.5 * MM),
        z_bot=z1_ztop - Z1_DEPTH_MM * MM,
        z_top=z1_ztop - Z1_DEPTH_MM * MM + 0.3 * MM,
    )
    _assign_mat(z1_sil, m_sil)

    # ── Zone 2 — Buds Qi dish (front-centre, rounded rectangle) ─────────────
    log("Cutting Zone 2 buds dish")
    z2_y    = Z2_Y_MM * MM
    z2_cx   = 0.0   # centred on X
    z2_ztop = height_at_y(z2_y) + TOP_T

    z2_cut = _rrect_prism(
        "Zone2_Cutter",
        z2_cx, z2_y,
        Z2_W_MM * MM, Z2_H_MM * MM,
        Z2_CORNER_MM * MM,
        z_bot=z2_ztop - Z2_DEPTH_MM * MM,
        z_top=z2_ztop + 0.5 * MM,
    )
    _bool_diff(top_plate, z2_cut)

    z2_sil = _rrect_prism(
        "Zone2_Silicone",
        z2_cx, z2_y,
        (Z2_W_MM - 2.0) * MM, (Z2_H_MM - 2.0) * MM,
        max((Z2_CORNER_MM - 1.0) * MM, 0.5 * MM),
        z_bot=z2_ztop - Z2_DEPTH_MM * MM,
        z_top=z2_ztop - Z2_DEPTH_MM * MM + 0.3 * MM,
    )
    _assign_mat(z2_sil, m_sil)

    # Small bevel on top plate (applied after all Boolean cuts)
    _add_bevel(top_plate, 0.5, 3)

    # ── Zone 3 — Watch cradle pod (teardrop: cylinder + cone) ────────────────
    log("Building Zone 3 watch cradle")
    z3_y      = Z3_Y_MM * MM
    z3_cx     = x_from_left(z3_y, Z3_FROM_LEFT_MM)
    z3_base_z = height_at_y(z3_y) + TOP_T

    total_h = Z3_HEIGHT_MM * MM
    cyl_h   = total_h * 0.65
    cone_h  = total_h * 0.35
    cyl_r   = Z3_DIAM_MM / 2.0 * MM

    bpy.ops.mesh.primitive_cylinder_add(
        vertices=48, radius=cyl_r, depth=cyl_h,
        location=(z3_cx, z3_y, z3_base_z + cyl_h / 2),
    )
    cyl_obj = bpy.context.active_object
    cyl_obj.name = "_Z3_Cyl"

    bpy.ops.mesh.primitive_cone_add(
        vertices=48, radius1=cyl_r, radius2=0.0, depth=cone_h,
        location=(z3_cx, z3_y, z3_base_z + cyl_h + cone_h / 2),
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

    # Pivot at pod base, then tilt 30° toward front
    # Positive X-axis rotation → top of pod leans toward −Y (front)
    bpy.context.scene.cursor.location = (z3_cx, z3_y, z3_base_z)
    bpy.ops.object.origin_set(type="ORIGIN_CURSOR")
    pod.rotation_euler = Euler((math.radians(Z3_TILT_DEG), 0.0, 0.0), "XYZ")
    _assign_mat(pod, m_abs)

    # ── LED bar — 4 sections along underside of front lip ────────────────────
    log("Adding LED bar (4 sections)")
    section_len_mm = (LED_SPAN_MM - (LED_SECTIONS - 1) * LED_GAP_MM) / LED_SECTIONS
    x_start_mm     = -LED_SPAN_MM / 2.0 + section_len_mm / 2.0

    led_y = -2.0 * MM   # peeking out from under the front lip
    led_z =  LED_H_MM / 2.0 * MM   # Z centroid (0 → 3 mm range)

    for idx in range(LED_SECTIONS):
        sec_cx = (x_start_mm + idx * (section_len_mm + LED_GAP_MM)) * MM
        bpy.ops.mesh.primitive_cube_add(size=1.0,
                                        location=(sec_cx, led_y, led_z))
        sec = bpy.context.active_object
        sec.name = f"LED_Section_{idx + 1}"
        sec.scale = (section_len_mm * MM,
                     LED_W_MM * MM,
                     LED_H_MM * MM)
        bpy.ops.object.transform_apply(scale=True)
        _assign_mat(sec, m_led)

    # ── Rubber feet (4 × at corners, 15 mm inset) ────────────────────────────
    log("Adding rubber feet")
    inset_y_front = FOOT_INSET_MM * MM
    inset_y_rear  = LENGTH - FOOT_INSET_MM * MM
    foot_positions = [
        (x_from_left (inset_y_front, FOOT_INSET_MM), inset_y_front),
        (x_from_right(inset_y_front, FOOT_INSET_MM), inset_y_front),
        (x_from_left (inset_y_rear,  FOOT_INSET_MM), inset_y_rear),
        (x_from_right(inset_y_rear,  FOOT_INSET_MM), inset_y_rear),
    ]
    for idx, (fx, fy) in enumerate(foot_positions, start=1):
        bpy.ops.mesh.primitive_cylinder_add(
            vertices=48,
            radius=FOOT_R_MM * MM,
            depth=FOOT_H_MM * MM,
            location=(fx, fy, -FOOT_H_MM * MM / 2.0),
        )
        foot = bpy.context.active_object
        foot.name = f"Foot_{idx}"
        _assign_mat(foot, m_rub)

    # ── Zone labels (laser-etched text on top plate) ──────────────────────────
    log("Adding zone labels and wordmark")
    dz = 0.15 * MM   # Z offset above top-plate surface

    _zone_label(
        "PHONE",
        (z1_cx - 12 * MM,
         z1_y + Z1_H_MM * MM / 2 + 4 * MM,
         z1_ztop + dz),
        6.0, m_eth,
    )
    _zone_label(
        "BUDS",
        (z2_cx - 10 * MM,
         z2_y + Z2_H_MM * MM / 2 + 4 * MM,
         z2_ztop + dz),
        6.0, m_eth,
    )

    z3_top_z = height_at_y(z3_y) + TOP_T + dz
    _zone_label(
        "WATCH",
        (z3_cx - 12 * MM, z3_y - 30 * MM, z3_top_z),
        6.0, m_eth,
    )

    z4_label_y = 240 * MM
    z4_label_x = x_from_right(z4_label_y, 48.0)
    z4_label_z = height_at_y(z4_label_y) + TOP_T + dz
    _zone_label(
        "LAPTOP",
        (z4_label_x, z4_label_y, z4_label_z),
        6.0, m_eth,
    )

    wm_y = 270 * MM
    wm_z = height_at_y(wm_y) + TOP_T + dz
    _zone_label("Quad-Dock", (-22 * MM, wm_y, wm_z), 8.0, m_eth)

    # ── Studio ground ─────────────────────────────────────────────────────────
    log("Building studio ground and background")
    bpy.ops.mesh.primitive_plane_add(size=8.0,
                                     location=(0.0, LENGTH / 2, 0.0))
    gnd = bpy.context.active_object
    gnd.name = "Studio_Ground"
    _assign_mat(gnd, m_gnd)

    world = bpy.data.worlds["World"]
    world.use_nodes = True
    bg = world.node_tree.nodes["Background"]
    bg.inputs["Color"].default_value    = (1.0, 1.0, 1.0, 1.0)
    bg.inputs["Strength"].default_value = 0.8

    # ── Three-point studio lighting ───────────────────────────────────────────
    log("Setting up studio lights")
    _area_light(
        "Key_Light",
        location=(-0.6, -0.5, 0.7),
        rotation=(math.radians(58), math.radians(8), math.radians(-30)),
        size_x=1.5, size_y=1.5, energy=600.0,
        color=(1.000, 0.961, 0.902),    # warm white #FFF5E6
    )
    _area_light(
        "Fill_Light",
        location=(0.7, 0.1, 0.4),
        rotation=(math.radians(70), math.radians(-5), math.radians(38)),
        size_x=1.2, size_y=1.2, energy=200.0,
        color=(0.918, 0.957, 1.000),    # cool white #EAF4FF
    )
    _area_light(
        "Rim_Light",
        location=(0.0, 0.7, 0.5),
        rotation=(math.radians(120), 0.0, math.radians(180)),
        size_x=0.4, size_y=0.4, energy=150.0,
        color=(1.0, 1.0, 1.0),
    )

    # ── Camera ────────────────────────────────────────────────────────────────
    log("Configuring camera")
    bpy.ops.object.camera_add(location=(-0.25, -0.30, 0.22))
    cam = bpy.context.active_object
    cam.name = "Product_Camera"
    cam.data.lens = 85.0
    look_at(cam, Vector((0.0, 0.13, 0.015)))
    bpy.context.scene.camera = cam

    # ── Render ────────────────────────────────────────────────────────────────
    log(f"Rendering to {OUTPUT_PATH}")
    try:
        result = bpy.ops.render.render(write_still=True)
        if "FINISHED" in result:
            log("Render complete")
            log(f"Output saved: {OUTPUT_PATH}")
        else:
            log(f"Render returned: {result}")
    except Exception as exc:
        log(f"Render raised exception: {exc!r}")
        ri = bpy.data.images.get("Render Result")
        if ri is not None:
            log("Attempting to save partial render result…")
            ri.save_render(str(OUTPUT_PATH))
            log(f"Output saved: {OUTPUT_PATH}")
        else:
            raise


if __name__ == "__main__":
    main()
