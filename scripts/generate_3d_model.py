"""
Epitome Step — Technical Diagrams
Produces engineering-style views with dimensions.

Usage:
    python generate_3d_model.py
"""

import os
from PIL import Image, ImageDraw, ImageFont

TOP_W, TOP_H = 1200, 900
SIDE_W, SIDE_H = 900, 900

BG = (14, 14, 14)
GRID = (30, 30, 30)
WHITE = (230, 230, 230)
DIM_COL = (255, 220, 80)
ZONE1_COL = (51, 180, 255, 80)
ZONE2_COL = (153, 102, 255, 80)
ZONE3_COL = (51, 200, 130, 80)
USBC_COL = (255, 140, 50, 100)
LINE = (180, 180, 180)
DIM_LINE = (255, 220, 80)


def try_font(size):
    try:
        return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", size)
    except Exception:
        return ImageFont.load_default()


def try_bold(size):
    try:
        return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size)
    except Exception:
        return ImageFont.load_default()


def draw_dim_h(draw, x0, x1, y, label, font, above=True):
    """Draw horizontal dimension arrow between x0 and x1 at height y."""
    arrow_y = y - 10 if above else y + 10
    draw.line([(x0, arrow_y), (x1, arrow_y)], fill=DIM_LINE, width=1)
    draw.line([(x0, arrow_y - 5), (x0, arrow_y + 5)], fill=DIM_LINE, width=1)
    draw.line([(x1, arrow_y - 5), (x1, arrow_y + 5)], fill=DIM_LINE, width=1)
    draw.text(((x0 + x1) // 2 - 20, arrow_y - 22 if above else arrow_y + 4),
              label, font=font, fill=DIM_COL)


def draw_dim_v(draw, x, y0, y1, label, font, right=True):
    """Draw vertical dimension arrow."""
    arrow_x = x + 10 if right else x - 10
    draw.line([(arrow_x, y0), (arrow_x, y1)], fill=DIM_LINE, width=1)
    draw.line([(arrow_x - 5, y0), (arrow_x + 5, y0)], fill=DIM_LINE, width=1)
    draw.line([(arrow_x - 5, y1), (arrow_x + 5, y1)], fill=DIM_LINE, width=1)
    mid_y = (y0 + y1) // 2
    draw.text((arrow_x + 6 if right else arrow_x - 45, mid_y - 8),
              label, font=font, fill=DIM_COL)


def generate_top_view() -> Image.Image:
    img = Image.new("RGB", (TOP_W, TOP_H), BG)
    draw = ImageDraw.Draw(img, "RGBA")

    fb = try_bold(20)
    fn = try_font(14)

    # Title
    draw.text((40, 24), "Epitome Step — Top View (Z = 40mm, looking down)", font=fb, fill=WHITE)
    draw.text((40, 52), "Dimensions in mm", font=fn, fill=(140, 140, 140))

    # Scale: 4 px/mm
    S = 4
    OX = 200   # origin X
    OY = 120   # origin Y

    def px(x_mm): return OX + x_mm * S
    def py(y_mm): return OY + y_mm * S

    # Step 1 outline (165 × 100)
    draw.rectangle([px(0), py(0), px(165), py(100)], outline=LINE, width=2)

    # Zone 1 (phone pad 75×90 centred on step 1)
    z1x0, z1y0 = 82.5 - 37.5, 50 - 45
    z1x1, z1y1 = 82.5 + 37.5, 50 + 45
    z1_pts = [(px(z1x0), py(z1y0)), (px(z1x1), py(z1y0)),
              (px(z1x1), py(z1y1)), (px(z1x0), py(z1y1))]
    draw.polygon(z1_pts, fill=ZONE1_COL)
    draw.rectangle([px(z1x0), py(z1y0), px(z1x1), py(z1y1)], outline=(51, 180, 255), width=1)
    draw.text((px(65), py(45)), "Zone 1\nPhone\nQi2 20W", font=fn, fill=(51, 180, 255))

    # Step 2 (130 × 100)
    draw.rectangle([px(17.5), py(0), px(147.5), py(100)], outline=(100, 100, 200), width=2)
    z2_pts = [(px(82.5 - 32.5), py(50 - 25)), (px(82.5 + 32.5), py(50 - 25)),
              (px(82.5 + 32.5), py(50 + 25)), (px(82.5 - 32.5), py(50 + 25))]
    draw.polygon(z2_pts, fill=ZONE2_COL)
    draw.text((px(50), py(62)), "Zone 2  Qi 5W", font=fn, fill=(153, 102, 255))

    # Step 3 (95 × 80, y starts at 20)
    draw.rectangle([px(35), py(20), px(130), py(100)], outline=(51, 200, 130), width=2)
    z3_pts = [(px(82.5 - 27.5), py(60 - 27.5)), (px(82.5 + 27.5), py(60 - 27.5)),
              (px(82.5 + 27.5), py(60 + 27.5)), (px(82.5 - 27.5), py(60 + 27.5))]
    draw.polygon(z3_pts, fill=ZONE3_COL)
    draw.text((px(55), py(70)), "Zone 3\nWatch 5W", font=fn, fill=(51, 200, 130))

    # Step 3 setback annotation
    draw.line([(px(35), py(0)), (px(35), py(20))], fill=(255, 80, 80), width=1)
    draw.line([(px(130), py(0)), (px(130), py(20))], fill=(255, 80, 80), width=1)
    draw.text((px(60), py(5)), "Y=20 setback", font=fn, fill=(255, 80, 80))

    # Rear ports (shown at Y=100 edge)
    for xp, label in [(40, "DC"), (120, "USB-A"), (140, "USB-B")]:
        cx_p = px(xp)
        draw.rectangle([cx_p - 6, py(98), cx_p + 6, py(100)], fill=USBC_COL)
        draw.text((cx_p - 14, py(101)), label, font=fn, fill=(255, 140, 50))

    # Dimension arrows
    draw_dim_h(draw, px(0), px(165), py(0), "165 mm", fn, above=True)
    draw_dim_h(draw, px(17.5), px(147.5), py(100) + 20, "130 mm", fn, above=False)
    draw_dim_h(draw, px(35), px(130), py(100) + 45, "95 mm", fn, above=False)
    draw_dim_v(draw, px(165), py(0), py(100), "100 mm", fn, right=True)
    draw_dim_v(draw, px(165) + 30, py(20), py(100), "80 mm", fn, right=True)

    # Legend
    lx, ly = 40, TOP_H - 200
    draw.text((lx, ly), "Legend:", font=fb, fill=WHITE)
    for col, label in [
        ((51, 180, 255), "Zone 1 — Phone (Qi2 20W)"),
        ((153, 102, 255), "Zone 2 — Buds (Qi 5W)"),
        ((51, 200, 130), "Zone 3 — Watch (5W)"),
        ((255, 140, 50), "Rear ports (DC / USB-C A / USB-C B)"),
    ]:
        ly += 26
        draw.rectangle([lx, ly, lx + 16, ly + 14], fill=col + (180,))
        draw.text((lx + 24, ly), label, font=fn, fill=(180, 180, 180))

    return img


def generate_side_view() -> Image.Image:
    img = Image.new("RGB", (SIDE_W, SIDE_H), BG)
    draw = ImageDraw.Draw(img, "RGBA")

    fb = try_bold(20)
    fn = try_font(14)

    draw.text((40, 24), "Epitome Step — Side Cross-Section (X = 82.5 mm)", font=fb, fill=WHITE)
    draw.text((40, 52), "Dimensions in mm", font=fn, fill=(140, 140, 140))

    S = 6
    OX = 180   # origin X (Z axis, vertical)
    OY = 820   # origin Y (Y axis, horizontal, Y=0 at front)

    def px(y_mm): return OX + y_mm * S
    def pz(z_mm): return OY - z_mm * S

    # Draw ground line
    draw.line([(px(0), pz(0)), (px(100), pz(0))], fill=GRID, width=1)

    # Base 0–3
    draw.rectangle([px(0), pz(3), px(100), pz(0)], outline=LINE, width=2,
                   fill=(26, 26, 26))
    draw.text((px(105), pz(3)), "Base 3mm", font=fn, fill=LINE)

    # Riser 3–25
    draw.rectangle([px(0), pz(25), px(100), pz(3)], outline=LINE, width=2,
                   fill=(22, 22, 22))
    draw.text((px(105), pz(14)), "Riser 22mm", font=fn, fill=LINE)

    # LED diffuser strip
    draw.rectangle([px(0), pz(36), px(100), pz(26)],
                   fill=(255, 214, 160, 60), outline=(255, 214, 160), width=1)
    draw.text((px(-120), pz(31)), "LED diffuser", font=fn, fill=(255, 214, 160))
    draw.line([(px(-5), pz(31)), (px(0), pz(31))], fill=(255, 214, 160), width=1)

    # Step 1 25–40
    draw.rectangle([px(0), pz(40), px(100), pz(25)],
                   fill=(*[50, 40, 20], 255), outline=LINE, width=2)
    draw.polygon([(px(0), pz(40)), (px(100), pz(40)),
                  (px(100), pz(40)), (px(0), pz(40))],
                 fill=ZONE1_COL)
    draw.text((px(105), pz(40)), "Z=40 Phone", font=fn, fill=(51, 180, 255))

    # Step 2 40–55 (starts at Y=0)
    draw.rectangle([px(0), pz(55), px(100), pz(40)],
                   fill=(*[30, 25, 50], 255), outline=LINE, width=2)
    draw.polygon([(px(0), pz(55)), (px(100), pz(55)),
                  (px(100), pz(55)), (px(0), pz(55))], fill=ZONE2_COL)
    draw.text((px(105), pz(55)), "Z=55 Buds", font=fn, fill=(153, 102, 255))

    # Step 3 55–70 (starts at Y=20)
    draw.rectangle([px(20), pz(70), px(100), pz(55)],
                   fill=(*[20, 40, 30], 255), outline=LINE, width=2)
    draw.polygon([(px(20), pz(70)), (px(100), pz(70)),
                  (px(100), pz(70)), (px(20), pz(70))], fill=ZONE3_COL)
    draw.text((px(105), pz(70)), "Z=70 Watch", font=fn, fill=(51, 200, 130))

    # Step 3 setback annotation
    draw.line([(px(0), pz(55)), (px(20), pz(55))], fill=(255, 80, 80, 180), width=1)
    draw.text((px(2), pz(57)), "Y=20\nsetback", font=fn, fill=(255, 80, 80))

    # Rear port at Y=100, Z=15
    draw.rectangle([px(96), pz(18), px(100), pz(12)],
                   fill=USBC_COL, outline=(255, 140, 50), width=1)
    draw.text((px(105), pz(15)), "DC/USB-C\nZ=15", font=fn, fill=(255, 140, 50))

    # Z dimension arrows (left side)
    for z0, z1, label in [
        (0, 3, "3"),
        (3, 25, "22"),
        (25, 40, "15"),
        (40, 55, "15"),
        (55, 70, "15"),
        (0, 70, "70mm"),
    ]:
        ax = OX - 30 if z1 - z0 > 10 else OX - 20
        if label == "70mm":
            ax = OX - 60
        draw.line([(ax, pz(z0)), (ax, pz(z1))], fill=DIM_LINE, width=1)
        draw.line([(ax - 4, pz(z0)), (ax + 4, pz(z0))], fill=DIM_LINE, width=1)
        draw.line([(ax - 4, pz(z1)), (ax + 4, pz(z1))], fill=DIM_LINE, width=1)
        mid = pz((z0 + z1) / 2)
        draw.text((ax - 40, mid - 8), label, font=fn, fill=DIM_COL)

    # Y dimension arrow (bottom)
    draw_dim_h(draw, px(0), px(100), pz(0) + 20, "100 mm", fn, above=False)

    return img


def main():
    os.makedirs("../assets", exist_ok=True)
    os.makedirs("assets", exist_ok=True)
    out_dir = "../assets" if os.path.isdir("../assets") else "assets"

    top = generate_top_view()
    path = os.path.join(out_dir, "step-technical-top.png")
    top.save(path)
    print(f"Saved: {path}")

    side = generate_side_view()
    path = os.path.join(out_dir, "step-technical-side.png")
    side.save(path)
    print(f"Saved: {path}")


if __name__ == "__main__":
    main()
