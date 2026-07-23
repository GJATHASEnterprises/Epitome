#!/usr/bin/env python3
"""
Quad-Dock — Comprehensive Multi-View Technical Product Sheet
Generates assets/quad-dock-product-sheet.png at 7200×5400px (dpi=300, figsize=(24,18)).
Uses only matplotlib, numpy, math, pathlib.
"""
from __future__ import annotations

import math
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import (
    Arc, Circle, FancyArrowPatch, FancyBboxPatch, Polygon, Rectangle,
    Wedge, Ellipse,
)
from matplotlib.path import Path as MplPath
from matplotlib.patches import PathPatch
from matplotlib.collections import LineCollection


# ─── Output path ────────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = ROOT / "assets" / "quad-dock-product-sheet.png"

# ─── Colour palette ─────────────────────────────────────────────────────────
PAGE_BG      = "#0d0d1a"   # deep navy/charcoal page background
PANEL_BG     = "#1a1a2e"   # panel background
PANEL_BORDER = "#2a2a4a"   # panel border
TEXT_WHITE   = "#ffffff"
TEXT_LIGHT   = "#cccccc"
TEXT_DIM     = "#888899"
GOLD         = "#c8a84b"   # accent / title colour
RED_CONF     = "#cc3333"

# Zone accent colours
Z1_BLUE   = "#3a7bd5"   # Phone
Z2_PURPLE = "#9b59b6"   # Buds
Z3_GREEN  = "#27ae60"   # Watch
Z4_ORANGE = "#e67e22"   # Laptop

# Material colours
ALU_TOP  = "#8a9ba8"   # brushed aluminium
ABS_BODY = "#1a1a1a"   # dark ABS
LED_COL  = "#ffb347"   # warm amber LED

ZONE_COLS = [Z1_BLUE, Z2_PURPLE, Z3_GREEN, Z4_ORANGE]


# ─── Physical constants (mm) ─────────────────────────────────────────────────
L   = 300.0   # length (Y-axis in top view)
FW  = 110.0   # front width
RW  = 140.0   # rear width
FH  = 12.0    # front height
RH  = 22.0    # rear height
CR  = 20.0    # corner radius

def hw(y: float) -> float:
    """Half-width at Y position."""
    return 55.0 + 15.0 * (y / 300.0)

def body_h(y: float) -> float:
    """Body height at Y position."""
    return 12.0 + 10.0 * (y / 300.0)


# ─── Helper: rounded trapezoid path ─────────────────────────────────────────
def rounded_trapezoid_path(pts: np.ndarray, radius: float) -> MplPath:
    """Build a rounded-corner closed path through pts."""
    pts = np.asarray(pts, dtype=float)
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


def _trapezoid_pts() -> np.ndarray:
    """Standard top-view trapezoid corners in mm coords (centred on X=0, Y=0..300)."""
    return np.array([[-55, 0], [55, 0], [70, 300], [-70, 300]], dtype=float)


def _panel_box(ax: plt.Axes, title: str) -> None:
    """Style an axis as a dark panel and add title."""
    ax.set_facecolor(PANEL_BG)
    for spine in ax.spines.values():
        spine.set_edgecolor(PANEL_BORDER)
        spine.set_linewidth(1.5)
    ax.text(0.01, 0.99, title, transform=ax.transAxes,
            ha="left", va="top", fontsize=8, color=GOLD,
            fontweight="bold", fontfamily="monospace")


def _dim_arrow(ax: plt.Axes, x1: float, y1: float, x2: float, y2: float,
               label: str, offset: tuple = (0, 0), fontsize: float = 6.5,
               color: str = TEXT_DIM) -> None:
    """Draw a dimension annotation with double-ended arrow and label."""
    mx, my = (x1 + x2) / 2 + offset[0], (y1 + y2) / 2 + offset[1]
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="<->", color=color,
                                lw=0.8, mutation_scale=6))
    ax.text(mx, my, label, ha="center", va="center",
            fontsize=fontsize, color=color,
            bbox=dict(facecolor=PANEL_BG, edgecolor="none", pad=0.5))


def _callout(ax: plt.Axes, xy: tuple, xytext: tuple, label: str,
             color: str = TEXT_DIM, fontsize: float = 6) -> None:
    ax.annotate(label, xy=xy, xytext=xytext,
                arrowprops=dict(arrowstyle="->", color=color, lw=0.7,
                                connectionstyle="arc3,rad=0.1"),
                color=color, fontsize=fontsize, ha="center",
                bbox=dict(facecolor=PANEL_BG, edgecolor=color, pad=1.5,
                          linewidth=0.5))


