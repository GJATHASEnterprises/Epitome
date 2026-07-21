#!/usr/bin/env python3
from __future__ import annotations

import math
from pathlib import Path

import bpy
from mathutils import Euler, Vector

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = ROOT / "assets" / "quad-dock-render.png"

MM = 0.001
LENGTH = 300 * MM
FRONT_W = 110 * MM
REAR_W = 140 * MM
BASE_FRONT_H = 12 * MM
BASE_REAR_H = 22 * MM
TOP_THICKNESS = 2 * MM


# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------

def log(message: str) -> None:
    print(f"[quad-dock-render] {message}")


def hex_color(hex_code: str, alpha: float = 1.0) -> tuple[float, float, float, float]:
    code = hex_code.lstrip("#")
    r = int(code[0:2], 16) / 255.0
    g = int(code[2:4], 16) / 255.0
    b = int(code[4:6], 16) / 255.0
    return (r, g, b, alpha)


def width_at_y(y_m: float) -> float:
    y_mm = y_m / MM
    width_mm = 110.0 + (140.0 - 110.0) * (y_mm / 300.0)
    return width_mm * MM


def top_height_at_y(y_m: float) -> float:
    y_mm = y_m / MM
    height_mm = 12.0 + (22.0 - 12.0) * (y_mm / 300.0)
    return height_mm * MM


def x_from_left(y_m: float, distance_from_left_mm: float) -> float:
    width = width_at_y(y_m)
    left = -width / 2.0
    return left + distance_from_left_mm * MM


def x_from_right(y_m: float, distance_from_right_mm: float) -> float:
    width = width_at_y(y_m)
    right = width / 2.0
    return right - distance_from_right_mm * MM


def look_at(obj: bpy.types.Object, target: Vector) -> None:
    direction = target - obj.location
    obj.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def clear_scene() -> None:
    log("Clearing existing scene")
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)

    for datablock in (bpy.data.meshes, bpy.data.materials, bpy.data.lights, bpy.data.curves, bpy.data.cameras):
        for block in list(datablock):
            if block.users == 0:
                datablock.remove(block)


def setup_cycles() -> None:
    log("Configuring Cycles render settings")
    scene = bpy.context.scene
    scene.render.engine = "CYCLES"
    scene.cycles.samples = 256
    scene.cycles.use_denoising = True
    scene.render.resolution_x = 2400
    scene.render.resolution_y = 1600
    scene.render.image_settings.file_format = "PNG"
    scene.render.filepath = str(OUTPUT_PATH)

    scene.unit_settings.system = "METRIC"
    scene.unit_settings.scale_length = 1.0

    prefs = bpy.context.preferences.addons["cycles"].preferences
    gpu_types = ["CUDA", "OPTIX", "HIP", "METAL", "ONEAPI"]
    selected_gpu = None

    for device_type in gpu_types:
        try:
            prefs.compute_device_type = device_type
            prefs.get_devices()
            has_enabled = False
            for device in prefs.devices:
                if device.type != "CPU":
                    device.use = True
                    has_enabled = True
            if has_enabled:
                selected_gpu = device_type
                scene.cycles.device = "GPU"
                break
        except Exception:
            continue

    if selected_gpu:
        log(f"Using GPU device type: {selected_gpu}")
    else:
        scene.cycles.device = "CPU"
        log("No GPU backend available; falling back to CPU")


def build_trapezoid_mesh(name: str, z0_front: float, z0_rear: float, z1_front: float, z1_rear: float) -> bpy.types.Object:
    mesh = bpy.data.meshes.new(name)
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)

    y0 = 0.0
    y1 = LENGTH
    xf0 = FRONT_W / 2.0
    xr1 = REAR_W / 2.0

    verts = [
        (-xf0, y0, z0_front),
        ( xf0, y0, z0_front),
        ( xr1, y1, z0_rear),
        (-xr1, y1, z0_rear),
        (-xf0, y0, z1_front),
        ( xf0, y0, z1_front),
        ( xr1, y1, z1_rear),
        (-xr1, y1, z1_rear),
    ]

    faces = [
        (0, 1, 2, 3),
        (4, 7, 6, 5),
        (0, 4, 5, 1),
        (1, 5, 6, 2),
        (2, 6, 7, 3),
        (3, 7, 4, 0),
    ]

    mesh.from_pydata(verts, [], faces)
    mesh.update()
    return obj


