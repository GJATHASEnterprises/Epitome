"""
Epitome Step — Hero Product Image
Clean isometric renders. No labels, no text. Pure product shot.

Usage:
    python generate_image.py                 # both models
    python generate_image.py --model walnut
    python generate_image.py --model obsidian
"""

import argparse
import math
import os
from PIL import Image, ImageDraw, ImageFilter

OUTPUT_W, OUTPUT_H = 1200, 800

CONFIGS = {
    "walnut": {
        "bg": (245, 240, 232),
        "base": (30, 30, 30),
        "riser": (28, 28, 28),
        "step_top": (135, 95, 38),
        "step_face_light": (155, 115, 52),
        "step_face_dark": (110, 78, 18),
        "led_glow": (255, 214, 160),
        "shadow_col": (180, 170, 160),
    },
    "obsidian": {
        "bg": (13, 13, 13),
        "base": (18, 18, 18),
        "riser": (16, 16, 16),
        "step_top": (28, 28, 28),
        "step_face_light": (38, 38, 38),
        "step_face_dark": (18, 18, 18),
        "led_glow": (51, 153, 255),
        "shadow_col": (5, 5, 10),
    },
}


def iso_pt(x_mm, y_mm, z_mm, cx, cy, s=2.2):
    a = math.radians(30)
    px = (x_mm - y_mm) * math.cos(a)
    py = (x_mm + y_mm) * math.sin(a) - z_mm
    return cx + px * s, cy + py * s


def face4(draw, pts, fill, outline=None):
    draw.polygon(pts, fill=fill, outline=outline)


def build_hero(model: str) -> Image.Image:
    c = CONFIGS[model]
    img = Image.new("RGB", (OUTPUT_W, OUTPUT_H), c["bg"])
    draw = ImageDraw.Draw(img, "RGBA")

    cx = OUTPUT_W * 0.48
    cy = OUTPUT_H * 0.66

    def pt(x, y, z):
        return iso_pt(x, y, z, cx, cy)

    # Shadow ellipse
    shadow_layer = Image.new("RGBA", (OUTPUT_W, OUTPUT_H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow_layer)
    if model == "walnut":
        sd.ellipse([cx - 180, cy - 30, cx + 180, cy + 40],
                   fill=(150, 140, 130, 60))
    else:
        sd.ellipse([cx - 180, cy - 30, cx + 180, cy + 40],
                   fill=(0, 0, 0, 120))
    shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(20))
    img.paste(shadow_layer, mask=shadow_layer)
    draw = ImageDraw.Draw(img, "RGBA")

    # Base
    face4(draw, [pt(0, 0, 3), pt(165, 0, 3), pt(165, 100, 3), pt(0, 100, 3)], c["base"])
    face4(draw, [pt(0, 0, 0), pt(165, 0, 0), pt(165, 0, 3), pt(0, 0, 3)],
          tuple(max(0, v - 10) for v in c["riser"]))

    # Riser
    face4(draw, [pt(0, 0, 25), pt(165, 0, 25), pt(165, 100, 25), pt(0, 100, 25)], c["riser"])
    face4(draw, [pt(0, 0, 3), pt(165, 0, 3), pt(165, 0, 25), pt(0, 0, 25)],
          tuple(max(0, v - 15) for v in c["riser"]))
    face4(draw, [pt(165, 0, 3), pt(165, 100, 3), pt(165, 100, 25), pt(165, 0, 25)],
          tuple(max(0, v - 30) for v in c["riser"]))

    # LED glow on front riser
    glow_layer = Image.new("RGBA", (OUTPUT_W, OUTPUT_H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow_layer)
    gd.polygon([pt(17.5, 0, 26), pt(147.5, 0, 26),
                pt(147.5, 0, 36), pt(17.5, 0, 36)],
               fill=c["led_glow"] + (90,))
    glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(8))
    img.paste(Image.alpha_composite(img.convert("RGBA"), glow_layer).convert("RGB"))
    draw = ImageDraw.Draw(img, "RGBA")

    # Step 1
    face4(draw, [pt(0, 0, 40), pt(165, 0, 40), pt(165, 100, 40), pt(0, 100, 40)],
          c["step_top"])
    face4(draw, [pt(0, 0, 25), pt(165, 0, 25), pt(165, 0, 40), pt(0, 0, 40)],
          c["step_face_light"])
    face4(draw, [pt(165, 0, 25), pt(165, 100, 25), pt(165, 100, 40), pt(165, 0, 40)],
          c["step_face_dark"])

    # Step 2
    face4(draw, [pt(17.5, 0, 55), pt(147.5, 0, 55), pt(147.5, 100, 55), pt(17.5, 100, 55)],
          c["step_top"])
    face4(draw, [pt(17.5, 0, 40), pt(147.5, 0, 40), pt(147.5, 0, 55), pt(17.5, 0, 55)],
          c["step_face_light"])
    face4(draw, [pt(147.5, 0, 40), pt(147.5, 100, 40), pt(147.5, 100, 55), pt(147.5, 0, 55)],
          c["step_face_dark"])

    # Step 3
    face4(draw, [pt(35, 20, 70), pt(130, 20, 70), pt(130, 100, 70), pt(35, 100, 70)],
          c["step_top"])
    face4(draw, [pt(35, 20, 55), pt(130, 20, 55), pt(130, 20, 70), pt(35, 20, 70)],
          c["step_face_light"])
    face4(draw, [pt(130, 20, 55), pt(130, 100, 55), pt(130, 100, 70), pt(130, 20, 70)],
          c["step_face_dark"])

    return img


def main():
    parser = argparse.ArgumentParser(description="Generate Epitome Step hero images")
    parser.add_argument("--model", choices=["walnut", "obsidian", "both"], default="both")
    args = parser.parse_args()

    os.makedirs("../assets", exist_ok=True)
    os.makedirs("assets", exist_ok=True)

    models = ["walnut", "obsidian"] if args.model == "both" else [args.model]
    for model in models:
        img = build_hero(model)
        out_dir = "../assets" if os.path.isdir("../assets") else "assets"
        path = os.path.join(out_dir, f"step-{model}-hero.png")
        img.save(path)
        print(f"Saved: {path}")


if __name__ == "__main__":
    main()
