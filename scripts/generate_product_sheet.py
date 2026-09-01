"""
Epitome Step — Product Sheet
Two-panel layout: dock render (left 55%) + spec panel (right 45%).
Minimum 12pt body text, 28pt title.

Usage:
    python generate_product_sheet.py                 # both models
    python generate_product_sheet.py --model walnut
    python generate_product_sheet.py --model obsidian
"""

import argparse
import math
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUTPUT_W, OUTPUT_H = 1200, 800
PANEL_SPLIT = int(OUTPUT_W * 0.55)  # 660 left, 540 right

SHEET_CONFIGS = {
    "walnut": {
        "bg": (15, 12, 10),
        "panel_bg": (20, 16, 12),
        "accent": (212, 168, 75),
        "title_col": (255, 255, 255),
        "price_col": (212, 168, 75),
        "body_col": (200, 190, 175),
        "dim_col": (130, 120, 110),
        "divider_col": (60, 50, 40),
        "step_top": (140, 100, 40),
        "step_face_light": (160, 120, 55),
        "step_face_dark": (110, 80, 20),
        "riser_col": (26, 26, 26),
        "led_glow": (255, 214, 160),
        "model_name": "Step Walnut",
        "price": "$99",
        "spec_lines": [
            ("① Phone", "20W", "Qi2"),
            ("② Buds", " 5W", "Qi"),
            ("③ Watch", " 5W", "Apple + Qi"),
            ("④ USB-C A", "60W", "Port A"),
            ("⑤ USB-C B", "30W", "Port B"),
        ],
        "detail_lines": [
            "Oiled walnut · Matte black ABS",
            "Warm white LED",
            "165 × 100 × 70 mm",
            "100W USB-C brick included",
            "3× USB-C cables included",
        ],
        "footer": "epitomecharge.com · PRE-ORDER",
    },
    "obsidian": {
        "bg": (10, 10, 15),
        "panel_bg": (14, 14, 20),
        "accent": (51, 153, 255),
        "title_col": (255, 255, 255),
        "price_col": (51, 153, 255),
        "body_col": (180, 185, 200),
        "dim_col": (100, 110, 130),
        "divider_col": (30, 35, 55),
        "step_top": (28, 28, 28),
        "step_face_light": (38, 38, 42),
        "step_face_dark": (18, 18, 22),
        "riser_col": (20, 20, 26),
        "led_glow": (51, 153, 255),
        "model_name": "Step Obsidian",
        "price": "$79",
        "spec_lines": [
            ("① Phone", "20W", "Qi2"),
            ("② Buds", " 5W", "Qi"),
            ("③ Watch", " 5W", "Apple + Qi"),
            ("④ USB-C A", "60W", "Port A"),
            ("⑤ USB-C B", "30W", "Port B"),
        ],
        "detail_lines": [
            "Full matte black ABS",
            "RGB LED · 8 colour modes",
            "165 × 100 × 70 mm",
            "100W USB-C brick included",
            "3× USB-C cables included",
        ],
        "footer": "epitomecharge.com · PRE-ORDER",
    },
}


def iso_pt(x, y, z, cx, cy, s=1.7):
    a = math.radians(30)
    px = (x - y) * math.cos(a)
    py = (x + y) * math.sin(a) - z
    return cx + px * s, cy + py * s


