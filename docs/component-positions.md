# Epitome Step — Component Positions

All coordinates in mm. Origin at bottom-left-front corner of base plate.
X: left → right | Y: front → rear | Z: bottom → top

Both models use identical positions. LED strip type noted where different.

---

## Riser cavity components (Z = 3 to Z = 25, flat-mounted)

| Component | X centre | Y centre | Z (board bottom) | Notes |
|---|---:|---:|---:|---|
| 12V buck converter | 20 | 50 | 5 | Flat, max 8 mm tall |
| 5V buck converter | 55 | 50 | 5 | Flat, max 8 mm tall |
| ATtiny85 (DIP-8 on strip socket) | 90 | 30 | 5 | |
| USB-C PD 60W trigger board | 120 | 70 | 5 | Aligned to Port A rear cutout |
| USB-C PD 30W trigger board | 140 | 70 | 5 | Aligned to Port B rear cutout |
| Zone 3 relay board | 82 | 80 | 5 | |
| Polyfuse strip (×5) | 30 | 20 | 5 | Laid horizontal |

---

## Rear face ports (Y = 100, Z = 15)

| Port | X | Z | Notes |
|---|---:|---:|---|
| DC barrel jack inlet | 40 | 15 | Panel-mount, male 5.5/2.5 mm |
| USB-C Port A (60W) | 120 | 15 | Panel-mount receptacle |
| USB-C Port B (30W) | 140 | 15 | Panel-mount receptacle |

---

## Charging zone components

| Component | X centre | Y centre | Z | Notes |
|---|---:|---:|---:|---|
| Qi2 20W coil (Zone 1) | 82.5 | 50 | 30 | Beneath Step 1 surface |
| Zone 1 silicone pad | 82.5 | 50 | 40 | 75 × 90 mm, 1 mm recess |
| NTC thermistor Zone 1 | 82.5 | 50 | 28 | Glued to coil underside |
| Qi 5W coil (Zone 2) | 82.5 | 50 | 44 | Beneath Step 2 surface |
| Zone 2 silicone pad | 82.5 | 50 | 55 | 65 × 50 mm flat |
| Apple Watch PCBA (Zone 3) | 75 | 60 | 59 | Beneath cradle |
| Qi watch coil (Zone 3) | 95 | 60 | 59 | Adjacent to Watch PCBA, relay-switched |
| Zone 3 watch cradle | 82.5 | 60 | 70 | 55 × 55 mm with lip |

---

## LED strip and diffuser

| Component | X start | X end | Z | Notes |
|---|---:|---:|---:|---|
| LED strip | 17.5 | 147.5 | 27 | 130 mm, 8 LEDs, behind diffuser |
| Frosted acrylic diffuser | 17.5 | 147.5 | 26 | 130 × 10 × 3 mm, front face of riser |

- **Walnut model:** WS2811 warm white strip
- **Obsidian model:** WS2812B RGB strip

---

## Obsidian-only: mode button

| Component | X | Y | Z | Notes |
|---|---:|---:|---:|---|
| Rear mode button (tactile) | 82.5 | 100 | 35 | Rear spine, centred |

---

## Bumpons

| Bumpon | X | Y | Z | Notes |
|---|---:|---:|---:|---|
| Front-left | 10 | 10 | 0 | Base underside |
| Front-right | 155 | 10 | 0 | Base underside |
| Rear-left | 10 | 90 | 0 | Base underside |
| Rear-right | 155 | 90 | 0 | Base underside |

