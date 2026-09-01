# Epitome

**Charge everything. Touch nothing.**

[epitomecharge.com](https://epitomecharge.com)

---

## Who we are

Epitome makes charging stands that look like they belong in your space. Wireless chargers are ugly — blobs of plastic that ruin a carefully considered desk or nightstand. Epitome is the alternative: handmade in small batches, designed around the materials and aesthetics of the setups people actually care about.

---

## The problem

You spent real money on your desk, your keyboard, your lamp. Then you put a $25 flat plastic puck in the middle of it and it ruins everything. Or you get a $130 Belkin stand that looks like it escaped from a hospital supply catalogue. Neither of these is acceptable.

---

## The solution — Epitome Step

A three-zone wireless charging stand shaped like a staircase. Each step charges one category of device. The whole thing is small (165 × 100 × 70 mm), intentional, and made to match your setup.

One product. Two models. Same electronics. Different aesthetic.

---

## Two models

| | **Step Walnut** | **Step Obsidian** |
|---|---|---|
| **Price** | $99 | $79 |
| **Step faces** | Oiled walnut (4 mm laser-cut) | Matte black ABS |
| **Base / riser** | Matte black ABS | Matte black ABS |
| **Edges** | Soft rounded | Sharp angular |
| **LED** | Warm white (WS2811, #FFD6A0) | Full RGB — 8 modes (WS2812B) |
| **RGB button** | — | Rear tactile button cycles modes |
| **Zone 1 — Phone** | Qi2 · 20W | Qi2 · 20W |
| **Zone 2 — Buds** | Qi · 5W | Qi · 5W |
| **Zone 3 — Watch** | Apple Watch + Qi · 5W | Apple Watch + Qi · 5W |
| **USB-C Port A** | 60W | 60W |
| **USB-C Port B** | 30W | 30W |
| **Footprint** | 165 × 100 × 70 mm | 165 × 100 × 70 mm |
| **In the box** | 100W USB-C brick + 3× USB-C cables | 100W USB-C brick + 3× USB-C cables |
| **Target buyer** | Neutral desk, plants, Grovemade keys | RGB setup, dark battlestation |

### Step Walnut — $99
Warm, premium, minimal. Oiled walnut faces catch the light. Warm white LEDs glow softly through a frosted diffuser. This is the dock that sits next to your coffee on a Saturday morning.

### Step Obsidian — $79
Dark, bold, colourful. Full matte black ABS throughout. RGB LEDs cycle through 8 colour modes — vivid blue, purple, green, red, cyan, yellow, white, off — controlled by a single rear button. This is the dock for the battlestation.

---

## Quick specs

| Spec | Value |
|---|---|
| Overall dimensions | 165 × 100 × 70 mm |
| Zone 1 (Phone, Step 1) | Qi2 20W, Z = 40 mm |
| Zone 2 (Buds, Step 2) | Qi 5W, Z = 55 mm |
| Zone 3 (Watch, Step 3) | Apple Watch + Qi 5W, Z = 70 mm |
| USB-C Port A (rear) | 60W PD |
| USB-C Port B (rear) | 30W PD |
| Power inlet | DC barrel jack (rear) |
| Included brick | 100W USB-C GaN |
| Included cables | 3× USB-C (1 for brick + 2 spare) |
| MCU | ATtiny85 |
| Night mode | LEDs off 23:00 – 07:00 |
| Soft power cap | 60W (ATtiny85 enforced) |

---

## Repo structure

```
README.md                   ← you are here
docs/
  design-spec.md            ← physical dimensions, step geometry, zones
  electronics.md            ← schematic, power paths, ATtiny85, LED differences
  bom.md                    ← full BOM + unit economics for both models
  enclosure.md              ← 3D print, laser cut, finishing specs
  wiring.md                 ← wiring guide, JST assignments
  component-positions.md    ← XYZ positions for all components
  layout-diagram.md         ← ASCII diagrams (top / front / side / rear)
  compatibility.md          ← device compatibility
  firmware-notes.md         ← ATtiny85 firmware, LED logic
  finishing-guide.md        ← walnut oiling + obsidian paint guide
  prototype-guide.md        ← batch 1 build guide (10 units)
  packaging.md              ← box, foam, brick, cables, belly band
  parts-tools-links.md      ← supplier links, tool list
  marketability.md          ← positioning, competitive landscape, channels
  uvp.md                    ← one-page UVP
  pre-order-page.md         ← Shopify copy for both models
  production-roadmap.md     ← batch plan and timeline
  app-spec.md               ← future features (Batch 2+)
  product-sheet.html        ← HTML comparison page
  render-guide.md           ← how to run the render scripts
scripts/
  generate_render.py        ← marketing render (walnut + obsidian)
  generate_image.py         ← hero product image (walnut + obsidian)
  generate_product_sheet.py ← product sheet (walnut + obsidian)
  generate_3d_model.py      ← technical diagrams
  requirements.txt
firmware/
  led_controller.h
  led_controller.cpp
assets/                     ← generated output images
```

---

## Running the render scripts

```bash
cd scripts
pip install -r requirements.txt

# All renders
python generate_render.py
python generate_image.py
python generate_product_sheet.py
python generate_3d_model.py

# Single model
python generate_render.py --model walnut
python generate_render.py --model obsidian
```

Output files appear in `assets/`:
- `step-walnut-render.png` / `step-obsidian-render.png`
- `step-walnut-hero.png` / `step-obsidian-hero.png`
- `step-walnut-product-sheet.png` / `step-obsidian-product-sheet.png`
- `step-technical-top.png` / `step-technical-side.png`

---

[epitomecharge.com](https://epitomecharge.com)
