#!/usr/bin/env python3
from __future__ import annotations

import math
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle, FancyArrowPatch, FancyBboxPatch, Polygon, Rectangle
from matplotlib.path import Path as MplPath
from matplotlib.patches import PathPatch


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = ROOT / "assets" / "quad-dock-product-sheet.png"

BG = "#f5f5f5"
ACCENT = "#1a1a2e"
ZONE_FILL = "#2a2a2a"
ZONE_EDGE = "#c0a060"
LED = "#FFB347"


def rounded_polygon_path(points: np.ndarray, radius: float) -> MplPath:
    pts = np.asarray(points, dtype=float)
    n = len(pts)
    verts: list[tuple[float, float]] = []
    codes: list[int] = []
    for i in range(n):
        p_prev = pts[(i - 1) % n]
        p_curr = pts[i]
        p_next = pts[(i + 1) % n]
        v1 = p_prev - p_curr
        v2 = p_next - p_curr
        l1 = np.linalg.norm(v1)
        l2 = np.linalg.norm(v2)
        rr = min(radius, l1 * 0.45, l2 * 0.45)
        u1 = v1 / l1
        u2 = v2 / l2
        p1 = p_curr + u1 * rr
        p2 = p_curr + u2 * rr
        if i == 0:
            verts.append((p1[0], p1[1]))
            codes.append(MplPath.MOVETO)
        else:
            verts.append((p1[0], p1[1]))
            codes.append(MplPath.LINETO)
        verts.append((p_curr[0], p_curr[1]))
        codes.append(MplPath.CURVE3)
        verts.append((p2[0], p2[1]))
        codes.append(MplPath.CURVE3)
    verts.append((verts[0][0], verts[0][1]))
    codes.append(MplPath.CLOSEPOLY)
    return MplPath(verts, codes)


def draw_top_panel(ax: plt.Axes) -> None:
    ax.set_xlim(-95, 95)
    ax.set_ylim(-25, 330)
    ax.set_aspect("equal")
    ax.axis("off")

    dock_pts = np.array([[-55, 0], [55, 0], [70, 300], [-70, 300]], dtype=float)
    dock_patch = PathPatch(
        rounded_polygon_path(dock_pts, radius=14),
        facecolor="#3a3a3a",
        edgecolor=ACCENT,
        linewidth=1.8,
    )
    ax.add_patch(dock_patch)

    led_bar = Rectangle((-55, 0), 110, 7, facecolor=LED, edgecolor="#e7a95f", linewidth=0.8, alpha=0.95)
    ax.add_patch(led_bar)
    ax.text(0, 11, "LED Status Bar", ha="center", va="bottom", fontsize=8, color=ACCENT, fontweight="bold")

    z1 = FancyBboxPatch((-60, 42.5), 80, 55, boxstyle="round,pad=0.0,rounding_size=8", facecolor=ZONE_FILL, edgecolor=ZONE_EDGE, linewidth=1.2)
    z2 = FancyBboxPatch((-12.5, 42.5), 65, 55, boxstyle="round,pad=0.0,rounding_size=8", facecolor=ZONE_FILL, edgecolor=ZONE_EDGE, linewidth=1.2)
    z3 = Circle((-22, 225), 25, facecolor=ZONE_FILL, edgecolor=ZONE_EDGE, linewidth=1.2)
    z4 = FancyBboxPatch((18, 288), 22, 12, boxstyle="round,pad=0.0,rounding_size=3", facecolor=ZONE_FILL, edgecolor=ZONE_EDGE, linewidth=1.2)
    for patch in (z1, z2, z3, z4):
        ax.add_patch(patch)

    ax.text(-20, 70, "⚡\nPHONE / Qi2 15W", ha="center", va="center", fontsize=7, color="white", fontweight="bold")
    ax.text(20, 70, "BUDS / Qi 5W", ha="center", va="center", fontsize=7, color="white", fontweight="bold")
    ax.text(-22, 225, "WATCH\nMagSafe", ha="center", va="center", fontsize=7, color="white", fontweight="bold")
    ax.text(29, 294, "LAPTOP\nUSB-C 100W", ha="center", va="center", fontsize=5.2, color="white", fontweight="bold")

    iec = Rectangle((-8, 302), 16, 8, facecolor="#525252", edgecolor=ZONE_EDGE, linewidth=1.0)
    ax.add_patch(iec)
    ax.text(0, 314, "IEC C13", ha="center", va="bottom", fontsize=7, color=ACCENT, fontweight="bold")

    ax.text(0, 326, "TOP-DOWN ZONE LAYOUT", ha="center", va="top", fontsize=11, color=ACCENT, fontweight="bold")


