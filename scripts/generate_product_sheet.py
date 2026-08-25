#!/usr/bin/env python3
"""Penta Dock — comprehensive multi-view technical product sheet.

Generates assets/epitome-penta-product-sheet.png at 7200×5400px
(dpi=300, figsize=(24,18)).
"""
from __future__ import annotations

import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, Circle, Ellipse, Polygon

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = ROOT / "assets" / "epitome-penta-product-sheet.png"

# Palette
PAGE_BG = "#0d0d1a"
PANEL_BG = "#1a1a2e"
PANEL_BORDER = "#2a2a4a"
TEXT_WHITE = "#ffffff"
TEXT_LIGHT = "#cccccc"
TEXT_DIM = "#8e90a8"
GOLD = "#c8a84b"
ABS_BODY = "#1a1a1a"
ABS_LIGHT = "#2b2d34"
ABS_DARK = "#111217"
SIL = "#2d3137"
LED_AMBER = "#ffb347"

# Zone colours
Z1_BLUE = "#3a7bd5"
Z2_PURPLE = "#9b59b6"
Z3_GREEN = "#27ae60"
Z4_ORANGE = "#e67e22"
Z5_BLUE = "#3a7bd5"

# Geometry (mm)
DOCK_W = 250.0
DOCK_D = 100.0
DOCK_H = 100.0
LEFT_W = 35.0
RIGHT_W = 20.0
LEFT_H = 95.0
RIGHT_H = 75.0
RISER_H = 50.0
STEP_H = 15.0


def _panel_box(ax: plt.Axes, title: str) -> None:
    ax.set_facecolor(PANEL_BG)
    for spine in ax.spines.values():
        spine.set_edgecolor(PANEL_BORDER)
        spine.set_linewidth(1.4)
    ax.text(0.01, 0.99, title, transform=ax.transAxes, ha="left", va="top", fontsize=8,
            color=GOLD, fontweight="bold", fontfamily="monospace")


def _dim_arrow(ax: plt.Axes, x1: float, y1: float, x2: float, y2: float, label: str,
               color: str = TEXT_DIM, fs: float = 6.5, offx: float = 0.0, offy: float = 0.0) -> None:
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle="<->", color=color, lw=0.8, mutation_scale=7))
    ax.text((x1 + x2) / 2 + offx, (y1 + y2) / 2 + offy, label, color=color, fontsize=fs,
            ha="center", va="center", bbox=dict(facecolor=PANEL_BG, edgecolor="none", pad=0.5))


def draw_top_view(ax: plt.Axes) -> None:
    ax.set_xlim(-20, 290)
    ax.set_ylim(-25, 140)
    ax.set_aspect("equal")
    ax.axis("off")
    _panel_box(ax, "TOP VIEW — COMPACT RECTANGULAR DOCK")

    # Body
    body = FancyBboxPatch((0, 0), DOCK_W, DOCK_D, boxstyle="round,pad=0,rounding_size=8",
                          facecolor="#252535", edgecolor="#454a64", linewidth=1.6)
    ax.add_patch(body)

    # Section separators
    ax.plot([LEFT_W, LEFT_W], [0, DOCK_D], color="#4c4f66", lw=1.0)
    ax.plot([DOCK_W - RIGHT_W, DOCK_W - RIGHT_W], [0, DOCK_D], color="#4c4f66", lw=1.0)

    # Left slot opening
    ax.add_patch(Rectangle((0.8, 5), LEFT_W - 1.6, 90, facecolor="#0e1015", edgecolor=Z4_ORANGE, linewidth=1.0))
    # Right slot opening
    ax.add_patch(Rectangle((DOCK_W - RIGHT_W + 0.8, 15), RIGHT_W - 1.6, 70, facecolor="#0e1015", edgecolor=Z5_BLUE, linewidth=1.0))

    # Step outlines (top surfaces)
    cx = DOCK_W / 2
    ax.add_patch(Rectangle((cx - 90, 0), 180, 100, fill=False, edgecolor=Z1_BLUE, linewidth=1.4))
    ax.add_patch(Rectangle((cx - 70, 0), 140, 100, fill=False, edgecolor=Z2_PURPLE, linewidth=1.2, linestyle="--"))
    ax.add_patch(Rectangle((cx - 50, 0), 100, 80, fill=False, edgecolor=Z3_GREEN, linewidth=1.2, linestyle="--"))

    # Zone labels
    ax.text(LEFT_W / 2, 50, "ZONE 4\nLAPTOP\n100W PD", ha="center", va="center", color=TEXT_WHITE, fontsize=6.3)
    ax.text(cx, 54, "ZONE 1\nPHONE\n20W Qi2", ha="center", va="center", color=Z1_BLUE, fontsize=6.1, fontweight="bold")
    ax.text(cx, 36, "ZONE 2\nBUDS OR\nSECOND PHONE\n20W Qi", ha="center", va="center", color=Z2_PURPLE, fontsize=5.6, fontweight="bold")
    ax.text(cx, 74, "ZONE 3\nWATCH\n5W", ha="center", va="center", color=Z3_GREEN, fontsize=5.6, fontweight="bold")
    ax.text(DOCK_W - RIGHT_W / 2, 50, "ZONE 5\nTABLET\n45W PD", ha="center", va="center", color=TEXT_WHITE, fontsize=6.0)

    _dim_arrow(ax, 0, -10, DOCK_W, -10, "250 mm overall width")
    _dim_arrow(ax, 260, 0, 260, DOCK_D, "100 mm depth", offx=10)
    _dim_arrow(ax, 0, 108, LEFT_W, 108, "35 mm")
    _dim_arrow(ax, DOCK_W - RIGHT_W, 108, DOCK_W, 108, "20 mm")



