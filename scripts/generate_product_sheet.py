#!/usr/bin/env python3
"""
Step — product sheet generator.
Two-panel layout: dock render left (55%), spec right (45%).
Run:
  python scripts/generate_product_sheet.py
Output:
  assets/step-product-sheet.png  (1200×800 px, dpi=150)
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
from matplotlib.patches import Polygon, FancyBboxPatch

ROOT = Path(__file__).resolve().parents[1]
OUT  = ROOT / "assets" / "step-product-sheet.png"
OUT.parent.mkdir(exist_ok=True)

DPI = 150
W_IN = 1200 / DPI   # 8.0 inches
H_IN = 800  / DPI   # 5.333 inches

# ── Colour palette ────────────────────────────────────────────────────────────
C_BG        = "#111111"
C_PANEL     = "#1a1a1a"
C_ABS       = "#222222"
C_ABS_SIDE  = "#161616"
C_WALNUT    = "#8B6914"
C_WALNUT_DK = "#5C4209"
C_DIVIDER   = "#333333"
C_TEXT      = "#EEEEEE"
C_SUBTEXT   = "#AAAAAA"
C_ACCENT    = "#FFFFFF"
C_GLOW_1    = "#0044FF"
C_GLOW_2    = "#8800FF"
C_GLOW_3    = "#00CC44"
C_GLOW_A    = "#FF6600"
C_GLOW_B    = "#00BBAA"

# ── Isometric helpers ─────────────────────────────────────────────────────────
def iso(x, y, z):
    return (x - y) * 0.6, (x + y) * 0.3 + z * 0.6

def face_top(x0, y0, x1, y1, z, **kw):
    return Polygon([iso(x0,y0,z),iso(x1,y0,z),iso(x1,y1,z),iso(x0,y1,z)], closed=True, **kw)

def face_front(x0, x1, y, z0, z1, **kw):
    return Polygon([iso(x0,y,z0),iso(x1,y,z0),iso(x1,y,z1),iso(x0,y,z1)], closed=True, **kw)

def face_right(x, y0, y1, z0, z1, **kw):
    return Polygon([iso(x,y0,z0),iso(x,y1,z0),iso(x,y1,z1),iso(x,y0,z1)], closed=True, **kw)


def draw_block(ax, bx, ex, by, ey, z0, z1, walnut_top=False, zbase=1):
    ax.add_patch(face_front(bx, ex, by, z0, z1, facecolor=C_ABS, edgecolor=C_ABS_SIDE, lw=0.3, zorder=zbase))
    ax.add_patch(face_right(ex, by, ey, z0, z1, facecolor=C_ABS_SIDE, edgecolor=C_ABS_SIDE, lw=0.3, zorder=zbase))
    tc = C_WALNUT if walnut_top else C_ABS
    te = C_WALNUT_DK if walnut_top else C_ABS_SIDE
    ax.add_patch(face_top(bx, by, ex, ey, z1, facecolor=tc, edgecolor=te, lw=0.3, zorder=zbase+0.5))
    if walnut_top:
        for g in np.linspace(by+(ey-by)*0.08, ey-(ey-by)*0.08, 7):
            p0 = iso(bx+(ex-bx)*0.03, g, z1)
            p1 = iso(ex-(ex-bx)*0.03, g, z1)
            ax.plot([p0[0],p1[0]], [p0[1],p1[1]], color=C_WALNUT_DK, lw=0.25, alpha=0.45, zorder=zbase+0.6)


def draw_glow(ax, cx, cy, z, color, rx=0.12, ry=0.06):
    px, py = iso(cx, cy, z)
    ax.add_patch(mpatches.Ellipse((px,py), rx*2, ry*2, facecolor=color, alpha=0.2, zorder=30))
    ax.add_patch(mpatches.Ellipse((px,py), rx*0.7, ry*0.7, facecolor=color, alpha=0.45, zorder=31))


def draw_dock(ax):
    """Draw Step isometric render on the given axes."""
    S = 0.025

    # Base + riser
    draw_block(ax, 0, 165*S, 0, 100*S, 0, 3*S,  walnut_top=False, zbase=1)
    draw_block(ax, 0, 165*S, 0, 100*S, 3*S, 25*S, walnut_top=False, zbase=2)

    # LED diffuser strip
    ax.add_patch(face_front(17.5*S, 147.5*S, 0, 26*S, 33*S,
                             facecolor="#334466", edgecolor="#446688", lw=0.3, alpha=0.7, zorder=3))
    # LED dots on diffuser
    for gx_mm, gc in [(40, C_GLOW_1), (65, C_GLOW_2), (90, C_GLOW_3), (120, C_GLOW_A), (140, C_GLOW_B)]:
        px, py = iso(gx_mm*S, 0, 29*S)
        ax.add_patch(mpatches.Ellipse((px,py), 0.09, 0.04, facecolor=gc, alpha=0.6, zorder=4))

    # Step 1
    draw_block(ax, 0, 165*S, 0, 100*S, 25*S, 40*S, walnut_top=True, zbase=5)
    # Zone 1 pad + glow
    ax.add_patch(face_top(57*S, 32*S, 108*S, 68*S, 40*S,
                           facecolor="#1a1a1a", edgecolor="#333", lw=0.2, zorder=6))
    draw_glow(ax, 82.5*S, 50*S, 40*S, C_GLOW_1, rx=0.10, ry=0.06)

    # Step 2
    draw_block(ax, 17.5*S, 147.5*S, 0, 100*S, 40*S, 55*S, walnut_top=True, zbase=7)
    ax.add_patch(face_top(50*S, 25*S, 115*S, 75*S, 55*S,
                           facecolor="#1a1a1a", edgecolor="#333", lw=0.2, zorder=8))
    draw_glow(ax, 82.5*S, 50*S, 55*S, C_GLOW_2, rx=0.09, ry=0.055)

    # Step 3
    draw_block(ax, 35*S, 130*S, 20*S, 100*S, 55*S, 70*S, walnut_top=True, zbase=9)
    ax.add_patch(face_top(55*S, 32*S, 110*S, 87*S, 70*S,
                           facecolor="#1a1a1a", edgecolor="#333", lw=0.2, zorder=10))
    draw_glow(ax, 82.5*S, 60*S, 70*S, C_GLOW_3, rx=0.08, ry=0.05)

    # Rear USB-C ports
    for px_mm, col in [(120, C_GLOW_A), (140, C_GLOW_B)]:
        px, py = iso(px_mm*S, 100*S, 15*S)
        ax.add_patch(mpatches.Circle((px, py), 0.03, facecolor=col, alpha=0.7, zorder=15))

    # Zone labels on left side
    label_data = [
        (82.5*S, 50*S, 42*S, "① PHONE  Qi2", C_GLOW_1),
        (82.5*S, 50*S, 57*S, "② BUDS    Qi",  C_GLOW_2),
        (82.5*S, 60*S, 72*S, "③ WATCH   5W",  C_GLOW_3),
    ]
    for lx, ly, lz, text, col in label_data:
        px, py = iso(lx, ly, lz)
        epx, epy = px - 0.28, py + 0.04
        ax.annotate("", xy=(px,py), xytext=(epx,epy),
                    arrowprops=dict(arrowstyle="-", color=col, lw=0.6), zorder=50)
        ax.text(epx-0.02, epy, text, color=col, fontsize=5.5, va="center", ha="right",
                fontfamily="monospace", zorder=51)

    # Fit view
    pts = [(0,0,0),(165*S,0,0),(0,100*S,0),(165*S,100*S,0),(82.5*S,60*S,80*S)]
    xs = [iso(*p)[0] for p in pts]
    ys = [iso(*p)[1] for p in pts]
    cx = (min(xs)+max(xs))/2
    cy = (min(ys)+max(ys))/2
    span = max(max(xs)-min(xs), max(ys)-min(ys)) * 0.65
    ax.set_xlim(cx - span, cx + span)
    ax.set_ylim(cy - span*0.55, cy + span*0.95)


def draw_spec_panel(ax):
    """Draw spec text panel on right axes."""
    ax.set_facecolor(C_PANEL)
    ax.axis("off")

    import matplotlib.lines as mlines
    def rule(y_axes, lw=0.5, color=C_DIVIDER):
        line = mlines.Line2D([0.05, 0.95], [y_axes, y_axes],
                             color=color, lw=lw, transform=ax.transAxes)
        ax.add_line(line)

    # Title
    ax.text(0.06, 0.91, "STEP", color=C_TEXT, fontsize=22, fontweight="bold",
            transform=ax.transAxes, va="top", fontfamily="monospace")
    ax.text(0.85, 0.91, "$89", color=C_TEXT, fontsize=18, fontweight="bold",
            transform=ax.transAxes, va="top", ha="right", fontfamily="monospace")
    ax.text(0.06, 0.82, "Charge everything. Touch nothing.",
            color=C_SUBTEXT, fontsize=7, transform=ax.transAxes, va="top", fontfamily="monospace")

    rule(0.79)

    # Zones table
    zones = [
        ("1", "PHONE",   "20W", "Qi2",         C_GLOW_1),
        ("2", "BUDS",    " 5W", "Qi",           C_GLOW_2),
        ("3", "WATCH",   " 5W", "Apple + Qi",   C_GLOW_3),
        ("4", "USB-C A", "60W", "Port A",       C_GLOW_A),
        ("5", "USB-C B", "30W", "Port B",       C_GLOW_B),
    ]

    y_start = 0.74
    row_h   = 0.11
    for i, (num, name, watts, std, col) in enumerate(zones):
        y = y_start - i * row_h
        ax.text(0.06, y, num,   color=col,       fontsize=9,  transform=ax.transAxes, va="center", fontfamily="monospace")
        ax.text(0.17, y, name,  color=C_TEXT,    fontsize=9,  transform=ax.transAxes, va="center", fontfamily="monospace")
        ax.text(0.62, y, watts, color=C_TEXT,    fontsize=12, fontweight="bold",
                transform=ax.transAxes, va="center", ha="right", fontfamily="monospace")
        ax.text(0.66, y, std,   color=C_SUBTEXT, fontsize=7.5, transform=ax.transAxes, va="center", fontfamily="monospace")

    rule_y = y_start - len(zones) * row_h + 0.02
    rule(rule_y)

    # Materials + size
    detail_y = rule_y - 0.06
    details = [
        "Walnut + matte black ABS",
        "165 x 100 x 70mm",
        "65W USB-C brick included",
        "Bring your own USB-C cables",
    ]
    for j, line in enumerate(details):
        y = detail_y - j * 0.09
        ax.text(0.06, y, line, color=C_SUBTEXT, fontsize=7.5,
                transform=ax.transAxes, va="center", fontfamily="monospace")

    footer_y = detail_y - len(details) * 0.09 - 0.04
    rule(footer_y)

    # Footer
    ax.text(0.06, footer_y - 0.06, "epitomecharge.com  ·  PRE-ORDER",
            color=C_ACCENT, fontsize=7.5, transform=ax.transAxes, va="center",
            fontfamily="monospace")


def main():
    fig = plt.figure(figsize=(W_IN, H_IN), facecolor=C_BG)

    # Two panels: left 55%, right 45%
    gs = gridspec.GridSpec(1, 2, figure=fig, width_ratios=[55, 45],
                           left=0.0, right=1.0, top=1.0, bottom=0.0, wspace=0.0)

    ax_left  = fig.add_subplot(gs[0])
    ax_right = fig.add_subplot(gs[1])

    # Left panel — dock render
    ax_left.set_facecolor(C_BG)
    ax_left.set_aspect("equal")
    ax_left.axis("off")
    draw_dock(ax_left)

    # Right panel — spec
    draw_spec_panel(ax_right)

    fig.savefig(OUT, dpi=DPI, bbox_inches="tight", facecolor=C_BG)
    plt.close(fig)
    print(f"Product sheet saved: {OUT}")


if __name__ == "__main__":
    main()