def draw_dock(img: Image.Image, cfg: dict, cx: float, cy: float):
    """Draw the dock isometric render into the left panel."""
    draw = ImageDraw.Draw(img, "RGBA")

    def pt(x, y, z):
        return iso_pt(x, y, z, cx, cy)

    def f4(pts, fill):
        draw.polygon(pts, fill=fill)

    # Base
    f4([pt(0, 0, 3), pt(165, 0, 3), pt(165, 100, 3), pt(0, 100, 3)], cfg["riser_col"])
    f4([pt(0, 0, 0), pt(165, 0, 0), pt(165, 0, 3), pt(0, 0, 3)],
       tuple(max(0, v - 8) for v in cfg["riser_col"]))

    # Riser
    f4([pt(0, 0, 25), pt(165, 0, 25), pt(165, 100, 25), pt(0, 100, 25)], cfg["riser_col"])
    f4([pt(0, 0, 3), pt(165, 0, 3), pt(165, 0, 25), pt(0, 0, 25)],
       tuple(max(0, v - 12) for v in cfg["riser_col"]))
    f4([pt(165, 0, 3), pt(165, 100, 3), pt(165, 100, 25), pt(165, 0, 25)],
       tuple(max(0, v - 25) for v in cfg["riser_col"]))

    # LED glow
    glow_layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow_layer)
    gd.polygon([pt(17.5, 0, 26), pt(147.5, 0, 26),
                pt(147.5, 0, 36), pt(17.5, 0, 36)],
               fill=cfg["led_glow"] + (100,))
    glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(6))
    base_rgba = img.convert("RGBA")
    img.paste(Image.alpha_composite(base_rgba, glow_layer).convert("RGB"))

    draw = ImageDraw.Draw(img, "RGBA")

    def f4(pts, fill):
        draw.polygon(pts, fill=fill)

    # Step 1
    f4([pt(0, 0, 40), pt(165, 0, 40), pt(165, 100, 40), pt(0, 100, 40)],
       cfg["step_top"])
    f4([pt(0, 0, 25), pt(165, 0, 25), pt(165, 0, 40), pt(0, 0, 40)],
       cfg["step_face_light"])
    f4([pt(165, 0, 25), pt(165, 100, 25), pt(165, 100, 40), pt(165, 0, 40)],
       cfg["step_face_dark"])

    # Zone 1 phone silhouette
    draw.polygon([pt(75.75, 12, 41), pt(89.25, 12, 41),
                  pt(89.25, 52, 41), pt(75.75, 52, 41)],
                 fill=(240, 240, 255, 140))

    # Zone 1 label leader
    try:
        fl = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
    except Exception:
        fl = ImageFont.load_default()
    anchor = pt(82.5, 20, 42)
    draw.line([anchor, (anchor[0] - 60, anchor[1] - 30)], fill=(150, 150, 150), width=1)
    draw.text((anchor[0] - 130, anchor[1] - 42), "Qi2 · 20W", font=fl, fill=(180, 180, 180))

    # Step 2
    f4([pt(17.5, 0, 55), pt(147.5, 0, 55), pt(147.5, 100, 55), pt(17.5, 100, 55)],
       cfg["step_top"])
    f4([pt(17.5, 0, 40), pt(147.5, 0, 40), pt(147.5, 0, 55), pt(17.5, 0, 55)],
       cfg["step_face_light"])
    f4([pt(147.5, 0, 40), pt(147.5, 100, 40), pt(147.5, 100, 55), pt(147.5, 0, 55)],
       cfg["step_face_dark"])

    draw.polygon([pt(75, 12, 56), pt(90, 12, 56), pt(90, 24, 56), pt(75, 24, 56)],
                 fill=(200, 200, 240, 140))
    anchor2 = pt(82.5, 15, 57)
    draw.line([anchor2, (anchor2[0] - 50, anchor2[1] - 25)], fill=(150, 150, 150), width=1)
    draw.text((anchor2[0] - 110, anchor2[1] - 36), "Qi · 5W", font=fl, fill=(180, 180, 180))

    # Step 3
    f4([pt(35, 20, 70), pt(130, 20, 70), pt(130, 100, 70), pt(35, 100, 70)],
       cfg["step_top"])
    f4([pt(35, 20, 55), pt(130, 20, 55), pt(130, 20, 70), pt(35, 20, 70)],
       cfg["step_face_light"])
    f4([pt(130, 20, 55), pt(130, 100, 55), pt(130, 100, 70), pt(130, 20, 70)],
       cfg["step_face_dark"])

    wc_x, wc_y, r = 82.5, 60, 14
    watch_pts = [pt(wc_x + r * math.cos(math.radians(a)),
                    wc_y + r * math.sin(math.radians(a)) * 0.5, 71)
                 for a in range(0, 360, 45)]
    draw.polygon(watch_pts, fill=(220, 220, 220, 180))
    anchor3 = pt(82.5, 45, 72)
    draw.line([anchor3, (anchor3[0] - 40, anchor3[1] - 22)], fill=(150, 150, 150), width=1)
    draw.text((anchor3[0] - 108, anchor3[1] - 32), "Watch · 5W", font=fl,
              fill=(180, 180, 180))