def draw_front_elevation(ax: plt.Axes) -> None:
    ax.set_xlim(-20, 290)
    ax.set_ylim(-10, 120)
    ax.set_aspect("equal")
    ax.axis("off")
    _panel_box(ax, "FRONT ELEVATION — ZONE FACES + FASCIA")

    # Front fascia + LED channel
    ax.add_patch(Rectangle((0, 0), DOCK_W, 20, facecolor="#20242b", edgecolor="#4b5164", linewidth=1.2))
    ax.add_patch(Rectangle((8, 7.5), DOCK_W - 16, 5, facecolor="#8a6a33", edgecolor="#f1c27a", linewidth=0.6, alpha=0.6))
    for i, col in enumerate([Z1_BLUE, Z2_PURPLE, Z3_GREEN, Z4_ORANGE, Z5_BLUE]):
        ax.add_patch(Rectangle((10 + i * 46, 8.1), 36, 3.8, facecolor=col, edgecolor="none", alpha=0.85))

    # Left laptop slot face
    ax.add_patch(Rectangle((0, 20), LEFT_W, LEFT_H - 20, facecolor=ABS_DARK, edgecolor="#41485b", linewidth=1.2))
    ax.add_patch(Rectangle((3, 23), LEFT_W - 6, LEFT_H - 27, facecolor="#0a0e12", edgecolor="#262c36", linewidth=0.8))

    # Right tablet slot face
    ax.add_patch(Rectangle((DOCK_W - RIGHT_W, 20), RIGHT_W, RIGHT_H - 20, facecolor=ABS_DARK, edgecolor="#41485b", linewidth=1.2))
    ax.add_patch(Rectangle((DOCK_W - RIGHT_W + 2, 23), RIGHT_W - 4, RIGHT_H - 27, facecolor="#0a0e12", edgecolor="#262c36", linewidth=0.8))

    # Centre riser and steps
    cx = DOCK_W / 2
    ax.add_patch(Rectangle((cx - 90, 0), 180, RISER_H, facecolor="#191c22", edgecolor="#3d4458", linewidth=1.0, alpha=0.9))
    ax.add_patch(Rectangle((cx - 90, RISER_H), 180, STEP_H, facecolor="#262b33", edgecolor=Z1_BLUE, linewidth=1.0))
    ax.add_patch(Rectangle((cx - 70, RISER_H + STEP_H), 140, STEP_H, facecolor="#2d323a", edgecolor=Z2_PURPLE, linewidth=1.0))
    ax.add_patch(Rectangle((cx - 50, RISER_H + 2 * STEP_H), 100, STEP_H, facecolor="#343941", edgecolor=Z3_GREEN, linewidth=1.0))

    # Grommets + cable tails
    ax.add_patch(Circle((LEFT_W / 2, LEFT_H - 2), 2.2, facecolor="#181d24", edgecolor="#6a7380", linewidth=0.8))
    ax.add_patch(Circle((DOCK_W - RIGHT_W / 2, RIGHT_H - 2), 2.2, facecolor="#181d24", edgecolor="#6a7380", linewidth=0.8))
    ax.plot([LEFT_W / 2, LEFT_W / 2 - 3, LEFT_W / 2 - 1], [LEFT_H - 2, LEFT_H - 14, LEFT_H - 21], color="#545f6f", lw=1.5)
    ax.plot([DOCK_W - RIGHT_W / 2, DOCK_W - RIGHT_W / 2 + 2], [RIGHT_H - 2, RIGHT_H - 12], color="#545f6f", lw=1.2)

    ax.text(cx, 100, "Three-step centre platform (15 mm each)", color=TEXT_LIGHT, fontsize=5.7, ha="center")
    _dim_arrow(ax, -10, 0, -10, LEFT_H, "95 mm", offx=-7)
    _dim_arrow(ax, 265, 0, 265, RIGHT_H, "75 mm", offx=8)
    _dim_arrow(ax, cx - 90, 106, cx + 90, 106, "Step 1 width 180 mm")
    _dim_arrow(ax, 0, -4, DOCK_W, -4, "250 mm overall width")


