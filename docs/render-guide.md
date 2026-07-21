# Generating the Product Render

## Requirements
Blender 4.0+ (free) — https://www.blender.org/download/

## Run
blender --background --python scripts/generate_render.py

## Output
assets/quad-dock-render.png — 2400x1600px photorealistic render

## Notes
- First run: 5–15 minutes depending on GPU/CPU
- Uses Cycles ray tracing renderer
- GPU (NVIDIA CUDA or Apple Metal) used automatically if available
- Re-run any time the design changes