# ════════════════════════════════════════════════════════════════════════════
#  VIEW 1 — TOP-DOWN VIEW
# ════════════════════════════════════════════════════════════════════════════
def draw_top_view(ax: plt.Axes) -> None:
    # Illustration uses wider body so zones fit comfortably (illustration only, not physical spec)
    ILL_FHW = 100.0   # illustration front half-width (200mm total front)
    ILL_RHW = 120.0   # illustration rear half-width (240mm total rear)

    def ill_hw(y: float) -> float:
        return ILL_FHW + (ILL_RHW - ILL_FHW) * (y / 300.0)

    ill_pts = np.array([[-ILL_FHW, 0], [ILL_FHW, 0], [ILL_RHW, 300], [-ILL_RHW, 300]], dtype=float)

    ax.set_xlim(-170, 200)
    ax.set_ylim(-35, 360)
    ax.set_aspect("equal")
    ax.axis("off")
    _panel_box(ax, "TOP VIEW — 1:3 SCALE")

    # ── Dock body fill ──
    body = PathPatch(rounded_trapezoid_path(ill_pts, radius=CR),
                     facecolor="#252535", edgecolor="#4a4a6a", linewidth=1.5, zorder=2)
    ax.add_patch(body)

    # ── Top plate (1.5mm aluminium) — same outline, slightly lighter ──
    plate = PathPatch(rounded_trapezoid_path(ill_pts, radius=CR),
                      facecolor="#2e3040", edgecolor=GOLD, linewidth=0.8,
                      alpha=0.35, zorder=3)
    ax.add_patch(plate)

    # ── Centerline ──
    ax.plot([0, 0], [-5, 305], color=TEXT_DIM, linewidth=0.6,
            linestyle="--", dashes=(4, 4), zorder=2, alpha=0.5)

    # ── Y grid lines at zone centres ──
    for yg, col in [(70, TEXT_DIM), (150, TEXT_DIM), (225, Z3_GREEN), (294, Z4_ORANGE)]:
        xw = ill_hw(yg)
        ax.plot([-xw, xw], [yg, yg], color=col, linewidth=0.4,
                linestyle="--", dashes=(3, 5), alpha=0.3, zorder=2)

    # LED bar — inside front edge, full width clipped to illustration front edge
    ill_front_hw = ILL_FHW  # 100mm half-width at Y=0
    ax.add_patch(Rectangle((-ill_front_hw, 1), ill_front_hw * 2, 6,
                            facecolor="#221800", edgecolor="#443300", linewidth=0.8, zorder=4))
    # 4 equal segments across full front width
    seg_w = (ill_front_hw * 2) / 4  # 50mm each
    seg_centres = [-75, -25, 25, 75]  # centred in each quarter
    for lx, lc in zip(seg_centres, [Z1_BLUE, Z2_PURPLE, Z3_GREEN, Z4_ORANGE]):
        ax.add_patch(Rectangle((lx - seg_w / 2 + 1, 1.5), seg_w - 2, 5,
                                facecolor=lc, alpha=0.85, linewidth=0, zorder=5))
    # Dividers
    for div_x in [-50, 0, 50]:
        ax.plot([div_x, div_x], [1, 7], color="#111122", linewidth=1.0, zorder=6)
    # Glow
    ax.plot([-ill_front_hw + 2, ill_front_hw - 2], [4, 4],
            color="#ffb347", linewidth=2.0, alpha=0.7, zorder=6)

    ax.text(0, -5, "WS2812B LED STATUS BAR  ·  4-ZONE  ·  290×8mm",
            ha="center", va="top", fontsize=5.5, color="#ffb347", zorder=6)

    # ── Zone 1 — Phone Qi dish ──
    z1_dish = FancyBboxPatch((-45 - 40, 70 - 27.5), 80, 55,
                              boxstyle="round,pad=0,rounding_size=10",
                              facecolor="#1c2a3a", edgecolor=Z1_BLUE,
                              linewidth=1.4, zorder=6)
    ax.add_patch(z1_dish)
    # Silicone insert
    z1_si = FancyBboxPatch((-45 - 39, 70 - 26.5), 78, 53,
                            boxstyle="round,pad=0,rounding_size=9",
                            facecolor="#162030", edgecolor=Z1_BLUE,
                            linewidth=0.6, linestyle="--", zorder=7, alpha=0.7)
    ax.add_patch(z1_si)
    # Qi coil circle
    ax.add_patch(Circle((-45, 70), 27, facecolor="none",
                         edgecolor=Z1_BLUE, linewidth=0.5, linestyle=":",
                         alpha=0.5, zorder=7))
    # N52 magnets ring
    ax.add_patch(Circle((-45, 70), 27, facecolor="none",
                         edgecolor="#4488ff", linewidth=1.0, alpha=0.25, zorder=7))
    ax.text(-45, 70, "PHONE\nQi2 · 15W", ha="center", va="center",
            fontsize=6.5, color=TEXT_WHITE, fontweight="bold", zorder=8)
    ax.text(-45, 63, "Ø54mm coil · N52 ring", ha="center", va="top",
            fontsize=4.5, color=Z1_BLUE, zorder=8)
    # Phone silhouette in Zone 1
    ax.add_patch(FancyBboxPatch((-45 - 9, 70 - 18), 18, 32, boxstyle="round,pad=0,rounding_size=3", facecolor="#0d1520", edgecolor=Z1_BLUE, linewidth=0.8, alpha=0.55, zorder=7))
    ax.add_patch(Circle((-45, 70 - 14), 2.5, facecolor="#0d1520", edgecolor=Z1_BLUE, linewidth=0.5, alpha=0.55, zorder=7))
    ax.add_patch(Rectangle((-45 - 4, 70 + 12), 8, 1.5, facecolor=Z1_BLUE, alpha=0.4, linewidth=0, zorder=7))

    # ── Zone 2 — Buds Qi dish ──
    z2_dish = FancyBboxPatch((45 - 32.5, 70 - 27.5), 65, 55,
                              boxstyle="round,pad=0,rounding_size=10",
                              facecolor="#251a35", edgecolor=Z2_PURPLE,
                              linewidth=1.4, zorder=6)
    ax.add_patch(z2_dish)
    z2_si = FancyBboxPatch((45 - 31.5, 70 - 26.5), 63, 53,
                            boxstyle="round,pad=0,rounding_size=9",
                            facecolor="#1e1428", edgecolor=Z2_PURPLE,
                            linewidth=0.6, linestyle="--", zorder=7, alpha=0.7)
    ax.add_patch(z2_si)
    ax.add_patch(Circle((45, 70), 27, facecolor="none",
                         edgecolor=Z2_PURPLE, linewidth=0.5, linestyle=":",
                         alpha=0.5, zorder=7))
    ax.text(45, 70, "BUDS\nQi · 5W", ha="center", va="center",
            fontsize=6.5, color=TEXT_WHITE, fontweight="bold", zorder=8)
    ax.text(45, 63, "Ø54mm coil", ha="center", va="top",
            fontsize=4.5, color=Z2_PURPLE, zorder=8)
    # AirPods case silhouette in Zone 2
    ax.add_patch(FancyBboxPatch((45 - 10, 70 - 13), 20, 24, boxstyle="round,pad=0,rounding_size=5", facecolor="#150d20", edgecolor=Z2_PURPLE, linewidth=0.8, alpha=0.55, zorder=7))
    ax.add_patch(Circle((45 - 4, 70 - 4), 3.5, facecolor="#1a1030", edgecolor=Z2_PURPLE, linewidth=0.5, alpha=0.6, zorder=8))
    ax.add_patch(Circle((45 + 4, 70 - 4), 3.5, facecolor="#1a1030", edgecolor=Z2_PURPLE, linewidth=0.5, alpha=0.6, zorder=8))

    # ── Zone 3 — Watch cradle pod ──
    z3 = Circle((-30, 225), 25, facecolor="#1a2a1a",
                 edgecolor=Z3_GREEN, linewidth=1.4, zorder=6)
    ax.add_patch(z3)
    # Inner puck (tilted ellipse)
    ax.add_patch(Ellipse((-30, 225), 34, 28, angle=0,
                          facecolor="#152515", edgecolor=Z3_GREEN,
                          linewidth=0.6, linestyle="--", zorder=7, alpha=0.8))
    ax.text(-30, 225, "WATCH\nMagSafe 5W", ha="center", va="center",
            fontsize=6.5, color=TEXT_WHITE, fontweight="bold", zorder=8)
    ax.text(-30, 217, "Ø50 pod · 30° tilt", ha="center", va="top",
            fontsize=4.5, color=Z3_GREEN, zorder=8)

    # ── Zone 4 — Laptop groove ──
    z4 = FancyBboxPatch((44, 288), 22, 12,
                         boxstyle="round,pad=0,rounding_size=3",
                         facecolor="#2a1a0a", edgecolor=Z4_ORANGE,
                         linewidth=1.4, zorder=6)
    ax.add_patch(z4)
    ax.text(55, 294, "LAPTOP\nUSB-C 100W", ha="center", va="center",
            fontsize=5.5, color=TEXT_WHITE, fontweight="bold", zorder=8)
    # Left guide wall
    ax.add_patch(Rectangle((44, 288), 1.5, 12, facecolor="#333333", edgecolor=Z4_ORANGE, linewidth=0.8, zorder=7))
    # Right guide wall
    ax.add_patch(Rectangle((64.5, 288), 1.5, 12, facecolor="#333333", edgecolor=Z4_ORANGE, linewidth=0.8, zorder=7))
    # Back wall
    ax.add_patch(Rectangle((44, 298.5), 22, 1.5, facecolor="#333333", edgecolor=Z4_ORANGE, linewidth=0.8, zorder=7))
    # USB-C port indicator
    ax.add_patch(FancyBboxPatch((50, 295), 10, 4, boxstyle="round,pad=0,rounding_size=1", facecolor="#444455", edgecolor="#aaaacc", linewidth=0.6, zorder=8))
    ax.text(55, 297, "USB-C", ha="center", va="center", fontsize=3.5, color="#aaaacc", zorder=9)

    # ── IEC C13 inlet (rear wall) ──
    iec = Rectangle((-14, 296), 28, 20, facecolor="#1a1a2a",
                     edgecolor=GOLD, linewidth=1.0, zorder=6)
    ax.add_patch(iec)
    ax.text(0, 318, "IEC C13\n28×20mm", ha="center", va="bottom",
            fontsize=5, color=GOLD, zorder=8)
    ax.plot([0, 0], [306, 318], color=GOLD, linewidth=0.5, linestyle="--", zorder=5)

    # ── M3 screw holes ──
    for sx, sy in [(-50, 150), (45, 150)]:
        ax.add_patch(Circle((sx, sy), 1.6, facecolor="#0d0d1a",
                             edgecolor=TEXT_DIM, linewidth=0.8, zorder=8))
        ax.add_patch(Circle((sx, sy), 3.5, facecolor="none",
                             edgecolor=TEXT_DIM, linewidth=0.4, linestyle=":",
                             zorder=7, alpha=0.5))

    # ── Etched labels ──
    etched_labels = [
        (-45, 93,  "PHONE",     6.0, "#aaaacc"),
        ( 45, 93,  "BUDS",      6.0, "#aaaacc"),
        (-30, 203, "WATCH",     6.0, "#aaaacc"),
        ( 55, 260, "LAPTOP",    6.0, "#aaaacc"),
        (  0, 278, "Quad-Dock", 7.5, GOLD),
    ]
    for lx, ly, lt, lfs, lcol in etched_labels:
        ax.text(lx + 0.4, ly - 0.4, lt, ha="center", va="center",
                fontsize=lfs, color="#222233", style="italic", zorder=7)
        ax.text(lx, ly, lt, ha="center", va="center",
                fontsize=lfs, color=lcol, style="italic", zorder=8)

    # ── PCB and ESP32 ghost outlines ──
    ax.add_patch(Rectangle((-5 - 80, 110 - 40), 160, 80,
                             facecolor="none", edgecolor="#2a4a2a",
                             linewidth=0.5, linestyle=":", alpha=0.4, zorder=4))
    ax.add_patch(Rectangle((-15 - 9, 85 - 10), 18, 20,
                             facecolor="none", edgecolor="#3a6a3a",
                             linewidth=0.4, linestyle=":", alpha=0.5, zorder=4))

    # ── Dimension annotations ──
    # Overall length (left side)
    _dim_arrow(ax, -ILL_RHW - 15, 0, -ILL_RHW - 15, 300, "300mm", offset=(-4, 0),
               fontsize=5.5, color=TEXT_DIM)
    ax.plot([-ILL_RHW - 15, -ILL_RHW], [0, 0], color=TEXT_DIM, linewidth=0.5)
    ax.plot([-ILL_RHW - 15, -ILL_RHW], [300, 300], color=TEXT_DIM, linewidth=0.5)

    # Front width (bottom)
    _dim_arrow(ax, -ILL_FHW, -22, ILL_FHW, -22, "200mm (illustration — spec: 110mm front)", offset=(0, 0),
               fontsize=5.5, color=TEXT_DIM)
    ax.plot([-ILL_FHW, -ILL_FHW], [-22, 0], color=TEXT_DIM, linewidth=0.5)
    ax.plot([ ILL_FHW,  ILL_FHW], [-22, 0], color=TEXT_DIM, linewidth=0.5)

    # Rear width (top)
    _dim_arrow(ax, -ILL_RHW, 313, ILL_RHW, 313, "240mm (illustration — spec: 140mm rear)", offset=(0, 0),
               fontsize=5.5, color=TEXT_DIM)
    ax.plot([-ILL_RHW, -ILL_RHW], [300, 313], color=TEXT_DIM, linewidth=0.5)
    ax.plot([ ILL_RHW,  ILL_RHW], [300, 313], color=TEXT_DIM, linewidth=0.5)

    # Zone 1 callout
    _callout(ax, (-45, 98), (-10, 120), "80×55mm\nR10 · 2.5mm deep",
             color=Z1_BLUE, fontsize=5)
    # Zone 2 callout
    _callout(ax, (45, 98), (110, 120), "65×55mm\nR10 · 2.5mm deep",
             color=Z2_PURPLE, fontsize=5)
    # Zone 3 callout
    _callout(ax, (-30, 250), (-120, 255), "Ø50mm\n18mm tall · 30°",
             color=Z3_GREEN, fontsize=5)
    # Zone 4 callout
    _callout(ax, (55, 301), (130, 295), "22×12mm\nUSB-C groove",
             color=Z4_ORANGE, fontsize=5)
    # M3 screw callout
    _callout(ax, (-50, 150), (-95, 168), "M3 × Ø3.2mm",
             color=TEXT_DIM, fontsize=4.5)