def _iso(x: float, y: float, z: float, scale: float = 1.9, ox: float = 115, oy: float = 60) -> tuple[float, float]:
    a = math.radians(30)
    sx = (x - y) * math.cos(a) * scale + ox
    sy = (x + y) * math.sin(a) * scale - z * scale + oy
    return sx, sy


def _iso_poly(ax: plt.Axes, pts3d, fc, ec="#0b0d10", lw=0.5, alpha=1.0, z=3):
    pts = [_iso(*p) for p in pts3d]
    ax.add_patch(Polygon(pts, closed=True, facecolor=fc, edgecolor=ec, linewidth=lw, alpha=alpha, zorder=z))


def _iso_box(ax: plt.Axes, x0, x1, y0, y1, z0, z1, ct=ABS_LIGHT, cr=ABS_BODY, cf=ABS_DARK, z=4):
    _iso_poly(ax, [(x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)], ct, z=z + 2)
    _iso_poly(ax, [(x1, y0, z0), (x1, y1, z0), (x1, y1, z1), (x1, y0, z1)], cr, z=z + 1)
    _iso_poly(ax, [(x0, y0, z0), (x1, y0, z0), (x1, y0, z1), (x0, y0, z1)], cf, z=z)


def draw_perspective_view(ax: plt.Axes) -> None:
    ax.set_xlim(-140, 520)
    ax.set_ylim(340, -80)
    ax.axis("off")
    _panel_box(ax, "PERSPECTIVE VIEW — COMPACT ABS ENCLOSURE")

    # base + structural strips
    _iso_box(ax, 0, DOCK_W, 0, DOCK_D, 0, 3, ct="#20242b", cr="#12161b", cf="#101318", z=2)
    _iso_box(ax, 0, DOCK_W, 0, 3, 0, 20, ct="#232932", cr="#161c24", cf="#131820", z=5)
    _iso_box(ax, 0, DOCK_W, 97, 100, 0, 25, ct="#20252c", cr="#151a20", cf="#12161b", z=4)

    # slots
    _iso_box(ax, 0, 35, 5, 95, 0, 95, z=7)
    _iso_poly(ax, [(3, 5, 8), (32, 5, 8), (32, 5, 86), (3, 5, 86)], "#0b0f14", ec="#27303a", z=10)
    _iso_box(ax, 230, 250, 15, 85, 0, 75, z=7)
    _iso_poly(ax, [(232, 15, 8), (248, 15, 8), (248, 15, 68), (232, 15, 68)], "#0b0f14", ec="#27303a", z=10)

    # centre steps
    _iso_box(ax, 35, 215, 0, 100, 0, 50, ct="#1f242b", cr="#15191f", cf="#12161b", z=5)
    _iso_box(ax, 35, 215, 0, 100, 50, 65, ct="#2a3038", cr="#1a1f26", cf="#171c22", z=8)
    _iso_box(ax, 55, 195, 0, 100, 65, 80, ct="#313740", cr="#20252d", cf="#1d2229", z=9)
    _iso_box(ax, 75, 175, 0, 80, 80, 95, ct="#383f48", cr="#252b33", cf="#222830", z=10)

    # silicone surfaces
    _iso_poly(ax, [(45, 8, 65.2), (205, 8, 65.2), (205, 96, 65.2), (45, 96, 65.2)], SIL, ec="#49505b", z=13)
    _iso_poly(ax, [(80, 10, 80.2), (170, 10, 80.2), (170, 74, 80.2), (80, 74, 80.2)], "#2a2e35", ec="#565e6b", z=14)

    # watch pod
    pod_pts = []
    for i in range(28):
        t = 2 * math.pi * i / 28
        pod_pts.append((125 + 25 * math.cos(t), 56 + 17 * math.sin(t), 103))
    _iso_poly(ax, pod_pts, "#3d444f", ec="#626b77", z=16)

    # cable tail + connector
    cable = [_iso(17.5, 12, 95), _iso(17.5, 8, 90), _iso(17.5, 5, 85)]
    ax.plot([p[0] for p in cable], [p[1] for p in cable], color="#5a6472", lw=2.2, zorder=20)
    ax.plot([cable[-1][0] - 2, cable[-1][0] + 3], [cable[-1][1], cable[-1][1]], color="#a5afbc", lw=1.8, zorder=21)

    # LED glow
    p0 = _iso(10, 0.2, 10)
    p1 = _iso(240, 0.2, 10)
    for w, a in [(16, 0.05), (8, 0.12), (3, 0.38)]:
        ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=LED_AMBER, lw=w, alpha=a, solid_capstyle="round", zorder=23)

    # labels
    ax.text(340, 62, "Zone 4 laptop slot\n(on-edge, top cable)", color=Z4_ORANGE, fontsize=5.9, ha="left")
    ax.text(370, 154, "Zone 5 tablet slot\n(on-edge, top cable)", color=Z5_BLUE, fontsize=5.9, ha="left")
    ax.text(282, 228, "Zone 3 watch cradle", color=Z3_GREEN, fontsize=5.9)
    ax.text(200, 260, "Zone 2 buds or second phone · 20W Qi · 120×80mm dish", color=Z2_PURPLE, fontsize=5.9)
    ax.text(115, 292, "Zone 1 phone · 20W Qi2", color=Z1_BLUE, fontsize=5.9)
    ax.text(250, 307, "20 mm fascia with frosted diffuser", color=TEXT_LIGHT, fontsize=5.6)
    ax.text(298, 111, "25 mm low rear rail", color=TEXT_LIGHT, fontsize=5.6)


