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
from mathutils import Euler, Vector

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = ROOT / "assets" / "quad-dock-render.png"
MM = 0.001

# Envelope
FRONT_W = 110.0
REAR_W = 140.0
LENGTH = 300.0
FRONT_H = 12.0
REAR_H = 22.0
CORNER_R = 20.0
TOP_T = 1.5

# Zones (mm, table-locked)
Z1 = dict(cx=-20.0, cy=70.0, w=80.0, d=55.0, r=10.0, cut=2.5, sil_w=78.0, sil_d=53.0, sil_r=9.0, sil_t=2.2)
Z2 = dict(cx=+20.0, cy=70.0, w=65.0, d=55.0, r=10.0, cut=2.5, sil_w=63.0, sil_d=53.0, sil_r=9.0, sil_t=2.2)

WATCH_BASE = Vector((-22.0 * MM, 225.0 * MM, 21.0 * MM))
WATCH_DIAM = 50.0
WATCH_CYL_H = 12.0
WATCH_CONE_H = 6.0
WATCH_TIP_D = 8.0
WATCH_TILT = 30.0

GROOVE = dict(x0=18.0, x1=40.0, y0=288.0, y1=300.0, h=20.0)

IEC = dict(w=28.0, h=20.0, x=0.0, y=298.5, bottom=1.0)
USB_C = dict(x=29.0, y=297.0, z=8.0, w=10.0, h=4.0, d=3.0)

LED_CENTERS = [-108.75, -35.25, 38.25, 111.75]

TEXT_ITEMS = [
    ("PHONE", -28.0, 93.0, 6.0),
    ("BUDS", 12.0, 93.0, 6.0),
    ("WATCH", -38.0, 203.0, 6.0),
    ("LAPTOP", 10.0, 260.0, 6.0),
    ("Quad-Dock", -18.0, 278.0, 8.0),
]

FEET = [(-39.17, 15.0), (39.17, 15.0), (-53.50, 285.0), (53.50, 285.0)]


def h(y_mm: float) -> float:
    return FRONT_H + (REAR_H - FRONT_H) * (y_mm / LENGTH)


def clear_scene() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for datablock in (bpy.data.meshes, bpy.data.materials, bpy.data.images, bpy.data.curves):
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


def _rrect_pts(width, depth, corner_r, segments=16):
    hw, hd = width / 2.0, depth / 2.0
    pts = []
    corners = [
        (hw - corner_r, -hd + corner_r, -math.pi / 2, 0),
        (hw - corner_r, hd - corner_r, 0, math.pi / 2),
        (-hw + corner_r, hd - corner_r, math.pi / 2, math.pi),
        (-hw + corner_r, -hd + corner_r, math.pi, 3 * math.pi / 2),
    ]
    for cx, cy, a0, a1 in corners:
        for i in range(segments):
            t = i / max(1, segments - 1)
            a = a0 + (a1 - a0) * t
            pts.append((cx + corner_r * math.cos(a), cy + corner_r * math.sin(a)))
    return pts


def make_rounded_rect_cutter(name, cx, cy, cz, width, depth, corner_r, height, segments=16):
    pts = _rrect_pts(width, depth, corner_r, segments)
    n = len(pts)
    verts = [(x * MM, y * MM, (cz - height / 2.0) * MM) for x, y in pts] + [
        (x * MM, y * MM, (cz + height / 2.0) * MM) for x, y in pts
    ]
    faces = [list(range(n - 1, -1, -1)), list(range(n, 2 * n))]
    for i in range(n):
        j = (i + 1) % n
        faces.append([i, j, n + j, n + i])
    mesh = bpy.data.meshes.new(name)
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj.location = (cx * MM, cy * MM, 0.0)
    return obj


def safe_boolean_difference(target, cutter, label):
    try:
        mod = target.modifiers.new(name=f"bool_{label}", type="BOOLEAN")
        mod.operation = "DIFFERENCE"
        mod.solver = "FAST"
        mod.object = cutter
        bpy.context.view_layer.objects.active = target
        bpy.ops.object.modifier_apply(modifier=mod.name)
        bpy.data.objects.remove(cutter, do_unlink=True)
    except Exception as exc:
        print(f"[warn] boolean '{label}' failed: {exc}")


def rounded_trapezoid_footprint_40() -> list[tuple[float, float]]:
    corners = [(-FRONT_W / 2, 0.0), (FRONT_W / 2, 0.0), (REAR_W / 2, LENGTH), (-REAR_W / 2, LENGTH)]

    def norm(dx, dy):
        mag = math.hypot(dx, dy)
        return (dx / mag, dy / mag)

    # 9 points per corner from generic fillet builder
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

    # Insert one midpoint on each straight transition: 36 -> 40 vertices
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


def add_text_etch(target, label, x, y, size_mm):
    z = h(y) + TOP_T + 0.1
    bpy.ops.object.text_add(location=(x * MM, y * MM, z * MM))
    txt = bpy.context.active_object
    txt.data.body = label
    txt.data.size = size_mm * MM
    txt.data.extrude = 0.35 * MM
    txt.data.align_x = "CENTER"
    txt.data.align_y = "CENTER"
    txt.rotation_euler = Euler((0.0, 0.0, 0.0), "XYZ")
    bpy.ops.object.convert(target="MESH")
    safe_boolean_difference(target, txt, f"etch_{label}")


