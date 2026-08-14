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

- Captive USB-C cable indicators in Zone 4 and Zone 5 slots
- Zone 3 rear watch cradle with dual charging intent (Apple puck + Qi support)
- Zone 2 pad at front of Step 2 (90×65, 15W)
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