def draw_perspective_panel(ax: plt.Axes) -> None:
    ax.set_xlim(0, 430)
    ax.set_ylim(0, 315)
    ax.set_aspect("equal")
    ax.axis("off")

    def h(y: float) -> float:
        return 12.0 + (10.0 * y / 300.0)

    def proj(x: float, y: float, z: float) -> tuple[float, float]:
        return 120 + x + 0.62 * y, 48 + z + 0.29 * y

    FL, FR = (-55.0, 0.0), (55.0, 0.0)
    RR, RL = (70.0, 300.0), (-70.0, 300.0)
    top = [proj(*FL, h(FL[1])), proj(*FR, h(FR[1])), proj(*RR, h(RR[1])), proj(*RL, h(RL[1]))]
    bot = [proj(*FL, 0.0), proj(*FR, 0.0), proj(*RR, 0.0), proj(*RL, 0.0)]

    ax.add_patch(Polygon([bot[0], bot[1], top[1], top[0]], closed=True, facecolor="#222227", edgecolor=ACCENT, linewidth=1.2))
    ax.add_patch(Polygon([bot[1], bot[2], top[2], top[1]], closed=True, facecolor="#26262d", edgecolor=ACCENT, linewidth=1.2))
    ax.add_patch(Polygon([bot[3], bot[0], top[0], top[3]], closed=True, facecolor="#202028", edgecolor=ACCENT, linewidth=1.2))
    ax.add_patch(Polygon(top, closed=True, facecolor="#d2d5dc", edgecolor=ACCENT, linewidth=1.3))

    led_front = [proj(-53, 0, h(0) + 0.5), proj(53, 0, h(0) + 0.5)]
    ax.plot([led_front[0][0], led_front[1][0]], [led_front[0][1], led_front[1][1]], color=LED, linewidth=4.2, alpha=0.95, solid_capstyle="round")
    ax.plot([led_front[0][0], led_front[1][0]], [led_front[0][1] + 1.0, led_front[1][1] + 1.0], color=LED, linewidth=8.0, alpha=0.2, solid_capstyle="round")

    zone_specs = [(-20, 70, 80, 55), (20, 70, 65, 55), (29, 294, 22, 12)]
    for cx, cy, w, d in zone_specs:
        p = [
            proj(cx - w / 2, cy - d / 2, h(cy - d / 2) + 0.2),
            proj(cx + w / 2, cy - d / 2, h(cy - d / 2) + 0.2),
            proj(cx + w / 2, cy + d / 2, h(cy + d / 2) + 0.2),
            proj(cx - w / 2, cy + d / 2, h(cy + d / 2) + 0.2),
        ]
        ax.add_patch(Polygon(p, closed=True, facecolor="#2f3138", edgecolor=ZONE_EDGE, linewidth=1.0))

    watch_ctr = proj(-22, 225, h(225) + 0.2)
    ax.add_patch(Circle(watch_ctr, 14, facecolor="#2f3138", edgecolor=ZONE_EDGE, linewidth=1.0))

    pod_base = proj(-48, 258, h(258))
    ax.add_patch(Circle((pod_base[0], pod_base[1] + 2), 8, facecolor="#1f2026", edgecolor=ACCENT, linewidth=1.0))
    angle = math.radians(30)
    tip = (pod_base[0] - 18 * math.cos(angle), pod_base[1] + 18 * math.sin(angle) + 20)
    ax.add_patch(Polygon([(pod_base[0] - 6, pod_base[1]), (pod_base[0] + 6, pod_base[1]), tip], closed=True, facecolor="#454b56", edgecolor=ACCENT, linewidth=1.0))
    ax.add_patch(Circle(tip, 5, facecolor="#2a2a2a", edgecolor=ZONE_EDGE, linewidth=1.0))

    for p in (proj(-50, 28, -1), proj(50, 28, -1), proj(-60, 282, -1), proj(60, 282, -1)):
        ax.add_patch(Circle((p[0], p[1] - 6), 3.2, facecolor="#1e1e23", edgecolor="#444", linewidth=0.8))

    cord_origin = proj(70, 296, 8)
    for i in range(4):
        ax.add_patch(Arc((cord_origin[0] + 26 + i * 14, cord_origin[1] + 4), 18 + i * 8, 12 + i * 4, theta1=20, theta2=340, color="#32323a", linewidth=1.7))
    ax.add_patch(FancyArrowPatch((cord_origin[0], cord_origin[1]), (cord_origin[0] + 25, cord_origin[1] + 2), arrowstyle="-", linewidth=2.0, color="#32323a"))

    ax.text(215, 302, "PERSPECTIVE PRODUCT SKETCH", ha="center", va="top", fontsize=11, color=ACCENT, fontweight="bold")


