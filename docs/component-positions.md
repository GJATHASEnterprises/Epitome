# Quad-Dock Definitive Component Positions (0.01mm)

This file is the single source of truth for all physical placement coordinates.

## Coordinate System

- **X axis**: left(-) to right(+), centered at 0
  - Front width: 110.00mm (`X=-55.00..+55.00`)
  - Rear width: 140.00mm (`X=-70.00..+70.00`)
  - Width by depth: `W(Y)=110+30*(Y/300)`
- **Y axis**: front `Y=0.00`, rear `Y=300.00`
- **Z axis**: `Z=0.00` is base floor (underside rubber-feet reference plane), +Z up
  - Height by depth: `H(Y)=12+10*(Y/300)`
- **All coordinates are center-points unless explicitly noted**
- **All dimensions are in mm and held to 0.01mm**

## How to Read Coordinates

- A feature marked `X=-20.00, Y=70.00` is 20mm left of centerline at 70mm depth from front edge.
- Features tied to taper use `H(Y)` so they remain physically correct on the wedge.
- “Cutout bottom at Z=1.00” means a vertical feature anchored from the enclosure floor reference.

## Exterior / Top Surface

| Component | X (mm) | Y (mm) | Z (mm) | Notes |
|---|---:|---:|---:|---|
| Zone 1 — Phone Qi dish centre | -20.00 | 70.00 | 14.83 | Rounded rect 80×55 R10, 2.50 deep, front-left premium reach zone |
| Zone 1 — Silicone lining | -20.00 | 70.00 | 12.63 | 78×53 R9, 2.20 deep, anti-slip and anti-scratch |
| Zone 2 — Buds Qi dish centre | +20.00 | 70.00 | 14.83 | Rounded rect 65×55 R10, 2.50 deep, front-right symmetry |
| Zone 2 — Silicone lining | +20.00 | 70.00 | 12.63 | 63×53 R9, 2.20 deep |
| Zone 3 — Watch cradle pod base | -22.00 | 225.00 | 21.00 | Ø50 cylinder+cone pod, 18 tall, 30° tilt toward front |
| Zone 4 — Laptop groove | +29.00 | 294.00 | rear-wall centered | 22 wide × 12 deep, X:+18..+40, Y:288..300 |
| IEC C13 inlet | 0.00 | 298.50 | 6.00 | Rear centered, 28×20 cutout, cutout bottom at Z=1 |
| Label: PHONE | -28.00 | 93.00 | 16.70 | 6mm etched text, centered over Zone 1 |
| Label: BUDS | +12.00 | 93.00 | 16.70 | 6mm etched text |
| Label: WATCH | -38.00 | 203.00 | 20.37 | 6mm etched text |
| Label: LAPTOP | +10.00 | 260.00 | 22.27 | 6mm etched text |
| Wordmark: Quad-Dock | -18.00 | 278.00 | 22.87 | 8mm etched rear wordmark |
| M3 screw hole left | -35.00 | 150.00 | top plate through | Ø3.20 through top plate |
| M3 screw hole right | +30.00 | 150.00 | top plate through | Ø3.20 through top plate |
| Rubber foot FL | -39.17 | 15.00 | -1.50 | Ø15, H=3 (centroid at Z=-1.50) |
| Rubber foot FR | +39.17 | 15.00 | -1.50 | Ø15, H=3 |
| Rubber foot RL | -53.50 | 285.00 | -1.50 | Ø15, H=3 |
| Rubber foot RR | +53.50 | 285.00 | -1.50 | Ø15, H=3 |
| LED section 1 (PHONE) | -108.75 | -2.00 | 1.50 | 71×8×3 emissive warm white |
| LED section 2 (BUDS) | -35.25 | -2.00 | 1.50 | 71×8×3 |
| LED section 3 (WATCH) | +38.25 | -2.00 | 1.50 | 71×8×3 |
| LED section 4 (LAPTOP) | +111.75 | -2.00 | 1.50 | 71×8×3 |
| LED diffuser strip | 0.00 | -2.00 | 1.50 | 290×8×3 frosted strip |

## Interior (from base floor up)