def add_bevel_modifier(obj: bpy.types.Object, radius_mm: float, segments: int) -> None:
    mod = obj.modifiers.new(name="Bevel", type="BEVEL")
    mod.limit_method = "ANGLE"
    mod.width = radius_mm * MM
    mod.segments = segments
    mod.profile = 0.7


def add_boolean_difference(target: bpy.types.Object, cutter: bpy.types.Object) -> None:
    mod = target.modifiers.new(name=f"Bool_{cutter.name}", type="BOOLEAN")
    mod.operation = "DIFFERENCE"
    mod.solver = "FAST"
    mod.object = cutter
    bpy.context.view_layer.objects.active = target
    bpy.ops.object.modifier_apply(modifier=mod.name)
    bpy.data.objects.remove(cutter, do_unlink=True)


def create_material_abs_black() -> bpy.types.Material:
    mat = bpy.data.materials.new("ABS_Matte_Black")
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = hex_color("#1A1A1A")
    bsdf.inputs["Roughness"].default_value = 0.9
    bsdf.inputs["Metallic"].default_value = 0.0
    return mat


def create_material_aluminum() -> bpy.types.Material:
    mat = bpy.data.materials.new("Aluminum_Brushed")
    mat.use_nodes = True
    nt = mat.node_tree
    nodes = nt.nodes
    links = nt.links

    bsdf = nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = hex_color("#2C2C2C")
    bsdf.inputs["Metallic"].default_value = 0.95
    bsdf.inputs["Roughness"].default_value = 0.15
    bsdf.inputs["Anisotropic"].default_value = 0.6

    texcoord = nodes.new("ShaderNodeTexCoord")
    mapping = nodes.new("ShaderNodeMapping")
    noise = nodes.new("ShaderNodeTexNoise")
    ramp = nodes.new("ShaderNodeValToRGB")

    texcoord.location = (-800, 200)
    mapping.location = (-620, 200)
    noise.location = (-440, 200)
    ramp.location = (-250, 200)

    mapping.inputs["Scale"].default_value = (220.0, 1.2, 1.2)
    noise.inputs["Scale"].default_value = 340.0
    noise.inputs["Detail"].default_value = 2.0
    noise.inputs["Roughness"].default_value = 0.3
    ramp.color_ramp.elements[0].position = 0.35
    ramp.color_ramp.elements[1].position = 0.7

    links.new(texcoord.outputs["Object"], mapping.inputs["Vector"])
    links.new(mapping.outputs["Vector"], noise.inputs["Vector"])
    links.new(noise.outputs["Fac"], ramp.inputs["Fac"])
    links.new(ramp.outputs["Color"], bsdf.inputs["Roughness"])

    return mat


def create_material_silicone() -> bpy.types.Material:
    mat = bpy.data.materials.new("Silicone_Dark")
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = hex_color("#2A2A2A")
    bsdf.inputs["Roughness"].default_value = 0.95
    bsdf.inputs["Metallic"].default_value = 0.0
    return mat


def create_material_rubber() -> bpy.types.Material:
    mat = bpy.data.materials.new("Rubber_Black")
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = hex_color("#0D0D0D")
    bsdf.inputs["Roughness"].default_value = 1.0
    return mat


def create_material_etched() -> bpy.types.Material:
    mat = bpy.data.materials.new("Etched_Text")
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = hex_color("#222222")
    bsdf.inputs["Roughness"].default_value = 0.3
    bsdf.inputs["Metallic"].default_value = 0.7
    return mat


