#!/usr/bin/env python3
"""
High-quality Penta Dock marketing render generator.
Uses matplotlib + Pillow only (no Blender / bpy required).
Run:
  python scripts/generate_render.py
Output:
  assets/penta-dock-render.png  (1200×800 px)
  assets/quad-dock-render.png   (copy, backwards-compat)
"""
from __future__ import annotations

import shutil
from pathlib import Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Polygon
from matplotlib.collections import PatchCollection

ROOT = Path(__file__).resolve().parents[1]
PRIMARY_OUT  = ROOT / "assets" / "penta-dock-render.png"
COMPAT_OUT   = ROOT / "assets" / "quad-dock-render.png"

# ── Colours ──────────────────────────────────────────────────────────────────
C_BG        = "#1a1a1a"
C_BODY      = "#2a2a2a"
C_STEP      = "#333333"
C_SILICONE  = "#1f1f1f"
C_WHITE     = "#ffffff"
C_GREY      = "#aaaaaa"
C_BLUE      = "#3399ff"
C_PURPLE    = "#9966ff"
C_GREEN     = "#33cc66"
C_ORANGE    = "#ff8800"

# ── Canvas ───────────────────────────────────────────────────────────────────
W_PX, H_PX = 1200, 800
DPI = 100
FIG_W, FIG_H = W_PX / DPI, H_PX / DPI   # 12 × 8 inches


# ── Isometric helpers ────────────────────────────────────────────────────────
ISO_ANGLE = np.radians(30)
ISO_X_SCALE = np.cos(ISO_ANGLE)
ISO_Y_SCALE = np.sin(ISO_ANGLE)

def iso(x: float, y: float, z: float = 0.0):
    """Convert 3-D dock coords → 2-D canvas coords (units = inches)."""
    px = (x - y) * ISO_X_SCALE
    py = (x + y) * ISO_Y_SCALE + z
    return px, py


def iso_poly(pts3d):
    """List of (x,y,z) → numpy array of 2-D points."""
    return np.array([iso(*p) for p in pts3d])


# ── Drawing origin (centre of canvas) ────────────────────────────────────────
OX, OY = FIG_W * 0.48, FIG_H * 0.44


def shift(xy):
    return xy + np.array([OX, OY])


def draw_poly(ax, pts3d, color, alpha=1.0, zorder=2, ec=None, lw=0.5):
    verts = shift(iso_poly(pts3d))
    patch = Polygon(verts, closed=True, facecolor=color, edgecolor=ec or color,
                    linewidth=lw, alpha=alpha, zorder=zorder)
    ax.add_patch(patch)
    return patch


def draw_rect_face(ax, x0, x1, y0, y1, z0, z1, color, alpha=1.0, zorder=2):
    """Draw one rectangular face in 3-D iso space."""
    pts = [(x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0)]
    draw_poly(ax, pts, color, alpha=alpha, zorder=zorder)


def glow(ax, pts3d, color, layers=6, max_alpha=0.18, zorder=1):
    """Soft glow by drawing progressively expanded transparent polygons."""
    verts2d = shift(iso_poly(pts3d))
    cx = verts2d[:, 0].mean()
    cy = verts2d[:, 1].mean()
    for i in range(layers, 0, -1):
        scale = 1.0 + i * 0.06
        expanded = (verts2d - np.array([cx, cy])) * scale + np.array([cx, cy])
        patch = Polygon(expanded, closed=True, facecolor=color, edgecolor="none",
                        alpha=max_alpha * (i / layers) ** 1.5, zorder=zorder)
        ax.add_patch(patch)


