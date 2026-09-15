# Epitome Step — Component Positions

All coordinates in mm. Origin at bottom-left-front corner of base plate.
X: left → right | Y: front → rear | Z: bottom → top

Both Step models use identical core positions; lighting and the Obsidian mode button vary by model.

---

## Riser cavity components (Z = 3 to Z = 25, flat-mounted)

| Component | X centre | Y centre | Z (board bottom) | Notes |
|---|---:|---:|---:|---|
| Raw DC distribution PCB / block | 20 | 70 | 5 | Screw-terminal power fan-out from the 20V input rail |
| USB-C PD input trigger board | 40 | 70 | 5 | Aligned to the rear USB-C IN cutout; negotiates 20V input |
| 12V buck converter (screw-terminal) | 20 | 50 | 5 | Flat, max 8 mm tall |
| 5V buck converter (screw-terminal) | 55 | 50 | 5 | Flat, max 8 mm tall |
| Digispark-style ATtiny85 USB board | 90 | 30 | 5 | Shared MCU for both Step models |
| USB-C PD 60W trigger board | 120 | 70 | 5 | Aligned to Port A rear cutout |
| USB-C PD 30W trigger board | 140 | 70 | 5 | Aligned to Port B rear cutout |
| Zone 3 relay board | 82 | 80 | 5 | |
| Polyfuse strip (×5) | 30 | 20 | 5 | Laid horizontal |

---

## Rear face ports (Y = 100, Z = 15)

| Port | X | Z | Notes |
|---|---:|---:|---|
| USB-C IN (PD power) | 40 | 15 | Panel-mount receptacle; differentiate with deeper recess or engraved **IN** |
| USB-C Port A (60W) | 120 | 15 | Panel-mount receptacle |
| USB-C Port B (30W) | 140 | 15 | Panel-mount receptacle |

---

## Charging zone components

| Component | X centre | Y centre | Z | Notes |
|---|---:|---:|---:|---|
| Qi2 20W coil (Zone 1) | 82.5 | 50 | 30 | Beneath Step 1 surface |
| Zone 1 silicone pad | 82.5 | 50 | 40 | 75 × 90 mm, 1 mm recess |
| NTC thermistor Zone 1 | 82.5 | 50 | 28 | Pre-crimped, glued to coil underside |
| Qi 5W coil (Zone 2) | 82.5 | 50 | 44 | Beneath Step 2 surface |
| Zone 2 silicone pad | 82.5 | 50 | 55 | 65 × 50 mm flat |
| Apple Watch PCBA (Zone 3) | 75 | 60 | 59 | Beneath cradle |
| Qi watch coil (Zone 3) | 95 | 60 | 59 | Adjacent to Watch PCBA, relay-switched |
| Zone 3 watch cradle | 82.5 | 60 | 70 | 55 × 55 mm with lip |

---

## Lighting

| Component | X start | X end | Z | Notes |
|---|---:|---:|---:|---|
| Walnut status light pipe | 81 | 84 | 14 | Front face, single white LED behind pipe |
| Obsidian left LED strip | 16 | 149 | 27 | Pre-wired WS2812B strip, 8 LEDs |
| Obsidian right LED strip | 16 | 149 | 27 | Pre-wired WS2812B strip, 8 LEDs |
| Obsidian diffuser bars | 16 | 149 | 26 | Flush side diffusers |

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