| Component | X (mm) | Y (mm) | Z (mm) | Notes |
|---|---:|---:|---:|---|
| 180W PSU module | 0.00 | 210.00 | 5.00 | 150×80×35 on 5mm standoffs, keeps CG rear-stable |
| PCB main board | -5.00 | 110.00 | 5.00 | 120×80, X:-65..+55, Y:70..150 on 5mm standoffs |
| ESP32-C3 Mini | -15.00 | 85.00 | 8.50 | 18×20 on PCB, short control-path routing |
| INA3221 | +20.00 | 95.00 | 8.50 | 10×10 on PCB |
| INA219 | +30.00 | 110.00 | 8.50 | 8×8 on PCB near PD branch |
| BH1750 | -40.00 | 80.00 | 8.50 | 8×13 near PCB edge for ambient exposure |
| 3.3V LDO | -5.00 | 100.00 | 8.50 | 5×5 SMD on PCB |
| Bulk cap 470µF | +10.00 | 75.00 | 9.00 | Ø10×12 at PSU rail entry |
| Qi coil 1 (Phone) | -20.00 | 70.00 | 4.00 | Ø54×5 in dedicated pocket |
| Qi coil 2 (Buds) | +20.00 | 70.00 | 4.00 | Ø54×5 in dedicated pocket |
| N52 ring magnets Zone 1 | -20.00 | 70.00 | 7.50 | Ø54 ring, 2 thick above Qi coil 1 |
| Watch puck module | -22.00 | 225.00 | 4.00 | Ø34×5 below watch cradle |
| USB-C PD board | +32.00 | 155.00 | 5.00 | 40×30, X:+12..+52, Y:140..170 |
| USB-C port (Zone 4, exterior) | +29.00 | 297.00 | 8.00 | Flush in laptop groove zone |
| Polyfuse Zone 1 | -20.00 | 75.00 | 8.50 | SMD near Qi1 lead-in |
| Polyfuse Zone 2 | +20.00 | 75.00 | 8.50 | SMD near Qi2 lead-in |
| Polyfuse Zone 3 | -15.00 | 115.00 | 8.50 | SMD watch power branch |
| Polyfuse Zone 4 | +35.00 | 120.00 | 8.50 | SMD PD branch |
| NTC thermistor Zone 1 | -25.00 | 65.00 | 4.50 | Under Qi coil 1 |
| NTC thermistor Zone 2 | +25.00 | 65.00 | 4.50 | Under Qi coil 2 |
| NTC thermistor Zone 3 | -22.00 | 220.00 | 4.50 | Under watch puck |
| IEC C13 inlet interior face | 0.00 | 297.00 | 11.00 | Internal panel-mount connection plane |
| Vent slot row 1, slot 1 | -20.00 | 25.00 | -1.25 | 40×4×2.5 underside recess |
| Vent slot row 1, slot 2 | -20.00 | 45.00 | -1.25 | 40×4×2.5 underside recess |
| Vent slot row 1, slot 3 | -20.00 | 65.00 | -1.25 | 40×4×2.5 underside recess |
| Vent slot row 1, slot 4 | -20.00 | 85.00 | -1.25 | 40×4×2.5 underside recess |
| Vent slot row 2, slot 1 | +20.00 | 25.00 | -1.25 | 40×4×2.5 underside recess |
| Vent slot row 2, slot 2 | +20.00 | 45.00 | -1.25 | 40×4×2.5 underside recess |
| Vent slot row 2, slot 3 | +20.00 | 65.00 | -1.25 | 40×4×2.5 underside recess |
| Vent slot row 2, slot 4 | +20.00 | 85.00 | -1.25 | 40×4×2.5 underside recess |

## Premium Placement Rationale

- **Spacing:** front charging zones are symmetric for visual balance and daily ergonomics.
- **Thermal management:** PSU, vents, and coil regions are separated to reduce local hotspots.
- **Signal integrity:** sensor and monitor ICs sit near controlled branches to keep traces short and stable.
- **Manufacturability:** all coordinates map cleanly to CNC/laser/print workflows with ±0.10mm tolerance target.
