#!/usr/bin/env python3
"""Generate a 3/4 isometric render of the compact Penta Dock.

Usage:
    python scripts/generate_image.py

Output:
    assets/penta-dock-hero.png  (1200×800 px)
"""
from __future__ import annotations

import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = ROOT / "assets" / "penta-dock-hero.png"
CANVAS_W, CANVAS_H = 1200, 800

# Dimensions (mm)
DOCK_W, DOCK_D = 250.0, 100.0
BASE_T = 3.0
LAPTOP_SLOT_W, LAPTOP_SLOT_H = 35.0, 95.0
TABLET_SLOT_W, TABLET_SLOT_H = 20.0, 75.0
RISER_H, STEP_H = 50.0, 15.0
FASCIA_H, REAR_RAIL_H = 20.0, 25.0

# Colors
C_BG = "#eef1f4"
C_ABS = "#1a1b1d"
C_ABS_LIGHT = "#272a2f"
C_ABS_DARK = "#0f1114"
C_SIL = "#2b2f35"
C_SLOT = "#0c0f12"
C_LED = "#ffb347"
C_Z1 = "#3a7bd5"
C_Z2 = "#9b59b6"
C_Z3 = "#27ae60"
C_Z4 = "#e67e22"
C_Z5 = "#3a7bd5"


# Isometric projection
ANGLE = math.radians(30.0)
SCALE = 2.6
OX, OY = 370, 470


def iso(x: float, y: float, z: float) -> tuple[float, float]:
    sx = (x - y) * math.cos(ANGLE) * SCALE + OX
    sy = (x + y) * math.sin(ANGLE) * SCALE - z * SCALE + OY
    return sx, sy


def poly(ax, pts3d, fc, ec="#0a0c0f", lw=0.8, alpha=1.0, z=2):
    pts2d = [iso(*p) for p in pts3d]
    ax.add_patch(Polygon(pts2d, closed=True, facecolor=fc, edgecolor=ec, linewidth=lw, alpha=alpha, zorder=z))


def draw_box(ax, x0, x1, y0, y1, z0, z1, c_top=C_ABS_LIGHT, c_right=C_ABS, c_front=C_ABS_DARK, zorder=3):
    # top
    poly(ax, [(x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)], c_top, z=zorder + 2)
    # right
    poly(ax, [(x1, y0, z0), (x1, y1, z0), (x1, y1, z1), (x1, y0, z1)], c_right, z=zorder + 1)
    # front
    poly(ax, [(x0, y0, z0), (x1, y0, z0), (x1, y0, z1), (x0, y0, z1)], c_front, z=zorder)


def add_label(ax, x, y, text, color="#6d7784"):
    ax.text(x, y, text, fontsize=10, color=color, ha="left", va="center", zorder=20)