def draw_side_elevation(ax: plt.Axes) -> None:
    ax.set_xlim(-20, 170)
    ax.set_ylim(-8, 112)
    ax.set_aspect("equal")
    ax.axis("off")
    _panel_box(ax, "SIDE CROSS-SECTION — RIGHT ELEVATION")

    # Stack outline
    ax.add_patch(Rectangle((0, 0), 130, 3, facecolor="#252a34", edgecolor="#48506a", linewidth=1.0))
    ax.add_patch(Rectangle((8, 3), 114, 30, facecolor="#1f2430", edgecolor="#59627d", linewidth=1.0))
    ax.text(65, 18, "PSU 199×98×30 (Mean Well LRS-200-24)", color=TEXT_LIGHT, fontsize=5.2, ha="center")

    ax.add_patch(Rectangle((8, 33), 114, 17, facecolor="#1a1f29", edgecolor="#3f4760", linewidth=1.0))
    ax.text(65, 41.5, "Riser cavity + wiring\nESP32 / INA3221 shelf @ Z=35", color=TEXT_DIM, fontsize=5.1, ha="center", va="center")

    ax.add_patch(Rectangle((8, 50), 110, 15, facecolor="#2b313c", edgecolor=Z1_BLUE, linewidth=1.0))
    ax.add_patch(Circle((52, 57.5), 6.0, facecolor="none", edgecolor=Z1_BLUE, linestyle=":", linewidth=1.0))
    ax.text(86, 56.5, "Step 1\n20W Qi2", color=Z1_BLUE, fontsize=5.5, ha="center")

    ax.add_patch(Rectangle((8, 65), 100, 15, facecolor="#303741", edgecolor=Z2_PURPLE, linewidth=1.0))
    ax.add_patch(Circle((48, 72.5), 5.5, facecolor="none", edgecolor=Z2_PURPLE, linestyle=":", linewidth=1.0))
    ax.text(82, 72.0, "Step 2\n20W Qi", color=Z2_PURPLE, fontsize=5.4, ha="center")

    ax.add_patch(Rectangle((8, 80), 80, 15, facecolor="#363e49", edgecolor=Z3_GREEN, linewidth=1.0))
    ax.add_patch(Circle((36, 87.5), 4.8, facecolor="none", edgecolor=Z3_GREEN, linestyle=":", linewidth=1.0))
    ax.add_patch(Ellipse((58, 87.5), 16, 8, facecolor="none", edgecolor=Z3_GREEN, linewidth=1.0))
    ax.text(83, 87.5, "Step 3\nWatch puck + Qi", color=Z3_GREEN, fontsize=5.3, ha="center")

    # Slot walls context
    ax.plot([140, 140], [0, LEFT_H], color=Z4_ORANGE, lw=2)
    ax.plot([152, 152], [0, RIGHT_H], color=Z5_BLUE, lw=2)
    ax.text(140, LEFT_H + 2, "L slot wall 95mm", color=Z4_ORANGE, fontsize=5.0, ha="center")
    ax.text(152, RIGHT_H + 2, "R slot wall 75mm", color=Z5_BLUE, fontsize=5.0, ha="center")

    # Dimension arrows
    _dim_arrow(ax, -8, 0, -8, 95, "95 mm", offx=-8)
    _dim_arrow(ax, -2, 0, -2, 50, "50 mm", offx=-9)
    _dim_arrow(ax, 130, 3, 130, 33, "PSU 30 mm", offx=9)
    _dim_arrow(ax, 130, 50, 130, 65, "15 mm", offx=9)
    _dim_arrow(ax, 130, 65, 130, 80, "15 mm", offx=9)
    _dim_arrow(ax, 130, 80, 130, 95, "15 mm", offx=9)