def add_area_light(name, location, size_xy, energy, color):
    ldata = bpy.data.lights.new(name=name, type="AREA")
    ldata.energy = energy
    ldata.color = color
    ldata.shape = "RECTANGLE"
    ldata.size = size_xy[0]
    ldata.size_y = size_xy[1]
    obj = bpy.data.objects.new(name, ldata)
    bpy.context.collection.objects.link(obj)
    obj.location = location
    obj.rotation_euler = (math.radians(55), 0, math.radians(30))
    return obj


def main() -> None:
    clear_scene()

    # Render engine
    scene = bpy.context.scene
    scene.render.engine = "CYCLES"
    scene.cycles.samples = 512
    scene.cycles.use_denoising = False
    scene.render.resolution_x = 4800
    scene.render.resolution_y = 3200
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_depth = "16"
    scene.render.filepath = str(OUTPUT_PATH)

    # World
    scene.world = bpy.data.worlds.new("World")
    scene.world.use_nodes = True
    wbg = scene.world.node_tree.nodes["Background"]
    wbg.inputs["Color"].default_value = (1, 1, 1, 1)
    wbg.inputs["Strength"].default_value = 1.2

    # Materials
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

    # Body wedge: explicit rounded trapezoid prism, top tapered by H(Y)
    outline = rounded_trapezoid_footprint_40()
    body = build_prism("Body", outline, lambda _y: 0.0, h)
    apply_mat(body, m_abs)

    # slight floor edge softening only
    bev = body.modifiers.new("FloorBevel", type="BEVEL")
    bev.width = 0.5 * MM
    bev.segments = 2
    bev.limit_method = "ANGLE"
    bpy.context.view_layer.objects.active = body
    try:
        bpy.ops.object.modifier_apply(modifier=bev.name)
    except Exception as exc:
        print(f"[warn] floor bevel apply failed: {exc}")

    # Top plate: separate object
    top = build_prism("TopPlate", outline, h, lambda y: h(y) + TOP_T)
    apply_mat(top, m_al)

    # Zone dishes
    for tag, z in (("z1", Z1), ("z2", Z2)):
        cy = z["cy"]
        top_z = h(cy) + TOP_T
        cutter = make_rounded_rect_cutter(f"{tag}_dish", z["cx"], cy, top_z - z["cut"] / 2.0, z["w"], z["d"], z["r"], z["cut"] + 2.0, segments=16)
        safe_boolean_difference(top, cutter, f"dish_{tag}")

        sil_h = z["sil_t"]
        sil_z = h(cy) + TOP_T - sil_h / 2.0
        sil = make_rounded_rect_cutter(f"{tag}_sil", z["cx"], cy, sil_z, z["sil_w"], z["sil_d"], z["sil_r"], sil_h, segments=16)
        apply_mat(sil, m_sil)

    # Watch cradle: cylinder + cone, tilt 30 toward front around pod base pivot
    cyl_r = WATCH_DIAM * 0.5 * MM
    bpy.ops.mesh.primitive_cylinder_add(vertices=64, radius=cyl_r, depth=WATCH_CYL_H * MM, location=(WATCH_BASE.x, WATCH_BASE.y, WATCH_BASE.z + (WATCH_CYL_H * MM) / 2.0))
    c1 = bpy.context.active_object
    bpy.ops.mesh.primitive_cone_add(vertices=64, radius1=cyl_r, radius2=(WATCH_TIP_D * 0.5) * MM, depth=WATCH_CONE_H * MM, location=(WATCH_BASE.x, WATCH_BASE.y, WATCH_BASE.z + WATCH_CYL_H * MM + (WATCH_CONE_H * MM) / 2.0))
    c2 = bpy.context.active_object
    bpy.ops.object.select_all(action="DESELECT")
    c1.select_set(True)
    c2.select_set(True)
    bpy.context.view_layer.objects.active = c1
    bpy.ops.object.join()
    pod = bpy.context.active_object
    pod.name = "WatchPod"
    apply_mat(pod, m_abs)
    bpy.context.scene.cursor.location = WATCH_BASE
    bpy.ops.object.origin_set(type="ORIGIN_CURSOR")
    pod.rotation_euler = Euler((math.radians(WATCH_TILT), 0, 0), "XYZ")

    # Visible watch puck on top
    bpy.ops.mesh.primitive_cylinder_add(vertices=48, radius=17.0 * MM, depth=5.0 * MM, location=(WATCH_BASE.x, WATCH_BASE.y, WATCH_BASE.z + (WATCH_CYL_H + WATCH_CONE_H - 1.0) * MM))
    puck = bpy.context.active_object
    apply_mat(puck, m_watch)
    puck.rotation_euler = pod.rotation_euler

    # Zone 4 groove cut in rear wall
    gx = ((GROOVE["x0"] + GROOVE["x1"]) / 2.0) * MM
    gy = ((GROOVE["y0"] + GROOVE["y1"]) / 2.0) * MM
    gz = (h(294.0) / 2.0) * MM
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(gx, gy, gz))
    groove_cut = bpy.context.active_object
    groove_cut.scale = (((GROOVE["x1"] - GROOVE["x0"]) / 2.0) * MM, ((GROOVE["y1"] - GROOVE["y0"]) / 2.0) * MM, (GROOVE["h"] / 2.0) * MM)
    safe_boolean_difference(body, groove_cut, "zone4_groove")

    # Groove silicone lining (1 mm, 3 walls)
    wall_t = 1.0 * MM
    for loc, scl in [
        ((GROOVE["x0"] + 0.5, gy / MM, gz / MM), (0.5, (GROOVE["y1"] - GROOVE["y0"]) / 2.0, GROOVE["h"] / 2.0)),
        ((GROOVE["x1"] - 0.5, gy / MM, gz / MM), (0.5, (GROOVE["y1"] - GROOVE["y0"]) / 2.0, GROOVE["h"] / 2.0)),
        (((GROOVE["x0"] + GROOVE["x1"]) / 2.0, GROOVE["y0"] + 0.5, gz / MM), ((GROOVE["x1"] - GROOVE["x0"]) / 2.0, 0.5, GROOVE["h"] / 2.0)),
    ]:
        bpy.ops.mesh.primitive_cube_add(size=1.0, location=(loc[0] * MM, loc[1] * MM, loc[2] * MM))
        w = bpy.context.active_object
        w.scale = (scl[0] * MM, scl[1] * MM, scl[2] * MM)
        apply_mat(w, m_sil)

    # USB-C visible object
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(USB_C["x"] * MM, USB_C["y"] * MM, USB_C["z"] * MM))
    usb = bpy.context.active_object
    usb.scale = (USB_C["w"] * MM / 2.0, USB_C["d"] * MM / 2.0, USB_C["h"] * MM / 2.0)
    apply_mat(usb, m_usbc)

    # IEC inlet cutout
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(IEC["x"] * MM, IEC["y"] * MM, (IEC["bottom"] + IEC["h"] / 2.0) * MM))
    iec_cut = bpy.context.active_object
    iec_cut.scale = ((IEC["w"] / 2.0) * MM, 2.0 * MM, (IEC["h"] / 2.0) * MM)
    safe_boolean_difference(body, iec_cut, "iec")

    # LED diffuser strip and 4 emissive segments
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0.0, -2.0 * MM, 1.5 * MM))
    diffuser = bpy.context.active_object
    diffuser.scale = (145.0 * MM, 4.0 * MM, 1.5 * MM)
    apply_mat(diffuser, m_sil)
    for i, cx in enumerate(LED_CENTERS, start=1):
        bpy.ops.mesh.primitive_cube_add(size=1.0, location=(cx * MM, -2.0 * MM, 1.5 * MM))
        sec = bpy.context.active_object
        sec.name = f"LED_{i}"
        sec.scale = (35.5 * MM, 4.0 * MM, 1.5 * MM)
        apply_mat(sec, m_led)

    # Etched text labels
    for txt, x, y, size in TEXT_ITEMS:
        add_text_etch(top, txt, x, y, size)

    # Rubber feet
    for x, y in FEET:
        bpy.ops.mesh.primitive_cylinder_add(vertices=48, radius=7.5 * MM, depth=3.0 * MM, location=(x * MM, y * MM, -1.5 * MM))
        ft = bpy.context.active_object
        apply_mat(ft, m_rub)

    # Ground plane
    bpy.ops.mesh.primitive_plane_add(size=4.0, location=(0.0, 0.35, -0.003))
    ground = bpy.context.active_object
    apply_mat(ground, m_ground)

    # Coiled power cord behind dock (2-turn loop, radius 60 mm)
    curve = bpy.data.curves.new("PowerCord", type="CURVE")
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

    # Camera (zoomed out, full product visible)
    cam_data = bpy.data.cameras.new("Camera")
    cam = bpy.data.objects.new("Camera", cam_data)
    bpy.context.collection.objects.link(cam)
    cam.location = Vector((-0.65, -0.65, 0.55))
    target = Vector((0.0, 0.16, 0.018))
    cam.rotation_euler = (target - cam.location).to_track_quat("-Z", "Y").to_euler()
    cam_data.lens = 65.0
    scene.camera = cam

    # Lighting (Apple-style)
    add_area_light("Key_Light", (-1.0, -0.8, 1.2), (2.5, 2.5), 1500.0, (1.0, 0.96, 0.90))
    add_area_light("Fill_Light", (1.2, 0.3, 0.7), (2.0, 2.0), 500.0, (0.92, 0.96, 1.0))
    add_area_light("Rim_Light", (0.0, 1.0, 0.8), (0.6, 0.6), 300.0, (1.0, 1.0, 1.0))
    add_area_light("Top_Bounce", (0.0, 0.16, 1.8), (4.0, 3.0), 200.0, (1.0, 1.0, 1.0))

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.render.render(write_still=True)
    print(f"✓ Render written: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
