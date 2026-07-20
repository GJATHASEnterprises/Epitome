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
CANVAS_SIZE = (1600, 900)
BACKGROUND = "#e7eaef"
DOCK_COLOR = "#171b21"
DOCK_EDGE = "#2a313b"
ZONE_FILL = "#202732"
ZONE_OUTLINE = "#4a5462"
ACCENT = "#73d6ff"
TEXT_PRIMARY = "#f7f8fa"
TEXT_MUTED = "#b7bec8"
LED_RED = "#ff4f4f"
LED_GREEN = "#5fe087"
LED_OFF = "#5e6672"
RAIL_FILL = (230, 239, 246, 92)
RUBBER_FILL = (62, 70, 79, 180)


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


def draw_centered_text(draw: ImageDraw.ImageDraw, xy: tuple[float, float], text: str, font, fill: str) -> None:
    bbox = draw.textbbox((0, 0), text, font=font)
    width = bbox[2] - bbox[0]
    height = bbox[3] - bbox[1]
    draw.text((xy[0] - width / 2, xy[1] - height / 2), text, font=font, fill=fill)


def draw_qi_coil(draw: ImageDraw.ImageDraw, center: tuple[int, int], radius: int) -> None:
    for offset in range(0, 22, 7):
        draw.ellipse(
            (center[0] - radius + offset, center[1] - radius + offset, center[0] + radius - offset, center[1] + radius - offset),
            outline=ACCENT,
            width=3,
        )
    draw.line((center[0] - radius - 18, center[1], center[0] - radius + 8, center[1]), fill=ACCENT, width=3)
    draw.line((center[0] + radius - 8, center[1], center[0] + radius + 18, center[1]), fill=ACCENT, width=3)


