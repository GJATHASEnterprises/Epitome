#!/usr/bin/env python3
"""
High-quality Quad-Dock render generator.
Run:
  blender --background --python scripts/generate_render.py
"""
from __future__ import annotations

import math
from pathlib import Path

import bpy
from mathutils import Vector

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = ROOT / "assets" / "quad-dock-render.png"
MM = 0.001

# Envelope (mm)
FRONT_W = 110.0
REAR_W = 140.0
LENGTH = 300.0
FRONT_H = 12.0
REAR_H = 22.0
CORNER_R = 20.0
TOP_T = 1.5

# Zones (mm)
Z1 = dict(cx=-20.0, cy=70.0, w=80.0, d=55.0, r=10.0, depth=2.2)
Z2 = dict(cx=+20.0, cy=70.0, w=65.0, d=55.0, r=10.0, depth=2.2)

WATCH_BASE_MM = (-22.0, 225.0, 21.0)
WATCH_DIAM = 50.0
WATCH_CYL_H = 12.0
WATCH_CONE_H = 6.0
WATCH_TIP_D = 8.0
WATCH_TILT = 30.0

TEXT_ITEMS = [
    ("PHONE", -28.0, 93.0, 6.0),
    ("BUDS", 12.0, 93.0, 6.0),
    ("WATCH", -38.0, 203.0, 6.0),
    ("LAPTOP", 10.0, 260.0, 6.0),
    ("Quad-Dock", -18.0, 278.0, 8.0),
]

LED_SECTION_W = 71.0
LED_SECTION_POSITIONS = [-109.5, -36.5, 36.5, 109.5]

FEET = [(-39.17, 15.0), (39.17, 15.0), (-53.50, 285.0), (53.50, 285.0)]


def h(y_mm: float) -> float:
    """Top surface height in mm at y_mm."""
    return FRONT_H + (REAR_H - FRONT_H) * (y_mm / LENGTH)


def clear_scene() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for datablock in (bpy.data.meshes, bpy.data.materials, bpy.data.images, bpy.data.curves, bpy.data.cameras, bpy.data.lights, bpy.data.worlds):
        for item in list(datablock):
            if item.users == 0:
                datablock.remove(item)


def make_mat(name: str, base=(0.8, 0.8, 0.8, 1), metallic=0.0, roughness=0.5, emission=(0, 0, 0, 1), emission_strength=0.0, anisotropic=0.0):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    bsdf = m.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = base
    bsdf.inputs["Metallic"].default_value = metallic
    bsdf.inputs["Roughness"].default_value = roughness
    bsdf.inputs["Anisotropic"].default_value = anisotropic
    if emission_strength > 0.0:
        bsdf.inputs["Emission Color"].default_value = emission
        bsdf.inputs["Emission Strength"].default_value = emission_strength
    return m


def make_aluminum(name: str):
    m = make_mat(name, base=(0.42, 0.42, 0.44, 1), metallic=0.96, roughness=0.12, anisotropic=0.75)
    nt = m.node_tree
    noise = nt.nodes.new("ShaderNodeTexNoise")
    mapping = nt.nodes.new("ShaderNodeMapping")
    tc = nt.nodes.new("ShaderNodeTexCoord")
    bump = nt.nodes.new("ShaderNodeBump")
    noise.inputs["Scale"].default_value = 280.0
    noise.inputs["Detail"].default_value = 3.0
    noise.inputs["Roughness"].default_value = 0.25
    bump.inputs["Strength"].default_value = 0.03
    nt.links.new(tc.outputs["Object"], mapping.inputs["Vector"])
    nt.links.new(mapping.outputs["Vector"], noise.inputs["Vector"])
    nt.links.new(noise.outputs["Fac"], bump.inputs["Height"])
    nt.links.new(bump.outputs["Normal"], nt.nodes["Principled BSDF"].inputs["Normal"])
    return m


def apply_mat(obj, mat):
    obj.data.materials.clear()
    obj.data.materials.append(mat)


def make_box(cx_mm, cy_mm, cz_mm, w_mm, d_mm, h_mm, name: str | None = None):
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(cx_mm * MM, cy_mm * MM, cz_mm * MM))
    obj = bpy.context.active_object
    if name:
        obj.name = name
    obj.scale = (w_mm * MM / 2.0, d_mm * MM / 2.0, h_mm * MM / 2.0)
    bpy.ops.object.transform_apply(scale=True)
    return obj


def make_cyl(cx_mm, cy_mm, cz_mm, r_mm, h_mm, verts=48, name: str | None = None):
    bpy.ops.mesh.primitive_cylinder_add(vertices=verts, radius=r_mm * MM, depth=h_mm * MM, location=(cx_mm * MM, cy_mm * MM, cz_mm * MM))
    obj = bpy.context.active_object
    if name:
        obj.name = name
    return obj


