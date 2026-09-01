"""
Epitome Step — Marketing Render
Produces labelled isometric renders for both models.

Usage:
    python generate_render.py                 # both models
    python generate_render.py --model walnut
    python generate_render.py --model obsidian
"""

import argparse
import math
import os
from PIL import Image, ImageDraw, ImageFont

# ── Geometry constants (mm → pixels, 4px/mm) ──────────────────────────────────
SCALE = 4
W = 165 * SCALE   # 660 px
D = 100 * SCALE   # 400 px
H_BASE = 3 * SCALE
H_RISER = 22 * SCALE
H_S1 = 15 * SCALE
H_S2 = 15 * SCALE
H_S3 = 15 * SCALE
H_TOTAL = (3 + 22 + 15 + 15 + 15) * SCALE  # 280 px

S2_W = 130 * SCALE
S3_W = 95 * SCALE
S3_D = 80 * SCALE

OUTPUT_W, OUTPUT_H = 1200, 800

# ── Colour palettes ────────────────────────────────────────────────────────────
PALETTES = {
    "walnut": {
        "bg": (17, 17, 17),
        "base": (26, 26, 26),
        "riser": (26, 26, 26),
        "step_face_light": (160, 120, 60),
        "step_face_dark": (139, 105, 20),
        "step_top": (140, 100, 40),
        "led_glow": (255, 214, 160),
        "led_core": (255, 230, 180),
        "zone_colour": (255, 214, 160, 80),
        "price_colour": (212, 168, 75),
        "text_colour": (255, 255, 255),
        "label_colour": (200, 200, 200),
        "leader_colour": (120, 120, 120),
    },
    "obsidian": {
        "bg": (10, 10, 10),
        "base": (20, 20, 20),
        "riser": (18, 18, 18),
        "step_face_light": (35, 35, 35),
        "step_face_dark": (20, 20, 20),
        "step_top": (28, 28, 28),
        "led_glow": (51, 153, 255),
        "led_core": (150, 100, 255),
        "zone_colour": (51, 153, 255, 80),
        "price_colour": (51, 153, 255),
        "text_colour": (255, 255, 255),
        "label_colour": (180, 180, 180),
        "leader_colour": (80, 100, 120),
    },
}


def iso_project(x, y, z, cx, cy, angle_deg=30):
    """Project 3D (mm-scale) point to 2D canvas using simple isometric projection."""
    a = math.radians(angle_deg)
    px = (x - y) * math.cos(a)
    py = (x + y) * math.sin(a) - z
    return cx + px, cy + py


def draw_face(draw, pts, fill, outline=(0, 0, 0)):
    draw.polygon(pts, fill=fill, outline=outline)


