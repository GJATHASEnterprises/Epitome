# Quad-Dock — 5-Zone Enclosure Specification

## Core Envelope

- Length: **300.00mm**
- Front width: **110.00mm**
- Rear width: **140.00mm**
- Front height: **12.00mm**
- Rear height: **22.00mm**
- Corner radius: **R20.00mm**

Coordinate model used everywhere: see [component-positions.md](component-positions.md).

## Definitive Component Positions

All exact feature coordinates are locked in [component-positions.md](component-positions.md).

Critical zone anchors now fixed to:

- **Zone 1 (Phone dish):** `X=-45.00, Y=60.00`
- **Zone 2 (Buds dish):** `X=-45.00, Y=140.00`
- **Zone 3 (Watch cradle):** `X=-45.00, Y=225.00`
- **Zone 4 (Laptop groove):** `X=+40.00, Y=15..285`, **22mm wide**
- **Zone 5 (iPad/Phone groove):** `X=+80.00, Y=15..285`, **18mm wide**

## Top-Side Features

- Zone 1 dish: rounded rect **80×55 R10**, depth **2.50mm**, silicone insert **78×53 R9**, depth **2.20mm**
- Zone 2 dish: rounded rect **65×55 R10**, depth **2.50mm**, silicone insert **63×53 R9**, depth **2.20mm**
- Zone 3 pod: **Ø50** cylinder + cone, total **18mm** above plate, **30°** tilt toward front
- Zone 4 groove: **22mm** wide × **12mm** deep, silicone-lined, USB‑C interface in groove
- Zone 5 groove: **18mm** wide × **12mm** deep, silicone-lined, USB‑C port in groove
- Rear inlet: IEC C13 **28×20mm** cutout centered on rear wall, bottom at **Z=1.00mm**

## Fastening and Bottom Features

- M3 clearance holes: **Ø3.20mm** at `(-60.00,150.00)` and `(+60.00,150.00)`
- 4 rubber feet: **Ø15×3mm** at the definitive coordinates in [component-positions.md](component-positions.md)
- 8 underside vent slots: **40×4×2.5mm** at definitive coordinates

## Materials

- Base: matte ABS
- Top plate: 1.5mm aluminium (gunmetal brushed)
- Silicone contact zones: dark grey, anti-slip/anti-scratch