# ════════════════════════════════════════════════════════════════════════════
#  VIEW 2 — FRONT ELEVATION
# ════════════════════════════════════════════════════════════════════════════
def draw_front_elevation(ax: plt.Axes) -> None:
    ax.set_xlim(-80, 80)
    ax.set_ylim(-20, 40)
    ax.set_aspect("equal")
    ax.axis("off")
    _panel_box(ax, "FRONT ELEVATION")

    # Body outline (front face): 110mm wide × 12mm tall
    body = FancyBboxPatch((-55, 0), 110, 12,
                           boxstyle="round,pad=0,rounding_size=2",
                           facecolor="#252535", edgecolor="#4a4a6a",
                           linewidth=1.5, zorder=2)
    ax.add_patch(body)

    # LED diffuser strip (290×8×3mm — only 110mm visible from front)
    diffuser = FancyBboxPatch((-55, -3), 110, 3,
                               boxstyle="round,pad=0,rounding_size=1",
                               facecolor="#221800", edgecolor="#443300",
                               linewidth=0.8, zorder=3)
    ax.add_patch(diffuser)

    # 4 LED sections with zone colours
    led_xs = [-3 * 110 / 8, -1 * 110 / 8, 1 * 110 / 8, 3 * 110 / 8]
    zone_labels = ["PHONE", "BUDS", "WATCH", "LAPTOP"]
    for i, (lx, zc, zl) in enumerate(zip(led_xs, ZONE_COLS, zone_labels)):
        seg_w = 110 / 4 - 1
        # Frosted diffuser block (three translucent layers widening outward)
        for alpha, width in [(0.15, seg_w + 4), (0.35, seg_w), (0.7, seg_w - 4)]:
            ax.add_patch(Rectangle((lx - width / 2, -2.8),
                                    width, 2.8,
                                    facecolor=zc, alpha=alpha, linewidth=0, zorder=4))
        # LED glow line
        ax.plot([lx - seg_w / 2 + 1, lx + seg_w / 2 - 1], [-1.4, -1.4],
                color=zc, linewidth=2.5, alpha=0.9, solid_capstyle="round", zorder=5)
        # Divider
        if i < 3:
            ax.plot([lx + seg_w / 2 + 0.5, lx + seg_w / 2 + 0.5], [-3, 0],
                    color="#111122", linewidth=0.8, zorder=6)
        # Zone label below
        ax.text(lx, -8, zl, ha="center", va="top",
                fontsize=5.5, color=zc, fontweight="bold")
        # Small dot indicator
        ax.add_patch(Circle((lx, -6), 1.5, facecolor=zc, edgecolor="none",
                             alpha=0.8, zorder=5))

    # Front edge radius indicators
    ax.text(-59, 5, "R2", ha="right", va="center", fontsize=4.5, color=TEXT_DIM)
    ax.text( 59, 5, "R2", ha="left",  va="center", fontsize=4.5, color=TEXT_DIM)

    # Top aluminium plate line
    ax.plot([-55, 55], [12, 12], color=ALU_TOP, linewidth=2.0, alpha=0.6, zorder=4)
    ax.plot([-55, 55], [13.5, 13.5], color=ALU_TOP, linewidth=0.8,
            alpha=0.3, zorder=4)
    ax.text(0, 15, "1.5mm BRUSHED ALUMINIUM TOP PLATE", ha="center",
            va="bottom", fontsize=4.5, color=ALU_TOP, alpha=0.8)

    # Dimension: 110mm width
    _dim_arrow(ax, -55, -15, 55, -15, "110mm", fontsize=5.5, color=TEXT_DIM)
    ax.plot([-55, -55], [-15, 0], color=TEXT_DIM, linewidth=0.5)
    ax.plot([55, 55],   [-15, 0], color=TEXT_DIM, linewidth=0.5)

    # Dimension: 12mm height
    _dim_arrow(ax, 62, 0, 62, 12, "12mm", offset=(8, 0),
               fontsize=5.5, color=TEXT_DIM)
    ax.plot([55, 62], [0, 0],   color=TEXT_DIM, linewidth=0.5)
    ax.plot([55, 62], [12, 12], color=TEXT_DIM, linewidth=0.5)

    # Corner radius callout
    ax.text(0, 20, "FRONT FACE  ·  110 × 12mm  ·  LED BAR VISIBLE",
            ha="center", va="bottom", fontsize=6, color=GOLD,
            fontweight="bold")
    ax.text(0, 17, "4-section frosted polycarbonate diffuser · WS2812B addressable",
            ha="center", va="bottom", fontsize=5, color=TEXT_LIGHT)


