# Step — Render & Asset Generation Guide

All assets are generated using Python scripts with matplotlib and numpy. No Blender required.

---

## Scripts and Outputs

| Script | Output | Purpose |
|---|---|---|
| `generate_render.py` | `assets/step-render.png` | Marketing render, dark background |
| `generate_product_sheet.py` | `assets/step-product-sheet.png` | Two-panel product sheet |
| `generate_image.py` | `assets/step-hero.png` | Hero product image, light background |
| `generate_3d_model.py` | `assets/step-top-view.dxf` | DXF top-view layout |

---

## Running Scripts

```bash
cd /path/to/repo

# Marketing render (1200×800px dark)
python scripts/generate_render.py

# Hero product image (1200×800px light)
python scripts/generate_image.py

# Product sheet (1200×800px, two-panel)
python scripts/generate_product_sheet.py

# DXF top view + geometry summary
python scripts/generate_3d_model.py
```

---

## Dependencies

```
matplotlib
numpy
```

Install: `pip install matplotlib numpy`

See `scripts/requirements.txt` for pinned versions.

---

## Asset Descriptions

- **step-render.png** — Isometric marketing render. Dark background (#111111). Shows three-step dock with device silhouettes and zone colour glows. Use for README header and product listings.
- **step-product-sheet.png** — Two-panel product sheet. Left panel: isometric dock render. Right panel: spec panel with zone list and pricing. Use for social media and pre-order page.
- **step-hero.png** — Clean isometric view, light grey background. No text labels. Use for Etsy and Shopify product photos.
- **step-top-view.dxf** — DXF top-view drawing with step outlines, zone pads, and port positions. Load in Inkscape or send to laser cutter as layout reference.

---

## Coordinate System (Scripts)

All scripts use the same coordinate system as the design spec:
- X=0 left edge, X=165 right edge
- Y=0 front, Y=100 rear
- Z=0 base floor, up = +Z
- Scale factor S=0.025 in scripts (mm → figure units)
