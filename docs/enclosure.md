# Epitome Penta — 5-Zone Enclosure Specification

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
- **Zone 5 (iPad/Phone groove):** `X=+64.00, Y=60..285`, **18mm wide**
  <!-- Zone 5 position reasoning: Zone 4 right edge X=+51 (centre +40, width 22mm). 6mm structural wall → Zone 5 left edge X=+57. Width 18mm → centre X=+64, right edge X=+71. At rear Y=285 half-width=69.25mm, right edge +71 just fits ✅. At Y=60 half-width=58mm, right edge +71 just fits ✅. Groove starts at Y=60 (not Y=15) because at Y<60 the taper clips the right edge. -->

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