# ════════════════════════════════════════════════════════════════════════════
#  VIEW 3 — PERSPECTIVE / ISOMETRIC VIEW
# ════════════════════════════════════════════════════════════════════════════
def draw_perspective_view(ax: plt.Axes) -> None:
    # Oblique projection: iso_x = x + 0.6*y, iso_y = z + 0.35*y
    # Scale everything by s, offset to centre in panel
    s = 0.95
    ox, oy = 30.0, 10.0

    def proj(x: float, y: float, z: float) -> tuple[float, float]:
        px = ox + (x + 0.60 * y) * s
        py = oy + (z + 0.38 * y) * s
        return px, py

    # Figure out bounds by projecting extremes
    corners_3d = [
        (-55, 0, 0), (55, 0, 0), (70, 300, 0), (-70, 300, 0),
        (-55, 0, FH), (55, 0, FH), (70, 300, RH), (-70, 300, RH),
    ]
    all_proj = [proj(*c) for c in corners_3d]
    xs = [p[0] for p in all_proj]
    ys = [p[1] for p in all_proj]
    margin = 20
    ax.set_xlim(min(xs) - margin, max(xs) + margin + 80)
    ax.set_ylim(min(ys) - margin - 10, max(ys) + margin + 20)
    ax.set_aspect("equal")
    ax.axis("off")
    _panel_box(ax, "PERSPECTIVE VIEW")

    FL = (-55.0, 0.0)
    FR = (55.0, 0.0)
    RR = (70.0, 300.0)
    RL = (-70.0, 300.0)

    # ── Bottom face ──
    bot = [proj(FL[0], FL[1], 0), proj(FR[0], FR[1], 0),
           proj(RR[0], RR[1], 0), proj(RL[0], RL[1], 0)]
    ax.add_patch(Polygon(bot, closed=True, facecolor="#0d0d17",
                          edgecolor="#333344", linewidth=0.8, zorder=1))

    # ── Side faces ──
    # Front face
    front_face = [proj(FL[0], FL[1], 0), proj(FR[0], FR[1], 0),
                  proj(FR[0], FR[1], FH), proj(FL[0], FL[1], FH)]
    ax.add_patch(Polygon(front_face, closed=True, facecolor="#1c1c2c",
                          edgecolor="#3a3a5a", linewidth=1.0, zorder=3))

    # Right side face
    right_face = [proj(FR[0], FR[1], 0), proj(RR[0], RR[1], 0),
                  proj(RR[0], RR[1], RH), proj(FR[0], FR[1], FH)]
    ax.add_patch(Polygon(right_face, closed=True, facecolor="#1a1a2a",
                          edgecolor="#3a3a5a", linewidth=1.0, zorder=3))

    # Left side face (slightly darker — in shadow)
    left_face = [proj(FL[0], FL[1], 0), proj(RL[0], RL[1], 0),
                 proj(RL[0], RL[1], RH), proj(FL[0], FL[1], FH)]
    ax.add_patch(Polygon(left_face, closed=True, facecolor="#141420",
                          edgecolor="#2a2a4a", linewidth=1.0, zorder=3))

    # Rear face
    rear_face = [proj(RR[0], RR[1], 0), proj(RL[0], RL[1], 0),
                 proj(RL[0], RL[1], RH), proj(RR[0], RR[1], RH)]
    ax.add_patch(Polygon(rear_face, closed=True, facecolor="#111120",
                          edgecolor="#2a2a4a", linewidth=0.8, zorder=3))

    # ── Top face (aluminium plate) with hatching ──
    top_face = [proj(FL[0], FL[1], FH), proj(FR[0], FR[1], FH),
                proj(RR[0], RR[1], RH), proj(RL[0], RL[1], RH)]
    ax.add_patch(Polygon(top_face, closed=True, facecolor=ALU_TOP,
                          edgecolor="#aabbcc", linewidth=1.2, zorder=4,
                          hatch="////", alpha=0.9))
    # Slightly brighter overlay for brushed effect
    ax.add_patch(Polygon(top_face, closed=True, facecolor="#9ab0be",
                          edgecolor="none", linewidth=0, zorder=5, alpha=0.2))

    # ── LED bar on front face ──
    led_y = 0.0
    led_height = 3.0
    led_pts = [proj(-53, led_y, FH - led_height),
               proj(53, led_y, FH - led_height),
               proj(53, led_y, FH + 0.5),
               proj(-53, led_y, FH + 0.5)]
    ax.add_patch(Polygon(led_pts, closed=True, facecolor="#1a1000",
                          edgecolor="#332200", linewidth=0.6, zorder=6))
    # LED glow
    for i, (lx, zc) in enumerate(zip(
            [-3 * 110 / 8, -1 * 110 / 8, 1 * 110 / 8, 3 * 110 / 8], ZONE_COLS)):
        p0 = proj(lx - 12, 0, FH - 2)
        p1 = proj(lx + 12, 0, FH - 2)
        ax.plot([p0[0], p1[0]], [p0[1], p1[1]],
                color=zc, linewidth=3.5, alpha=0.9,
                solid_capstyle="round", zorder=7)
        ax.plot([p0[0], p1[0]], [p0[1] + 1, p1[1] + 1],
                color=zc, linewidth=6, alpha=0.15,
                solid_capstyle="round", zorder=7)

    # ── Zones on top face ──
    # Zone 1 — Phone
    z1_corners = [
        proj(-45 - 40, 70 - 27.5, FH + 0.3),
        proj(-45 + 40, 70 - 27.5, FH + 0.3),
        proj(-45 + 40, 70 + 27.5, body_h(70) + 0.3),
        proj(-45 - 40, 70 + 27.5, body_h(70) + 0.3),
    ]
    ax.add_patch(Polygon(z1_corners, closed=True, facecolor="#1c2a3a",
                          edgecolor=Z1_BLUE, linewidth=1.0, zorder=8, alpha=0.9))
    z1c = proj(-45, 70, FH + 0.5)
    ax.text(z1c[0], z1c[1], "PHONE\nQi2 15W", ha="center", va="center",
            fontsize=4.5, color=TEXT_WHITE, fontweight="bold", zorder=10)

    # Zone 2 — Buds
    z2_corners = [
        proj(45 - 32.5, 70 - 27.5, FH + 0.3),
        proj(45 + 32.5, 70 - 27.5, FH + 0.3),
        proj(45 + 32.5, 70 + 27.5, body_h(70) + 0.3),
        proj(45 - 32.5, 70 + 27.5, body_h(70) + 0.3),
    ]
    ax.add_patch(Polygon(z2_corners, closed=True, facecolor="#251a35",
                          edgecolor=Z2_PURPLE, linewidth=1.0, zorder=8, alpha=0.9))
    z2c = proj(45, 70, FH + 0.5)
    ax.text(z2c[0], z2c[1], "BUDS\nQi 5W", ha="center", va="center",
            fontsize=4.5, color=TEXT_WHITE, fontweight="bold", zorder=10)

    # Zone 4 — Laptop groove (rear right)
    z4_corners = [
        proj(18, 288, body_h(288) + 0.3),
        proj(40, 288, body_h(288) + 0.3),
        proj(40, 300, RH + 0.3),
        proj(18, 300, RH + 0.3),
    ]
    ax.add_patch(Polygon(z4_corners, closed=True, facecolor="#2a1a0a",
                          edgecolor=Z4_ORANGE, linewidth=1.0, zorder=8, alpha=0.9))

    # Zone 3 — Watch cradle pod (raised cylinder + cone)
    pod_z = body_h(225)
    pod_ctr = proj(-22, 225, pod_z)
    pod_r = 14.0
    # Pod base circle (ellipse in projection)
    theta = np.linspace(0, 2 * math.pi, 36)
    pod_rim = [proj(-22 + pod_r * math.cos(t), 225 + pod_r * 0.4 * math.sin(t),
                    pod_z + 0.5) for t in theta]
    ax.add_patch(Polygon(pod_rim, closed=True, facecolor="#1a2a1a",
                          edgecolor=Z3_GREEN, linewidth=1.0, zorder=9))
    # Pod cone/spike (tilted 30°)
    cone_base_l = proj(-22 - 6, 225, pod_z + 2)
    cone_base_r = proj(-22 + 6, 225, pod_z + 2)
    cone_tip    = proj(-22 - 10, 225, pod_z + 18)
    ax.add_patch(Polygon([cone_base_l, cone_base_r, cone_tip],
                          closed=True, facecolor="#2a3a2a",
                          edgecolor=Z3_GREEN, linewidth=0.8, zorder=10))
    ax.add_patch(Circle(cone_tip, 3.5, facecolor="#1f301f",
                         edgecolor=Z3_GREEN, linewidth=0.8, zorder=11))
    z3c = proj(-22, 225, pod_z + 1)
    ax.text(z3c[0] + 5, z3c[1] - 2, "WATCH\n5W", ha="center", va="center",
            fontsize=4, color=Z3_GREEN, fontweight="bold", zorder=12)

    # ── Rubber feet (bottom corners) ──
    for fx, fy in [(-39.17, 15), (39.17, 15), (-53.5, 285), (53.5, 285)]:
        fp = proj(fx, fy, -3)
        ax.add_patch(Ellipse(fp, 12, 5, facecolor="#0a0a12",
                              edgecolor="#222233", linewidth=0.6, zorder=2))

    # ── IEC C13 power cord ──
    # IEC C13 socket housing on rear wall
    iec_pt = proj(0, 299, 6)
    socket_tl = proj(-5, 299, 10)
    socket_tr = proj(5, 299, 10)
    socket_bl = proj(-5, 299, 2)
    socket_br = proj(5, 299, 2)
    ax.add_patch(Polygon([socket_tl, socket_tr, socket_br, socket_bl],
                          closed=True, facecolor="#1a1a2a", edgecolor=GOLD,
                          linewidth=1.2, zorder=8))
    # Cord leaving the socket
    cord_start = proj(0, 300, 6)
    cord_end = (cord_start[0] + 35, cord_start[1] + 4)
    ax.plot([cord_start[0], cord_end[0]], [cord_start[1], cord_end[1]],
            color="#2d2d38", linewidth=8, solid_capstyle="round", zorder=6)
    ax.plot([cord_start[0], cord_end[0]], [cord_start[1], cord_end[1]],
            color="#1e1e28", linewidth=5, solid_capstyle="round", zorder=7)
    # Coil loops
    for i in range(6):
        ci_x = cord_end[0] + 5 + i * 14
        ci_y = cord_end[1] + 2
        ax.add_patch(Arc((ci_x, ci_y), 16 + i * 2, 10 + i,
                          theta1=15, theta2=345,
                          color="#2e2e3c", linewidth=2.0, zorder=7))
    # Label
    ax.text(cord_end[0] + 30, cord_end[1] + 12, "IEC C13\nPOWER",
            ha="center", va="bottom", fontsize=4.5, color=GOLD, zorder=10)

    # ── Shadow under dock ──
    shadow = [proj(FL[0], FL[1], -2), proj(FR[0], FR[1], -2),
              proj(RR[0], RR[1], -2), proj(RL[0], RL[1], -2)]
    ax.add_patch(Polygon(shadow, closed=True, facecolor="#050508",
                          edgecolor="none", linewidth=0, zorder=0, alpha=0.7))

    # ── Labels ──
    ax.text(proj(0, 150, RH + 5)[0], proj(0, 150, RH + 5)[1] + 18,
            "PERSPECTIVE VIEW  ·  OBLIQUE PROJECTION",
            ha="center", va="bottom", fontsize=6, color=GOLD,
            fontweight="bold", zorder=15)


