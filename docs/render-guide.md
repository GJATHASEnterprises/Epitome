# Generating the Product Render

## Command

```bash
blender --background --python scripts/generate_render.py
```

## Output

- `assets/quad-dock-render.png`
- Cycles, **4800×3200**, **512 samples**, PNG 16-bit

## Expected Runtime

- CPU-only: typically **45–180 minutes** at full quality
- GPU acceleration can reduce runtime significantly

## Scene Contents

The render includes all exterior production features:

- Exact tapered rounded-trapezoid wedge body
- Zone 1 and Zone 2 rounded-rectangle dishes + silicone liners
- Zone 3 tilted watch cradle pod + visible watch puck
- Zone 4 laptop groove with silicone lining + USB-C port
- Front LED diffuser + 4 warm-white emissive LED sections
- Raised dark labels and rear Quad-Dock wordmark mesh
- Rear IEC C13 inlet housing mesh
- Coiled/stowed power cord behind dock
- Rubber feet visible under the body

Coordinate source of truth: [component-positions.md](component-positions.md)

## Product Sheet (Fast — No Blender Required)

```bash
python scripts/generate_product_sheet.py
```

Output: `assets/quad-dock-product-sheet.png`  
Time: ~5 seconds