def draw_spec_panel(img: Image.Image, cfg: dict):
    """Draw the right spec panel."""
    draw = ImageDraw.Draw(img)

    px = PANEL_SPLIT + 36
    py = 48
    pw = OUTPUT_W - PANEL_SPLIT - 36
    line_h = OUTPUT_H

    # Panel background
    draw.rectangle([PANEL_SPLIT, 0, OUTPUT_W, OUTPUT_H], fill=cfg["panel_bg"])

    try:
        f_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 32)
        f_price = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40)
        f_zone_name = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
        f_zone_watt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)
        f_detail = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
        f_footer = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 14)
    except Exception:
        f_title = f_price = f_zone_name = f_zone_watt = f_detail = f_footer = \
            ImageFont.load_default()

    # Model name
    draw.text((px, py), cfg["model_name"], font=f_title, fill=cfg["title_col"])
    py += 44

    # Price
    draw.text((px, py), cfg["price"], font=f_price, fill=cfg["price_col"])
    py += 54

    # Divider
    draw.line([(px, py), (OUTPUT_W - 20, py)], fill=cfg["divider_col"], width=1)
    py += 14

    # Spec rows
    for zone_name, watts, protocol in cfg["spec_lines"]:
        draw.text((px, py), zone_name, font=f_zone_name, fill=cfg["body_col"])
        draw.text((px + 160, py), watts, font=f_zone_watt, fill=cfg["accent"])
        draw.text((px + 210, py), protocol, font=f_zone_name, fill=cfg["dim_col"])
        py += 34

    # Divider
    draw.line([(px, py), (OUTPUT_W - 20, py)], fill=cfg["divider_col"], width=1)
    py += 14

    # Detail lines
    for line in cfg["detail_lines"]:
        draw.text((px, py), line, font=f_detail, fill=cfg["body_col"])
        py += 26

    # Divider
    draw.line([(px, py), (OUTPUT_W - 20, py)], fill=cfg["divider_col"], width=1)
    py += 18

    # Footer
    draw.text((px, py), cfg["footer"], font=f_footer, fill=cfg["accent"])


def build_sheet(model: str) -> Image.Image:
    cfg = SHEET_CONFIGS[model]
    img = Image.new("RGB", (OUTPUT_W, OUTPUT_H), cfg["bg"])

    # Draw dock in left panel
    draw_dock(img, cfg, cx=PANEL_SPLIT * 0.48, cy=OUTPUT_H * 0.67)

    # Draw spec panel on right
    draw_spec_panel(img, cfg)

    return img


def main():
    parser = argparse.ArgumentParser(description="Generate Epitome Step product sheets")
    parser.add_argument("--model", choices=["walnut", "obsidian", "both"], default="both")
    args = parser.parse_args()

    os.makedirs("../assets", exist_ok=True)
    os.makedirs("assets", exist_ok=True)

    models = ["walnut", "obsidian"] if args.model == "both" else [args.model]
    for model in models:
        img = build_sheet(model)
        out_dir = "../assets" if os.path.isdir("../assets") else "assets"
        path = os.path.join(out_dir, f"step-{model}-product-sheet.png")
        img.save(path)
        print(f"Saved: {path}")


if __name__ == "__main__":
    main()
