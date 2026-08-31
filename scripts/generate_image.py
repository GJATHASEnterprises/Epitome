#!/usr/bin/env python3
"""
Step — hero product image generator.
Light grey background, clean isometric view, no text labels.
Run:
  python scripts/generate_image.py
Output:
  assets/step-hero.png  (1200×800 px)
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

ROOT = Path(__file__).resolve().parents[1]
OUT  = ROOT / "assets" / "step-hero.png"
OUT.parent.mkdir(exist_ok=True)

# ── Palette ───────────────────────────────────────────────────────────────────
C_BG        = "#f0f0f0"
C_ABS       = "#2a2a2a"
C_ABS_SIDE  = "#1a1a1a"
C_WALNUT    = "#8B6914"
C_WALNUT_DK = "#5C4209"
C_WALNUT_LT = "#A87B1E"
C_SILICONE  = "#3a3a3a"
C_SHADOW    = "#d8d8d8"

W, H = 12, 8

# ── Isometric projection ──────────────────────────────────────────────────────
def iso(x, y, z):
    px = (x - y) * 0.6
    py = (x + y) * 0.3 + z * 0.6
    return px, py

def face_top(x0, y0, x1, y1, z, **kw):
    c = [iso(x0,y0,z), iso(x1,y0,z), iso(x1,y1,z), iso(x0,y1,z)]
    return Polygon(c, closed=True, **kw)

def face_front(x0, x1, y, z0, z1, **kw):
    c = [iso(x0,y,z0), iso(x1,y,z0), iso(x1,y,z1), iso(x0,y,z1)]
    return Polygon(c, closed=True, **kw)

def face_right(x, y0, y1, z0, z1, **kw):
    c = [iso(x,y0,z0), iso(x,y1,z0), iso(x,y1,z1), iso(x,y0,z1)]
    return Polygon(c, closed=True, **kw)


def draw_block(ax, bx, ex, by, ey, z0, z1, walnut_top=False, zbase=None):
    if zbase is None:
        zbase = z1
    # Front face
    ax.add_patch(face_front(bx, ex, by, z0, z1,
                             facecolor=C_ABS, edgecolor=C_ABS_SIDE, lw=0.4, zorder=zbase))
    # Right face
    ax.add_patch(face_right(ex, by, ey, z0, z1,
                             facecolor=C_ABS_SIDE, edgecolor=C_ABS_SIDE, lw=0.4, zorder=zbase))
    # Top face
    top_c = C_WALNUT if walnut_top else C_ABS
    top_edge = C_WALNUT_DK if walnut_top else C_ABS_SIDE
    ax.add_patch(face_top(bx, by, ex, ey, z1,
                           facecolor=top_c, edgecolor=top_edge, lw=0.4, zorder=zbase+0.5))

    # Walnut grain (hatching lines across Y axis on top)
    if walnut_top:
        for g in np.linspace(by + (ey-by)*0.05, ey - (ey-by)*0.05, 10):
            p0 = iso(bx + (ex-bx)*0.02, g, z1)
            p1 = iso(ex - (ex-bx)*0.02, g, z1)
            ax.plot([p0[0], p1[0]], [p0[1], p1[1]],
                    color=C_WALNUT_DK, lw=0.25, alpha=0.45, zorder=zbase+0.6)


def draw_pad(ax, cx, cy, z, w, d, zorder=25):
    bx, ex = cx - w/2, cx + w/2
    by, ey = cy - d/2, cy + d/2
    ax.add_patch(face_top(bx, by, ex, ey, z,
                           facecolor=C_SILICONE, edgecolor="#444", lw=0.3, zorder=zorder, alpha=0.85))


def draw_ground_shadow(ax, S):
    """Soft shadow on the ground plane."""
    sx0, sx1 = iso(0*S, 0*S, 0), iso(165*S, 100*S, 0)
    # Draw a stretched ellipse under the dock
    cx = (sx0[0] + sx1[0]) / 2
    cy = (sx0[1] + sx1[1]) / 2 - 0.05
    shadow = mpatches.Ellipse((cx, cy - 0.08), 1.8, 0.35,
                               facecolor=C_SHADOW, alpha=0.5, zorder=0)
    ax.add_patch(shadow)


def main():
    S = 0.025   # mm → figure units

    fig, ax = plt.subplots(figsize=(W, H), facecolor=C_BG)
    ax.set_facecolor(C_BG)
    ax.set_aspect("equal")
    ax.axis("off")

    draw_ground_shadow(ax, S)

    # ── Base plate ───────────────────────────────────────────────────────────
    draw_block(ax, 0*S, 165*S, 0*S, 100*S, 0, 3*S, walnut_top=False, zbase=1)

    # ── Riser ────────────────────────────────────────────────────────────────
    draw_block(ax, 0*S, 165*S, 0*S, 100*S, 3*S, 25*S, walnut_top=False, zbase=2)

    # LED diffuser strip on front face
    ax.add_patch(face_front(17.5*S, 147.5*S, 0*S, 26*S, 33*S,
                             facecolor="#445566", edgecolor="#556677", lw=0.3, alpha=0.6, zorder=3))

    # ── Step 1 ───────────────────────────────────────────────────────────────
    draw_block(ax, 0*S, 165*S, 0*S, 100*S, 25*S, 40*S, walnut_top=True, zbase=4)
    draw_pad(ax, 82.5*S, 50*S, 40*S, 75*S, 90*S, zorder=5)

    # ── Step 2 ───────────────────────────────────────────────────────────────
    draw_block(ax, 17.5*S, 147.5*S, 0*S, 100*S, 40*S, 55*S, walnut_top=True, zbase=6)
    draw_pad(ax, 82.5*S, 50*S, 55*S, 65*S, 50*S, zorder=7)

    # ── Step 3 ───────────────────────────────────────────────────────────────
    draw_block(ax, 35*S, 130*S, 20*S, 100*S, 55*S, 70*S, walnut_top=True, zbase=8)
    draw_pad(ax, 82.5*S, 60*S, 70*S, 55*S, 55*S, zorder=9)

    # ── Rear USB-C port indicators ────────────────────────────────────────────
    for px_mm, col in [(120, "#FF8833"), (140, "#22CCBB")]:
        px, py = iso(px_mm*S, 100*S, 15*S)
        circle = mpatches.Circle((px, py), 0.035, facecolor=col, alpha=0.7, zorder=15)
        ax.add_patch(circle)

    # ── Rear DC jack ─────────────────────────────────────────────────────────
    px, py = iso(40*S, 100*S, 15*S)
    circle = mpatches.Circle((px, py), 0.04, facecolor="#888", alpha=0.6, zorder=15)
    ax.add_patch(circle)

    # ── Minimal callout dots (no text) ───────────────────────────────────────
    for cx_mm, cy_mm, z_mm, col in [
        (82.5, 50, 42, "#0044FF"),
        (82.5, 50, 57, "#8800FF"),
        (82.5, 60, 72, "#00CC44"),
    ]:
        px, py = iso(cx_mm*S, cy_mm*S, z_mm*S)
        dot = mpatches.Circle((px, py), 0.025, facecolor=col, alpha=0.5, zorder=20)
        ax.add_patch(dot)

    # ── Fit view ─────────────────────────────────────────────────────────────
    pts = [(0,0,0),(165*S,0,0),(0,100*S,0),(165*S,100*S,0),(82.5*S,60*S,80*S)]
    xs = [iso(*p)[0] for p in pts]
    ys = [iso(*p)[1] for p in pts]
    cx = (min(xs)+max(xs))/2
    cy = (min(ys)+max(ys))/2
    span = max(max(xs)-min(xs), max(ys)-min(ys)) * 0.7
    ax.set_xlim(cx - span, cx + span)
    ax.set_ylim(cy - span*0.6, cy + span*0.9)

    fig.tight_layout(pad=0)
    fig.savefig(OUT, dpi=100, bbox_inches="tight", facecolor=C_BG)
    plt.close(fig)
    print(f"Hero image saved: {OUT}")


if __name__ == "__main__":
    main()
