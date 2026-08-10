#!/usr/bin/env python3
"""
Generate a high-quality 3/4 isometric product render of the Epitome Penta.

Usage:
    python scripts/generate_image.py

Output:
    assets/epitome-penta-render.png  (1200×800 px)
"""
from __future__ import annotations

import math
import os
from pathlib import Path

import numpy as np

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    from matplotlib.patches import FancyBboxPatch, Arc, Ellipse, Polygon, Circle
    from matplotlib.path import Path as MPath
    from matplotlib.patheffects import withStroke
    import matplotlib.patheffects as pe
except ImportError as exc:
    raise SystemExit(
        "matplotlib is required. Install with: pip install matplotlib"
    ) from exc

try:
    from PIL import Image, ImageFilter, ImageDraw, ImageFont
except ImportError as exc:
    raise SystemExit(
        "Pillow is required. Install with: pip install Pillow"
    ) from exc

# ---------------------------------------------------------------------------
# Output path
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = ROOT / "assets" / "epitome-penta-render.png"
CANVAS_W, CANVAS_H = 1200, 800

# ---------------------------------------------------------------------------
# Colour palette — Epitome Penta Black model
# ---------------------------------------------------------------------------
C_BG          = "#f0f2f4"          # canvas background (very light grey)
C_BODY        = "#1a1d22"          # ABS base (near-black)
C_BODY_SHADE  = "#0d0f12"          # darker ABS for shaded faces
C_TOP         = "#282d34"          # brushed aluminium (gunmetal/dark grey)
C_TOP_LIGHT   = "#323840"          # highlight edge of top plate
C_TOP_HILIGHT = "#3d4550"          # brightest highlight strip
C_ZONE_FILL   = "#1e2229"          # charging zone recessed pocket
C_ZONE_EDGE   = "#404a56"          # zone pocket edge
C_SI_EDGE     = "#4a5a6a"          # silicone pad outline
C_LED_WARM    = "#ffcc66"          # warm-white/amber LED glow
C_LED_DIM     = "#3a3020"          # off-state LED
C_WATCH_RING  = "#b0bac4"          # watch ring chrome
C_LAPTOP_SLOT = "#151820"          # laptop groove slot
C_BRAND       = "#8090a0"          # wordmark on rear
C_LABEL       = "#7a8898"          # text labels
C_LABEL_LIGHT = "#a8b8c8"          # lighter labels
C_ICON_FILL   = "#50c8ff"          # laser-etched icon / QI ring highlight
C_RUBBER      = "#111417"          # rubber feet
C_SHADOW_RGBA = (0, 0, 0, 90)      # drop-shadow


# ---------------------------------------------------------------------------
# 3D → 2D isometric projection helpers
# ---------------------------------------------------------------------------

def iso(x: float, y: float, z: float,
        scale: float = 2.4,
        ox: float = 420, oy: float = 420) -> tuple[float, float]:
    """
    Classic 2:1 isometric projection (30° elevation, 45° azimuth).

    Coordinate system (right-hand, dock-centred):
      x  = width (left → right when looking at the dock from front-left)
      y  = height (bottom → top)
      z  = depth  (front → rear)

    Returns (screen_x, screen_y) for matplotlib (y grows upward).
    """
    angle = math.radians(30)
    sx = (x - z) * math.cos(angle) * scale + ox
    sy = (x + z) * math.sin(angle) * scale - y * scale + oy
    return sx, sy


def iso_pts(pts3d: list[tuple[float, float, float]],
            **kwargs) -> list[tuple[float, float]]:
    """Project a list of 3-D points to 2-D screen coords."""
    return [iso(*p, **kwargs) for p in pts3d]


# ---------------------------------------------------------------------------
# Geometry constants — all measurements in mm mapped to drawing units
# ---------------------------------------------------------------------------
#  The dock occupies z = 0 (front lip) … z = 300 (rear wall)
#  Width tapers: 110 mm at z=0, 140 mm at z=300
#  Height tapers: 12 mm at z=0, 22 mm at z=300 (base sits on desk = y=0)
#  The top plate is a thin panel (2 mm thick) inset 5 mm from the edges.

