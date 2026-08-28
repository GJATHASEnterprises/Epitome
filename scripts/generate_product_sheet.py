#!/usr/bin/env python3
"""Penta Dock — single-page marketing product sheet.

One dock perspective view (left 55%) + one spec panel (right 45%).
Clean, dark, readable at 1200×800px — suitable for Reddit or Shopify.

Output:
    assets/penta-dock-product-sheet.png  (1200×800 px, dpi=150)
"""
from __future__ import annotations

import math
import shutil
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyBboxPatch
from matplotlib.lines import Line2D

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH        = ROOT / "assets" / "penta-dock-product-sheet.png"
COMPAT_OUTPUT_PATH = ROOT / "assets" / "quad-dock-product-sheet.png"

# Canvas: 1200×800 px at 150 dpi → 8×5.333 inches
W_IN, H_IN = 8.0, 16.0 / 3.0
DPI = 150

# ── Palette ──────────────────────────────────────────────────────────────────
C_BG       = "#111111"
C_PANEL    = "#1a1a1a"
C_BODY     = "#2a2a2a"
C_STEP     = "#333333"
C_SILICONE = "#1f1f1f"
C_WHITE    = "#ffffff"
C_LGREY    = "#cccccc"
C_GREY     = "#888888"
C_DGREY    = "#444444"
C_BLUE     = "#3399ff"
C_PURPLE   = "#9966ff"
C_GREEN    = "#33cc66"
C_ORANGE   = "#ff8800"
C_AMBER    = "#ffb347"

# ── Isometric projection helpers ─────────────────────────────────────────────
_ISO_A = math.radians(30)
_COS   = math.cos(_ISO_A)
_SIN   = math.sin(_ISO_A)


def iso(x: float, y: float, z: float = 0.0,
        scale: float = 1.0, ox: float = 0.0, oy: float = 0.0):
    """Dock 3-D coords → 2-D canvas coords."""
    px = (x - y) * _COS * scale + ox
    py = (x + y) * _SIN * scale - z * scale + oy
    return px, py


def ipoly(ax, pts3d, fc, ec=None, lw=0.5, alpha=1.0, zorder=3,
          scale=1.0, ox=0.0, oy=0.0):
    pts2d = [iso(*p, scale=scale, ox=ox, oy=oy) for p in pts3d]
    patch = Polygon(pts2d, closed=True, facecolor=fc,
                    edgecolor=ec or fc, linewidth=lw, alpha=alpha, zorder=zorder)
    ax.add_patch(patch)


def ibox(ax, x0, x1, y0, y1, z0, z1,
         ct=C_BODY, cr=None, cf=None, z=3, scale=1.0, ox=0.0, oy=0.0):
    """Draw top, right, and front faces of a box in iso space."""
    cr = cr or "#1e1e1e"
    cf = cf or "#1c1c1c"
    # top
    ipoly(ax, [(x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)],
          ct, z=z + 2, scale=scale, ox=ox, oy=oy)
    # right face
    ipoly(ax, [(x1, y0, z0), (x1, y1, z0), (x1, y1, z1), (x1, y0, z1)],
          cr, z=z + 1, scale=scale, ox=ox, oy=oy)
    # front face
    ipoly(ax, [(x0, y0, z0), (x1, y0, z0), (x1, y0, z1), (x0, y0, z1)],
          cf, z=z, scale=scale, ox=ox, oy=oy)


def glow_poly(ax, pts3d, color, layers=5, max_alpha=0.22, zorder=1,
              scale=1.0, ox=0.0, oy=0.0):
    verts = [iso(*p, scale=scale, ox=ox, oy=oy) for p in pts3d]
    cx = sum(v[0] for v in verts) / len(verts)
    cy = sum(v[1] for v in verts) / len(verts)
    for i in range(layers, 0, -1):
        s = 1.0 + i * 0.07
        expanded = [((v[0] - cx) * s + cx, (v[1] - cy) * s + cy) for v in verts]
        ax.add_patch(Polygon(expanded, closed=True, facecolor=color,
                             edgecolor="none",
                             alpha=max_alpha * (i / layers) ** 1.5,
                             zorder=zorder))