def _rrect_pts(width, depth, corner_r, segments=16):
    hw, hd = width / 2.0, depth / 2.0
    r = max(0.0, min(corner_r, hw, hd))
    pts = []
    corners = [
        (hw - r, -hd + r, -math.pi / 2, 0),
        (hw - r, hd - r, 0, math.pi / 2),
        (-hw + r, hd - r, math.pi / 2, math.pi),
        (-hw + r, -hd + r, math.pi, 3 * math.pi / 2),
    ]
    for cx, cy, a0, a1 in corners:
        for i in range(segments):
            t = i / max(1, segments - 1)
            a = a0 + (a1 - a0) * t
            pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


def make_rrect_box(cx_mm, cy_mm, cz_mm, w_mm, d_mm, r_mm, h_mm, name: str | None = None):
    pts = _rrect_pts(w_mm, d_mm, r_mm, segments=16)
    n = len(pts)
    z0 = (cz_mm - h_mm / 2.0) * MM
    z1 = (cz_mm + h_mm / 2.0) * MM
    verts = [(cx_mm * MM + x * MM, cy_mm * MM + y * MM, z0) for x, y in pts] + [
        (cx_mm * MM + x * MM, cy_mm * MM + y * MM, z1) for x, y in pts
    ]
    faces = [list(range(n - 1, -1, -1)), list(range(n, 2 * n))]
    for i in range(n):
        j = (i + 1) % n
        faces.append([i, j, n + j, n + i])
    mesh = bpy.data.meshes.new(name or "RRectBox")
    obj = bpy.data.objects.new(name or "RRectBox", mesh)
    bpy.context.collection.objects.link(obj)
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    return obj


def rounded_trapezoid_footprint_40() -> list[tuple[float, float]]:
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


def build_prism(name, outline, z0_fn, z1_fn):
    n = len(outline)
    verts = [(x * MM, y * MM, z0_fn(y) * MM) for x, y in outline] + [(x * MM, y * MM, z1_fn(y) * MM) for x, y in outline]
    faces = [list(range(n - 1, -1, -1)), list(range(n, 2 * n))]
    for i in range(n):
        j = (i + 1) % n
        faces.append([i, j, n + j, n + i])
    me = bpy.data.meshes.new(name)
    obj = bpy.data.objects.new(name, me)
    bpy.context.collection.objects.link(obj)
    me.from_pydata(verts, [], faces)
    me.update()
    return obj


def add_zone_dish(name, cx_mm, cy_mm, w_mm, d_mm, r_mm, depth_mm, mat_sil, mat_border):
    z_top_mm = h(cy_mm) + TOP_T
    pad = make_rrect_box(cx_mm, cy_mm, z_top_mm - depth_mm / 2.0, w_mm - 2.0, d_mm - 2.0, max(0.0, r_mm - 1.0), depth_mm, name=f"{name}_Silicone")
    apply_mat(pad, mat_sil)

    border = make_rrect_box(cx_mm, cy_mm, z_top_mm + 0.3, w_mm, d_mm, r_mm, 0.6, name=f"{name}_Border")
    apply_mat(border, mat_border)


def add_label(name, text, x_mm, y_mm, size_mm, mat):
    z_mm = h(y_mm) + TOP_T + 0.2
    bpy.ops.object.text_add(location=(x_mm * MM, y_mm * MM, z_mm * MM))
    obj = bpy.context.active_object
    obj.name = name
    obj.data.body = text
    obj.data.size = size_mm * MM
    obj.data.extrude = 0.15 * MM
    obj.data.align_x = "CENTER"
    obj.data.align_y = "CENTER"
    bpy.ops.object.convert(target="MESH")
    mesh_obj = bpy.context.active_object
    mesh_obj.name = name
    apply_mat(mesh_obj, mat)


def add_laptop_groove(mat_sil, mat_usbc):
    x0, x1 = 18.0, 40.0
    y0, y1 = 288.0, 300.0
    groove_h = 20.0
    cx = (x0 + x1) / 2.0
    cy = (y0 + y1) / 2.0
    z_base = h(cy)

    back = make_box(cx, y1 - 0.5, z_base + groove_h / 2.0, x1 - x0, 1.0, groove_h, name="Zone4_GrooveWalls_Back")
    apply_mat(back, mat_sil)
    left = make_box(x0 + 0.5, cy, z_base + groove_h / 2.0, 1.0, y1 - y0, groove_h, name="Zone4_GrooveWalls_Left")
    apply_mat(left, mat_sil)
    right = make_box(x1 - 0.5, cy, z_base + groove_h / 2.0, 1.0, y1 - y0, groove_h, name="Zone4_GrooveWalls_Right")
    apply_mat(right, mat_sil)

    usbc = make_box(cx, y1 - 1.5, z_base + 8.0, 10.0, 3.0, 4.0, name="Zone4_USBC")
    apply_mat(usbc, mat_usbc)