DW_FRONT = 110      # dock width at front (x direction)
DW_REAR  = 140      # dock width at rear
DL       = 300      # dock length (z direction)
DH_FRONT = 12       # dock height at front
DH_REAR  = 22       # dock height at rear
TP_INSET = 5        # top-plate inset from body edges

# Centre the dock on the canvas around a visual anchor
OX, OY = 390, 450   # isometric origin shift


def dock_width_at(z: float) -> float:
    """Width of the dock at depth z (linear taper)."""
    return DW_FRONT + (DW_REAR - DW_FRONT) * z / DL


def dock_height_at(z: float) -> float:
    """Height of the dock at depth z (linear taper)."""
    return DH_FRONT + (DH_REAR - DH_FRONT) * z / DL


# Precompute corner heights
hf = dock_height_at(0)     # = DH_FRONT
hr = dock_height_at(DL)    # = DH_REAR
wf = dock_width_at(0)      # = DW_FRONT
wr = dock_width_at(DL)     # = DW_REAR


# ---------------------------------------------------------------------------
# Drawing helpers
# ---------------------------------------------------------------------------

def filled_polygon(ax, pts3d, color, alpha=1.0, zorder=2, lw=0, ec=None):
    """Draw a filled 3-D polygon projected to 2-D."""
    pts2d = iso_pts(pts3d, ox=OX, oy=OY)
    poly = Polygon(pts2d, closed=True,
                   facecolor=color, edgecolor=ec or color,
                   linewidth=lw, alpha=alpha, zorder=zorder)
    ax.add_patch(poly)
    return poly


def stroked_polygon(ax, pts3d, color, ec="#000", lw=1.5, alpha=1.0, zorder=3):
    pts2d = iso_pts(pts3d, ox=OX, oy=OY)
    poly = Polygon(pts2d, closed=True,
                   facecolor=color, edgecolor=ec,
                   linewidth=lw, alpha=alpha, zorder=zorder)
    ax.add_patch(poly)
    return poly


def iso_p(x, y, z):
    return iso(x, y, z, ox=OX, oy=OY)


# ---------------------------------------------------------------------------
# Glow helper  (drawn into a PIL layer, composited on top of the mpl figure)
# ---------------------------------------------------------------------------

