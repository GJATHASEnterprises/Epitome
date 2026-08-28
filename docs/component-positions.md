# Penta Dock — Definitive Component Positions (0.01mm)

> **Note: Coordinates revised for compact 250×100×100mm footprint, on-edge slot geometry, and PSU under centre platform.**

This file is the single source of truth for all physical placement coordinates.

## Coordinate System

- **Dock envelope:** ~250mm wide × ~100mm deep × ~98mm tall
- **X axis:** left edge = `X=0`, right edge = `X=250` (absolute coordinates, not centred)
- **Y axis:** front `Y=0.00`, rear `Y=100.00`
- **Z axis:** `Z=0.00` base floor, +Z up
- **All dimensions are in mm**

## Z Height Stack Reference

| Z position | What is here |
|---|---|
| Z=0 | Base plate floor |
| Z=3 | Base plate top / PSU resting surface |
| Z=33 | PSU top (30mm PSU height) |
| Z=50 | Step 1 base / riser cavity top |
| Z=65 | Step 1 top / Step 2 base |
| Z=80 | Step 2 top / Step 3 base |
| Z=95 | Step 3 top (watch cradle surface) |
| Z=98 | Approximate overall dock height |

> Riser cavity = **Z=33 to Z=50 = 17mm** clearance.

## How to Read Coordinates

- Coordinates are center-points unless noted.
- Slot and panel entries use the centre of their primary occupied volume unless a face is called out in the notes.

## Exterior / Top Surface

| Component | X (mm) | Y (mm) | Z (mm) | Notes |
|---|---:|---:|---:|---|
| Step 1 top centre (180×100) | 125.00 | 50.00 | 65.00 | Base step top surface, full front-to-back depth |
| Step 2 top centre (140×100) | 125.00 | 50.00 | 80.00 | Middle step top surface, same front face as Step 1 |
| Step 3 top centre (100×80) | 125.00 | 60.00 | 95.00 | Top step, set back 20mm from front (Y=20 to Y=100) |
| Zone 1 — Phone pad centre | 125.00 | 50.00 | 65.00 | 160×100mm silicone surface, 20W Qi2, 1mm recessed dish |
| Zone 2 — Buds/phone dish centre | 125.00 | 50.00 | 80.00 | 90×70mm dish, 20W Qi, same front face as Step 1 |
| Zone 3 — Watch cradle | 125.00 | 60.00 | 95.00 | Apple puck + Qi watch coil, on Step 3 (set back) |
| Zone 4 — Laptop slot centreline | 17.50 | 50.00 | 47.50 | X=0 to X=35, 35mm wide, 90mm deep, 95mm tall |
| Zone 5 — Tablet slot centreline | 232.50 | 50.00 | 37.50 | X=215 to X=250, 20mm wide, 70mm deep, 80mm tall |
| Rear spine plate | 125.00 | 99.00 | 49.00 | Full-width rear structural face |
| Front fascia strip | 125.00 | 1.50 | 10.00 | Full-width front base strip |
| IEC C13 inlet cutout | 45.00 | 99.00 | 49.00 | Rear-left position for short AC wire run |

## Interior (from base floor up)

| Component | X (mm) | Y (mm) | Z (mm) | Notes |
|---|---:|---:|---:|---|
| PSU (Mean Well LRS-200-24, 199×98×30mm) | 103.00 | 49.00 | 18.00 | Offset 6mm to laptop side: X=4 to X=203. Y=1 to Y=99. Z=3 to Z=33 |
| PSU cavity perimeter wall | 103.00 | 49.00 | 26.50 | Encloses PSU under raised centre platform |
| ATtiny85 controller | 100.00 | 42.00 | 40.00 | Mounted flat in 17mm riser cavity |
| Hardware relay (Zone 3) | 115.00 | 42.00 | 40.00 | Mounted flat in riser cavity, adjacent to ATtiny85 |
| 12V buck ×1 (Zone 1 Qi2) | 80.00 | 35.00 | 36.00 | Mounted flat in riser cavity |
| 12V buck ×2 (Zone 2 Qi) | 80.00 | 65.00 | 36.00 | Mounted flat in riser cavity |
| 5V buck (Zone 3 + logic) | 100.00 | 55.00 | 36.00 | Mounted flat in riser cavity |
| Qi2 coil (Zone 1 Phone) | 125.00 | 50.00 | 62.00 | Inside Step 1 body under recessed silicone |
| Qi coil (Zone 2 Buds/phone) | 125.00 | 50.00 | 77.00 | Inside Step 2 body under 90×70 dish |
| Apple Watch puck module | 125.00 | 60.00 | 92.00 | Inside Step 3 body |
| Qi watch coil (Zone 3) | 125.00 | 58.00 | 92.00 | Inside Step 3 body, adjacent to puck |
| USB-C PD 100W board (Zone 4) | 17.50 | 70.00 | 60.00 | Inner wall of laptop slot, wired to captive cable at top |
| USB-C PD 45W board (Zone 5) | 232.50 | 55.00 | 45.00 | Inner wall of tablet slot, wired to captive cable at top |

## Component Mounting Rule

> **Riser cavity mounting rule:** All components in the riser cavity (Z=33 to Z=50, 17mm clearance) must be mounted **flat/horizontal** against the cavity floor. Buck converters, ATtiny85, and relay boards must not stand upright. JST connectors should exit sideways not upward. This ensures clearance under Step 1 base at Z=50.
