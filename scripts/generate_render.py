#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFilter, ImageFont
except ImportError as exc:  # pragma: no cover - runtime guard for environments without Pillow
    raise SystemExit(
        "Pillow is required to generate the dock render. Install it with `python -m pip install pillow`."
    ) from exc

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATHS = [
    ROOT / "images" / "quad-dock-render.png",
    ROOT / "docs" / "images" / "quad-dock-render.png",
]

# Canvas holds both black and white variants side by side.
CANVAS_SIZE = (1700, 960)
BACKGROUND = "#d8dce2"
TEXT_PRIMARY = "#f7f8fa"
TEXT_MUTED = "#b7bec8"
ACCENT = "#73d6ff"
LED_RED = "#ff4f4f"
LED_GREEN = "#5fe087"
LED_OFF = "#3a3f47"

VARIANTS = [
    {
        "label": "Black",
        "offset_x": 20,
        "dock_color": "#171b21",
        "dock_edge": "#2a313b",
        "top_plate": "#1a1e24",
        "top_edge": "#3a4250",
        "zone_fill": "#202732",
        "zone_outline": "#4a5462",
        "rail_fill": (60, 70, 80, 120),
        "rubber_fill": (40, 48, 58, 200),
        "led_bar_bg": "#0f1218",
        "text_muted": "#9ba5b2",
        "silicone_pad_outline": "#556677",
        "brand_text_color": TEXT_PRIMARY,
        "description_text_color": TEXT_MUTED,
    },
    {
        "label": "White",
        "offset_x": 870,
        "dock_color": "#e8eaed",
        "dock_edge": "#c8ccd4",
        "top_plate": "#f0f2f4",
        "top_edge": "#b0b8c4",
        "zone_fill": "#d0d4da",
        "zone_outline": "#a0a8b2",
        "rail_fill": (180, 190, 200, 120),
        "rubber_fill": (130, 140, 150, 200),
        "led_bar_bg": "#b0b5bc",
        "text_muted": "#505870",
        "silicone_pad_outline": "#8899aa",
        "brand_text_color": "#303848",
        "description_text_color": "#606878",
    },
]


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    font_names = [
        "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for font_name in font_names:
        try:
            return ImageFont.truetype(font_name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def draw_centered_text(
    draw: ImageDraw.ImageDraw,
    xy: tuple[float, float],
    text: str,
    font,
    fill: str,
) -> None:
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    draw.text((xy[0] - w / 2, xy[1] - h / 2), text, font=font, fill=fill)


def draw_qi_coil(draw: ImageDraw.ImageDraw, center: tuple[int, int], radius: int) -> None:
    for offset in range(0, 22, 7):
        draw.ellipse(
            (
                center[0] - radius + offset,
                center[1] - radius + offset,
                center[0] + radius - offset,
                center[1] + radius - offset,
            ),
            outline=ACCENT,
            width=3,
        )
    draw.line((center[0] - radius - 18, center[1], center[0] - radius + 8, center[1]), fill=ACCENT, width=3)
    draw.line((center[0] + radius - 8, center[1], center[0] + radius + 18, center[1]), fill=ACCENT, width=3)


def draw_glow(base: Image.Image, center: tuple[int, int], color_hex: str, radius: int) -> None:
    glow = Image.new("RGBA", base.size, (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(glow)
    r, g, b = hex_to_rgb(color_hex)
    gdraw.ellipse(
        (center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius),
        fill=(r, g, b, 160),
    )
    glow = glow.filter(ImageFilter.GaussianBlur(radius=18))
    base.alpha_composite(glow)


def hex_to_rgb(color: str) -> tuple[int, int, int]:
    color = color.lstrip("#")
    return int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16)


def draw_ws2812b_bar(
    image: Image.Image,
    draw: ImageDraw.ImageDraw,
    bar_box: tuple[int, int, int, int],
    bg_color: str,
    led_states: list[str],  # 16 hex color strings (4 per zone)
) -> None:
    """Draw the continuous WS2812B LED strip across the full front edge."""
    bx1, by1, bx2, by2 = bar_box
    draw.rounded_rectangle(bar_box, radius=10, fill=bg_color, outline="#2a2f38", width=2)
    bar_w = bx2 - bx1
    led_spacing = bar_w / len(led_states)
    for idx, color in enumerate(led_states):
        cx = int(bx1 + (idx + 0.5) * led_spacing)
        cy = (by1 + by2) // 2
        if color != LED_OFF:
            draw_glow(image, (cx, cy), color, 14)
            draw = ImageDraw.Draw(image)
        draw.ellipse((cx - 8, cy - 8, cx + 8, cy + 8), fill=color)


def draw_variant(image: Image.Image, v: dict, fonts: dict) -> None:
    draw = ImageDraw.Draw(image)
    ox = v["offset_x"]

    # --- Dock body shadow ---
    shadow = Image.new("RGBA", image.size, (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(shadow)
    dock_box = (ox + 20, 80, ox + 810, 840)
    sdraw.rounded_rectangle(
        (dock_box[0] + 12, dock_box[1] + 18, dock_box[2] + 16, dock_box[3] + 24),
        radius=40,
        fill=(0, 0, 0, 110),
    )
    shadow = shadow.filter(ImageFilter.GaussianBlur(radius=18))
    image.alpha_composite(shadow)

    # --- Dock base (ABS, rear tier height visible as full body) ---
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle(dock_box, radius=36, fill=v["dock_color"], outline=v["dock_edge"], width=3)

    # --- Aluminum top plate (covers rear + front tier top surface) ---
    top_plate_box = (ox + 40, 120, ox + 790, 650)
    draw.rounded_rectangle(top_plate_box, radius=24, fill=v["top_plate"], outline=v["top_edge"], width=3)

    # --- Tier step: raised rear section (Zones 3 and 4) ---
    rear_tier_box = (ox + 430, 140, ox + 780, 620)
    draw.rounded_rectangle(
        rear_tier_box, radius=18, fill=v["dock_color"], outline=v["dock_edge"], width=2
    )
    # Rear tier top surface (aluminum plate continues over it)
    rear_top = (ox + 440, 150, ox + 770, 610)
    draw.rounded_rectangle(rear_top, radius=14, fill=v["top_plate"], outline=v["top_edge"], width=2)

    # Step edge highlight (the visible front face of the rear tier rise)
    draw.rectangle((ox + 430, 510, ox + 780, 540), fill=v["dock_edge"])

    # --- Zone boxes ---
    # Front tier: Zones 1 and 2
    zone_boxes = [
        (ox + 60, 170, ox + 270, 490),   # Zone 1 — phone Qi
        (ox + 300, 170, ox + 410, 490),  # Zone 2 — phone/AirPods Qi
        (ox + 455, 165, ox + 610, 490),  # Zone 3 — Watch (on rear tier)
        (ox + 640, 165, ox + 760, 530),  # Zone 4 — Laptop (on rear tier)
    ]
    zone_titles = [
        ("Zone 1", "Phone Qi"),
        ("Zone 2", "Phone/Buds"),
        ("Zone 3", "Watch"),
        ("Zone 4", "USB-C"),
    ]
    for idx, box in enumerate(zone_boxes):
        draw.rounded_rectangle(box, radius=18, fill=v["zone_fill"], outline=v["zone_outline"], width=2)
        cx = (box[0] + box[2]) / 2
        draw_centered_text(draw, (cx, box[1] + 22), zone_titles[idx][0], fonts["zone"], v["text_muted"])
        draw_centered_text(draw, (cx, box[1] + 46), zone_titles[idx][1], fonts["small"], v["text_muted"])

    # --- Integrated ABS rail overlays (Zones 1–3 small, Zone 4 tall) ---
    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)
    rf = v["rail_fill"]

    # Zone 1 rails
    for lx, rx in [(ox + 62, ox + 76), (ox + 256, ox + 270)]:
        odraw.polygon([(lx, 220), (lx + 12, 232), (lx + 12, 475), (lx, 487)], fill=rf)
        odraw.polygon([(rx, 220), (rx - 12, 232), (rx - 12, 475), (rx, 487)], fill=rf)
    # Zone 2 rails
    for lx, rx in [(ox + 302, ox + 314), (ox + 398, ox + 410)]:
        odraw.polygon([(lx, 220), (lx + 12, 232), (lx + 12, 475), (lx, 487)], fill=rf)
        odraw.polygon([(rx, 220), (rx - 12, 232), (rx - 12, 475), (rx, 487)], fill=rf)
    # Zone 3 rails (small, on rear tier)
    for lx, rx in [(ox + 457, ox + 467), (ox + 600, ox + 610)]:
        odraw.polygon([(lx, 210), (lx + 8, 220), (lx + 8, 473), (lx, 483)], fill=rf)
        odraw.polygon([(rx, 210), (rx - 8, 220), (rx - 8, 473), (rx, 483)], fill=rf)
    # Zone 4 tall rails (40–50mm, with rubber inner pads)
    rub = v["rubber_fill"]
    for lx, rx in [(ox + 642, ox + 655), (ox + 747, ox + 760)]:
        odraw.polygon([(lx, 175), (lx + 16, 190), (lx + 16, 520), (lx, 535)], fill=rf)
        odraw.polygon([(rx, 175), (rx - 16, 190), (rx - 16, 520), (rx, 535)], fill=rf)
        odraw.rectangle((lx + 4, 196, lx + 12, 514), fill=rub)
        odraw.rectangle((rx - 12, 196, rx - 4, 514), fill=rub)
    image.alpha_composite(overlay)
    draw = ImageDraw.Draw(image)

    # --- Silicone pads on charging zone surfaces ---
    for box in zone_boxes[:3]:
        pad_box = (box[0] + 16, box[1] + 62, box[2] - 16, box[3] - 16)
        draw.rounded_rectangle(pad_box, radius=10, fill=None, outline=v["silicone_pad_outline"], width=1)

    # --- Qi coils (Zones 1 and 2) ---
    draw_qi_coil(draw, (ox + 165, 340), 68)
    draw_qi_coil(draw, (ox + 355, 340), 50)

    # --- MagSafe ring magnet indicator below Zone 1 coil ---
    draw.ellipse((ox + 125, 420, ox + 205, 460), outline=ACCENT, width=2)
    draw.text((ox + 90, 467), "N52 magnet", font=fonts["tiny"], fill=v["text_muted"])

    # --- Watch cradle (Zone 3) ---
    draw.rounded_rectangle((ox + 486, 220, ox + 578, 390), radius=34, outline="#cfd7df", width=5)
    draw.arc((ox + 504, 238, ox + 560, 294), start=205, end=335, fill="#cfd7df", width=6)
    draw.rounded_rectangle((ox + 520, 310, ox + 544, 372), radius=12, fill="#95a5b4")
    draw.text((ox + 462, 398), "Watch cradle", font=fonts["tiny"], fill=v["text_muted"])

    # --- Laptop placeholder (Zone 4) ---
    draw.rounded_rectangle((ox + 660, 195, ox + 742, 430), radius=16, fill=v["zone_fill"], outline="#697382", width=2)
    draw.line((ox + 701, 432, ox + 701, 490), fill="#d7dde6", width=6)
    draw.rounded_rectangle((ox + 676, 483, ox + 726, 498), radius=6, fill="#d7dde6")
    draw.text((ox + 645, 502), "USB-C 100W", font=fonts["tiny"], fill=v["text_muted"])

    # --- WS2812B LED bar (full front edge) ---
    led_bar_box = (ox + 45, 665, ox + 780, 700)
    # LED states: 4 per zone (charging=red, full=green, off=LED_OFF)
    led_states = (
        [LED_RED] * 4   # Zone 1 — charging
        + [LED_GREEN] * 4  # Zone 2 — full
        + [LED_OFF] * 4    # Zone 3 — no device
        + [LED_RED] * 4    # Zone 4 — charging
    )
    draw_ws2812b_bar(image, draw, led_bar_box, v["led_bar_bg"], led_states)
    draw = ImageDraw.Draw(image)
    draw_centered_text(draw, ((led_bar_box[0] + led_bar_box[2]) / 2, led_bar_box[3] + 14),
                       "WS2812B LED strip — full front edge", fonts["tiny"], v["text_muted"])

    # --- IEC C13 inlet (rear left) ---
    iec_box = (ox + 45, 742, ox + 155, 784)
    draw.rounded_rectangle(iec_box, radius=8, fill="#0f1319", outline="#5c6674", width=2)
    draw.rounded_rectangle((ox + 58, 750, ox + 143, 776), radius=5, fill="#1a2030", outline="#5c6674", width=1)
    draw_centered_text(draw, ((iec_box[0] + iec_box[2]) / 2, iec_box[3] + 12), "IEC C13 in", fonts["tiny"], v["text_muted"])

    # --- Cooling vents in base ---
    for vi in range(6):
        vx = ox + 200 + vi * 80
        draw.rectangle((vx, 752, vx + 50, 762), fill=v["dock_edge"])

    # --- USB-A port on right side ---
    usba_box = (ox + 790, 420, ox + 820, 480)
    draw.rounded_rectangle(usba_box, radius=4, fill="#1a2030", outline="#5c6674", width=2)
    draw.rectangle((ox + 798, 432, ox + 812, 468), fill="#0f1319")
    draw.text((ox + 790, 488), "USB-A", font=fonts["tiny"], fill=v["text_muted"])
    draw.text((ox + 790, 504), "12W", font=fonts["tiny"], fill=v["text_muted"])

    # --- Cable clips on rear ---
    for ci in range(3):
        cx2 = ox + 400 + ci * 100
        draw.arc((cx2, 795, cx2 + 28, 830), start=0, end=180, fill=v["dock_edge"], width=4)
    draw.text((ox + 360, 840), "Cable clips", font=fonts["tiny"], fill=v["text_muted"])

    # --- Variant label ---
    draw_centered_text(draw, (ox + 415, 900), f"Quad Device Dock — {v['label']}", fonts["brand"], v["brand_text_color"])
    draw_centered_text(draw, (ox + 415, 930), "Internal 180W PSU · IEC C13 · WS2812B LED bar · MagSafe magnets · USB-A",
                       fonts["tiny"], v["description_text_color"])


def main() -> None:
    for output_path in OUTPUT_PATHS:
        output_path.parent.mkdir(parents=True, exist_ok=True)

    image = Image.new("RGBA", CANVAS_SIZE, BACKGROUND)
    draw = ImageDraw.Draw(image)

    fonts = {
        "title": load_font(36, bold=True),
        "zone": load_font(20, bold=True),
        "label": load_font(18, bold=False),
        "brand": load_font(26, bold=True),
        "small": load_font(16, bold=False),
        "tiny": load_font(13, bold=False),
    }

    draw_centered_text(draw, (CANVAS_SIZE[0] / 2, 44), "Quad Device Dock — Rendered Product Visualization", fonts["title"], "#36414f")
    draw_centered_text(draw, (CANVAS_SIZE[0] / 2, 76), "Available in Black and White · Tiered enclosure · Internal 180W PSU", fonts["label"], "#607080")

    for v in VARIANTS:
        draw_variant(image, v, fonts)

    image = image.convert("RGB")
    for output_path in OUTPUT_PATHS:
        image.save(output_path)
        print(f"Saved render to {output_path}")


if __name__ == "__main__":
    main()
