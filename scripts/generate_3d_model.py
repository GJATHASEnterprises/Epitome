"""
generate_3d_model.py — Step 3D model generator

Generates:
  - DXF top-view layout (assets/step-top-view.dxf)
  - ASCII geometry summary

Coordinate system:
  X=0 left, X=165 right, centred at X=82.5
  Y=0 front, Y=100 rear
  Z=0 base floor, up = +Z

Dimensions (mm):
  Base plate:  165 × 100 × 3    (Z=0  to Z=3)
  Riser:       165 × 100 × 22   (Z=3  to Z=25)
  Step 1:      165 × 100 × 15   (Z=25 to Z=40)  top surface Z=40
  Step 2:      130 × 100 × 15   (Z=40 to Z=55)  top surface Z=55
  Step 3:       95 ×  80 × 15   (Z=55 to Z=70)  top surface Z=70, Y=20 to Y=100
"""

import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# Geometry definitions
# ---------------------------------------------------------------------------

BODIES = {
    "base_plate": {
        "x": 0, "y": 0, "z": 0,
        "w": 165, "d": 100, "h": 3,
        "desc": "Base plate",
    },
    "riser": {
        "x": 0, "y": 0, "z": 3,
        "w": 165, "d": 100, "h": 22,
        "desc": "Riser / wiring cavity",
    },
    "step1": {
        "x": 0, "y": 0, "z": 25,
        "w": 165, "d": 100, "h": 15,
        "desc": "Step 1 (phone) — top surface Z=40",
    },
    "step2": {
        "x": 17.5, "y": 0, "z": 40,
        "w": 130, "d": 100, "h": 15,
        "desc": "Step 2 (buds) — top surface Z=55",
    },
    "step3": {
        "x": 35, "y": 20, "z": 55,
        "w": 95, "d": 80, "h": 15,
        "desc": "Step 3 (watch) — top surface Z=70, setback Y=20",
    },
}

ZONES = {
    "zone1_phone": {
        "cx": 82.5, "cy": 50, "z": 40,
        "w": 75, "d": 90,
        "desc": "Zone 1 phone pad (Qi2 20W) — portrait 75×90mm",
    },
    "zone2_buds": {
        "cx": 82.5, "cy": 50, "z": 55,
        "w": 65, "d": 50,
        "desc": "Zone 2 buds pad (Qi 5W) — 65×50mm",
    },
    "zone3_watch": {
        "cx": 82.5, "cy": 60, "z": 70,
        "w": 55, "d": 55,
        "desc": "Zone 3 watch cradle — 55×55mm",
    },
}

PORTS = {
    "dc_jack":  {"x": 40,  "y": 100, "z": 15, "r": 5.5, "desc": "DC barrel jack inlet"},
    "usbc_a":   {"x": 120, "y": 100, "z": 15, "r": 5.0, "desc": "USB-C Port A (60W)"},
    "usbc_b":   {"x": 140, "y": 100, "z": 15, "r": 5.0, "desc": "USB-C Port B (30W)"},
}

LED_DIFFUSER = {
    "x": 17.5, "y": 0, "z": 27,
    "w": 130, "h": 8,
    "desc": "LED diffuser slot — front fascia, 130×8mm",
}


# ---------------------------------------------------------------------------
# DXF writer (minimal, no external deps)
# ---------------------------------------------------------------------------

def dxf_header():
    return "0\nSECTION\n2\nHEADER\n9\n$ACADVER\n1\nAC1009\n0\nENDSEC\n"

def dxf_entities_start():
    return "0\nSECTION\n2\nENTITIES\n"

def dxf_entities_end():
    return "0\nENDSEC\n0\nEOF\n"

def dxf_rect(x, y, w, d, layer="0", color=7):
    """Draw a rectangle as 4 LINE entities in DXF."""
    lines = []
    corners = [
        (x, y), (x+w, y), (x+w, y+d), (x, y+d), (x, y)
    ]
    for i in range(4):
        x1, y1 = corners[i]
        x2, y2 = corners[i+1]
        lines.append(
            f"0\nLINE\n8\n{layer}\n62\n{color}\n"
            f"10\n{x1:.3f}\n20\n{y1:.3f}\n30\n0.0\n"
            f"11\n{x2:.3f}\n21\n{y2:.3f}\n31\n0.0\n"
        )
    return "".join(lines)