def draw_glow(base: Image.Image, center: tuple[int, int], color: str, radius: int) -> None:
    glow = Image.new("RGBA", base.size, (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(glow)
    rgba_with_alpha = ImageColor.getrgb(color) + (160,)
    gdraw.ellipse((center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius), fill=rgba_with_alpha)
    glow = glow.filter(ImageFilter.GaussianBlur(radius=18))
    base.alpha_composite(glow)


class ImageColor:
    @staticmethod
    def getrgb(color: str) -> tuple[int, int, int]:
        color = color.lstrip("#")
        return tuple(int(color[offset:offset + 2], 16) for offset in (0, 2, 4))


def main() -> None:
    for output_path in OUTPUT_PATHS:
        output_path.parent.mkdir(parents=True, exist_ok=True)
    image = Image.new("RGBA", CANVAS_SIZE, BACKGROUND)
    draw = ImageDraw.Draw(image)

    title_font = load_font(46, bold=True)
    zone_font = load_font(28, bold=True)
    label_font = load_font(24, bold=False)
    brand_font = load_font(34, bold=True)
    small_font = load_font(20, bold=False)

    shadow = Image.new("RGBA", CANVAS_SIZE, (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(shadow)
    dock_box = (120, 140, 1480, 760)
    sdraw.rounded_rectangle((dock_box[0] + 14, dock_box[1] + 20, dock_box[2] + 18, dock_box[3] + 28), radius=54, fill=(0, 0, 0, 130))
    shadow = shadow.filter(ImageFilter.GaussianBlur(radius=22))
    image.alpha_composite(shadow)

    draw.rounded_rectangle(dock_box, radius=50, fill=DOCK_COLOR, outline=DOCK_EDGE, width=4)
    draw.rounded_rectangle((160, 650, 1440, 712), radius=24, fill="#252c36", outline="#39414d", width=2)

    zone_boxes = [
        (180, 220, 470, 610),
        (500, 220, 790, 610),
        (835, 220, 1095, 610),
        (1130, 220, 1420, 610),
    ]
    led_centers = [(325, 681), (645, 681), (965, 681), (1275, 681)]
    zone_titles = [
        ("Zone 1", "Phone"),
        ("Zone 2", "Phone / AirPods"),
        ("Zone 3", "Watch"),
        ("Zone 4", "USB-C Laptop"),
    ]

    for idx, box in enumerate(zone_boxes):
        draw.rounded_rectangle(box, radius=28, fill=ZONE_FILL, outline=ZONE_OUTLINE, width=3)
        draw_centered_text(draw, ((box[0] + box[2]) / 2, box[1] + 34), zone_titles[idx][0], zone_font, TEXT_PRIMARY)
        draw_centered_text(draw, ((box[0] + box[2]) / 2, box[1] + 76), zone_titles[idx][1], label_font, TEXT_MUTED)

    overlay = Image.new("RGBA", CANVAS_SIZE, (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)

    for left, right, top, bottom, width in [
        (212, 225, 285, 570, 13),
        (425, 438, 285, 570, 13),
        (532, 545, 285, 570, 13),
        (745, 758, 285, 570, 13),
        (875, 888, 315, 555, 13),
        (1040, 1053, 315, 555, 13),
    ]:
        odraw.polygon([(left, top), (left + width, top + 12), (left + width, bottom - 12), (left, bottom)], fill=RAIL_FILL)
        odraw.polygon([(right, top), (right - width, top + 12), (right - width, bottom - 12), (right, bottom)], fill=RAIL_FILL)

    for left, right in [(1168, 1192), (1358, 1382)]:
        odraw.polygon([(left, 250), (left + 18, 270), (left + 18, 595), (left, 620)], fill=RAIL_FILL)
        odraw.polygon([(right, 250), (right - 18, 270), (right - 18, 595), (right, 620)], fill=RAIL_FILL)
        odraw.rectangle((left + 5, 276, left + 14, 600), fill=RUBBER_FILL)
        odraw.rectangle((right - 14, 276, right - 5, 600), fill=RUBBER_FILL)

    image.alpha_composite(overlay)
    draw = ImageDraw.Draw(image)

    draw_qi_coil(draw, (325, 410), 78)
    draw_qi_coil(draw, (645, 410), 78)

    draw.rounded_rectangle((895, 310, 1035, 520), radius=46, outline="#cfd7df", width=6)
    draw.arc((918, 332, 1012, 426), start=205, end=335, fill="#cfd7df", width=8)
    draw.rounded_rectangle((943, 442, 987, 500), radius=18, fill="#95a5b4")
    draw.text((878, 538), "Magnetic cradle", font=small_font, fill=TEXT_MUTED)

    draw.rounded_rectangle((1202, 285, 1348, 542), radius=26, fill="#313847", outline="#697382", width=3)
    draw.line((1275, 545, 1275, 604), fill="#d7dde6", width=8)
    draw.rounded_rectangle((1245, 594, 1305, 612), radius=8, fill="#d7dde6")
    draw.line((1306, 603, 1376, 637), fill="#d7dde6", width=7)
    draw.rounded_rectangle((1370, 630, 1412, 648), radius=8, fill="#d7dde6")
    draw.text((1182, 548), "Integrated USB-C output", font=small_font, fill=TEXT_MUTED)

    led_colors = [LED_RED, LED_GREEN, LED_OFF, LED_RED]
    for center, color in zip(led_centers, led_colors):
        if color != LED_OFF:
            draw_glow(image, center, color, 32)
        draw = ImageDraw.Draw(image)
        draw.ellipse((center[0] - 16, center[1] - 16, center[0] + 16, center[1] + 16), fill=color, outline="#dfe6ef" if color != LED_OFF else "#818894", width=2)

    draw.rounded_rectangle((1332, 666, 1425, 698), radius=14, fill="#0f1319", outline="#5c6674", width=2)
    draw_centered_text(draw, (1378, 682), "Dark", small_font, TEXT_MUTED)
    draw_centered_text(draw, (1378, 704), "Mode", small_font, TEXT_MUTED)

    draw_centered_text(draw, (800, 188), "Rendered Product Visualization", title_font, "#36414f")
    draw_centered_text(draw, (800, 728), "Quad Device Dock", brand_font, TEXT_PRIMARY)
    draw_centered_text(draw, (800, 772), "Wireless charging, watch cradle, upright laptop support, and per-zone LED status", label_font, TEXT_MUTED)

    image = image.convert("RGB")
    for output_path in OUTPUT_PATHS:
        image.save(output_path)
        print(f"Saved render to {output_path}")


if __name__ == "__main__":
    main()
