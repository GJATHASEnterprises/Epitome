# Epitome Step — Component Positions

All coordinates in mm. Origin at bottom-left-front corner of base plate.
X: left → right | Y: front → rear | Z: bottom → top

Both Step models use identical core positions; lighting and Obsidian mode button vary by model.

---

## Riser cavity components (Z = 3 to Z = 25, flat-mounted)

| Component | X centre | Y centre | Z (board bottom) | Notes |
|---|---:|---:|---:|---|
| 20V distribution PCB / block | 20 | 70 | 5 | Screw-terminal power fan-out |
| USB-C PD input trigger board | 40 | 70 | 5 | Rear USB-C IN cutout |
| 12V buck converter (screw-terminal) | 20 | 50 | 5 | Feeds Zone 1 + Zone 2 |
| 5V buck converter (screw-terminal) | 55 | 50 | 5 | Feeds Zone 3 + control |
| Digispark-style ATtiny85 USB board | 90 | 30 | 5 | Shared MCU |
| USB-C PD 15W output trigger board | 130 | 70 | 5 | Rear OUT cutout |
| Polyfuse strip | 30 | 20 | 5 | Branch protection |

---

## Rear face ports (Y = 100, Z = 15)

| Port | X | Z | Notes |
|---|---:|---:|---|
| USB-C IN (PD power) | 40 | 15 | Differentiate with deeper recess or engraved **IN** |
| USB-C OUT (15W) | 130 | 15 | Panel-mount receptacle |

---

## Charging zone components

| Component | X centre | Y centre | Z | Notes |
|---|---:|---:|---:|---|
| Qi2 20W coil (Zone 1) | 82.5 | 50 | 30 | Beneath Step 1 surface |
| Zone 1 silicone pad | 82.5 | 50 | 40 | 75 × 90 mm, 1 mm recess |
| Qi TX up-to-15W coil (Zone 2) | 82.5 | 50 | 44 | Beneath Step 2 surface |
| Zone 2 silicone pad | 82.5 | 50 | 55 | 65 × 50 mm flat |
| Watch TX coil (Zone 3) | 82.5 | 60 | 59 | Generic default, MFi optional |
| Zone 3 watch cradle | 82.5 | 60 | 70 | 55 × 55 mm with lip |