# ── Draw the dock diagram in the given axes ──────────────────────────────────
def draw_dock(ax: plt.Axes) -> None:
    ax.set_facecolor(C_BG)
    ax.axis("off")

    # Canvas is ax data coords 0..1 (we use transAxes), but we'll work in
    # figure inches via a fixed scale + origin offset.
    # The dock diagram is centred around (ox, oy) in data units.
    sc   = 0.048    # scale: 1 dock-unit ≈ 0.048 inches on a ~4.4in wide panel
    OX   = 0.48     # origin x in axes fraction
    OY   = 0.54     # origin y in axes fraction

    # Dock dimensions (dock units, 1 unit ≈ 50mm)
    BW, BD, BH = 5.0, 2.0, 0.12   # base footprint & height

    def p(x, y, z=0.0):
        """Convert dock units → axes fraction coords."""
        px, py = iso(x, y, z, scale=sc)
        return OX + px, OY + py

    def ipoly_ax(pts3d, fc, ec=None, lw=0.5, alpha=1.0, z=3):
        pts2d = [p(*pt) for pt in pts3d]
        patch = Polygon(pts2d, closed=True, facecolor=fc,
                        edgecolor=ec or fc, linewidth=lw, alpha=alpha, zorder=z,
                        transform=ax.transAxes)
        ax.add_patch(patch)

    def ibox_ax(x0, x1, y0, y1, z0, z1, ct=C_BODY, cr="#1e1e1e", cf="#1c1c1c", z=3):
        ipoly_ax([(x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)],
                 ct, z=z + 2)
        ipoly_ax([(x1, y0, z0), (x1, y1, z0), (x1, y1, z1), (x1, y0, z1)],
                 cr, z=z + 1)
        ipoly_ax([(x0, y0, z0), (x1, y0, z0), (x1, y0, z1), (x0, y0, z1)],
                 cf, z=z)

    def glow_ax(pts3d, color, layers=5, max_alpha=0.22, z=1):
        verts = [p(*pt) for pt in pts3d]
        cx = sum(v[0] for v in verts) / len(verts)
        cy = sum(v[1] for v in verts) / len(verts)
        for i in range(layers, 0, -1):
            s = 1.0 + i * 0.07
            exp = [((v[0] - cx) * s + cx, (v[1] - cy) * s + cy) for v in verts]
            ax.add_patch(Polygon(exp, closed=True, facecolor=color,
                                 edgecolor="none",
                                 alpha=max_alpha * (i / layers) ** 1.5,
                                 zorder=z, transform=ax.transAxes))

    # Drop shadow
    glow_ax([(-2.7, -1.2, 0), (2.7, -1.2, 0), (2.7, 1.2, 0), (-2.7, 1.2, 0)],
            "#000000", layers=8, max_alpha=0.45, z=0)

    # Base body
    ibox_ax(-BW/2, BW/2, -BD/2, BD/2, 0, BH, ct="#252525", cr="#1a1a1a", cf="#181818", z=2)

    # Front fascia strip
    ibox_ax(-BW/2, BW/2, -BD/2, -BD/2 + 0.06, 0, 0.4,
            ct="#222222", cr="#1a1a1a", cf="#161616", z=4)

    # ── Three-step staircase ─────────────────────────────────────────────────
    # Steps rise from Z=BH upward.  Step heights (above base):
    SH = 0.30   # each step height in dock units (≈15mm)
    steps = [
        (-1.8,  1.8, -BD/2, BD/2, BH,            BH + SH    ),  # Step 1
        (-1.4,  1.4, -BD/2, BD/2, BH + SH,       BH + 2*SH  ),  # Step 2
        (-1.0,  1.0, -BD/2 + 0.4, BD/2, BH + 2*SH, BH + 3*SH),  # Step 3 setback
    ]
    step_tops = ["#313131", "#353535", "#383838"]
    for (x0, x1, y0, y1, z0, z1), ct in zip(steps, step_tops):
        ibox_ax(x0, x1, y0, y1, z0, z1, ct=ct, cr="#202020", cf="#1e1e1e", z=5)

    # ── Zone pad surfaces ─────────────────────────────────────────────────────
    pads = [
        # Zone 1 phone pad: 160×100mm on Step 1 (180mm)
        (-1.6, 1.6, -BD/2 + 0.06, BD/2 - 0.06, BH + SH + 0.004),
        # Zone 2 buds/phone 90×70mm on Step 2 (140mm)
        (-0.9, 0.9, -BD/2 + 0.2,  BD/2 - 0.2,  BH + 2*SH + 0.004),
        # Zone 3 watch cradle on Step 3
        (-0.5, 0.5, -BD/2 + 0.5,  BD/2 - 0.2,  BH + 3*SH + 0.004),
    ]
    pad_colors = [C_BLUE, C_PURPLE, C_GREEN]
    for (x0, x1, y0, y1, z), pc in zip(pads, pad_colors):
        ipoly_ax([(x0, y0, z), (x1, y0, z), (x1, y1, z), (x0, y1, z)],
                 C_SILICONE, ec=pc, lw=0.8, z=7)

    # ── Laptop slot (left) ───────────────────────────────────────────────────
    lx0, lx1 = -BW/2 - 0.1, -BW/2 + 0.1
    ly0, ly1 = -1.8, 1.8
    lz0, lz1 = BH, BH + 1.9   # 95mm ≈ 1.9 units
    ibox_ax(lx0, lx1, ly0, ly1, lz0, lz1,
            ct=C_ORANGE, cr="#3a2000", cf="#3a2000", z=6)
    ipoly_ax([(lx0, ly0, lz0 + 0.05), (lx1, ly0, lz0 + 0.05),
              (lx1, ly1, lz0 + 0.05), (lx0, ly1, lz0 + 0.05)],
             C_SILICONE, ec=C_ORANGE, lw=0.5, z=7)

    # ── Tablet slot (right) ──────────────────────────────────────────────────
    rx0, rx1 = BW/2 - 0.1, BW/2 + 0.1
    ry0, ry1 = -1.3, 1.3
    rz0, rz1 = BH, BH + 1.6   # 80mm
    ibox_ax(rx0, rx1, ry0, ry1, rz0, rz1,
            ct=C_BLUE, cr="#001a33", cf="#001a33", z=6)
    ipoly_ax([(rx0, ry0, rz0 + 0.05), (rx1, ry0, rz0 + 0.05),
              (rx1, ry1, rz0 + 0.05), (rx0, ry1, rz0 + 0.05)],
             C_SILICONE, ec=C_BLUE, lw=0.5, z=7)

    # ── Rear-left IEC inlet ──────────────────────────────────────────────────
    ipoly_ax([(-BW/2 + 0.05, BD/2, 0.12), (-BW/2 + 0.6, BD/2, 0.12),
              (-BW/2 + 0.6, BD/2, 0.44), (-BW/2 + 0.05, BD/2, 0.44)],
             C_PURPLE, ec=C_PURPLE, lw=0.7, alpha=0.9, z=6)

    # ── LED strip front ──────────────────────────────────────────────────────
    led_seg = [C_BLUE, C_PURPLE, C_GREEN, C_ORANGE, C_BLUE]
    seg_w = BW / len(led_seg)
    LY  = -BD/2 - 0.01
    LZ0 = 0.03
    LZ1 = 0.12
    for i, lc in enumerate(led_seg):
        xs = -BW/2 + i * seg_w
        xe = xs + seg_w
        pts = [(xs, LY, LZ0), (xe, LY, LZ0), (xe, LY, LZ1), (xs, LY, LZ1)]
        glow_ax(pts, lc, layers=4, max_alpha=0.4, z=2)
        ipoly_ax(pts, lc, alpha=0.95, z=8)

    # ── Zone labels ──────────────────────────────────────────────────────────
    def label(xd, yd, zd, txt, color, fs=6.5):
        px, py = p(xd, yd, zd)
        ax.text(px, py, txt, color=color, fontsize=fs, ha="center",
                va="bottom", fontweight="bold", zorder=15,
                multialignment="center", transform=ax.transAxes,
                bbox=dict(boxstyle="round,pad=0.12", fc=C_BG, ec=color,
                          lw=0.6, alpha=0.9))

    label(-0.8, -1.0, BH + SH + 0.02,     "① PHONE\n20W Qi2", C_BLUE)
    label( 0.5, -0.8, BH + 2*SH + 0.02,   "② BUDS/PHONE\n20W Qi", C_PURPLE)
    label( 1.05,-0.7, BH + 3*SH + 0.02,   "③ WATCH\n5W", C_GREEN)

    # Laptop label (left)
    lbx, lby = p(-BW/2 - 0.55, 0, BH + 0.95)
    ax.text(lbx, lby, "④ LAPTOP\n100W USB-C", color=C_ORANGE, fontsize=6.5,
            ha="center", va="center", fontweight="bold", zorder=15,
            multialignment="center", transform=ax.transAxes,
            bbox=dict(boxstyle="round,pad=0.12", fc=C_BG, ec=C_ORANGE,
                      lw=0.6, alpha=0.9))
    # Arrow to slot
    tgx, tgy = p(-BW/2 + 0.05, 0, BH + 0.95)
    ax.annotate("", xy=(tgx, tgy), xytext=(lbx, lby),
                arrowprops=dict(arrowstyle="-|>", color=C_ORANGE, lw=0.7),
                xycoords="axes fraction", textcoords="axes fraction",
                zorder=15)

    # Tablet label (right)
    rbx, rby = p(BW/2 + 0.55, 0, BH + 0.80)
    ax.text(rbx, rby, "⑤ TABLET\n45W USB-C", color=C_BLUE, fontsize=6.5,
            ha="center", va="center", fontweight="bold", zorder=15,
            multialignment="center", transform=ax.transAxes,
            bbox=dict(boxstyle="round,pad=0.12", fc=C_BG, ec=C_BLUE,
                      lw=0.6, alpha=0.9))
    tgx2, tgy2 = p(BW/2 - 0.05, 0, BH + 0.80)
    ax.annotate("", xy=(tgx2, tgy2), xytext=(rbx, rby),
                arrowprops=dict(arrowstyle="-|>", color=C_BLUE, lw=0.7),
                xycoords="axes fraction", textcoords="axes fraction",
                zorder=15)


