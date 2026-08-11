# Epitome Penta Definitive Component Positions (0.01mm)

This file is the single source of truth for all physical placement coordinates.

## Coordinate System

- **X axis**: left(-) to right(+), centered at 0
  - Front width: 146.00mm (`X=-73.00..+73.00`)
  - Rear width: 156.00mm (`X=-78.00..+78.00`)
  - Width by depth: `W(Y)=146+10*(Y/300)`
- **Y axis**: front `Y=0.00`, rear `Y=300.00`
- **Z axis**: `Z=0.00` is base floor (underside rubber-feet reference plane), +Z up
  - Height by depth: `H(Y)=16+10*(Y/300)`
- **All coordinates are center-points unless explicitly noted**
- **All dimensions are in mm and held to 0.01mm**

> **Zone 5 correction note:** Zone 5 was originally documented at X=+80 which falls outside the tapered top surface. Corrected first to X=+64, then finalised at X=+66 after widening the enclosure to front 146mm / rear 156mm — the wider body allows Zone 5 centre at X=+66 (right edge X=+75) with groove starting at Y=60 to stay within the enclosure boundary at all depths.

> **Groove-clearance note:** For clearance budgeting, the front-face reference is **Z=6.00mm** at `Y=0.00` (`16mm` front height with `10mm` groove depth). The actual groove floors begin at about **Z=6.50mm** for Zone 4 (`Y=15.00`) and **Z=8.00mm** for Zone 5 (`Y=60.00`), then rise with the enclosure taper to about **Z=11.00mm** at the PD-board depth (`Y=150.00`). These groove-floor Z values use the same base-floor reference plane defined above (`Z=0.00` is the base floor / underside rubber-feet reference plane). Any part taller than the local groove-floor height directly under Zone 4 / Zone 5 grooves must be shifted into the left half or lowered clear of the groove underside.
>
> **Collision-avoidance note:** INA219 Zone 4/5 and Polyfuse Zone 4/5 were moved into the left half, and both USB-C PD boards were lowered to `Z=3.00`, to avoid collision with the groove underside (front groove-floor reference `Z=6.00`).

## How to Read Coordinates

- A feature marked `X=-45.00, Y=60.00` is 45mm left of centerline at 60mm depth from front edge.
- Features tied to taper use `H(Y)` so they remain physically correct on the wedge.
- “Cutout bottom at Z=1.00” means a vertical feature anchored from the enclosure floor reference.

## Exterior / Top Surface

| Component | X (mm) | Y (mm) | Z (mm) | Notes |
|---|---:|---:|---:|---|
| Zone 1 — Phone Qi dish centre | -45.00 | 60.00 | 14.50 | Rounded rect 80×55 R10, 2.50 deep, left-half front zone |
| Zone 1 — Silicone lining | -45.00 | 60.00 | 12.30 | 78×53 R9, 2.20 deep, anti-slip and anti-scratch |
| Zone 2 — Buds Qi dish centre | -45.00 | 140.00 | 17.17 | Rounded rect 65×55 R10, 2.50 deep, stacked above phone zone |
| Zone 2 — Silicone lining | -45.00 | 140.00 | 14.97 | 63×53 R9, 2.20 deep |
| Zone 3 — Watch cradle pod base | -45.00 | 225.00 | 21.00 | Ø50 base tapering to Ø28 top, tapered pedestal with slight concave waist, 3mm retaining rim, 18 tall, 30° tilt toward front |
| Zone 4 — Laptop groove centre | +40.00 | 150.00 | right-half | 22mm wide spine slot, Y:15..285, silicone-lined |
| Zone 5 — iPad/Phone groove centre | +66.00 | 150.00 | right-half | 18mm wide spine slot, Y:60..285, silicone-lined |
| Zone 4 — USB-C port (exterior) | +40.00 | 258.00 | 8.00 | Within groove 1, aligned to slot |
| Zone 5 — USB-C port (exterior) | +66.00 | 258.00 | 8.00 | Within groove 2, aligned to slot |
| IEC C13 inlet | 0.00 | 298.50 | 6.00 | Rear centered, 28×20 cutout, cutout bottom at Z=1 |
| Label: PHONE | -45.00 | 78.00 | 15.20 | 6mm etched text, centered over Zone 1 |
| Label: BUDS | -45.00 | 158.00 | 17.87 | 6mm etched text |
| Label: WATCH | -45.00 | 247.00 | 21.73 | 6mm etched text |
| Label: LAPTOP | +40.00 | 95.00 | 18.17 | 6mm etched text |
| Label: iPAD/PHONE | +66.00 | 95.00 | 18.17 | 6mm etched text |
| Wordmark: Epitome Penta | 0.00 | 278.00 | 22.87 | 8mm etched rear wordmark |
| M3 screw hole left | -60.00 | 150.00 | top plate through | Ø3.20 through top plate |
| M3 screw hole right | +60.00 | 150.00 | top plate through | Ø3.20 through top plate |
| Rubber foot FL | -39.17 | 15.00 | -1.50 | Ø15, H=3 (centroid at Z=-1.50) |
| Rubber foot FR | +39.17 | 15.00 | -1.50 | Ø15, H=3 |
| Rubber foot RL | -53.50 | 285.00 | -1.50 | Ø15, H=3 |
| Rubber foot RR | +53.50 | 285.00 | -1.50 | Ø15, H=3 |
| LED section 1 (PHONE) | -116.00 | -2.00 | 1.50 | 56×8×3 emissive warm white |
| LED section 2 (BUDS) | -58.00 | -2.00 | 1.50 | 56×8×3 |
| LED section 3 (WATCH) | 0.00 | -2.00 | 1.50 | 56×8×3 |
| LED section 4 (LAPTOP) | +58.00 | -2.00 | 1.50 | 56×8×3 |
| LED section 5 (iPAD/PHONE) | +116.00 | -2.00 | 1.50 | 56×8×3 |
| LED diffuser strip | 0.00 | -2.00 | 1.50 | 290×8×3 frosted strip |