# ════════════════════════════════════════════════════════════════════════════
#  VIEW 4 — SIDE ELEVATION / CROSS-SECTION
# ════════════════════════════════════════════════════════════════════════════
def draw_side_elevation(ax: plt.Axes) -> None:
    ax.set_xlim(-30, 360)
    ax.set_ylim(-20, 55)
    ax.set_aspect("equal")
    ax.axis("off")
    _panel_box(ax, "SIDE ELEVATION — CROSS-SECTION")

    # ── Outer profile ──
    # Y-axis = left→right (0=front, 300=rear), Z-axis = up
    profile_pts = np.array([[0, 0], [300, 0], [300, RH], [0, FH]], dtype=float)
    body_profile = PathPatch(
        rounded_trapezoid_path(profile_pts, radius=5),
        facecolor="#252535", edgecolor="#4a4a6a", linewidth=1.5, zorder=2,
    )
    ax.add_patch(body_profile)

    # ── Top plate (1.5mm) ──
    top_plate = FancyBboxPatch((0, FH), 300, 1.5,
                                boxstyle="round,pad=0,rounding_size=1",
                                facecolor=ALU_TOP, edgecolor="#aabbcc",
                                linewidth=0.8, zorder=3)
    ax.add_patch(top_plate)

    # ── Interior components (ghost / cross-section style) ──
    def ghost_rect(x: float, y: float, w: float, h: float,
                   fc: str, ec: str, label: str = "", zorder: int = 5) -> None:
        ax.add_patch(Rectangle((x, y), w, h,
                                facecolor=fc, edgecolor=ec,
                                linewidth=0.8, linestyle="--",
                                alpha=0.65, zorder=zorder))
        if label:
            ax.text(x + w / 2, y + h / 2, label,
                    ha="center", va="center",
                    fontsize=4.0, color=ec, fontweight="bold", zorder=zorder + 1)

    # PSU block (150×35mm at Y=210-75..210+75, Z=5..40) — centred at Y=210
    ghost_rect(210 - 75, 5, 150, 28, "#1a1a2a", "#4466cc", "PSU\n180W")
    # PCB main (120mm wide at Y=110-60..170, 5mm thick)
    ghost_rect(110 - 60, 5, 120, 5, "#1a2a1a", "#44aa44", "PCB MAIN")
    # ESP32-C3 (18×20 at Y=85-9..85+9, Z=10)
    ghost_rect(85 - 9, 10, 18, 4, "#2a2a1a", "#aaaa44", "ESP32")
    # INA3221
    ghost_rect(20 - 5, 10, 10, 4, "#2a1a1a", "#aa4444", "INA")
    # Qi coil 1 cross-section at Y=70
    ax.add_patch(Ellipse((70, 4 + 2.5), 10, 5,
                          facecolor="#1a1a3a", edgecolor=Z1_BLUE,
                          linewidth=0.8, linestyle="--", alpha=0.7, zorder=5))
    ax.text(70, 4, "Qi", ha="center", va="center",
            fontsize=3.5, color=Z1_BLUE, zorder=6)
    # Watch puck at Y=225
    ax.add_patch(Ellipse((225, 4 + 2.5), 10, 5,
                          facecolor="#1a3a1a", edgecolor=Z3_GREEN,
                          linewidth=0.8, linestyle="--", alpha=0.7, zorder=5))
    ax.text(225, 4, "Ø34", ha="center", va="center",
            fontsize=3.5, color=Z3_GREEN, zorder=6)
    # USB-C PD board at Y=155
    ghost_rect(155 - 15, 5, 30, 4, "#2a1a2a", "#aa44aa", "PD\n100W")
    # IEC C13 cutout on rear wall
    ax.add_patch(Rectangle((296, 6), 4, 8,
                             facecolor="#0d0d1a", edgecolor=GOLD,
                             linewidth=0.8, zorder=6))
    # Vent slot suggestion
    for vy in [25, 45, 65, 85]:
        ax.add_patch(Rectangle((vy - 20, 0), 40, 1.5,
                                 facecolor="#0d0d1a", edgecolor=TEXT_DIM,
                                 linewidth=0.4, alpha=0.6, zorder=6))

    # ── Dimension lines ──
    # Total length
    _dim_arrow(ax, 0, -12, 300, -12, "300mm total length",
               fontsize=5, color=TEXT_DIM)
    ax.plot([0, 0],     [-12, 0],  color=TEXT_DIM, linewidth=0.5)
    ax.plot([300, 300], [-12, 0],  color=TEXT_DIM, linewidth=0.5)

    # Front height
    _dim_arrow(ax, -12, 0, -12, FH, f"{int(FH)}mm",
               offset=(-6, 0), fontsize=4.5, color=TEXT_DIM)
    ax.plot([-12, 0], [0, 0],   color=TEXT_DIM, linewidth=0.5)
    ax.plot([-12, 0], [FH, FH], color=TEXT_DIM, linewidth=0.5)

    # Rear height
    _dim_arrow(ax, 312, 0, 312, RH, f"{int(RH)}mm",
               offset=(8, 0), fontsize=4.5, color=TEXT_DIM)
    ax.plot([300, 312], [0, 0],   color=TEXT_DIM, linewidth=0.5)
    ax.plot([300, 312], [RH, RH], color=TEXT_DIM, linewidth=0.5)

    # Top plate callout
    ax.annotate("1.5mm Al plate", xy=(150, FH + 0.75),
                 xytext=(150, 32),
                 arrowprops=dict(arrowstyle="->", color=ALU_TOP, lw=0.7),
                 color=ALU_TOP, fontsize=4.5, ha="center", zorder=10)

    # PSU callout
    ax.text(210, 35, "PSU 180W\n150×80×35mm", ha="center", va="bottom",
            fontsize=4.5, color="#4466cc")
    ax.plot([210, 210], [33, 5 + 28], color="#4466cc", linewidth=0.4,
            linestyle=":", alpha=0.6)


