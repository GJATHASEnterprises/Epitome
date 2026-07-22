# Quad-Dock — Enclosure Specification

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

- **Zone 1 (Phone dish):** `X=-20.00, Y=70.00`
- **Zone 2 (Buds dish):** `X=+20.00, Y=70.00`
- **Zone 3 (Watch cradle base):** `X=-22.00, Y=225.00`
- **Zone 4 (Laptop groove):** `X=+29.00, Y=294.00` (feature range `X:+18..+40, Y:288..300`)

## Top-Side Features

- Zone 1 dish: rounded rect **80×55 R10**, depth **2.50mm**, silicone insert **78×53 R9**, depth **2.20mm**
- Zone 2 dish: rounded rect **65×55 R10**, depth **2.50mm**, silicone insert **63×53 R9**, depth **2.20mm**
- Zone 3 pod: **Ø50** cylinder + cone, total **18mm** above plate, **30°** tilt toward front
- Zone 4 groove: **22mm** wide × **12mm** deep, silicone-lined, USB‑C interface in groove
- Rear inlet: IEC C13 **28×20mm** cutout centered on rear wall, bottom at **Z=1.00mm**

## Fastening and Bottom Features

- M3 clearance holes: **Ø3.20mm** at `(-35.00,150.00)` and `(+30.00,150.00)`
- 4 rubber feet: **Ø15×3mm** at the definitive coordinates in [component-positions.md](component-positions.md)
- 8 underside vent slots: **40×4×2.5mm** at definitive coordinates

## Materials

- Base: matte ABS
- Top plate: 1.5mm aluminium (gunmetal brushed)
- Silicone contact zones: dark grey, anti-slip/anti-scratch