def dxf_circle(cx, cy, r, layer="0", color=3):
    return (
        f"0\nCIRCLE\n8\n{layer}\n62\n{color}\n"
        f"10\n{cx:.3f}\n20\n{cy:.3f}\n30\n0.0\n"
        f"40\n{r:.3f}\n"
    )

def dxf_text(x, y, text, height=4, layer="0", color=7):
    return (
        f"0\nTEXT\n8\n{layer}\n62\n{color}\n"
        f"10\n{x:.3f}\n20\n{y:.3f}\n30\n0.0\n"
        f"40\n{height:.1f}\n1\n{text}\n"
    )


def generate_dxf():
    dxf = dxf_header() + dxf_entities_start()

    # Step outlines (top-view footprints)
    # Color coding: 7=white, 3=green, 5=blue, 6=magenta, 4=cyan
    for name, b in BODIES.items():
        color = {"base_plate": 8, "riser": 8, "step1": 7, "step2": 5, "step3": 3}.get(name, 7)
        dxf += dxf_rect(b["x"], b["y"], b["w"], b["d"], layer=name, color=color)
        mid_x = b["x"] + b["w"] / 2
        mid_y = b["y"] + b["d"] / 2
        dxf += dxf_text(mid_x - 15, mid_y, name.upper(), height=3, layer=name, color=color)

    # Zone pads
    for name, z in ZONES.items():
        x0 = z["cx"] - z["w"] / 2
        y0 = z["cy"] - z["d"] / 2
        dxf += dxf_rect(x0, y0, z["w"], z["d"], layer="zones", color=1)
        dxf += dxf_text(x0 + 2, y0 + 2, name, height=2.5, layer="zones", color=1)

    # Rear ports (circles at Y=100 edge)
    for name, p in PORTS.items():
        dxf += dxf_circle(p["x"], p["y"], p["r"], layer="ports", color=6)
        dxf += dxf_text(p["x"] - 5, p["y"] - 8, name, height=2.5, layer="ports", color=6)

    # LED diffuser slot
    ld = LED_DIFFUSER
    dxf += dxf_rect(ld["x"], ld["y"], ld["w"], 2, layer="led_diffuser", color=4)
    dxf += dxf_text(ld["x"] + 5, ld["y"] + 3, "LED DIFFUSER", height=2.5, layer="led_diffuser", color=4)

    dxf += dxf_entities_end()
    return dxf


def print_geometry_summary():
    print("=" * 60)
    print("STEP — Geometry Summary")
    print("=" * 60)
    for name, b in BODIES.items():
        print(f"\n{name.upper()}: {b['desc']}")
        print(f"  Origin:     X={b['x']}, Y={b['y']}, Z={b['z']}")
        print(f"  Size:       {b['w']}W × {b['d']}D × {b['h']}H mm")
        print(f"  Top face Z: {b['z'] + b['h']}")

    print("\n" + "=" * 60)
    print("CHARGING ZONES")
    print("=" * 60)
    for name, z in ZONES.items():
        print(f"\n{name.upper()}: {z['desc']}")
        print(f"  Centre:  X={z['cx']}, Y={z['cy']}, Z={z['z']}")
        print(f"  Size:    {z['w']} × {z['d']} mm")

    print("\n" + "=" * 60)
    print("REAR PORTS")
    print("=" * 60)
    for name, p in PORTS.items():
        print(f"  {name}: X={p['x']}, Y={p['y']}, Z={p['z']} — {p['desc']}")

    print("\n" + "=" * 60)
    print("ASCII SIDE VIEW")
    print("=" * 60)
    print("""
Z=70 |            +--------+
     |            | Step 3 |  15mm  (watch)
Z=55 |      +-----+--------+
     |      |  Step 2       |  15mm  (buds)
Z=40 +------+---------------+
     |   Step 1              |  15mm  (phone)
Z=25 +-----------------------+
     | ~~~~ riser cavity ~~~~ |  22mm
Z=3  +=========================+
     |  base plate             |  3mm
Z=0  +=========================+
     |<------ 165mm ---------->|
""")


if __name__ == "__main__":
    print_geometry_summary()

    dxf_path = os.path.join(OUTPUT_DIR, "step-top-view.dxf")
    with open(dxf_path, "w") as f:
        f.write(generate_dxf())
    print(f"\nDXF written to: {dxf_path}")
