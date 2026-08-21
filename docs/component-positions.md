# Epitome Penta Definitive Component Positions (0.01mm)

This file is the single source of truth for all physical placement coordinates.

## Coordinate System

- **X axis**: left(-) to right(+), centered at 0
- **Y axis**: front `Y=0.00`, rear `Y=300.00`
- **Z axis**: `Z=0.00` base floor, +Z up
- **All dimensions are in mm**

> Coordinate model remains revision-A based and is being normalized to dual-SKU width constraints.

## How to Read Coordinates

- Coordinates are center-points unless noted.

## Exterior / Top Surface

| Component | X (mm) | Y (mm) | Z (mm) | Notes |
|---|---:|---:|---:|---|
| Step 1 top centre (180×110×15) | -45.00 | 95.00 | 15.00 | Base of 3-step centre stack |
| Step 2 top centre (140×100×15) | -45.00 | 165.00 | 30.00 | Middle step |
| Step 3 top centre (100×80×15) | -45.00 | 228.00 | 45.00 | Top step |
| Zone 1 — Phone pad centre | -45.00 | 95.00 | 15.00 | 160×100 silicone surface, 20W |
| Zone 2 — Buds/Phone Qi dish centre | -45.00 | 165.00 | 30.00 | 90×65, 15W, front-middle of Step 2 |
| Zone 3 — Watch cradle pod base | -45.00 | 236.00 | 46.00 | Rear of Step 3, Apple puck + Qi watch coil |
| Zone 4 — Laptop slot centreline | +40.00 | 150.00 | — | 28mm opening, captive 220mm cable |
| Zone 5 — Tablet slot centreline | +80.00 | 150.00 | — | 20mm opening, captive 200mm cable |
| Zone 4 cable clip | +40.00 | 262.00 | 14.00 | Silicone clip above stop shelf |
| Zone 5 cable clip | +80.00 | 262.00 | 12.00 | Silicone clip above stop shelf |
| Zone 4 stop shelf | +40.00 | 256.00 | 8.00 | 5mm silicone-covered rear stop shelf |
| Zone 5 stop shelf | +80.00 | 256.00 | 8.00 | 5mm silicone-covered rear stop shelf |
| Right-angle IEC C13 inlet | 0.00 | 298.50 | 6.00 | Rear centered |

## Interior (from base floor up)

| Component | X (mm) | Y (mm) | Z (mm) | Notes |
|---|---:|---:|---:|---|
| 160W PSU module | +30.00 | 210.00 | 5.00 | Under laptop slot cavity |
| PCB main board | -35.00 | 110.00 | 5.00 | Core controller + monitors |
| Qi coil 1 (Phone) | -45.00 | 95.00 | 12.00 | Zone 1, centred under 160×100 surface |
| Qi coil 2 (Buds/Phone) | -45.00 | 165.00 | 27.00 | Zone 2 |
| Apple Watch puck module | -45.00 | 236.00 | 42.00 | Zone 3 |
| Zone 3 Qi watch coil | -45.00 | 232.00 | 42.00 | Zone 3 universal mode |
| USB-C PD board (Zone 4) | +40.00 | 150.00 | 3.00 | Feeds captive 220mm cable |
| USB-C PD board (Zone 5) | +80.00 | 150.00 | 3.00 | Feeds captive 200mm cable |
| INA3221 #1 region | -22.00 | 112.00 | 5.00 | Zones 1–3 monitor |
| INA3221 #2 region | -6.00 | 112.00 | 5.00 | Zones 4–5 + spare/system monitor |
| Step riser reinforcement #1 | -45.00 | 132.00 | 15.00 | Between Step 1 and Step 2 |
| Step riser reinforcement #2 | -45.00 | 204.00 | 30.00 | Between Step 2 and Step 3 |
| Step 3 rear cradle reinforcement | -45.00 | 246.00 | 45.00 | Watch cradle support |

## Premium Placement Rationale

- **Usability:** captive cable clips + stop shelves remove blind slot-port insertion.
- **Universal charging:** Zone 3 supports Apple magnetic and Qi watches.
- **Thermals:** PSU under laptop slot reduces heat near centre Qi surfaces.
- **3-step theatre:** 40mm taper per step gives clear visual hierarchy without reducing practical landing area.
- **SKU strategy:** Standard width launches first; XL extends slot span while preserving central zone geometry.