def main() -> None:
    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H), dpi=DPI)
    fig.patch.set_facecolor(C_BG)
    ax.set_facecolor(C_BG)
    ax.set_xlim(0, FIG_W)
    ax.set_ylim(0, FIG_H)
    ax.set_aspect("equal")
    ax.axis("off")

    # ── Dock dimensions (in "dock units" ≈ 0.9 inch per unit) ────────────────
    # Base footprint: 5.0 wide × 3.0 deep × 0.6 tall
    BW, BD, BH = 5.0, 3.0, 0.6
    # Three-step staircase heights
    S1H, S2H, S3H = 1.0, 1.6, 2.2   # step top-surface heights above base

    # ── Drop shadow ──────────────────────────────────────────────────────────
    shadow_pts = [(-2.6, -1.6, 0), (2.6, -1.6, 0), (2.6, 1.6, 0), (-2.6, 1.6, 0)]
    glow(ax, shadow_pts, "#000000", layers=8, max_alpha=0.5, zorder=1)

    # ── Base body ─────────────────────────────────────────────────────────────
    # Top face
    draw_poly(ax, [(-BW/2, -BD/2, BH), ( BW/2, -BD/2, BH),
                   ( BW/2,  BD/2, BH), (-BW/2,  BD/2, BH)],
              C_BODY, zorder=3)
    # Front face
    draw_poly(ax, [(-BW/2, -BD/2, 0), ( BW/2, -BD/2, 0),
                   ( BW/2, -BD/2, BH), (-BW/2, -BD/2, BH)],
              "#222222", zorder=3)
    # Right face
    draw_poly(ax, [( BW/2, -BD/2, 0), ( BW/2, BD/2, 0),
                   ( BW/2,  BD/2, BH), ( BW/2, -BD/2, BH)],
              "#252525", zorder=3)

    # ── Three-step staircase (centre platform, rising front→back) ────────────
    FRONT_Y, REAR_Y = -1.0, 1.0
    steps = [
        (-1.8, 1.8, FRONT_Y, REAR_Y, S1H),   # Step 1: 180×100
        (-1.4, 1.4, FRONT_Y, REAR_Y, S2H),   # Step 2: 140×100
        (-1.0, 1.0, -0.6,    REAR_Y, S3H),   # Step 3: 100×80, set back 20mm
    ]

    for (x0, x1, y0, y1, sz) in steps:
        draw_poly(ax, [(x0, y0, BH + sz), (x1, y0, BH + sz), (x1, y1, BH + sz), (x0, y1, BH + sz)], C_STEP, zorder=4)
        draw_poly(ax, [(x0, y0, BH), (x1, y0, BH), (x1, y0, BH + sz), (x0, y0, BH + sz)], "#1e1e1e", zorder=4)
        draw_poly(ax, [(x1, y0, BH), (x1, y1, BH), (x1, y1, BH + sz), (x1, y0, BH + sz)], "#1c1c1c", zorder=4)

    # ── Zone pad surfaces (silicone recesses) ─────────────────────────────────
    pads = [
        (-1.6, 1.6, -0.8, 0.8, BH + S1H + 0.02),   # Zone 1 phone on Step 1
        (-1.2, 1.2, -0.8, 0.8, BH + S2H + 0.02),   # Zone 2 buds/phone on Step 2
        (-0.6, 0.6, -0.35, 0.65, BH + S3H + 0.02), # Zone 3 watch on Step 3 setback
    ]
    pad_colors = [C_BLUE, C_PURPLE, C_GREEN]
    for (x0, x1, y0, y1, z), pc in zip(pads, pad_colors):
        # Silicone pad
        draw_poly(ax, [(x0, y0, z), (x1, y0, z), (x1, y1, z), (x0, y1, z)],
                  C_SILICONE, zorder=5)
        # Thin accent border
        draw_poly(ax, [(x0, y0, z), (x1, y0, z), (x1, y1, z), (x0, y1, z)],
                  pc, alpha=0.25, zorder=5, ec=pc, lw=1.2)

    # ── Zone 4 – Laptop slot (LEFT side, tall vertical) ───────────────────────
    # Tall slot on the left flank of the base
    LX0, LX1 = -BW/2 - 0.06, -BW/2 + 0.06
    LY0, LY1 = -1.8, 1.8
    LZ0, LZ1 = BH, BH + 3.2
    draw_poly(ax, [(LX0, LY0, LZ0), (LX1, LY0, LZ0),
                   (LX1, LY0, LZ1), (LX0, LY0, LZ1)],
              C_ORANGE, alpha=0.85, zorder=6, ec=C_ORANGE, lw=0.8)
    draw_poly(ax, [(LX1, LY0, LZ0), (LX1, LY1, LZ0),
                   (LX1, LY1, LZ1), (LX1, LY0, LZ1)],
              "#3a2000", alpha=0.9, zorder=6)
    # Interior slot recess
    draw_poly(ax, [(LX0, LY0, LZ0+0.1), (LX1, LY0, LZ0+0.1),
                   (LX1, LY1, LZ0+0.1), (LX0, LY1, LZ0+0.1)],
              C_SILICONE, zorder=6, ec=C_ORANGE, lw=0.6)

    # ── Zone 5 – Tablet slot (RIGHT side, shorter vertical) ───────────────────
    RX0, RX1 = BW/2 - 0.06, BW/2 + 0.06
    RY0, RY1 = -1.3, 1.3
    RZ0, RZ1 = BH, BH + 2.4
    draw_poly(ax, [(RX0, RY0, RZ0), (RX1, RY0, RZ0),
                   (RX1, RY0, RZ1), (RX0, RY0, RZ1)],
              C_BLUE, alpha=0.85, zorder=6, ec=C_BLUE, lw=0.8)
    draw_poly(ax, [(RX0, RY0, RZ0), (RX0, RY1, RZ0),
                   (RX0, RY1, RZ1), (RX0, RY0, RZ1)],
              "#001a33", alpha=0.9, zorder=6)
    draw_poly(ax, [(RX0, RY0, RZ0+0.1), (RX1, RY0, RZ0+0.1),
                   (RX1, RY1, RZ0+0.1), (RX0, RY1, RZ0+0.1)],
              C_SILICONE, zorder=6, ec=C_BLUE, lw=0.6)

    # ── Rear-left IEC inlet indicator (X≈45mm from left edge) ─────────────────
    iec_x0, iec_x1 = -1.88, -1.32
    iec_y = BD / 2
    iec_z0, iec_z1 = 0.55, 1.0
    draw_poly(ax, [(iec_x0, iec_y, iec_z0), (iec_x1, iec_y, iec_z0),
                   (iec_x1, iec_y, iec_z1), (iec_x0, iec_y, iec_z1)],
              C_PURPLE, alpha=0.9, zorder=6, ec=C_PURPLE, lw=0.8)

    # ── LED strip on front fascia ──────────────────────────────────────────────
    led_colors = [C_BLUE, C_PURPLE, C_GREEN, C_ORANGE, C_BLUE]
    seg_w = BW / len(led_colors)
    LED_Y = -BD / 2 - 0.01
    LED_Z0, LED_Z1 = 0.05, 0.15
    for i, lc in enumerate(led_colors):
        x0 = -BW/2 + i * seg_w
        x1 = x0 + seg_w
        pts = [(x0, LED_Y, LED_Z0), (x1, LED_Y, LED_Z0),
               (x1, LED_Y, LED_Z1), (x0, LED_Y, LED_Z1)]
        glow(ax, pts, lc, layers=4, max_alpha=0.35, zorder=2)
        draw_poly(ax, pts, lc, alpha=0.9, zorder=7, ec=lc, lw=0.3)

    # ── Zone labels ───────────────────────────────────────────────────────────
    zone_labels = [
        (-1.0, -1.35, BH + S1H + 0.05, "PHONE\n20W Qi2", C_BLUE),
        (0.2, -1.35, BH + S2H + 0.05, "BUDS / PHONE\n20W Qi", C_PURPLE),
        (1.1, -0.95, BH + S3H + 0.05, "WATCH\n5W", C_GREEN),
    ]
    for (xd, yd, zd, label, color) in zone_labels:
        px, py = iso(xd, yd, zd)
        ax.text(OX + px, OY + py, label,
                color=color, fontsize=5.5, ha="center", va="bottom",
                fontfamily="DejaVu Sans", fontweight="bold",
                zorder=10, multialignment="center",
                bbox=dict(boxstyle="round,pad=0.15", fc="#1a1a1a", ec=color,
                          lw=0.7, alpha=0.88))

    # Zone 4 label (left side)
    lx4, ly4 = iso(-BW/2 - 0.5, 0, BH + 1.6)
    ax.text(OX + lx4, OY + ly4, "LAPTOP\n100W USB-C",
            color=C_ORANGE, fontsize=5.5, ha="center", va="center",
            fontfamily="DejaVu Sans", fontweight="bold", zorder=10,
            multialignment="center",
            bbox=dict(boxstyle="round,pad=0.15", fc="#1a1a1a", ec=C_ORANGE,
                      lw=0.7, alpha=0.88))
    # Arrow toward laptop slot
    ax.annotate("", xy=shift(iso_poly([(-BW/2 + 0.1, 0, BH + 1.6)]))[0],
                xytext=(OX + lx4, OY + ly4),
                arrowprops=dict(arrowstyle="-|>", color=C_ORANGE, lw=0.8),
                zorder=10)

    # Zone 5 label (right side)
    lx5, ly5 = iso(BW/2 + 0.5, 0, BH + 1.2)
    ax.text(OX + lx5, OY + ly5, "TABLET\n45W USB-C",
            color=C_BLUE, fontsize=5.5, ha="center", va="center",
            fontfamily="DejaVu Sans", fontweight="bold", zorder=10,
            multialignment="center",
            bbox=dict(boxstyle="round,pad=0.15", fc="#1a1a1a", ec=C_BLUE,
                      lw=0.7, alpha=0.88))
    ax.annotate("", xy=shift(iso_poly([(BW/2 - 0.1, 0, BH + 1.2)]))[0],
                xytext=(OX + lx5, OY + ly5),
                arrowprops=dict(arrowstyle="-|>", color=C_BLUE, lw=0.8),
                zorder=10)

    # ── Title text ────────────────────────────────────────────────────────────
    ax.text(0.04, 0.93, "PENTA DOCK",
            transform=ax.transAxes, color=C_WHITE, fontsize=28,
            fontfamily="DejaVu Sans", fontweight="bold", va="top",
            zorder=11)
    ax.text(0.04, 0.84, "One dock. Every device.",
            transform=ax.transAxes, color=C_GREY, fontsize=13,
            fontfamily="DejaVu Sans", va="top", zorder=11)

    # ── Bottom text ────────────────────────────────────────────────────────────
    ax.text(0.97, 0.05, "190W total output",
            transform=ax.transAxes, color=C_WHITE, fontsize=11,
            fontfamily="DejaVu Sans", ha="right", va="bottom",
            fontweight="bold", zorder=11)
    ax.text(0.03, 0.05, "epitomecharge.com",
            transform=ax.transAxes, color=C_GREY, fontsize=9,
            fontfamily="DejaVu Sans", ha="left", va="bottom", zorder=11)

    # ── Save ──────────────────────────────────────────────────────────────────
    PRIMARY_OUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(PRIMARY_OUT, dpi=DPI, facecolor=C_BG, bbox_inches="tight", pad_inches=0)
    plt.close(fig)

    shutil.copy2(PRIMARY_OUT, COMPAT_OUT)

    print(f"✓ Saved assets/penta-dock-render.png (1200×800 px)")


if __name__ == "__main__":
    main()