# ── Draw the spec panel ───────────────────────────────────────────────────────
def draw_spec(ax: plt.Axes) -> None:
    ax.set_facecolor(C_PANEL)
    ax.axis("off")

    x = 0.06
    y = 0.96
    lh_big  = 0.115   # line height for zone rows
    lh_sml  = 0.068

    def t(text, color=C_LGREY, fs=8.5, weight="normal", dy=None):
        nonlocal y
        ax.text(x, y, text, transform=ax.transAxes, ha="left", va="top",
                color=color, fontsize=fs, fontweight=weight)
        y -= dy if dy is not None else lh_sml

    # ── Zone list ────────────────────────────────────────────────────────────
    zones = [
        ("①", "PHONE",      "20W",  "Qi2",      C_BLUE),
        ("②", "BUDS/PHONE", "20W",  "Qi",        C_PURPLE),
        ("③", "WATCH",      " 5W",  "",          C_GREEN),
        ("④", "LAPTOP",     "100W", "USB-C PD",  C_ORANGE),
        ("⑤", "TABLET",     " 45W", "USB-C PD",  C_BLUE),
    ]
    for (num, name, watts, std, col) in zones:
        # Coloured circle number
        ax.text(x, y, num, transform=ax.transAxes, ha="left", va="top",
                color=col, fontsize=11, fontweight="bold")
        # Zone name
        ax.text(x + 0.13, y, name, transform=ax.transAxes, ha="left", va="top",
                color=C_WHITE, fontsize=10, fontweight="bold")
        # Wattage (hero number)
        ax.text(x + 0.53, y + 0.005, watts, transform=ax.transAxes,
                ha="left", va="top", color=col, fontsize=13, fontweight="bold")
        # Standard
        if std:
            ax.text(x + 0.74, y + 0.01, std, transform=ax.transAxes,
                    ha="left", va="top", color=C_GREY, fontsize=8)
        y -= lh_big

    y -= 0.01  # small gap

    # ── Headline stat ────────────────────────────────────────────────────────
    ax.text(x, y, "190W TOTAL OUTPUT", transform=ax.transAxes,
            ha="left", va="top", color=C_WHITE, fontsize=16, fontweight="bold")
    y -= 0.13

    # ── Technical detail ─────────────────────────────────────────────────────
    t("Mean Well LRS-200-24 · 201W PSU", color=C_GREY, fs=7.5)
    t("ATtiny85 · 185W soft cap",         color=C_GREY, fs=7.5)
    y -= 0.02
    t("250 × 100 × 100 mm · Full ABS",   color=C_LGREY, fs=8.0)
    t("Matte Black · Obsidian finish",    color=C_LGREY, fs=8.0)