def add_glow(pil_img: Image.Image,
             cx: float, cy: float,
             color_rgb: tuple[int, int, int],
             radius: int = 40,
             alpha: int = 180) -> None:
    """Add a soft radial glow at (cx, cy) on a PIL RGBA image."""
    glow = Image.new("RGBA", pil_img.size, (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(glow)
    r, g, b = color_rgb
    gdraw.ellipse(
        (cx - radius, cy - radius, cx + radius, cy + radius),
        fill=(r, g, b, alpha),
    )
    glow = glow.filter(ImageFilter.GaussianBlur(radius=radius // 2))
    pil_img.alpha_composite(glow)


# ---------------------------------------------------------------------------
# Main render function
# ---------------------------------------------------------------------------

def render(ax: plt.Axes) -> None:
    """Draw the complete Epitome Penta into *ax*."""

    # ------------------------------------------------------------------ #
    #  1. Drop shadow                                                      #
    # ------------------------------------------------------------------ #
    print("  Drawing drop shadow …")
    # Shadow is a slightly offset, blurred version of the dock footprint.
    # We simulate with a semi-transparent polygon.
    sh_off = 8  # shadow offset
    shadow_pts = [
        (sh_off, -4, sh_off),
        (wf + sh_off, -4, sh_off),
        (wr + sh_off, -4, DL + sh_off),
        (sh_off, -4, DL + sh_off),
    ]
    filled_polygon(ax, shadow_pts, color=(0, 0, 0, 0.18), alpha=0.6, zorder=1)

    # ------------------------------------------------------------------ #
    #  2. ABS base — rear face (far, drawn first)                         #
    # ------------------------------------------------------------------ #
    print("  Drawing ABS base rear face …")
    rear_pts = [
        (0,   0,   DL),
        (wr,  0,   DL),
        (wr,  hr,  DL),
        (0,   hr,  DL),
    ]
    stroked_polygon(ax, rear_pts, C_BODY_SHADE, ec="#0a0c0f", lw=1, zorder=3)

    # "Epitome Penta" wordmark on rear face
    rx, ry = iso_p(wr / 2, hr / 2, DL)
    ax.text(rx, ry, "Epitome Penta", ha="center", va="center",
            fontsize=7, color=C_BRAND, fontfamily="monospace",
            alpha=0.7, zorder=4)

    # ------------------------------------------------------------------ #
    #  3. ABS base — right side face                                      #
    # ------------------------------------------------------------------ #
    print("  Drawing ABS base right face …")
    right_pts = [
        (wr,  0,   DL),
        (wf,  0,   0),
        (wf,  hf,  0),
        (wr,  hr,  DL),
    ]
    stroked_polygon(ax, right_pts, C_BODY_SHADE, ec="#0a0c0f", lw=1, zorder=3)

    # ------------------------------------------------------------------ #
    #  4. ABS base — left side face                                       #
    # ------------------------------------------------------------------ #
    print("  Drawing ABS base left face …")
    left_pts = [
        (0,   0,   0),
        (0,   0,   DL),
        (0,   hr,  DL),
        (0,   hf,  0),
    ]
    stroked_polygon(ax, left_pts, C_BODY, ec="#0a0c0f", lw=1, zorder=4)

    # ------------------------------------------------------------------ #
    #  5. ABS base — front face  (with LED bar channel)                   #
    # ------------------------------------------------------------------ #
    print("  Drawing ABS base front face …")
    front_pts = [
        (0,   0,   0),
        (wf,  0,   0),
        (wf,  hf,  0),
        (0,   hf,  0),
    ]
    stroked_polygon(ax, front_pts, C_BODY, ec="#0f1215", lw=1.5, zorder=5)

    # LED channel groove on front face (thin strip near base of front face)
    led_ch_y0 = 1.5
    led_ch_y1 = 4.5
    led_ch_pts = [
        (2,        led_ch_y0, 0),
        (wf - 2,   led_ch_y0, 0),
        (wf - 2,   led_ch_y1, 0),
        (2,        led_ch_y1, 0),
    ]
    filled_polygon(ax, led_ch_pts, C_LED_DIM, zorder=6, lw=0)

    # LED segments: 4 warm-white glowing dots on the front face
    led_y_center = (led_ch_y0 + led_ch_y1) / 2
    zone_widths = [wf / 4] * 4  # equal segments across front width
    for i in range(4):
        lx = (i + 0.5) * wf / 4
        lx2, ly2 = iso_p(lx, led_y_center, 0)
        glow_patch = Circle((lx2, ly2), radius=3.5,
                            color=C_LED_WARM, zorder=7, alpha=0.95)
        ax.add_patch(glow_patch)

    # ------------------------------------------------------------------ #
    #  6. Rubber feet (bottom, barely visible — front-left corner)        #
    # ------------------------------------------------------------------ #
    print("  Drawing rubber feet …")
    feet_positions = [
        (8,  DL - 8),
        (8,  8),
    ]
    for (fx, fz) in feet_positions:
        foot_pts = [
            (fx - 4, -2, fz - 4),
            (fx + 4, -2, fz - 4),
            (fx + 4, 0,  fz - 4),
            (fx - 4, 0,  fz - 4),
        ]
        filled_polygon(ax, foot_pts, C_RUBBER, zorder=3)

    # ------------------------------------------------------------------ #
    #  7. Top plate (brushed aluminium, gunmetal grey)                    #
    # ------------------------------------------------------------------ #
    print("  Drawing aluminium top plate …")
    tp_wf = wf - TP_INSET * 2
    tp_wr = wr - TP_INSET * 2
    TP_THICK = 2.0   # top plate sits 2 mm above ABS body top

    # Main top surface
    top_pts = [
        (TP_INSET,          hf + TP_THICK,  0),
        (TP_INSET + tp_wf,  hf + TP_THICK,  0),
        (TP_INSET + tp_wr,  hr + TP_THICK,  DL),
        (TP_INSET,          hr + TP_THICK,  DL),
    ]
    stroked_polygon(ax, top_pts, C_TOP, ec=C_TOP_LIGHT, lw=1.5, zorder=8)

    # Subtle brushed metal highlight strip (bright near the front edge)
    hl_pts = [
        (TP_INSET,          hf + TP_THICK,  0),
        (TP_INSET + tp_wf,  hf + TP_THICK,  0),
        (TP_INSET + tp_wf,  hf + TP_THICK,  20),
        (TP_INSET,          hf + TP_THICK,  20),
    ]
    filled_polygon(ax, hl_pts, C_TOP_HILIGHT, alpha=0.45, zorder=9)

    # Top plate front edge (thin strip facing viewer — the lip)
    tp_edge_pts = [
        (TP_INSET,          hf + TP_THICK,  0),
        (TP_INSET + tp_wf,  hf + TP_THICK,  0),
        (TP_INSET + tp_wf,  hf,             0),
        (TP_INSET,          hf,             0),
    ]
    filled_polygon(ax, tp_edge_pts, C_TOP_HILIGHT, alpha=0.8, zorder=9)

    # Top plate left edge
    tp_left_pts = [
        (TP_INSET,  hf + TP_THICK,  0),
        (TP_INSET,  hr + TP_THICK,  DL),
        (TP_INSET,  hr,             DL),
        (TP_INSET,  hf,             0),
    ]
    filled_polygon(ax, tp_left_pts, C_TOP_LIGHT, alpha=0.6, zorder=9)

    # ------------------------------------------------------------------ #
    #  8.  Zone pockets on the top plate                                  #
    # ------------------------------------------------------------------ #
    print("  Drawing zone pockets …")
    #  Top surface Y level (with slight depth offset for the pocket)
    surf_y = hf + TP_THICK

    # Helper to draw a circular/elliptical Qi pocket in isometric projection
    # We approximate the ellipse by projecting a circle in the x-z plane.
    def draw_zone_icon(ax, cx, cz, y_level, zone_num, zorder=11):
        """Draw a laser-etched-style icon for each zone type using geometric shapes."""
        ix, iy = iso_p(cx, y_level, cz)
        if zone_num == 1:
            # Phone: rounded rectangle
            r = mpatches.FancyBboxPatch(
                (ix - 5, iy - 8), 10, 14,
                boxstyle="round,pad=1.2", linewidth=1.0,
                edgecolor=C_ICON_FILL, facecolor="none",
                alpha=0.75, zorder=zorder,
            )
            ax.add_patch(r)
            ax.plot([ix - 2, ix + 2], [iy + 4, iy + 4],
                    color=C_ICON_FILL, lw=1.0, alpha=0.6, zorder=zorder)
        elif zone_num == 2:
            # Buds: two small circles side by side
            for dx in [-4.5, 4.5]:
                c = Circle((ix + dx, iy), radius=3.5,
                            edgecolor=C_ICON_FILL, facecolor="none",
                            linewidth=1.0, alpha=0.75, zorder=zorder)
                ax.add_patch(c)
            ax.plot([ix - 4.5, ix - 4.5, ix, ix, ix + 4.5, ix + 4.5],
                    [iy - 3.5, iy - 7, iy - 7, iy - 7, iy - 7, iy - 3.5],
                    color=C_ICON_FILL, lw=0.9, alpha=0.6, zorder=zorder)
        elif zone_num == 3:
            # Watch: rounded rectangle face + band stubs
            r = mpatches.FancyBboxPatch(
                (ix - 5, iy - 5), 10, 10,
                boxstyle="round,pad=1.0", linewidth=1.2,
                edgecolor=C_WATCH_RING, facecolor="none",
                alpha=0.85, zorder=zorder,
            )
            ax.add_patch(r)
            # Band stubs
            ax.plot([ix - 3, ix + 3], [iy - 7.5, iy - 7.5],
                    color=C_WATCH_RING, lw=1.8, alpha=0.7, zorder=zorder)
            ax.plot([ix - 3, ix + 3], [iy + 7.5, iy + 7.5],
                    color=C_WATCH_RING, lw=1.8, alpha=0.7, zorder=zorder)
            # Watch hands
            ax.plot([ix, ix], [iy, iy + 3.5],
                    color=C_WATCH_RING, lw=0.9, alpha=0.7, zorder=zorder)
            ax.plot([ix, ix + 2.5], [iy, iy],
                    color=C_WATCH_RING, lw=0.9, alpha=0.7, zorder=zorder)
        elif zone_num == 4:
            # Laptop: open lid shape
            # Base
            ax.plot([ix - 8, ix + 8], [iy - 3, iy - 3],
                    color=C_ICON_FILL, lw=1.4, alpha=0.75, zorder=zorder)
            # Screen (open lid)
            screen = mpatches.FancyBboxPatch(
                (ix - 7, iy - 2), 14, 10,
                boxstyle="round,pad=0.5", linewidth=1.0,
                edgecolor=C_ICON_FILL, facecolor="none",
                alpha=0.75, zorder=zorder,
            )
            ax.add_patch(screen)

    def draw_qi_zone(ax, cx, cz, r, label, zone_num, zorder=10):
        """Draw a circular Qi charging pocket at (cx, _, cz) on the top plate."""
        n = 48
        theta = np.linspace(0, 2 * math.pi, n)
        xs = cx + r * np.cos(theta)
        zs = cz + r * np.sin(theta)
        # Top rim
        rim_pts3d = [(float(x), surf_y, float(z)) for x, z in zip(xs, zs)]
        rim_pts2d = iso_pts(rim_pts3d, ox=OX, oy=OY)
        rim = Polygon(rim_pts2d, closed=True,
                      facecolor=C_ZONE_FILL, edgecolor=C_ZONE_EDGE,
                      linewidth=1.2, zorder=zorder)
        ax.add_patch(rim)

        # Inner Qi coil rings (3 concentric circles drawn as ellipses in iso)
        for scale_r in [0.72, 0.55, 0.38]:
            cr = r * scale_r
            xsi = cx + cr * np.cos(theta)
            zsi = cz + cr * np.sin(theta)
            ring_pts = [(float(x), surf_y, float(z)) for x, z in zip(xsi, zsi)]
            ring_pts2d = iso_pts(ring_pts, ox=OX, oy=OY)
            ring = Polygon(ring_pts2d, closed=True,
                           facecolor="none", edgecolor=C_ICON_FILL,
                           linewidth=0.8, alpha=0.6, zorder=zorder + 1)
            ax.add_patch(ring)

        # Zone icon above the Qi coil centre
        draw_zone_icon(ax, cx, cz, surf_y + 0.5, zone_num, zorder=zorder + 2)
        # Label
        icon_x, icon_y = iso_p(cx, surf_y + 0.5, cz)
        ax.text(icon_x, icon_y - 2, label,
                ha="center", va="top", fontsize=5.5, color=C_LABEL,
                fontfamily="sans-serif", fontweight="bold", zorder=zorder + 3)

        # Laser-etched zone number near the LED bar edge
        edge_x, edge_y = iso_p(cx, surf_y, cz + r + 4)
        ax.text(edge_x, edge_y, f"Z{zone_num}",
                ha="center", va="top", fontsize=4.5, color=C_LABEL,
                alpha=0.6, zorder=zorder + 2)

    # ---- Zone 1: Phone — left-front ----
    z1_cx, z1_cz = 32, 60     # centre on top plate
    draw_qi_zone(ax, z1_cx, z1_cz, r=22, label="PHONE", zone_num=1)

    # ---- Zone 2: Buds — centre ----
    z2_cx, z2_cz = 75, 60
    draw_qi_zone(ax, z2_cx, z2_cz, r=19, label="BUDS", zone_num=2)

    # ---- Zone 3: Watch cradle — rear-left ----
    print("  Drawing watch cradle (Zone 3) …")
    z3_cx, z3_cz = 32, 215
    # Teardrop shape: elongated ellipse, elevated pod, 30° tilt
    z3_r_maj = 24   # major axis (front-back)
    z3_r_min = 17   # minor axis (left-right)
    cradle_elev = 4.0  # mm elevated above top plate

    n = 48
    theta = np.linspace(0, 2 * math.pi, n)
    # Teardrop = cardioid-ish approximation: widen toward rear
    xs3 = z3_cx + z3_r_min * (1 + 0.18 * np.cos(theta)) * np.cos(theta)
    zs3 = z3_cz + z3_r_maj * np.sin(theta)
    td_pts2d = iso_pts(
        [(float(x), surf_y + cradle_elev, float(z)) for x, z in zip(xs3, zs3)],
        ox=OX, oy=OY,
    )
    td_base_pts2d = iso_pts(
        [(float(x), surf_y, float(z)) for x, z in zip(xs3, zs3)],
        ox=OX, oy=OY,
    )
    # Side wall of elevated cradle
    ax.add_patch(Polygon(td_base_pts2d, closed=True,
                          facecolor=C_BODY_SHADE, edgecolor=C_ZONE_EDGE,
                          linewidth=0.8, zorder=11))
    # Top surface of cradle
    ax.add_patch(Polygon(td_pts2d, closed=True,
                          facecolor=C_ZONE_FILL, edgecolor=C_WATCH_RING,
                          linewidth=1.2, zorder=12))
    # Watch ring
    n2 = 36
    th2 = np.linspace(0, 2 * math.pi, n2)
    wr2_r = 12
    xw = z3_cx + wr2_r * 0.85 * np.cos(th2)
    zw = z3_cz + wr2_r * np.sin(th2)
    watch_ring_pts = iso_pts(
        [(float(x), surf_y + cradle_elev + 0.5, float(z)) for x, z in zip(xw, zw)],
        ox=OX, oy=OY,
    )
    ax.add_patch(Polygon(watch_ring_pts, closed=True,
                          facecolor="none", edgecolor=C_WATCH_RING,
                          linewidth=2.0, zorder=13))
    # Labels
    w_label_x, w_label_y = iso_p(z3_cx, surf_y + cradle_elev + 1, z3_cz)
    draw_zone_icon(ax, z3_cx, z3_cz, surf_y + cradle_elev + 1, zone_num=3, zorder=14)
    ax.text(w_label_x, w_label_y - 2, "WATCH",
            ha="center", va="top", fontsize=5.5, color=C_LABEL,
            fontfamily="sans-serif", fontweight="bold", zorder=14)

    # ---- Zone 4: Laptop groove — rear-right ----
    print("  Drawing laptop groove (Zone 4) …")
    z4_cx  = 95     # centre-x of the groove slot (in the top plate area)
    z4_cz  = 235    # centre-z
    slot_w = 22     # 22 mm wide
    slot_l = 60     # 60 mm long (front-back)
    slot_d = 12     # 12 mm deep (below top plate)

    # Slot opening corners on top plate
    slot_top = [
        (z4_cx - slot_w / 2, surf_y,  z4_cz - slot_l / 2),
        (z4_cx + slot_w / 2, surf_y,  z4_cz - slot_l / 2),
        (z4_cx + slot_w / 2, surf_y,  z4_cz + slot_l / 2),
        (z4_cx - slot_w / 2, surf_y,  z4_cz + slot_l / 2),
    ]
    # Slot interior (silicone lining — slightly lighter black)
    slot_inner = [
        (z4_cx - slot_w / 2 + 1.5, surf_y - slot_d, z4_cz - slot_l / 2 + 2),
        (z4_cx + slot_w / 2 - 1.5, surf_y - slot_d, z4_cz - slot_l / 2 + 2),
        (z4_cx + slot_w / 2 - 1.5, surf_y - slot_d, z4_cz + slot_l / 2 - 2),
        (z4_cx - slot_w / 2 + 1.5, surf_y - slot_d, z4_cz + slot_l / 2 - 2),
    ]
    # Draw slot rim (dark opening)
    stroked_polygon(ax, slot_top, C_LAPTOP_SLOT, ec=C_ZONE_EDGE, lw=1.2, zorder=10)
    # Draw slot interior side walls (visible from isometric view)
    slot_left_wall = [
        slot_top[0], slot_top[3],
        slot_inner[3], slot_inner[0],
    ]
    stroked_polygon(ax, slot_left_wall, C_ZONE_FILL, ec=C_ZONE_EDGE, lw=0.8, zorder=10)
    slot_right_wall = [
        slot_top[1], slot_top[2],
        slot_inner[2], slot_inner[1],
    ]
    stroked_polygon(ax, slot_right_wall, C_BODY_SHADE, ec=C_ZONE_EDGE, lw=0.8, zorder=10)
    # Silicone inner floor
    stroked_polygon(ax, slot_inner, C_ZONE_FILL, ec=C_SI_EDGE, lw=0.6, zorder=10)

    # Laptop standing in the groove (thin slab)
    lap_thick = 8     # laptop body thickness (mm)
    lap_h     = 70    # visible laptop height above slot
    lap_body = [
        (z4_cx - lap_thick / 2, surf_y,          z4_cz - 28),
        (z4_cx + lap_thick / 2, surf_y,          z4_cz - 28),
        (z4_cx + lap_thick / 2, surf_y + lap_h,  z4_cz - 28),
        (z4_cx - lap_thick / 2, surf_y + lap_h,  z4_cz - 28),
    ]
    stroked_polygon(ax, lap_body, "#1c2028", ec="#404a56", lw=1, zorder=12)
    # Screen slightly recessed from the body
    screen_pts = [
        (z4_cx - lap_thick / 2 + 1, surf_y + 6,         z4_cz - 28),
        (z4_cx + lap_thick / 2 - 1, surf_y + 6,         z4_cz - 28),
        (z4_cx + lap_thick / 2 - 1, surf_y + lap_h - 4, z4_cz - 28),
        (z4_cx - lap_thick / 2 + 1, surf_y + lap_h - 4, z4_cz - 28),
    ]
    filled_polygon(ax, screen_pts, "#0a1825", zorder=13)
    # Screen glow
    scr_x, scr_y = iso_p(z4_cx, surf_y + lap_h / 2, z4_cz - 28)
    ax.scatter([scr_x], [scr_y], s=80, color="#1a3050", alpha=0.5, zorder=12)

    # Label
    lap_lx, lap_ly = iso_p(z4_cx, surf_y + 2, z4_cz)
    draw_zone_icon(ax, z4_cx, z4_cz, surf_y + 2, zone_num=4, zorder=14)
    ax.text(lap_lx, lap_ly - 2, "LAPTOP",
            ha="center", va="top", fontsize=5.5, color=C_LABEL,
            fontfamily="sans-serif", fontweight="bold", zorder=14)

    # ------------------------------------------------------------------ #
    #  9. LED bar labels below each zone (etched on top plate rim)        #
    # ------------------------------------------------------------------ #
    print("  Drawing LED zone labels …")
    zone_centers_x = [z1_cx, z2_cx, z3_cx, z4_cx]
    zone_labels     = ["PHONE", "BUDS", "WATCH", "LAPTOP"]
    led_label_z     = 8   # just behind the front lip

    for i, (lbl_cx, lbl) in enumerate(zip(zone_centers_x, zone_labels)):
        lx, ly = iso_p(lbl_cx, surf_y - 0.5, led_label_z)
        ax.text(lx, ly, lbl,
                ha="center", va="top", fontsize=4.8, color=C_LABEL,
                alpha=0.75, zorder=12)

    # ------------------------------------------------------------------ #
    # 10. Title text / brand / info                                       #
    # ------------------------------------------------------------------ #
    print("  Adding title text …")
    ax.text(0.5, 0.97, "Epitome Penta — Product Render",
            transform=ax.transAxes, ha="center", va="top",
            fontsize=14, fontweight="bold", color="#2c3540",
            fontfamily="sans-serif")
    ax.text(0.5, 0.93, "Arc Enclosure · Brushed Aluminium Top · 4-Zone Wireless Charging",
            transform=ax.transAxes, ha="center", va="top",
            fontsize=8, color="#607080")
    ax.text(0.5, 0.04, "Zone 1: 15W Qi Phone  ·  Zone 2: 15W Qi Buds  ·  Zone 3: Apple Watch Cradle  ·  Zone 4: 100W USB-C Laptop",
            transform=ax.transAxes, ha="center", va="bottom",
            fontsize=7.5, color="#607080")

    # Callout annotations
    callouts = [
        (z1_cx + 5,  surf_y + 2, 30,   "15W Qi\n(phone)"),
        (z2_cx + 5,  surf_y + 2, 50,   "15W Qi\n(buds)"),
        (z3_cx - 8,  surf_y + 5, 215,  "Watch\ncradle 30°"),
        (z4_cx + 15, surf_y + 1, 235,  "22mm groove\n(laptop spine)"),
    ]
    for (cx_c, cy_c, cz_c, txt) in callouts:
        tx, ty = iso_p(cx_c, cy_c, cz_c)
        ax.annotate(
            txt,
            xy=(tx, ty), xytext=(tx + 30, ty + 22),
            fontsize=6, color="#506070",
            arrowprops=dict(arrowstyle="-", color="#9ab0c0", lw=0.8),
            ha="left", va="bottom", zorder=15,
        )

    # LED bar callout
    led_x, led_y = iso_p(wf / 2, led_y_center, 0)
    ax.annotate(
        "WS2812B LED bar\n(warm white / amber)",
        xy=(led_x, led_y), xytext=(led_x - 60, led_y - 30),
        fontsize=6, color="#506070",
        arrowprops=dict(arrowstyle="-", color="#9ab0c0", lw=0.8),
        ha="right", va="top", zorder=15,
    )

    # Rear wordmark callout
    rw_x, rw_y = iso_p(wr / 2, hr / 2, DL)
    ax.annotate(
        '"Epitome Penta"\nwordmark (rear)',
        xy=(rw_x, rw_y), xytext=(rw_x + 35, rw_y - 20),
        fontsize=6, color="#506070",
        arrowprops=dict(arrowstyle="-", color="#9ab0c0", lw=0.8),
        ha="left", va="top", zorder=15,
    )


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    print("Epitome Penta image generator starting …")

    # Ensure output directory exists
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------------ #
    #  Create matplotlib figure                                           #
    # ------------------------------------------------------------------ #
    dpi = 150
    fig_w = CANVAS_W / dpi
    fig_h = CANVAS_H / dpi
    fig, ax = plt.subplots(figsize=(fig_w, fig_h), dpi=dpi)
    fig.patch.set_facecolor(C_BG)
    ax.set_facecolor(C_BG)
    ax.set_aspect("equal")
    ax.axis("off")

    # Set axes limits to match the dock's projected extents
    # (determined empirically; the iso projection centres around OX, OY)
    ax.set_xlim(50, CANVAS_W - 50)
    ax.set_ylim(50, CANVAS_H - 50)

    print("Rendering Epitome Penta geometry …")
    render(ax)

    # ------------------------------------------------------------------ #
    #  Save figure as intermediate PNG via PIL, then add LED glow         #
    # ------------------------------------------------------------------ #
    import io
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=dpi, bbox_inches="tight",
                facecolor=C_BG, pad_inches=0)
    buf.seek(0)
    base_img = Image.open(buf).convert("RGBA")
    plt.close(fig)

    # Resize to target canvas size
    base_img = base_img.resize((CANVAS_W, CANVAS_H), Image.LANCZOS)

    print("Adding LED glow effects …")
    # Compute screen positions of the 4 LED segments and add glow
    led_y_center_val = (1.5 + 4.5) / 2
    for i in range(4):
        lx = (i + 0.5) * wf / 4
        # Convert from iso to screen (note: figure is resized so we need to scale)
        iso_x, iso_y = iso_p(lx, led_y_center_val, 0)
        # Map from matplotlib data coords (50..1150, 50..750) to pixel coords (0..1200, 0..800)
        px = int((iso_x - 50) / (CANVAS_W - 100) * CANVAS_W)
        py = int(CANVAS_H - (iso_y - 50) / (CANVAS_H - 100) * CANVAS_H)
        r, g, b = 0xFF, 0xCC, 0x66  # warm amber
        add_glow(base_img, px, py, (r, g, b), radius=35, alpha=120)

    # Composite LED glow
    final_img = Image.alpha_composite(
        Image.new("RGBA", base_img.size, C_BG),
        base_img,
    ).convert("RGB")

    print(f"Saving render to {OUTPUT_PATH} …")
    final_img.save(OUTPUT_PATH, "PNG", optimize=True)
    print(f"✓  Saved {OUTPUT_PATH}  ({CANVAS_W}×{CANVAS_H} px)")


if __name__ == "__main__":
    main()