def add_iec_inlet(mat_usbc):
    iec = make_box(0.0, 299.5, 11.0, 28.0, 1.0, 20.0, name="IEC_Housing")
    apply_mat(iec, mat_usbc)


def look_at(obj, target):
    direction = Vector(target) - Vector(obj.location)
    obj.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def add_area_light(name, location, size_xy, energy, color, target):
    ldata = bpy.data.lights.new(name=name, type="AREA")
    ldata.energy = energy
    ldata.color = color
    ldata.shape = "RECTANGLE"
    ldata.size = size_xy[0]
    ldata.size_y = size_xy[1]
    obj = bpy.data.objects.new(name, ldata)
    bpy.context.collection.objects.link(obj)
    obj.location = location
    look_at(obj, target)
    return obj


def main() -> None:
    clear_scene()

    scene = bpy.context.scene
    scene.render.engine = "CYCLES"
    scene.cycles.samples = 512
    scene.cycles.use_denoising = False
    scene.render.resolution_x = 4800
    scene.render.resolution_y = 3200
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_depth = "16"
    scene.render.filepath = str(OUTPUT_PATH)
    scene.unit_settings.system = "METRIC"
    scene.unit_settings.scale_length = 1.0

    scene.world = bpy.data.worlds.new("World")
    scene.world.use_nodes = True
    wbg = scene.world.node_tree.nodes["Background"]
    wbg.inputs["Color"].default_value = (1, 1, 1, 1)
    wbg.inputs["Strength"].default_value = 1.2

    m_abs = make_mat("ABS", base=(0.08, 0.08, 0.08, 1), roughness=0.88)
    m_al = make_aluminum("ALUM")
    m_sil = make_mat("SILICONE", base=(0.18, 0.18, 0.18, 1), roughness=0.92)
    m_rub = make_mat("RUBBER", base=(0.05, 0.05, 0.05, 1), roughness=1.0)
    m_led = make_mat("LED", base=(1.0, 0.894, 0.710, 1), roughness=0.4, emission=(1.0, 0.894, 0.710, 1), emission_strength=5.0)
    m_etched = make_mat("ETCHED", base=(0.10, 0.10, 0.10, 1), metallic=0.6, roughness=0.25)
    m_ground = make_mat("GROUND", base=(0.96, 0.96, 0.96, 1), roughness=0.04)
    m_usbc = make_mat("USBC", base=(0.7, 0.7, 0.72, 1), metallic=0.9, roughness=0.2)
    m_cord = make_mat("CORD", base=(0.12, 0.12, 0.12, 1), roughness=0.7)
    m_watch = make_mat("WATCH_PUCK", base=(0.15, 0.15, 0.15, 1), metallic=0.3, roughness=0.5)

    outline = rounded_trapezoid_footprint_40()

    body = build_prism("Body", outline, lambda _y: 0.0, h)
    apply_mat(body, m_abs)

    bev = body.modifiers.new("FloorBevel", type="BEVEL")
    bev.width = 0.5 * MM
    bev.segments = 2
    bev.limit_method = "ANGLE"
    bpy.context.view_layer.objects.active = body
    bpy.ops.object.modifier_apply(modifier=bev.name)

    top = build_prism("TopPlate", outline, h, lambda y: h(y) + TOP_T)
    apply_mat(top, m_al)

    add_zone_dish("Zone1", Z1["cx"], Z1["cy"], Z1["w"], Z1["d"], Z1["r"], Z1["depth"], m_sil, m_al)
    add_zone_dish("Zone2", Z2["cx"], Z2["cy"], Z2["w"], Z2["d"], Z2["r"], Z2["depth"], m_sil, m_al)

    watch_base = Vector((WATCH_BASE_MM[0] * MM, WATCH_BASE_MM[1] * MM, WATCH_BASE_MM[2] * MM))
    cyl_r = WATCH_DIAM * 0.5 * MM
    bpy.ops.mesh.primitive_cylinder_add(vertices=64, radius=cyl_r, depth=WATCH_CYL_H * MM, location=(watch_base.x, watch_base.y, watch_base.z + (WATCH_CYL_H * MM) / 2.0))
    c1 = bpy.context.active_object
    bpy.ops.mesh.primitive_cone_add(vertices=64, radius1=cyl_r, radius2=(WATCH_TIP_D * 0.5) * MM, depth=WATCH_CONE_H * MM, location=(watch_base.x, watch_base.y, watch_base.z + WATCH_CYL_H * MM + (WATCH_CONE_H * MM) / 2.0))
    c2 = bpy.context.active_object
    bpy.ops.object.select_all(action="DESELECT")
    c1.select_set(True)
    c2.select_set(True)
    bpy.context.view_layer.objects.active = c1
    bpy.ops.object.join()
    pod = bpy.context.active_object
    pod.name = "WatchPod"
    apply_mat(pod, m_abs)
    bpy.context.scene.cursor.location = watch_base
    bpy.ops.object.origin_set(type="ORIGIN_CURSOR")
    pod.rotation_euler = (math.radians(WATCH_TILT), 0.0, 0.0)

    puck = make_cyl(WATCH_BASE_MM[0], WATCH_BASE_MM[1], WATCH_BASE_MM[2] + WATCH_CYL_H + WATCH_CONE_H - 1.0, 17.0, 5.0, verts=48, name="WatchPuck")
    apply_mat(puck, m_watch)
    puck.rotation_euler = pod.rotation_euler

    add_laptop_groove(m_sil, m_usbc)
    add_iec_inlet(m_usbc)

    magnet_ring = make_cyl(-20.0, 70.0, h(70.0) + TOP_T - 1.0, 27.0, 2.0, verts=64, name="Zone1_MagnetRing")
    apply_mat(magnet_ring, m_abs)

    for i, cx in enumerate(LED_SECTION_POSITIONS, start=1):
        led = make_box(cx, -3.0, 1.5, LED_SECTION_W, 8.0, 3.0, name=f"LED_{i}")
        apply_mat(led, m_led)

    diffuser = make_box(0.0, -3.0, 2.0, 292.0, 9.0, 2.0, name="LED_Diffuser")
    apply_mat(diffuser, m_sil)

    for txt, x, y, size in TEXT_ITEMS:
        if txt == "Quad-Dock":
            add_label("Label_QuadDock", txt, x, y, size, m_etched)
        else:
            add_label(f"Label_{txt}", txt, x, y, size, m_etched)

    for i, (x, y) in enumerate(FEET, start=1):
        foot = make_cyl(x, y, -1.5, 7.5, 3.0, verts=48, name=f"Foot_{i}")
        apply_mat(foot, m_rub)

    ground = make_box(0.0, 350.0, -3.0, 4000.0, 4000.0, 1.0, name="Ground")
    apply_mat(ground, m_ground)

    curve = bpy.data.curves.new("PowerCordCurve", type="CURVE")
    curve.dimensions = "3D"
    spline = curve.splines.new("POLY")
    turns = 2
    pts = []
    for i in range(200):
        t = 2 * math.pi * turns * (i / 199.0)
        r = 60.0 * MM
        x = r * math.cos(t)
        y = 0.36 + r * math.sin(t)
        z = 0.004
        pts.append((x, y, z, 1.0))
    spline.points.add(len(pts) - 1)
    spline.points.foreach_set("co", [c for p in pts for c in p])
    curve.bevel_depth = 4.0 * MM
    curve.bevel_resolution = 12
    cord = bpy.data.objects.new("PowerCord", curve)
    bpy.context.collection.objects.link(cord)
    if cord.data.materials:
        cord.data.materials[0] = m_cord
    else:
        cord.data.materials.append(m_cord)

    cam_data = bpy.data.cameras.new("Camera")
    cam = bpy.data.objects.new("Camera", cam_data)
    bpy.context.collection.objects.link(cam)
    cam.location = Vector((-0.55, -0.55, 0.42))
    cam_target = Vector((0.0, 0.18, 0.015))
    look_at(cam, cam_target)
    cam_data.lens = 58.0
    scene.camera = cam

    light_target = (0.0, 0.16, 0.012)
    add_area_light("Key_Light", (-1.0, -0.8, 1.2), (2.5, 2.5), 1500.0, (1.0, 0.96, 0.90), light_target)
    add_area_light("Fill_Light", (1.2, 0.3, 0.7), (2.0, 2.0), 500.0, (0.92, 0.96, 1.0), light_target)
    add_area_light("Rim_Light", (0.0, 1.0, 0.8), (0.6, 0.6), 300.0, (1.0, 1.0, 1.0), light_target)
    add_area_light("Top_Bounce", (0.0, 0.16, 1.8), (4.0, 3.0), 200.0, (1.0, 1.0, 1.0), light_target)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.render.render(write_still=True)
    print(f"✓ Render written: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