# ── Main ─────────────────────────────────────────────────────────────────────
def build_figure() -> None:
    fig = plt.figure(figsize=(W_IN, H_IN), dpi=DPI, facecolor=C_BG)

    # Header bar (top strip)
    fig.text(0.03, 0.955, "PENTA DOCK",
             color=C_WHITE, fontsize=32, fontweight="bold", va="top",
             fontfamily="DejaVu Sans")
    fig.text(0.03, 0.875, "One dock. Every device.",
             color=C_GREY, fontsize=13, va="top",
             fontfamily="DejaVu Sans")
    fig.text(0.97, 0.955, "PRE-ORDER  ·  $249",
             color=C_WHITE, fontsize=14, fontweight="bold",
             ha="right", va="top", fontfamily="DejaVu Sans")
    fig.text(0.97, 0.875, "epitomecharge.com",
             color=C_GREY, fontsize=10, ha="right", va="top",
             fontfamily="DejaVu Sans")

    # Main content area: two columns
    # Left dock view: [0.01, 0.01, 0.54, 0.80] in figure fraction
    ax_dock = fig.add_axes([0.01, 0.09, 0.55, 0.77])
    # Right spec panel: [0.56, 0.09, 0.43, 0.77]
    ax_spec = fig.add_axes([0.57, 0.09, 0.41, 0.77])

    # Spec panel background
    ax_spec.set_facecolor(C_PANEL)
    for sp in ax_spec.spines.values():
        sp.set_edgecolor(C_DGREY)
        sp.set_linewidth(0.8)

    draw_dock(ax_dock)
    draw_spec(ax_spec)

    # Bottom bar
    bar_ax = fig.add_axes([0.0, 0.0, 1.0, 0.08])
    bar_ax.set_facecolor("#0a0a0a")
    bar_ax.axis("off")
    bar_ax.text(0.03, 0.5, "epitomecharge.com",
                transform=bar_ax.transAxes, color=C_GREY, fontsize=9,
                va="center", fontfamily="DejaVu Sans")
    bar_ax.text(0.5, 0.5, "PRE-ORDER — $249",
                transform=bar_ax.transAxes, color=C_WHITE, fontsize=11,
                fontweight="bold", ha="center", va="center",
                fontfamily="DejaVu Sans")
    bar_ax.text(0.97, 0.5, "2026",
                transform=bar_ax.transAxes, color=C_GREY, fontsize=9,
                ha="right", va="center", fontfamily="DejaVu Sans")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT_PATH, dpi=DPI, facecolor=C_BG, bbox_inches="tight",
                pad_inches=0.02)
    plt.close(fig)


if __name__ == "__main__":
    build_figure()
    shutil.copy2(OUTPUT_PATH, COMPAT_OUTPUT_PATH)
    print(f"✓ Product sheet generated: {OUTPUT_PATH.relative_to(ROOT)}")