# ════════════════════════════════════════════════════════════════════════════
#  VIEW 5 — BOTTOM VIEW
# ════════════════════════════════════════════════════════════════════════════
def draw_bottom_view(ax: plt.Axes) -> None:
    ax.set_xlim(-110, 130)
    ax.set_ylim(-35, 355)
    ax.set_aspect("equal")
    ax.axis("off")
    _panel_box(ax, "BOTTOM VIEW")

    pts = _trapezoid_pts()

    # ── Dock body (bottom face) ──
    body = PathPatch(rounded_trapezoid_path(pts, radius=CR),
                     facecolor="#1a1a28", edgecolor="#3a3a5a",
                     linewidth=1.5, zorder=2)
    ax.add_patch(body)

    # Matte ABS texture label
    ax.text(0, 150, "MATTE ABS — SOFT TOUCH", ha="center", va="center",
            fontsize=8, color="#333344", fontweight="bold",
            style="italic", zorder=3, alpha=0.5)

    # ── Rubber feet (Ø15mm) ──
    feet = [(-39.17, 15), (39.17, 15), (-53.5, 285), (53.5, 285)]
    for fx, fy in feet:
        ax.add_patch(Circle((fx, fy), 7.5, facecolor="#0d0d17",
                             edgecolor="#444455", linewidth=1.0, zorder=5))
        ax.add_patch(Circle((fx, fy), 5.0, facecolor="#111120",
                             edgecolor="#333344", linewidth=0.5, zorder=6))
        # Grip rings
        for r in [6.5, 7.0]:
            ax.add_patch(Circle((fx, fy), r, facecolor="none",
                                 edgecolor="#222233", linewidth=0.3, zorder=6))

    # Feet dimensions callout
    _callout(ax, (-39.17, 22.5), (-85, 28), "Ø15×3mm\nrubber feet",
             color=TEXT_DIM, fontsize=4.5)

    # ── Vent slots (8 total: X=±20, Y=25/45/65/85, each 40×4mm) ──
    vent_cols = [-20, 20]
    vent_rows = [25, 45, 65, 85]
    for vx in vent_cols:
        for vy in vent_rows:
            ax.add_patch(FancyBboxPatch((vx - 20, vy - 2), 40, 4,
                                        boxstyle="round,pad=0,rounding_size=1",
                                        facecolor="#0d0d17",
                                        edgecolor="#2a2a3a",
                                        linewidth=0.7, zorder=5))

    _callout(ax, (-20, 25), (-88, 42), "40×4mm vent slots\n(8 total)",
             color=TEXT_DIM, fontsize=4.5)
    _callout(ax, (20, 25), (85, 42), "2 rows · 4 per row",
             color=TEXT_DIM, fontsize=4.5)

    # ── M3 screw holes ──
    for sx, sy in [(-35, 150), (30, 150)]:
        ax.add_patch(Circle((sx, sy), 1.6, facecolor="#0d0d1a",
                             edgecolor=TEXT_DIM, linewidth=0.8, zorder=8))
        ax.add_patch(Circle((sx, sy), 3.5, facecolor="none",
                             edgecolor=TEXT_DIM, linewidth=0.4, linestyle=":",
                             zorder=7, alpha=0.5))
    _callout(ax, (-35, 150), (-92, 165), "M3 × Ø3.2mm\nsnap-fit screw",
             color=TEXT_DIM, fontsize=4.5)

    # ── Dimension lines ──
    _dim_arrow(ax, -82, 0, -82, 300, "300mm", offset=(-4, 0),
               fontsize=5.5, color=TEXT_DIM)
    ax.plot([-82, -70], [0, 0],   color=TEXT_DIM, linewidth=0.5)
    ax.plot([-82, -70], [300, 300], color=TEXT_DIM, linewidth=0.5)

    _dim_arrow(ax, -55, -22, 55, -22, "110mm", fontsize=5.5, color=TEXT_DIM)
    ax.plot([-55, -55], [-22, 0], color=TEXT_DIM, linewidth=0.5)
    ax.plot([55, 55],   [-22, 0], color=TEXT_DIM, linewidth=0.5)

    _dim_arrow(ax, -70, 313, 70, 313, "140mm", fontsize=5.5, color=TEXT_DIM)
    ax.plot([-70, -70], [300, 313], color=TEXT_DIM, linewidth=0.5)
    ax.plot([70, 70],   [300, 313], color=TEXT_DIM, linewidth=0.5)