def render(ax):
    # soft shadow
    poly(
        ax,
        [(8, 5, -1), (DOCK_W + 18, 5, -1), (DOCK_W + 10, DOCK_D + 8, -1), (-2, DOCK_D + 8, -1)],
        "#000000",
        ec="none",
        alpha=0.16,
        z=1,
    )

    # Base plate
    draw_box(ax, 0, DOCK_W, 0, DOCK_D, 0, BASE_T, c_top="#22262c", c_right="#15181d", c_front="#111317", zorder=2)

    # Front fascia strip
    draw_box(ax, 0, DOCK_W, 0, 3, 0, FASCIA_H, c_top="#22272c", c_right="#171b20", c_front="#13161a", zorder=5)

    # Rear rail
    draw_box(ax, 0, DOCK_W, 97, 100, 0, REAR_RAIL_H, c_top="#20242a", c_right="#15191e", c_front="#12161b", zorder=4)

    # Laptop slot body (left)
    draw_box(ax, 0, 35, 5, 95, 0, LAPTOP_SLOT_H, c_top="#242930", c_right="#161a20", c_front="#12161b", zorder=6)
    # open front and top hint
    poly(ax, [(3, 5, 6), (32, 5, 6), (32, 5, 86), (3, 5, 86)], C_SLOT, ec="#20242a", z=12)
    poly(ax, [(4, 8, 95), (31, 8, 95), (31, 92, 95), (4, 92, 95)], C_SLOT, ec="#20242a", z=12)

    # Tablet slot body (right)
    draw_box(ax, DOCK_W - 20, DOCK_W, 15, 85, 0, TABLET_SLOT_H, c_top="#242930", c_right="#161a20", c_front="#12161b", zorder=6)
    poly(ax, [(DOCK_W - 18, 15, 6), (DOCK_W - 2, 15, 6), (DOCK_W - 2, 15, 68), (DOCK_W - 18, 15, 68)], C_SLOT, ec="#20242a", z=12)
    poly(ax, [(DOCK_W - 19, 18, 75), (DOCK_W - 1, 18, 75), (DOCK_W - 1, 82, 75), (DOCK_W - 19, 82, 75)], C_SLOT, ec="#20242a", z=12)

    # Centre riser and three steps
    sx0, sx1 = 35, 215
    draw_box(ax, sx0, sx1, 0, 100, 0, RISER_H, c_top="#20242a", c_right="#14181d", c_front="#111419", zorder=5)
    draw_box(ax, sx0, sx1, 0, 100, RISER_H, RISER_H + STEP_H, c_top="#2a2f36", c_right="#1a1e24", c_front="#171b20", zorder=8)
    draw_box(ax, 55, 195, 0, 100, RISER_H + STEP_H, RISER_H + 2 * STEP_H, c_top="#2f343b", c_right="#1d2127", c_front="#1a1d23", zorder=9)
    draw_box(ax, 75, 175, 0, 80, RISER_H + 2 * STEP_H, RISER_H + 3 * STEP_H, c_top="#343941", c_right="#21252b", c_front="#1e2228", zorder=10)

    # Silicone surfaces on steps
    poly(ax, [(45, 8, RISER_H + STEP_H + 0.3), (205, 8, RISER_H + STEP_H + 0.3), (205, 96, RISER_H + STEP_H + 0.3), (45, 96, RISER_H + STEP_H + 0.3)], C_SIL, ec="#3a3f46", z=15)
    poly(ax, [(80, 10, RISER_H + 2 * STEP_H + 0.3), (170, 10, RISER_H + 2 * STEP_H + 0.3), (170, 75, RISER_H + 2 * STEP_H + 0.3), (80, 75, RISER_H + 2 * STEP_H + 0.3)], "#2a2d33", ec="#4a4f57", z=16)

    # Watch cradle pod (top step)
    pod = []
    for a in range(36):
        t = 2 * math.pi * a / 36
        x = 125 + 25 * math.cos(t)
        y = 55 + 17 * math.sin(t)
        pod.append((x, y, RISER_H + 3 * STEP_H + 8))
    poly(ax, pod, "#3a3f46", ec="#5a616d", z=18)

    # Front LED diffuser glow strip
    p0 = iso(10, 0.2, 10)
    p1 = iso(DOCK_W - 10, 0.2, 10)
    for lw, a in [(18, 0.06), (10, 0.12), (4, 0.38)]:
        ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=C_LED, linewidth=lw, alpha=a, solid_capstyle="round", zorder=30)

    # Zone LED segments
    seg = [C_Z1, C_Z2, C_Z3, C_Z4, C_Z5]
    for i, col in enumerate(seg):
        x0 = 15 + i * 46
        x1 = x0 + 38
        s0 = iso(x0, 0.1, 10)
        s1 = iso(x1, 0.1, 10)
        ax.plot([s0[0], s1[0]], [s0[1], s1[1]], color=col, linewidth=3.0, alpha=0.95, solid_capstyle="round", zorder=31)

    # Captive USB-C cable tails from slot tops
    cable_pts = [(17.5, 12.0, 95), (17.5, 7.0, 90), (17.5, 5.0, 84)]
    c2d = [iso(*p) for p in cable_pts]
    ax.plot([p[0] for p in c2d], [p[1] for p in c2d], color="#353c46", linewidth=2.8, zorder=33)
    ax.plot([c2d[-1][0] - 3, c2d[-1][0] + 3], [c2d[-1][1], c2d[-1][1]], color="#aab3c0", linewidth=2.0, zorder=34)

    # C13 inlet on rear rail
    c13 = [(111, 100, 6), (139, 100, 6), (139, 100, 24), (111, 100, 24)]
    poly(ax, c13, "#0a0d11", ec="#2d3440", z=20)

    # Callouts
    add_label(ax, 820, 180, "Zone 4: Laptop slot · 100W USB-C PD")
    add_label(ax, 840, 220, "On-edge insertion + captive top cable")
    add_label(ax, 835, 320, "Zone 5: Tablet slot · 45W USB-C PD")
    add_label(ax, 730, 430, "Zone 3: Watch cradle · 5W")
    add_label(ax, 620, 500, "Zone 2: Buds or second phone dish · 20W Qi")
    add_label(ax, 500, 560, "Zone 1: Phone pad · 20W Qi2")
    add_label(ax, 680, 635, "20mm front fascia + WS2811 diffuser")
    add_label(ax, 850, 470, "25mm rear rail + centered IEC C13")


if __name__ == "__main__":
    fig = plt.figure(figsize=(CANVAS_W / 100, CANVAS_H / 100), dpi=100)
    fig.patch.set_facecolor(C_BG)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor(C_BG)
    ax.set_xlim(0, CANVAS_W)
    ax.set_ylim(CANVAS_H, 0)
    ax.axis("off")

    render(ax)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT_PATH, dpi=100, facecolor=C_BG, bbox_inches="tight", pad_inches=0)
    plt.close(fig)
    print(f"✓ Render written: {OUTPUT_PATH.relative_to(ROOT)}")