def create_material_led() -> bpy.types.Material:
    mat = bpy.data.materials.new("LED_Diffuser")
    mat.use_nodes = True
    nt = mat.node_tree
    nodes = nt.nodes

    bsdf = nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = hex_color("#FFE4B5")
    bsdf.inputs["Roughness"].default_value = 0.45
    bsdf.inputs["Transmission Weight"].default_value = 0.22
    bsdf.inputs["Emission Color"].default_value = hex_color("#FFE4B5")
    bsdf.inputs["Emission Strength"].default_value = 3.0

    return mat


def create_material_ground() -> bpy.types.Material:
    mat = bpy.data.materials.new("Ground_Studio")
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = hex_color("#F5F5F5")
    bsdf.inputs["Roughness"].default_value = 0.12
    bsdf.inputs["Specular IOR Level"].default_value = 0.35
    return mat


def assign_material(obj: bpy.types.Object, material: bpy.types.Material) -> None:
    if obj.data.materials:
        obj.data.materials[0] = material
    else:
        obj.data.materials.append(material)


def create_cylinder(name: str, radius_mm: float, depth_mm: float, location: tuple[float, float, float], vertices: int = 96) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=vertices,
        radius=radius_mm * MM,
        depth=depth_mm * MM,
        location=location,
    )
    obj = bpy.context.active_object
    obj.name = name
    return obj


