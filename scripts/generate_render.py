#!/usr/bin/env python3
"""
Step — marketing render generator.
Uses matplotlib + Pillow only (no Blender required).
Run:
  python scripts/generate_render.py
Output:
  assets/step-render.png  (1200×800 px)
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Polygon

ROOT = Path(__file__).resolve().parents[1]
OUT  = ROOT / "assets" / "step-render.png"
OUT.parent.mkdir(exist_ok=True)

# ── Colour palette ────────────────────────────────────────────────────────────
C_BG        = "#111111"
C_ABS       = "#1a1a1a"
C_WALNUT    = "#8B6914"
C_WALNUT_DK = "#5C4209"
C_SILICONE  = "#222222"
C_GLOW_1    = "#0044FF"   # Zone 1 phone — blue
C_GLOW_2    = "#8800FF"   # Zone 2 buds — purple
C_GLOW_3    = "#00CC44"   # Zone 3 watch — green
C_GLOW_A    = "#FF6600"   # Port A — orange
C_GLOW_B    = "#00BBAA"   # Port B — teal
C_LED_STRIP = "#334466"
C_TEXT      = "#EEEEEE"
C_LABEL     = "#AAAAAA"
C_ACCENT    = "#CCCCCC"

W, H = 12, 8  # figure size in inches at 100 dpi → 1200×800 px

# ── Isometric helpers ─────────────────────────────────────────────────────────
def iso(x, y, z, scale=1.0):
    """Isometric projection: returns (px, py) in figure units."""
    px = (x - y) * 0.6 * scale
    py = (x + y) * 0.3 * scale + z * 0.6 * scale
    return px, py

def face_top(x0, y0, x1, y1, z, **kw):
    corners = [iso(x0,y0,z), iso(x1,y0,z), iso(x1,y1,z), iso(x0,y1,z)]
    return Polygon(corners, closed=True, **kw)

def face_front(x0, x1, y, z0, z1, **kw):
    corners = [iso(x0,y,z0), iso(x1,y,z0), iso(x1,y,z1), iso(x0,y,z1)]
    return Polygon(corners, closed=True, **kw)

def face_right(x, y0, y1, z0, z1, **kw):
    corners = [iso(x,y0,z0), iso(x,y1,z0), iso(x,y1,z1), iso(x,y0,z1)]
    return Polygon(corners, closed=True, **kw)


def draw_step(ax, bx, ex, by, ey, z0, z1, walnut_top=True, alpha_top=1.0):
    """Draw one step block: front face, right face, top face."""
    ax.add_patch(face_front(bx, ex, by, z0, z1, facecolor=C_ABS, edgecolor="#333", lw=0.5, zorder=z1))
    ax.add_patch(face_right(ex, by, ey, z0, z1, facecolor="#151515", edgecolor="#333", lw=0.5, zorder=z1))
    top_color = C_WALNUT if walnut_top else C_ABS
    ax.add_patch(face_top(bx, by, ex, ey, z1, facecolor=top_color, edgecolor=C_WALNUT_DK if walnut_top else "#333",
                           lw=0.5, zorder=z1+0.5, alpha=alpha_top))
    # Walnut grain lines on top
    if walnut_top:
        for g in np.linspace(by+2, ey-2, 8):
            lx = [iso(bx+2, g, z1)[0], iso(ex-2, g, z1)[0]]
            ly = [iso(bx+2, g, z1)[1], iso(ex-2, g, z1)[1]]
            ax.plot(lx, ly, color=C_WALNUT_DK, lw=0.3, alpha=0.5, zorder=z1+0.6)


def draw_glow_ellipse(ax, cx, cy, z, color, rx=4, ry=2.5, zorder=20):
    px, py = iso(cx, cy, z)
    glow = mpatches.Ellipse((px, py), rx*2, ry*2, facecolor=color, alpha=0.25, zorder=zorder)
    ax.add_patch(glow)
    inner = mpatches.Ellipse((px, py), rx*0.8, ry*0.8, facecolor=color, alpha=0.4, zorder=zorder+0.1)
    ax.add_patch(inner)


def draw_device(ax, cx, cy, z, w, d, h, color, label="", glow_color=None):
    """Draw a simple device rectangle on top of a zone."""
    bx, ex = cx - w/2, cx + w/2
    by, ey = cy - d/2, cy + d/2
    draw_step(ax, bx, ex, by, ey, z, z+h, walnut_top=False, alpha_top=0.85)
    if glow_color:
        draw_glow_ellipse(ax, cx, cy, z, glow_color, rx=w*0.35, ry=d*0.2, zorder=z+h+1)


def add_label(ax, x, y, z, text, wattage=None, color=C_LABEL, offset_x=0.3, offset_y=0.0):
    px, py = iso(x, y, z)
    lx, ly = px + offset_x, py + offset_y
    ax.annotate("", xy=(px, py), xytext=(lx, ly),
                arrowprops=dict(arrowstyle="-", color=color, lw=0.8), zorder=50)
    label_text = f"{text}  {wattage}" if wattage else text
    ax.text(lx, ly, label_text, color=color, fontsize=7, va="center", ha="left",
            fontfamily="monospace", zorder=51)


def main():
    fig, ax = plt.subplots(figsize=(W, H), facecolor=C_BG)
    ax.set_facecolor(C_BG)
    ax.set_aspect("equal")
    ax.axis("off")

    # Scale for isometric view (mm → figure units)
    S = 0.025

    # ── Build Step geometry ──────────────────────────────────────────────────
    # Coordinates in mm, scaled by S

    # Base plate: 165×100×3mm Z=0..3
    ax.add_patch(face_front(0*S, 165*S, 0*S, 0*S, 3*S, facecolor=C_ABS, edgecolor="#2a2a2a", lw=0.3, zorder=1))
    ax.add_patch(face_right(165*S, 0*S, 100*S, 0*S, 3*S, facecolor="#111", edgecolor="#2a2a2a", lw=0.3, zorder=1))

    # Riser: 165×100×22mm Z=3..25
    ax.add_patch(face_front(0*S, 165*S, 0*S, 3*S, 25*S, facecolor=C_ABS, edgecolor="#2a2a2a", lw=0.4, zorder=2))
    ax.add_patch(face_right(165*S, 0*S, 100*S, 3*S, 25*S, facecolor="#111", edgecolor="#2a2a2a", lw=0.3, zorder=2))
    ax.add_patch(face_top(0*S, 0*S, 165*S, 100*S, 25*S, facecolor=C_ABS, edgecolor="#333", lw=0.3, zorder=2.5))

    # LED diffuser strip: front face of riser, 130mm wide
    led_x0, led_x1 = 17.5*S, 147.5*S
    ax.add_patch(face_front(led_x0, led_x1, 0*S, 25*S, 33*S,
                             facecolor=C_LED_STRIP, edgecolor="#446", lw=0.3, alpha=0.7, zorder=3))

    # Step 1: 165×100×15mm Z=25..40
    draw_step(ax, 0*S, 165*S, 0*S, 100*S, 25*S, 40*S, walnut_top=True)

    # Step 2: 130×100×15mm Z=40..55 centred (X=17.5..147.5)
    draw_step(ax, 17.5*S, 147.5*S, 0*S, 100*S, 40*S, 55*S, walnut_top=True)

    # Step 3: 95×80×15mm Z=55..70, Y=20..100 setback
    draw_step(ax, 35*S, 130*S, 20*S, 100*S, 55*S, 70*S, walnut_top=True)

    # ── LED glow on front fascia ─────────────────────────────────────────────
    for i, (gx, gc) in enumerate([(40*S, C_GLOW_1), (70*S, C_GLOW_2), (100*S, C_GLOW_3),
                                    (125*S, C_GLOW_A), (140*S, C_GLOW_B)]):
        px, py = iso(gx, 0*S, 29*S)
        glow = mpatches.Ellipse((px, py), 0.12, 0.05, facecolor=gc, alpha=0.5, zorder=4)
        ax.add_patch(glow)

    # ── Device silhouettes ───────────────────────────────────────────────────
    # Phone on Zone 1 (portrait, centred X=82.5, Y=50, Z=40)
    draw_device(ax, 82.5*S, 50*S, 40*S, 37*S, 68*S, 5*S, "#2a2a2a", glow_color=C_GLOW_1)
    # Buds case on Zone 2 (centred X=82.5, Y=50, Z=55)
    draw_device(ax, 82.5*S, 50*S, 55*S, 45*S, 35*S, 4*S, "#222222", glow_color=C_GLOW_2)
    # Watch on Zone 3 (centred X=82.5, Y=60, Z=70)
    draw_device(ax, 82.5*S, 60*S, 70*S, 38*S, 38*S, 4*S, "#1e1e1e", glow_color=C_GLOW_3)

    # ── Rear USB-C ports ─────────────────────────────────────────────────────
    for px_mm, col in [(120, C_GLOW_A), (140, C_GLOW_B)]:
        px, py = iso(px_mm*S, 100*S, 15*S)
        circle = mpatches.Circle((px, py), 0.04, facecolor=col, alpha=0.6, zorder=30)
        ax.add_patch(circle)

    # ── Labels ───────────────────────────────────────────────────────────────
    label_data = [
        (82.5*S, 50*S, 45*S, "① PHONE", "Qi2 20W", C_GLOW_1, -0.5, 0.1),
        (82.5*S, 50*S, 59*S, "② BUDS", "Qi 5W",  C_GLOW_2, -0.5, 0.1),
        (82.5*S, 60*S, 74*S, "③ WATCH", "5W",    C_GLOW_3, -0.4, 0.1),
        (120*S,  100*S, 22*S, "④ USB-C A", "60W", C_GLOW_A, 0.2,  0.1),
        (140*S,  100*S, 22*S, "⑤ USB-C B", "30W", C_GLOW_B, 0.2, -0.1),
    ]
    for lx, ly, lz, text, watts, col, ox, oy in label_data:
        px, py = iso(lx, ly, lz)
        epx, epy = px + ox, py + oy
        ax.annotate("", xy=(px, py), xytext=(epx, epy),
                    arrowprops=dict(arrowstyle="-", color=col, lw=0.7), zorder=50)
        ax.text(epx, epy, f"{text}  {watts}", color=col, fontsize=6.5,
                va="center", ha="left" if ox > 0 else "right",
                fontfamily="monospace", zorder=51)

    # ── Title and price ───────────────────────────────────────────────────────
    ax.text(0.03, 0.93, "Step", transform=ax.transAxes,
            color=C_TEXT, fontsize=32, fontweight="bold", va="top", zorder=60)
    ax.text(0.03, 0.84, "Charge everything. Touch nothing.",
            transform=ax.transAxes, color=C_LABEL, fontsize=9, va="top", zorder=60)
    ax.text(0.97, 0.05, "$89", transform=ax.transAxes,
            color=C_TEXT, fontsize=22, fontweight="bold", va="bottom", ha="right", zorder=60)

    # ── Fit and save ─────────────────────────────────────────────────────────
    # Centre the isometric view
    all_xs, all_ys = [], []
    for x, y, z in [(0, 0, 0), (165*S, 0, 0), (165*S, 100*S, 0), (0, 100*S, 0),
                    (82.5*S, 60*S, 80*S)]:
        px, py = iso(x, y, z)
        all_xs.append(px)
        all_ys.append(py)
    cx = (min(all_xs) + max(all_xs)) / 2
    cy = (min(all_ys) + max(all_ys)) / 2
    span = max(max(all_xs)-min(all_xs), max(all_ys)-min(all_ys)) * 0.75
    ax.set_xlim(cx - span, cx + span)
    ax.set_ylim(cy - span * 0.6, cy + span * 0.9)

    fig.tight_layout(pad=0)
    fig.savefig(OUT, dpi=100, bbox_inches="tight", facecolor=C_BG)
    plt.close(fig)
    print(f"Render saved: {OUT}")


if __name__ == "__main__":
    main()
