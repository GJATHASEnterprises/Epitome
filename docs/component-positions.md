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
| Zone 1 — Phone Qi dish centre | -45.00 | 60.00 | 14.50 | 90×65, 15W |
| Zone 2 — Buds/Phone Qi dish centre | -45.00 | 140.00 | 17.17 | 90×65, 15W, front edge of Step 2 |
| Zone 3 — Watch cradle pod base | -45.00 | 228.00 | 21.00 | Rear of Step 2, Apple puck + Qi watch coil |
| Zone 4 — Laptop slot centreline | +40.00 | 150.00 | — | 28mm opening, captive 300mm cable |
| Zone 5 — Tablet slot centreline | +80.00 | 150.00 | — | 20mm opening, captive 200mm cable |
| Zone 4 cable clip | +40.00 | 262.00 | 14.00 | Silicone clip above stop shelf |
| Zone 5 cable clip | +80.00 | 262.00 | 12.00 | Silicone clip above stop shelf |
| Zone 4 stop shelf | +40.00 | 256.00 | 8.00 | 5mm silicone-covered rear stop shelf |
| Zone 5 stop shelf | +80.00 | 256.00 | 8.00 | 5mm silicone-covered rear stop shelf |
| Right-angle IEC C13 inlet | 0.00 | 298.50 | 6.00 | Rear centered |

## Interior (from base floor up)

| Component | X (mm) | Y (mm) | Z (mm) | Notes |
|---|---:|---:|---:|---|
| 180W PSU module | +30.00 | 210.00 | 5.00 | **Relocated under laptop slot cavity** |
| PCB main board | -35.00 | 110.00 | 5.00 | Core controller + monitors |
| Qi coil 1 (Phone) | -45.00 | 60.00 | 4.00 | Zone 1 |
| Qi coil 2 (Buds/Phone) | -45.00 | 140.00 | 4.00 | Zone 2 |
| Apple Watch puck module | -45.00 | 226.00 | 4.00 | Zone 3 |
| Zone 3 Qi watch coil | -45.00 | 220.00 | 4.00 | Zone 3 universal mode |
| USB-C PD board (Zone 4) | +40.00 | 150.00 | 3.00 | Feeds captive 300mm cable |
| USB-C PD board (Zone 5) | +80.00 | 150.00 | 3.00 | Feeds captive 200mm cable |
| Step-riser reinforcement | -10.00 | 180.00 | 12.00 | Internal ribbing/insert region |

## Premium Placement Rationale

- **Usability:** captive cable clips + stop shelves remove blind slot-port insertion.
- **Universal charging:** Zone 3 supports Apple magnetic and Qi watches.
- **Thermals:** PSU moved beneath laptop slot, reducing heat exposure near centre Qi surfaces.
- **SKU strategy:** Standard width launches first; XL extends slot span while preserving central zone geometry.