## Interior (from base floor up)

| Component | X (mm) | Y (mm) | Z (mm) | Notes |
|---|---:|---:|---:|---|
| 180W PSU module | 0.00 | 210.00 | 5.00 | 150×80×35 on 5mm standoffs, keeps CG rear-stable |
| PCB main board | -35.00 | 110.00 | 5.00 | 120×80, X:-95..+25, Y:70..150 on 5mm standoffs for left-half electronics layout |
| ESP32-C3 Mini | -45.00 | 85.00 | 8.50 | 18×20 on PCB, short control-path routing |
| INA3221 | -10.00 | 95.00 | 8.50 | 10×10 on PCB |
| INA219 Zone 4 | -20.00 | 110.00 | 8.50 | 8×8 relocated into left half to clear Zone 4 groove underside |
| INA219 Zone 5 | -20.00 | 150.00 | 8.50 | 8×8 relocated into left half to clear Zone 5 groove underside |
| BH1750 | -70.00 | 80.00 | 8.50 | 8×13 near PCB edge for ambient exposure |
| 3.3V LDO | -35.00 | 100.00 | 8.50 | 5×5 SMD on PCB |
| Bulk cap 470µF | -20.00 | 75.00 | 9.00 | Ø10×12 at PSU rail entry |
| Qi coil 1 (Phone) | -45.00 | 60.00 | 4.00 | Ø54×5 in dedicated pocket |
| Qi coil 2 (Buds) | -45.00 | 140.00 | 4.00 | Ø44×5 in dedicated pocket |
| N52 ring magnets Zone 1 | -45.00 | 60.00 | 7.50 | Ø54 ring, 2 thick above Qi coil 1 |
| Watch puck module | -45.00 | 225.00 | 4.00 | Ø34×5 below watch cradle |
| USB-C PD board (Zone 4) | +40.00 | 150.00 | 3.00 | 40×30, X:+20..+60, Y:135..165 intentionally remains in the right-half electronics bay beneath the groove on low-profile 3mm standoffs; board top ~Z=7, below the local groove floor (~Z=11 at Y=150) |
| USB-C PD 20W board (Zone 5) | +66.00 | 150.00 | 3.00 | 18×20 compact board, X:+57..+75, Y:140..160 intentionally remains in the right-half electronics bay beneath the groove on low-profile 3mm standoffs; board top ~Z=7, below the local groove floor (~Z=11 at Y=150) |
| USB-C port (Zone 4, exterior) | +40.00 | 258.00 | 8.00 | Within groove 1, aligned to the spine slot |
| USB-C port (Zone 5, exterior) | +66.00 | 258.00 | 8.00 | Within groove 2, aligned to the spine slot |
| Polyfuse Zone 1 | -45.00 | 65.00 | 8.50 | SMD near Qi1 lead-in |
| Polyfuse Zone 2 | -45.00 | 145.00 | 8.50 | SMD near Qi2 lead-in |
| Polyfuse Zone 3 | -45.00 | 220.00 | 8.50 | SMD watch power branch |
| Polyfuse Zone 4 | -25.00 | 130.00 | 8.50 | SMD PD branch relocated into left half to clear Zone 4 groove underside |
| Polyfuse Zone 5 | -25.00 | 150.00 | 8.50 | SMD PD branch relocated into left half to clear Zone 5 groove underside |
| NTC thermistor Zone 1 | -50.00 | 55.00 | 4.50 | Under Qi coil 1 |
| NTC thermistor Zone 2 | -40.00 | 135.00 | 4.50 | Under Qi coil 2 |
| NTC thermistor Zone 3 | -45.00 | 220.00 | 4.50 | Under watch puck |
| NTC thermistor Zone 5 | +66.00 | 145.00 | 4.50 | Under Zone 5 port area |
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

- **Spacing:** the dock now supports **5 zones** with three parallel guide lines on the right half: laptop at `X=+40` and the new iPad/phone groove at `X=+66`, separated by a 6mm structural wall (Zone 4 right edge X=+51, wall X=+51..+57, Zone 5 left edge X=+57, centre X=+66, right edge X=+75). Enclosure widened to front 146mm / rear 156mm to accommodate all zones within the top surface.
- **Thermal management:** PSU, vents, coil regions, and the two USB-C PD branches are separated to reduce local hotspots.
- **Signal integrity:** sensor and monitor ICs sit near controlled branches to keep traces short and stable.
- **Manufacturability:** all coordinates map cleanly to CNC/laser/print workflows with ±0.10mm tolerance target.