# ════════════════════════════════════════════════════════════════════════════
#  VIEW 6 — FEATURE SPEC PANEL
# ════════════════════════════════════════════════════════════════════════════
def draw_spec_panel(ax: plt.Axes) -> None:
    ax.axis("off")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_facecolor(PANEL_BG)
    for spine in ax.spines.values():
        spine.set_edgecolor(PANEL_BORDER)
        spine.set_linewidth(1.5)

    def hline(y: float, lw: float = 0.8) -> None:
        ax.plot([0.03, 0.97], [y, y], color=PANEL_BORDER, linewidth=lw, zorder=2)

    def section_title(y: float, text: str) -> float:
        hline(y + 0.005)
        ax.text(0.05, y - 0.003, text, fontsize=7.5, color=GOLD,
                fontweight="bold", va="top", fontfamily="monospace")
        return y - 0.028

    def body_line(y: float, text: str, indent: float = 0.07,
                  color: str = TEXT_LIGHT, fs: float = 6.2) -> float:
        ax.text(indent, y, text, fontsize=fs, color=color, va="top")
        return y - 0.020

    def zone_block(y: float, dot_col: str, title: str,
                   lines: list[str]) -> float:
        ax.add_patch(Circle((0.055, y - 0.008), 0.007,
                             facecolor=dot_col, edgecolor="none", zorder=3))
        ax.text(0.07, y, title, fontsize=6.8, color=TEXT_WHITE,
                fontweight="bold", va="top")
        y -= 0.022
        for line in lines:
            y = body_line(y, line, indent=0.09, color=TEXT_LIGHT, fs=5.8)
        return y - 0.004

    # ── Header ──
    ax.text(0.5, 0.975, "QUAD-DOCK™", fontsize=16, color=GOLD,
            fontweight="bold", ha="center", va="top",
            fontfamily="monospace", zorder=3)
    ax.text(0.5, 0.940, "The 4-Zone Desktop Charging Station",
            fontsize=7, color=TEXT_LIGHT, ha="center", va="top")
    hline(0.925, lw=1.2)

    y = 0.910

    # ── Charging Zones ──
    y = section_title(y, "CHARGING ZONES")
    y = zone_block(y, Z1_BLUE, "ZONE 1 — PHONE", [
        "Protocol: Qi2 / MagSafe-compatible",
        "Power:    15W max",
        "Coil:     Ø54mm, embedded",
        "Magnets:  N52 ring array",
        "Dish:     80×55mm, 2.5mm recess",
    ])
    y = zone_block(y, Z2_PURPLE, "ZONE 2 — EARBUDS", [
        "Protocol: Qi 5W",
        "Power:    5W max",
        "Coil:     Ø54mm, embedded",
        "Dish:     65×55mm, 2.5mm recess",
    ])
    y = zone_block(y, Z3_GREEN, "ZONE 3 — APPLE WATCH", [
        "Protocol: MagSafe puck",
        "Power:    5W",
        "Cradle:   30° tilt, Ø50 pod",
        "Compat:   Series 1–9, SE, Ultra",
    ])
    y = zone_block(y, Z4_ORANGE, "ZONE 4 — LAPTOP / USB-C", [
        "Protocol: USB-C PD",
        "Power:    100W max",
        "Groove:   22×12mm silicone-lined",
        "Compat:   Any USB-C laptop (2018+)",
    ])

    y -= 0.005
    y = section_title(y, "ELECTRONICS")
    for line in [
        "MCU:     ESP32-C3 Mini  (WiFi + BLE)",
        "Monitors: INA3221 + INA219",
        "Ambient: BH1750 lux sensor",
        "LED:     WS2812B × 16  (4 per zone)",
        "PSU:     Internal 180W AC/DC",
        "Inlet:   IEC C13  (no external brick)",
        "Surge:   Built-in protection",
    ]:
        y = body_line(y, line, fs=5.8)

    y -= 0.005
    y = section_title(y, "PHYSICAL DIMENSIONS")
    physical_specs = [
        ("Length",         "300mm"),
        ("Width (front)",  "110mm"),
        ("Width (rear)",   "140mm"),
        ("Height (front)", " 12mm"),
        ("Height (rear)",  " 22mm"),
        ("Corner radius",  "R20mm"),
        ("Top plate",      "1.5mm brushed aluminium"),
        ("Body",           "Soft-touch matte ABS"),
        ("Finish",         "Gunmetal Black / Silver White"),
    ]
    for k, v in physical_specs:
        ax.text(0.07, y, k, fontsize=5.8, color=TEXT_DIM, va="top")
        ax.text(0.48, y, v, fontsize=5.8, color=TEXT_LIGHT, va="top",
                fontweight="bold")
        y -= 0.018

    y -= 0.005
    y = section_title(y, "LED STATUS SYSTEM")
    led_states = [
        ("#cc3333", "Red   — Charging active"),
        ("#33cc33", "Green — Fully charged"),
        ("#555566", "Off   — No device detected"),
    ]
    for lc, lt in led_states:
        ax.add_patch(Circle((0.055, y - 0.008), 0.006,
                             facecolor=lc, edgecolor="none", zorder=3))
        y = body_line(y, lt, indent=0.07, fs=5.8)
    y = body_line(y, "4 independent zones · WS2812B addressable strip", fs=5.8)
    y = body_line(y, "Frosted front-lip diffuser", fs=5.8)

    y -= 0.005
    y = section_title(y, "ASSEMBLY")
    for line in [
        "Snap-fit ABS base + 2× M3 screws",
        "Removable top plate (service access)",
        "Rubber feet: 4× Ø15×3mm",
    ]:
        y = body_line(y, line, fs=5.8)

    # ── Pricing & footer ──
    hline(max(y - 0.020, 0.12))
    y = max(y - 0.025, 0.115)
    ax.text(0.5, y, "$189  USD", fontsize=13, color=GOLD,
            fontweight="bold", ha="center", va="top")
    y -= 0.030
    ax.text(0.5, y, "Black or White Variant",
            fontsize=6.5, color=TEXT_LIGHT, ha="center", va="top")
    y -= 0.022
    ax.text(0.5, y, "GJATHASEnterprises © 2025",
            fontsize=6, color=TEXT_DIM, ha="center", va="top")
    y -= 0.018
    ax.text(0.5, y, "CONFIDENTIAL — INVESTOR PREVIEW",
            fontsize=6, color=RED_CONF, ha="center", va="top",
            fontweight="bold")


