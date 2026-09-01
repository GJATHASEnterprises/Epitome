# Epitome Step — Render Guide

How to run all four render scripts and use the outputs.

---

## Setup

```bash
cd scripts
pip install -r requirements.txt
```

All scripts use only standard Python + `Pillow` (PIL). No Blender, no 3D renderer, no external tools required.

---

## Scripts and outputs

### 1. `generate_render.py` — Marketing render

Produces labelled isometric renders with device silhouettes, LED glow, and zone labels.

```bash
python generate_render.py              # both models
python generate_render.py --model walnut
python generate_render.py --model obsidian
```

**Output:**
- `assets/step-walnut-render.png` — 1200 × 800 px, dark background (#111111)
- `assets/step-obsidian-render.png` — 1200 × 800 px, dark background (#0a0a0a)

**Use for:** Etsy listing secondary image, Reddit post, product page gallery.

---

### 2. `generate_image.py` — Hero product image

Clean isometric product shot. No labels, no text. Pure product photography style.

```bash
python generate_image.py              # both models
python generate_image.py --model walnut
python generate_image.py --model obsidian
```

**Output:**
- `assets/step-walnut-hero.png` — 1200 × 800 px, warm light background (#F5F0E8)
- `assets/step-obsidian-hero.png` — 1200 × 800 px, dark background (#0d0d0d)

**Use for:** Etsy listing primary image, Shopify product hero, Instagram.

---

### 3. `generate_product_sheet.py` — Product sheet

Two-panel layout: left panel is dock render with labels, right panel is spec sheet text. Fully readable at 1200 × 800 px.

```bash
python generate_product_sheet.py              # both models
python generate_product_sheet.py --model walnut
python generate_product_sheet.py --model obsidian
```

**Output:**
- `assets/step-walnut-product-sheet.png` — 1200 × 800 px
- `assets/step-obsidian-product-sheet.png` — 1200 × 800 px

**Use for:** Shopify product description, Etsy listing image 2–4, social media comparison post.

---

### 4. `generate_3d_model.py` — Technical diagrams

Engineering drawing style. Dimension arrows, zone labels, exact mm measurements.

```bash
python generate_3d_model.py
```

**Output:**
- `assets/step-technical-top.png` — 1200 × 900 px top view with dimensions
- `assets/step-technical-side.png` — 900 × 900 px side cross-section with dimensions

**Use for:** Design documentation, prototype guide, supplier communication.

---

## How to use the outputs

| Image | Platform | Purpose |
|---|---|---|
| `step-walnut-hero.png` | Etsy listing image 1, Shopify hero | Primary product shot |
| `step-walnut-render.png` | Etsy image 2, Reddit post | Labelled render showing zones |
| `step-walnut-product-sheet.png` | Etsy image 3, Shopify gallery | Spec sheet for informed buyers |
| `step-obsidian-hero.png` | Obsidian Etsy/Shopify primary | Dark product shot |
| `step-obsidian-render.png` | Reddit battlestations, Instagram | RGB glow visible |
| `step-obsidian-product-sheet.png` | Obsidian spec sheet | |
| `step-technical-top.png` | Docs, supplier PDFs | Engineering reference |
| `step-technical-side.png` | Docs, supplier PDFs | Engineering reference |

---

## Regenerating after design changes

If you change the physical dimensions in `docs/design-spec.md`, update the corresponding constants at the top of each script before regenerating:

- `generate_render.py` — `STEP_W`, `STEP_D`, `STEP_H` constants
- `generate_image.py` — same constants
- `generate_product_sheet.py` — same constants
- `generate_3d_model.py` — `DIM_*` constants

All four scripts share the same geometry. Change them consistently.

