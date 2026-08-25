# Generating the Penta Dock Renders and Product Sheet

## Running All 4 Scripts

```bash
cd scripts
pip install -r requirements.txt
python generate_3d_model.py
python generate_render.py
python generate_product_sheet.py
python generate_image.py
```

> **Note:** `generate_render.py` requires Blender. Run it with:
> ```bash
> blender --background --python scripts/generate_render.py
> ```
> The other three scripts (`generate_3d_model.py`, `generate_product_sheet.py`, `generate_image.py`) run with plain Python — no Blender required.

## Outputs

All outputs appear in the `/output` folder (or `/assets/` for PNG renders and `/assets/export/` for STL/DXF):

| Script | Output |
|---|---|
| `generate_render.py` | `assets/penta-dock-render.png` |
| `generate_product_sheet.py` | `assets/penta-dock-product-sheet.png` |
| `generate_image.py` | `assets/penta-dock-hero.png` |
| `generate_3d_model.py` | `assets/export/penta-dock-base.stl`, `penta-dock-top-plate.dxf`, etc. |

## What to Do With the Outputs

- **penta-dock-render.png** — High-quality Blender render. Use for README header and marketing materials.
- **penta-dock-product-sheet.png** — Technical product sheet. Use for social media posts and pre-order page.
- **penta-dock-hero.png** — Lightweight isometric image. Use for quick social media posts.
- **penta-dock-top-plate.dxf** — Laser cutting reference. Load in Inkscape or send to Pumping Station One.
- **STL files** — 3D print reference geometry. Load in Bambu Studio or PrusaSlicer.

## Blender Render Details

- **Command:** `blender --background --python scripts/generate_render.py`
- **Output:** `assets/penta-dock-render.png`
- **Expected Runtime:** CPU-only: typically 45–180 minutes

## Scene Contents (generate_render.py)

- 3-step staircase geometry with Zone 4 laptop slot on left, Zone 5 tablet slot on right
- Zone labels: PHONE 20W Qi2, BUDS/PHONE 20W Qi, WATCH 5W, LAPTOP 100W USB-C, TABLET 45W USB-C
- Total output annotation: 190W
- LED strip: per-zone colours (Zone 1 blue, Zone 2 purple, Zone 3 green, Zone 4 orange, Zone 5 blue)
- Colour scheme: matte black / Obsidian
- Title: "Penta Dock" and "One dock. Every device."

Coordinate source of truth: [component-positions.md](component-positions.md)

## Troubleshooting

- **ModuleNotFoundError:** Run `pip install [module name]` for the missing module, or run `pip install -r scripts/requirements.txt` to install all dependencies.
- **Blender not found:** Install Blender from blender.org and ensure `blender` is in your PATH.
- **ezdxf unavailable:** DXF/SVG export will be skipped with a warning. Install with `pip install ezdxf`.
- **Output folder missing:** The scripts create the output directory automatically. If you see a permissions error, ensure you have write access to the `assets/` directory.