# ════════════════════════════════════════════════════════════════════════════
#  HEADER
# ════════════════════════════════════════════════════════════════════════════
def draw_header(fig: plt.Figure) -> None:
    # Header strip using figure-level text/artists
    # Background rect
    hdr = fig.add_axes([0, 0.945, 1, 0.055])
    hdr.set_facecolor("#0a0a15")
    hdr.axis("off")
    for spine in hdr.spines.values():
        spine.set_visible(False)

    # Q logo (simple matplotlib patch)
    q_ax = fig.add_axes([0.008, 0.950, 0.028, 0.044])
    q_ax.set_xlim(0, 1)
    q_ax.set_ylim(0, 1)
    q_ax.axis("off")
    q_ax.set_facecolor("#0a0a15")
    # Draw Q shape using a ring + small tail
    q_ax.add_patch(Wedge((0.5, 0.52), 0.38, 0, 360,
                          width=0.13, facecolor=GOLD, edgecolor="none"))
    q_ax.plot([0.62, 0.82], [0.20, 0.10], color=GOLD, linewidth=2.5,
              solid_capstyle="round")

    # Title
    hdr.text(0.04, 0.5, "QUAD-DOCK™", fontsize=28, color=GOLD,
             fontweight="bold", va="center", fontfamily="monospace",
             transform=hdr.transAxes)

    # Subtitle
    hdr.text(0.04, 0.18,
             "4-Zone Desktop Charging Station  ·  "
             "Simultaneous Phone + Buds + Watch + Laptop",
             fontsize=9, color=TEXT_LIGHT, va="center",
             transform=hdr.transAxes)

    # Confidential tag (right)
    hdr.text(0.97, 0.5, "CONFIDENTIAL — INVESTOR PREVIEW",
             fontsize=10, color=RED_CONF, fontweight="bold",
             va="center", ha="right", transform=hdr.transAxes)

    # Thin gold rule at bottom of header
    fig.add_artist(plt.Line2D([0, 1], [0.944, 0.944],
                               color=GOLD, linewidth=0.8,
                               transform=fig.transFigure))


# ════════════════════════════════════════════════════════════════════════════
#  MAIN FIGURE ASSEMBLY
# ════════════════════════════════════════════════════════════════════════════
def build_figure() -> None:
    fig = plt.figure(figsize=(24, 18), dpi=300, facecolor=PAGE_BG)

    # 3-row × 2-column grid (below header at ~5.5% height)
    # Spec panel spans all 3 rows in column 2
    gs = fig.add_gridspec(
        3, 2,
        left=0.010, right=0.995,
        top=0.942, bottom=0.008,
        hspace=0.035, wspace=0.025,
        width_ratios=[1.15, 0.85],
        height_ratios=[1, 0.45, 1],
    )

    ax_top   = fig.add_subplot(gs[0, 0])   # Top-down view
    ax_front = fig.add_subplot(gs[1, 0])   # Front elevation
    ax_persp = fig.add_subplot(gs[2, 0])   # Perspective
    ax_side  = fig.add_subplot(gs[0, 1])   # Side cross-section
    ax_bot   = fig.add_subplot(gs[1, 1])   # Bottom view (small)
    ax_spec  = fig.add_subplot(gs[2, 1])   # Spec panel

    # Style all panels
    for ax in (ax_top, ax_front, ax_persp, ax_side, ax_bot, ax_spec):
        ax.set_facecolor(PANEL_BG)
        for spine in ax.spines.values():
            spine.set_edgecolor(PANEL_BORDER)
            spine.set_linewidth(1.2)

    # Draw header
    draw_header(fig)

    # Draw each view
    draw_top_view(ax_top)
    draw_front_elevation(ax_front)
    draw_perspective_view(ax_persp)
    draw_side_elevation(ax_side)
    draw_bottom_view(ax_bot)
    draw_spec_panel(ax_spec)

    # Save
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT_PATH, dpi=300, facecolor=PAGE_BG)
    plt.close(fig)


if __name__ == "__main__":
    build_figure()
    print(f"Saved: {OUTPUT_PATH}")
