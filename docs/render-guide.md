# Generating the Product Render

## Command

```bash
blender --background --python scripts/generate_render.py
```

## Output

- `assets/epitome-penta-render.png`

## Expected Runtime

- CPU-only: typically 45–180 minutes

## Scene Contents

The render brief should now include:

- Captive USB-C cable indicators in Zone 4 and Zone 5 slots (Zone 4 cable is 220mm)
- 3-step tapered centre platform:
  - Step 1 (180×110×15) with 160×100 full silicone 20W phone surface
  - Step 2 (140×100×15) with 90×65 buds/phone pad (15W)
  - Step 3 (100×80×15) with rear raised watch cradle (Apple puck + Qi)
- Brushed aluminium riser faces on each step with reinforcement intent
- Slot stop shelves and rear cable clips
- Right-angle rear IEC C13 inlet routing downward
- PSU placement represented under laptop slot cavity
- **Two SKU renders:** Standard (~530mm width) and XL (~700mm width)
- **Three color renders:** Black, White, Midnight Blue

Coordinate source of truth: [component-positions.md](component-positions.md)

## Product Sheet (Fast — No Blender Required)

```bash
python scripts/generate_product_sheet.py
```

Output: `assets/epitome-penta-product-sheet.png`