def draw_feature_panel(ax: plt.Axes) -> None:
    ax.axis("off")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    y = 0.95
    ax.text(0.05, y, "QUAD-DOCK", fontsize=20, color=ACCENT, fontweight="bold", va="top")
    y -= 0.045
    ax.plot([0.05, 0.95], [y, y], color="#d5d5dc", linewidth=1.2)

    blocks = [
        ("⚡", "Zone 1 — Phone", "Qi2 · 15W · MagSafe-compatible"),
        ("◉", "Zone 2 — Earbuds", "Qi · 5W · Universal"),
        ("◎", "Zone 3 — Watch", "Apple Watch MagSafe puck\nTilts 30° · Magnetic lock"),
        ("▣", "Zone 4 — Laptop", "USB-C PD · 100W\nFits MacBook / Surface / XPS"),
    ]
    y -= 0.03
    icon_colors = ["#c08a2c", "#5b79d4", "#6aa58a", "#7d6cd4"]
    for idx, (icon, title, body) in enumerate(blocks):
        ax.add_patch(Circle((0.067, y - 0.011), 0.0085, facecolor=icon_colors[idx], edgecolor="none"))
        ax.text(0.085, y, f"{icon}  {title}", fontsize=12.5, color=ACCENT, fontweight="bold", va="top")
        y -= 0.032
        ax.text(0.105, y, body, fontsize=10.8, color="#2a2a2a", va="top", linespacing=1.35)
        y -= 0.09 if "\n" in body else 0.068

    ax.plot([0.05, 0.95], [y, y], color="#d5d5dc", linewidth=1.2)
    y -= 0.03
    ax.text(0.06, y, "POWER", fontsize=12.5, color=ACCENT, fontweight="bold", va="top")
    y -= 0.03
    ax.text(0.08, y, "IEC C13 inlet · 150W PSU\nSurge protected", fontsize=10.8, color="#2a2a2a", va="top", linespacing=1.35)
    y -= 0.1

    ax.text(0.06, y, "DESIGN", fontsize=12.5, color=ACCENT, fontweight="bold", va="top")
    y -= 0.03
    ax.text(0.08, y, "Brushed aluminium top plate\nABS body · Wedge profile\n110→140mm × 300mm × 12→22mm", fontsize=10.8, color="#2a2a2a", va="top", linespacing=1.35)
    y -= 0.125

    ax.text(0.06, y, "LED STATUS BAR", fontsize=12.5, color=ACCENT, fontweight="bold", va="top")
    y -= 0.03
    ax.text(0.08, y, "4-segment warm white\nPer-zone charge indicators", fontsize=10.8, color="#2a2a2a", va="top", linespacing=1.35)
    y -= 0.085
    ax.plot([0.05, 0.95], [y, y], color="#d5d5dc", linewidth=1.2)

    ax.text(0.56, 0.06, "Quad-Dock™\nGJATHASEnterprises 2025", ha="center", va="center", fontsize=12.5, color=ACCENT)


def build_figure() -> None:
    fig = plt.figure(figsize=(24, 16), dpi=200, facecolor=BG)
    gs = fig.add_gridspec(1, 3, width_ratios=[40, 35, 25], left=0.025, right=0.975, top=0.95, bottom=0.09, wspace=0.03)
    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[0, 1])
    ax3 = fig.add_subplot(gs[0, 2])

    for ax in (ax1, ax2, ax3):
        ax.set_facecolor("white")
        for spine in ax.spines.values():
            spine.set_visible(True)
            spine.set_linewidth(1.0)
            spine.set_edgecolor("#dcdce4")

    draw_top_panel(ax1)
    draw_perspective_panel(ax2)
    draw_feature_panel(ax3)

    pos1, pos2, pos3 = ax1.get_position(), ax2.get_position(), ax3.get_position()
    fig.add_artist(plt.Line2D([pos1.x1 + 0.006, pos1.x1 + 0.006], [pos1.y0, pos1.y1], color="#d7d7de", linewidth=0.8))
    fig.add_artist(plt.Line2D([pos2.x1 + 0.006, pos2.x1 + 0.006], [pos2.y0, pos2.y1], color="#d7d7de", linewidth=0.8))
    fig.add_artist(plt.Line2D([0.03, 0.97], [0.055, 0.055], color="#e1e1e8", linewidth=0.8))
    fig.text(0.5, 0.028, "CONFIDENTIAL — INVESTOR PREVIEW", ha="center", va="center", fontsize=13, color="#c9c9cf")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT_PATH, dpi=200)
    plt.close(fig)


if __name__ == "__main__":
    build_figure()
    print(f"Saved: {OUTPUT_PATH}")