def build_render(model: str) -> Image.Image:
    p = PALETTES[model]
    img = Image.new("RGB", (OUTPUT_W, OUTPUT_H), p["bg"])
    draw = ImageDraw.Draw(img, "RGBA")

    # ── Isometric projection origin ────────────────────────────────────────────
    cx = OUTPUT_W * 0.45
    cy = OUTPUT_H * 0.62

    # Scale from mm to projection units
    s = 2.0  # mm → projection px

    def pt(x_mm, y_mm, z_mm):
        return iso_project(x_mm * s, y_mm * s, z_mm * s, cx, cy)

    def face4(x0, y0, z0, x1, y1, z1, x2, y2, z2, x3, y3, z3, fill, **kw):
        pts = [pt(x0, y0, z0), pt(x1, y1, z1), pt(x2, y2, z2), pt(x3, y3, z3)]
        draw_face(draw, pts, fill, **kw)

    # ── Draw base plate ────────────────────────────────────────────────────────
    bx0, bx1, by0, by1, bz0, bz1 = 0, 165, 0, 100, 0, 3
    face4(bx0, by0, bz1,  bx1, by0, bz1,  bx1, by1, bz1,  bx0, by1, bz1, p["base"])
    face4(bx0, by0, bz0,  bx1, by0, bz0,  bx1, by0, bz1,  bx0, by0, bz1,
          tuple(max(0, c - 30) for c in p["riser"]))

    # ── Draw riser ─────────────────────────────────────────────────────────────
    rz0, rz1 = 3, 25
    face4(0, 0, rz1,  165, 0, rz1,  165, 100, rz1,  0, 100, rz1, p["riser"])
    # Front face
    face4(0, 0, rz0,  165, 0, rz0,  165, 0, rz1,  0, 0, rz1,
          tuple(max(0, c - 20) for c in p["riser"]))
    # Right face
    face4(165, 0, rz0,  165, 100, rz0,  165, 100, rz1,  165, 0, rz1,
          tuple(max(0, c - 40) for c in p["riser"]))

    # ── LED glow on riser front face ────────────────────────────────────────────
    led_col = p["led_glow"] + (60,)
    face4(17.5, 0, 26,  147.5, 0, 26,  147.5, 0, 36,  17.5, 0, 36, led_col)

    # ── Draw Step 1 (phone) ────────────────────────────────────────────────────
    s1z0, s1z1 = 25, 40
    face4(0, 0, s1z1,  165, 0, s1z1,  165, 100, s1z1,  0, 100, s1z1,
          p["step_top"])
    face4(0, 0, s1z0,  165, 0, s1z0,  165, 0, s1z1,  0, 0, s1z1,
          p["step_face_light"])
    face4(165, 0, s1z0,  165, 100, s1z0,  165, 100, s1z1,  165, 0, s1z1,
          p["step_face_dark"])

    # Phone silhouette on Step 1 (portrait)
    phone_pts = [pt(75.75, 10, 40), pt(89.25, 10, 40),
                 pt(89.25, 55, 40), pt(75.75, 55, 40)]
    draw.polygon(phone_pts, fill=(240, 240, 255, 160))
    # Qi2 glow
    qi2_pts = [pt(72, 25, 40), pt(93, 25, 40), pt(93, 45, 40), pt(72, 45, 40)]
    draw.polygon(qi2_pts, fill=(p["led_core"][0], p["led_core"][1], p["led_core"][2], 40))

    # ── Draw Step 2 (buds) ─────────────────────────────────────────────────────
    s2x0, s2x1 = 17.5, 147.5
    s2z0, s2z1 = 40, 55
    face4(s2x0, 0, s2z1,  s2x1, 0, s2z1,  s2x1, 100, s2z1,  s2x0, 100, s2z1,
          p["step_top"])
    face4(s2x0, 0, s2z0,  s2x1, 0, s2z0,  s2x1, 0, s2z1,  s2x0, 0, s2z1,
          p["step_face_light"])
    face4(s2x1, 0, s2z0,  s2x1, 100, s2z0,  s2x1, 100, s2z1,  s2x1, 0, s2z1,
          p["step_face_dark"])
    # Buds silhouette
    buds_pts = [pt(75, 15, 55), pt(90, 15, 55), pt(90, 28, 55), pt(75, 28, 55)]
    draw.polygon(buds_pts, fill=(200, 200, 240, 160))

    # ── Draw Step 3 (watch) ────────────────────────────────────────────────────
    s3x0, s3x1 = 35, 130
    s3y0 = 20
    s3z0, s3z1 = 55, 70
    face4(s3x0, s3y0, s3z1,  s3x1, s3y0, s3z1,  s3x1, 100, s3z1,  s3x0, 100, s3z1,
          p["step_top"])
    face4(s3x0, s3y0, s3z0,  s3x1, s3y0, s3z0,  s3x1, s3y0, s3z1,  s3x0, s3y0, s3z1,
          p["step_face_light"])
    face4(s3x1, s3y0, s3z0,  s3x1, 100, s3z0,  s3x1, 100, s3z1,  s3x1, s3y0, s3z1,
          p["step_face_dark"])
    # Watch silhouette (circle approximation as octagon)
    wc_x, wc_y, wc_z = 82.5, 60, 70
    r = 14
    watch_pts = [pt(wc_x + r * math.cos(math.radians(a)),
                    wc_y + r * math.sin(math.radians(a)) * 0.5, wc_z)
                 for a in range(0, 360, 45)]
    draw.polygon(watch_pts, fill=(220, 220, 220, 200))

    # ── Labels ─────────────────────────────────────────────────────────────────
    try:
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 28)
        font_label = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
        font_price = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 32)
    except Exception:
        font_title = ImageFont.load_default()
        font_label = font_title
        font_price = font_title

    # Model title
    title = f"Epitome Step {'Walnut' if model == 'walnut' else 'Obsidian'}"
    draw.text((40, 40), title, font=font_title, fill=p["text_colour"])

    # Zone labels with leader lines
    labels = [
        ("Qi2 · 20W", pt(82.5, 10, 42)),
        ("Qi · 5W", pt(82.5, 10, 57)),
        ("Watch · 5W", pt(82.5, 30, 72)),
    ]
    lx = OUTPUT_W - 200
    for i, (text, anchor) in enumerate(labels):
        ty = 180 + i * 50
        draw.line([anchor, (lx, ty)], fill=p["leader_colour"], width=1)
        draw.text((lx + 4, ty - 10), text, font=font_label, fill=p["label_colour"])

    # USB-C port labels
    usb_a_pt = pt(120, 102, 15)
    usb_b_pt = pt(140, 102, 15)
    draw.text((usb_a_pt[0] - 30, usb_a_pt[1] + 8), "USB-C 60W", font=font_label,
              fill=p["label_colour"])
    draw.text((usb_b_pt[0] - 30, usb_b_pt[1] + 28), "USB-C 30W", font=font_label,
              fill=p["label_colour"])

    # Price
    price = "$99" if model == "walnut" else "$79"
    draw.text((OUTPUT_W - 120, OUTPUT_H - 60), price, font=font_price, fill=p["price_colour"])

    return img


def main():
    parser = argparse.ArgumentParser(description="Generate Epitome Step marketing renders")
    parser.add_argument("--model", choices=["walnut", "obsidian", "both"], default="both")
    args = parser.parse_args()

    os.makedirs("../assets", exist_ok=True)
    os.makedirs("assets", exist_ok=True)

    models = ["walnut", "obsidian"] if args.model == "both" else [args.model]
    for model in models:
        img = build_render(model)
        out_dir = "../assets" if os.path.isdir("../assets") else "assets"
        path = os.path.join(out_dir, f"step-{model}-render.png")
        img.save(path)
        print(f"Saved: {path}")


if __name__ == "__main__":
    main()