def draw_bottom_view(ax: plt.Axes) -> None:
    ax.set_xlim(-20, 290)
    ax.set_ylim(-25, 140)
    ax.set_aspect("equal")
    ax.axis("off")
    _panel_box(ax, "BOTTOM VIEW — BASE / FEET / VENTS")

    ax.add_patch(FancyBboxPatch((0, 0), DOCK_W, DOCK_D, boxstyle="round,pad=0,rounding_size=10",
                                facecolor="#222838", edgecolor="#4f5870", linewidth=1.4))

    # Vent slots
    for y in [25, 40, 55, 70]:
        ax.add_patch(Rectangle((95, y), 60, 5, facecolor="#0f131b", edgecolor="#2e3545", linewidth=0.7))

    # M3 holes
    m3 = [(18, 18), (232, 18), (18, 82), (232, 82)]
    for x, y in m3:
        ax.add_patch(Circle((x, y), 2.2, facecolor="#0b0e14", edgecolor="#8ea0c0", linewidth=0.8))

    # Rubber feet
    feet = [(12, 12), (238, 12), (12, 88), (238, 88)]
    for x, y in feet:
        ax.add_patch(Circle((x, y), 5.5, facecolor="#10151d", edgecolor="#4b5568", linewidth=0.9))

    ax.text(125, 53, "Vent slots", color=TEXT_DIM, fontsize=5.8, ha="center")
    ax.text(50, 52, "M3\nmount", color=TEXT_DIM, fontsize=5.3, ha="center", va="center")
    ax.text(205, 52, "M3\nmount", color=TEXT_DIM, fontsize=5.3, ha="center", va="center")

    _dim_arrow(ax, 0, -10, DOCK_W, -10, "250 mm")
    _dim_arrow(ax, 260, 0, 260, DOCK_D, "100 mm", offx=9)