def create_zone_text(label: str, location: tuple[float, float, float], rotation: tuple[float, float, float], size_mm: float, material: bpy.types.Material) -> None:
    bpy.ops.object.text_add(location=location, rotation=rotation)
    text_obj = bpy.context.active_object
    text_obj.data.body = label
    text_obj.data.size = size_mm * MM
    text_obj.data.extrude = 0.3 * MM
    text_obj.data.bevel_depth = 0.02 * MM

    bpy.ops.object.convert(target="MESH")
    text_mesh = bpy.context.active_object
    text_mesh.name = f"Text_{label}"

    text_mesh.location.z -= 0.3 * MM
    assign_material(text_mesh, material)


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    clear_scene()
    setup_cycles()

    log("Creating materials")
    mat_abs = create_material_abs_black()
    mat_al = create_material_aluminum()
    mat_silicone = create_material_silicone()
    mat_rubber = create_material_rubber()
    mat_etched = create_material_etched()
    mat_led = create_material_led()
    mat_ground = create_material_ground()

    log("Building base trapezoidal wedge")
    base = build_trapezoid_mesh(
        "Base_ABS",
        z0_front=0.0,
        z0_rear=0.0,
        z1_front=BASE_FRONT_H,
        z1_rear=BASE_REAR_H,
    )
    add_bevel_modifier(base, radius_mm=20.0, segments=8)
    assign_material(base, mat_abs)

    log("Building top aluminum plate")
    top_plate = build_trapezoid_mesh(
        "Top_Plate",
        z0_front=BASE_FRONT_H,
        z0_rear=BASE_REAR_H,
        z1_front=BASE_FRONT_H + TOP_THICKNESS,
        z1_rear=BASE_REAR_H + TOP_THICKNESS,
    )
    add_bevel_modifier(top_plate, radius_mm=1.0, segments=4)
    assign_material(top_plate, mat_al)

    log("Cutting Zone 1 recessed dish")
    z1_y = 55 * MM
    z1_x = x_from_left(z1_y, 35.0)
    z1_top = top_height_at_y(z1_y) + TOP_THICKNESS
    zone1_cut = create_cylinder(
        "Zone1_Cutter",
        radius_mm=40.0,
        depth_mm=2.5,
        location=(z1_x, z1_y, z1_top - (2.5 * MM / 2.0)),
    )
    add_boolean_difference(top_plate, zone1_cut)

    zone1_lining = create_cylinder(
        "Zone1_Silicone",
        radius_mm=39.0,
        depth_mm=2.3,
        location=(z1_x, z1_y, z1_top - (2.3 * MM / 2.0) - 0.05 * MM),
    )
    assign_material(zone1_lining, mat_silicone)

    log("Cutting Zone 2 recessed dish")
    z2_y = 55 * MM
    z2_x = 0.0
    z2_top = top_height_at_y(z2_y) + TOP_THICKNESS
    zone2_cut = create_cylinder(
        "Zone2_Cutter",
        radius_mm=30.0,
        depth_mm=2.5,
        location=(z2_x, z2_y, z2_top - (2.5 * MM / 2.0)),
    )
    add_boolean_difference(top_plate, zone2_cut)

    zone2_lining = create_cylinder(
        "Zone2_Silicone",
        radius_mm=29.0,
        depth_mm=2.3,
        location=(z2_x, z2_y, z2_top - (2.3 * MM / 2.0) - 0.05 * MM),
    )
    assign_material(zone2_lining, mat_silicone)

    log("Building Zone 3 watch cradle pod")
    z3_y = 220 * MM
    z3_x = x_from_left(z3_y, 35.0)
    z3_top = top_height_at_y(z3_y) + TOP_THICKNESS
    watch_pod = create_cylinder(
        "Zone3_Watch_Pod",
        radius_mm=25.0,
        depth_mm=8.0,
        location=(z3_x, z3_y, z3_top + (8 * MM / 2.0)),
    )
    watch_pod.rotation_euler = Euler((math.radians(30.0), 0.0, 0.0), "XYZ")
    assign_material(watch_pod, mat_abs)

    log("Cutting Zone 4 laptop groove")
    z4_y = LENGTH - (12 * MM / 2.0)
    z4_x = x_from_right(LENGTH, 30.0 + 11.0)
    z4_z = (BASE_REAR_H + TOP_THICKNESS) / 2.0
    bpy.ops.mesh.primitive_cube_add(
        size=1.0,
        location=(z4_x, z4_y, z4_z),
        scale=(22 * MM / 2.0, 12 * MM / 2.0, (BASE_REAR_H + TOP_THICKNESS) / 2.0),
    )
    zone4_cut_base = bpy.context.active_object
    zone4_cut_base.name = "Zone4_Groove_Cutter_Base"
    add_boolean_difference(base, zone4_cut_base)

    bpy.ops.mesh.primitive_cube_add(
        size=1.0,
        location=(z4_x, z4_y, z4_z),
        scale=(22 * MM / 2.0, 12 * MM / 2.0, (BASE_REAR_H + TOP_THICKNESS) / 2.0),
    )
    zone4_cut_top = bpy.context.active_object
    zone4_cut_top.name = "Zone4_Groove_Cutter_Top"
    add_boolean_difference(top_plate, zone4_cut_top)

    bpy.ops.mesh.primitive_cube_add(
        size=1.0,
        location=(z4_x, z4_y - 0.2 * MM, z4_z),
        scale=(20 * MM / 2.0, 10 * MM / 2.0, (BASE_REAR_H + TOP_THICKNESS - 0.8 * MM) / 2.0),
    )
    groove_lining = bpy.context.active_object
    groove_lining.name = "Zone4_Silicone"
    assign_material(groove_lining, mat_silicone)

    log("Adding LED bar underside (4 sections)")
    section_len_mm = (290.0 - (3.0 * 2.0)) / 4.0
    start_x = -145.0
    led_y = 4.0
    led_z = 3.5
    for idx in range(4):
        section_center_x_mm = start_x + section_len_mm / 2.0 + idx * (section_len_mm + 2.0)
        bpy.ops.mesh.primitive_cube_add(
            size=1.0,
            location=(section_center_x_mm * MM, led_y * MM, led_z * MM),
            scale=(section_len_mm * MM / 2.0, 8 * MM / 2.0, 1.2 * MM / 2.0),
        )
        led_section = bpy.context.active_object
        led_section.name = f"LED_Section_{idx + 1}"
        assign_material(led_section, mat_led)

    log("Adding rubber feet")
    foot_positions = [
        (x_from_left(10 * MM, 10.0), 10 * MM),
        (x_from_right(10 * MM, 10.0), 10 * MM),
        (x_from_left((300 - 10) * MM, 10.0), (300 - 10) * MM),
        (x_from_right((300 - 10) * MM, 10.0), (300 - 10) * MM),
    ]
    for idx, (fx, fy) in enumerate(foot_positions, start=1):
        foot = create_cylinder(
            f"Foot_{idx}",
            radius_mm=7.5,
            depth_mm=3.0,
            location=(fx, fy, -1.5 * MM),
            vertices=48,
        )
        assign_material(foot, mat_rubber)

    log("Adding zone labels and wordmark")
    text_rot = (0.0, 0.0, 0.0)
    create_zone_text("PHONE", (z1_x - 8 * MM, z1_y + 52 * MM, z1_top + 0.15 * MM), text_rot, 8.0, mat_etched)
    create_zone_text("BUDS", (z2_x - 9 * MM, z2_y + 52 * MM, z2_top + 0.15 * MM), text_rot, 8.0, mat_etched)
    create_zone_text("WATCH", (z3_x - 12 * MM, z3_y - 40 * MM, z3_top + 0.15 * MM), text_rot, 8.0, mat_etched)

    z4_text_y = 235 * MM
    z4_text_x = x_from_right(z4_text_y, 45.0)
    z4_top = top_height_at_y(z4_text_y) + TOP_THICKNESS
    create_zone_text("LAPTOP", (z4_text_x - 14 * MM, z4_text_y, z4_top + 0.15 * MM), text_rot, 8.0, mat_etched)

    wordmark_y = 270 * MM
    wordmark_x = -20 * MM
    wordmark_z = top_height_at_y(wordmark_y) + TOP_THICKNESS + 0.15 * MM
    create_zone_text("Quad-Dock", (wordmark_x, wordmark_y, wordmark_z), text_rot, 9.0, mat_etched)

    log("Building studio ground and background")
    bpy.ops.mesh.primitive_plane_add(size=8.0, location=(0.0, 0.15, 0.0))
    ground = bpy.context.active_object
    ground.name = "Studio_Ground"
    assign_material(ground, mat_ground)

    world = bpy.data.worlds["World"]
    world.use_nodes = True
    bg = world.node_tree.nodes["Background"]
    bg.inputs["Color"].default_value = hex_color("#FFFFFF")
    bg.inputs["Strength"].default_value = 1.0

    log("Setting up studio lights")
    key = add_area_light(
        name="Key_Light",
        location=(-0.45, -0.18, 0.42),
        rotation=(math.radians(58), math.radians(8), math.radians(-30)),
        size_x=1.2,
        size_y=1.2,
        energy=8.0,
        color="#FFF2E0",
    )
    fill = add_area_light(
        name="Fill_Light",
        location=(0.48, -0.05, 0.30),
        rotation=(math.radians(70), math.radians(-5), math.radians(38)),
        size_x=1.2,
        size_y=1.2,
        energy=3.0,
        color="#EAF4FF",
    )
    rim = add_area_light(
        name="Rim_Light",
        location=(0.0, 0.58, 0.23),
        rotation=(math.radians(120), 0.0, math.radians(180)),
        size_x=0.35,
        size_y=0.35,
        energy=5.0,
        color="#FFFFFF",
    )
    _ = (key, fill, rim)

    log("Configuring camera")
    bpy.ops.object.camera_add(location=(-0.38, -0.36, 0.24))
    camera = bpy.context.active_object
    camera.name = "Product_Camera"
    camera.data.lens = 85.0

    target = Vector((0.0, LENGTH * 0.55, 0.02))
    look_at(camera, target)
    bpy.context.scene.camera = camera

    log(f"Rendering to {OUTPUT_PATH}")
    bpy.ops.render.render(write_still=True)
    log("Render complete")


def add_area_light(
    name: str,
    location: tuple[float, float, float],
    rotation: tuple[float, float, float],
    size_x: float,
    size_y: float,
    energy: float,
    color: str,
) -> bpy.types.Object:
    data = bpy.data.lights.new(name=name, type="AREA")
    data.shape = "RECTANGLE"
    data.size = size_x
    data.size_y = size_y
    data.energy = energy
    data.color = hex_color(color)[:3]

    light = bpy.data.objects.new(name=name, object_data=data)
    bpy.context.collection.objects.link(light)
    light.location = location
    light.rotation_euler = Euler(rotation, "XYZ")
    return light


if __name__ == "__main__":
    main()
