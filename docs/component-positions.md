# Epitome Penta Definitive Component Positions (0.01mm)

> **Note: Coordinates revised for compact 250×100×100mm footprint, on-edge slot geometry, and PSU under centre platform.**

This file is the single source of truth for all physical placement coordinates.

## Coordinate System

- **Dock envelope:** ~250mm wide × ~100mm deep × ~100mm tall
- **X axis:** left(-) to right(+), centered at 0
- **Y axis:** front `Y=0.00`, rear `Y=100.00`
- **Z axis:** `Z=0.00` base floor, +Z up
- **All dimensions are in mm**

## Z Height Stack Reference

| Z position | What is here |
|---|---|
| Z=0 | Base plate floor |
| Z=3 | Base plate top / PSU resting surface |
| Z=33 | PSU top |
| Z=50 | Step 1 base / riser cavity top |
| Z=65 | Step 1 top / Step 2 base |
| Z=80 | Step 2 top / Step 3 base |
| Z=95 | Step 3 top |
| Z=98 | Approximate overall dock height |

## How to Read Coordinates

- Coordinates are center-points unless noted.
- Slot and panel entries use the centre of their primary occupied volume unless a face is called out in the notes.

## Exterior / Top Surface

| Component | X (mm) | Y (mm) | Z (mm) | Notes |
|---|---:|---:|---:|---|
| Step 1 top centre (180×110×15) | -45.00 | 50.00 | 65.00 | Base step top surface |
| Step 2 top centre (140×100×15) | -45.00 | 50.00 | 80.00 | Middle step top surface |
| Step 3 top centre (100×80×15) | -45.00 | 50.00 | 95.00 | Top step / watch presentation surface |
| Zone 1 — Phone pad centre | -45.00 | 50.00 | 65.00 | 160×100 silicone surface, 20W Qi |
| Zone 2 — Buds or second phone dish centre | -45.00 | 50.00 | 80.00 | 120×80 dish, 20W Qi |
| Zone 3 — Watch cradle pod base | -45.00 | 65.00 | 95.00 | Apple puck + Qi watch coil region |
| Zone 4 — Laptop slot centreline | +85.00 | 45.00 | 47.50 | 35mm wide, 90mm deep, 400mm long, 95mm tall; captive cable hangs from top |
| Zone 5 — Tablet slot centreline | -105.00 | 35.00 | 37.50 | 20mm wide, 70mm deep, 290mm long, 75mm tall; captive cable hangs from top |
| Rear spine plate | 0.00 | 98.50 | 49.00 | Full-width rear structural face, Z=0 to Z=98 |
| Front fascia strip | 0.00 | 1.50 | 10.00 | Full-width front base strip, Z=0 to Z=20 |
| Right-angle IEC C13 inlet cutout | 0.00 | 98.50 | 49.00 | Rear spine centered |

## Interior (from base floor up)

| Component | X (mm) | Y (mm) | Z (mm) | Notes |
|---|---:|---:|---:|---|
| 201W PSU module (Mean Well LRS-200-24) | 0.00 | 50.00 | 3.00 | Under centre platform, 199×98×30mm, centred |
| PSU cavity perimeter wall | -45.00 | 50.00 | 26.50 | Supports raised centre platform body over PSU |
| ESP32-C3 SuperMini | -22.00 | 42.00 | 40.00 | Mounted in riser cavity, keep antenna clear |
| INA3221 #1 | -8.00 | 42.00 | 42.00 | Mounted in riser cavity for Zones 1–3 monitor |
| INA3221 #2 | 8.00 | 42.00 | 42.00 | Mounted in riser cavity for Zones 4–5 + spare |
| Qi coil 1 (Phone) | -45.00 | 50.00 | 62.00 | Inside Step 1 body, under silicone surface |
| Qi coil 2 (Buds or second phone) | -45.00 | 50.00 | 77.00 | Inside Step 2 body, centred under 120×80 dish |
| Apple Watch puck module | -45.00 | 65.00 | 92.00 | Inside Step 3 body |
| Zone 3 Qi watch coil | -45.00 | 62.00 | 92.00 | Inside Step 3 body, adjacent to puck |
| USB-C PD 100W trigger board (Zone 4) | +85.00 | 70.00 | 60.00 | Mounted on inner wall of laptop slot, wired to captive cable at top |
| USB-C PD 45W trigger board (Zone 5) | -105.00 | 55.00 | 45.00 | Mounted on inner wall of tablet slot, wired to captive cable at top |
| Step 1 base plane | -45.00 | 50.00 | 50.00 | Bottom of Step 1 / top of riser cavity |
| Step 2 base plane | -45.00 | 50.00 | 65.00 | Bottom of Step 2 |
| Step 3 base plane | -45.00 | 50.00 | 80.00 | Bottom of Step 3 |

## Premium Placement Rationale

- **Usability:** captive cable hangs from the top of each slot so devices plug in naturally during insertion.
- **Universal charging:** Zone 3 still supports both Apple magnetic charging and generic Qi watch charging in the same top step.
- **Thermals:** PSU under the centre platform stays physically separated from the slot zones while the 20mm riser cavity preserves wiring clearance.
- **Compactness:** rear spine and front fascia let the dock stay within a ~250×100×100mm footprint without sacrificing step or slot function.
- **Serviceability:** ESP32-C3 and INA3221 boards stay in the riser cavity for short, flat I2C runs and easier access.