def draw_spec_panel(ax: plt.Axes) -> None:
    ax.axis("off")
    _panel_box(ax, "TECHNICAL SPECIFICATION PANEL")

    x = 0.04
    y = 0.94
    lh = 0.047

    def write(line: str, color=TEXT_LIGHT, fs=8, weight="normal"):
        nonlocal y
        ax.text(x, y, line, transform=ax.transAxes, ha="left", va="top", color=color,
                fontsize=fs, fontweight=weight, fontfamily="monospace")
        y -= lh

    write("PRE-ORDER — $249", color=GOLD, fs=11, weight="bold")
    y -= 0.01

    write("PHYSICAL", color=TEXT_WHITE, fs=8.7, weight="bold")
    write("• Envelope: ~250 × 100 × 100 mm")
    write("• Full ABS construction (no aluminium)")
    write("• Matte black painted finish")
    write("• Rear rail: 25 mm, centred IEC C13 inlet")
    write("• Front fascia: 20 mm, frosted diffuser channel")

    y -= 0.01
    write("5 ZONES", color=TEXT_WHITE, fs=8.7, weight="bold")
    write(f"• Zone 1 Phone — 20W Qi2", color=Z1_BLUE)
    write(f"• Zone 2 Buds or second phone — 20W Qi (120×80mm dish)", color=Z2_PURPLE)
    write(f"• Zone 3 Watch — 5W (Apple puck + Qi coil)", color=Z3_GREEN)
    write(f"• Zone 4 Laptop slot — 100W USB-C PD", color=Z4_ORANGE)
    write(f"• Zone 5 Tablet slot — 45W USB-C PD", color=Z5_BLUE)

    y -= 0.01
    write("ELECTRONICS", color=TEXT_WHITE, fs=8.7, weight="bold")
    write("• MCU: ESP32-C3 SuperMini (WiFi + BLE 5.0)")
    write("• Power safety MCU: ATtiny85 (global soft-cap gate)")
    write("• Power monitor: INA3221 ×2")
    write("• PSU: Mean Well LRS-200-24, 201W")
    write("• Output rail trimmed to 20V")
    write("• LED: WS2811 strip, 12–15 LEDs, 250mm")
    write("• Total output 190W, ATtiny85 soft cap 185W")
    write("• Night mode: LEDs off 23:00–07:00")

    y -= 0.01
    write("MATERIAL / DESIGN NOTES", color=TEXT_WHITE, fs=8.7, weight="bold")
    write("• On-edge laptop + tablet slot loading")
    write("• Captive USB-C cable hangs from slot top")
    write("• Silicone lining on slot floor + side walls")
    write("• Centre 3-step ABS staircase charging platform")

    ax.text(0.04, 0.03, "© 2026 GJATHASEnterprises · Penta Dock", transform=ax.transAxes,
            color=TEXT_DIM, fontsize=7, fontfamily="monospace")


def draw_header(fig: plt.Figure) -> None:
    fig.text(0.03, 0.975, "PENTA DOCK", color=TEXT_WHITE, fontsize=25, fontweight="bold", va="top")
    fig.text(0.03, 0.952, "190W TOTAL OUTPUT · 5-ZONE CHARGING DOCK", color=GOLD, fontsize=11, va="top")
    fig.text(0.97, 0.973, "PRE-ORDER — $249", color=GOLD, fontsize=12, ha="right", va="top", fontweight="bold")
    fig.text(0.97, 0.952, "FULL ABS · MATTE BLACK · 2026", color=TEXT_DIM, fontsize=9, ha="right", va="top")


def build_figure() -> None:
    fig = plt.figure(figsize=(24, 18), dpi=300, facecolor=PAGE_BG)
    gs = fig.add_gridspec(
        3,
        2,
        left=0.03,
        right=0.97,
        top=0.94,
        bottom=0.04,
        width_ratios=[1.08, 0.92],
        height_ratios=[1, 1, 1],
        hspace=0.14,
        wspace=0.08,
    )

    ax_top = fig.add_subplot(gs[0, 0])
    ax_front = fig.add_subplot(gs[1, 0])
    ax_persp = fig.add_subplot(gs[2, 0])
    ax_side = fig.add_subplot(gs[0, 1])
    ax_bottom = fig.add_subplot(gs[1, 1])
    ax_spec = fig.add_subplot(gs[2, 1])

    draw_top_view(ax_top)
    draw_front_elevation(ax_front)
    draw_perspective_view(ax_persp)
    draw_side_elevation(ax_side)
    draw_bottom_view(ax_bottom)
    draw_spec_panel(ax_spec)
    draw_header(fig)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT_PATH, dpi=300, facecolor=PAGE_BG)
    plt.close(fig)


if __name__ == "__main__":
    build_figure()
    print(f"✓ Product sheet generated: {OUTPUT_PATH.relative_to(ROOT)}")
