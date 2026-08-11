# Epitome Penta — 5-Zone Enclosure Specification

## Core Envelope

- Length: **300.00mm**
- Front width: **146.00mm**
- Rear width: **156.00mm**
- Front height: **16.00mm**
- Rear height: **26.00mm**
- Corner radius: **R20.00mm**

> **Width note:** Front width was increased from 110mm to 146mm and rear width from 140mm to 156mm to accommodate all 5 zones within the top surface boundary. With the original 110/140mm sizing, Zone 5 (right edge X=+75) fell outside the tapered surface at the front. The new width formula `W(Y) = 146 + 10*(Y/300)` ensures Zone 5's right edge at X=+75 stays within the half-width of 74mm at Y=60 (the groove start depth).
>
> **Structural-clearance note:** Front/rear heights were increased to **16/26mm**, so `H(Y)=16+10*(Y/300)`, and Zone 4/5 groove depths were reduced to **10mm** (from 12mm) to ensure 4–6mm of solid material below groove floor.

Coordinate model used everywhere: see [component-positions.md](component-positions.md).

## Definitive Component Positions

All exact feature coordinates are locked in [component-positions.md](component-positions.md).

Critical zone anchors now fixed to:

- **Zone 1 (Phone dish):** `X=-45.00, Y=60.00`
- **Zone 2 (Buds dish):** `X=-45.00, Y=140.00`
- **Zone 3 (Watch cradle):** `X=-45.00, Y=225.00`
- **Zone 4 (Laptop groove):** `X=+40.00, Y=15..285`, **22mm wide**
- **Zone 5 (iPad/Phone groove):** `X=+66.00, Y=60..285`, **18mm wide**
  <!-- Zone 5 position reasoning: Zone 4 right edge X=+51 (centre +40, width 22mm). 6mm structural wall → Zone 5 left edge X=+57. Width 18mm → centre X=+66, right edge X=+75. Enclosure widened to front 146mm / rear 156mm (W(Y)=146+10*(Y/300)), half-width at Y=60 = 73+5*(60/300) = 74mm → right edge +75 just fits ✅. Groove starts at Y=60 (not Y=15) because at Y<60 the half-width is less than 74mm. -->

## Top-Side Features

- Zone 1 dish: rounded rect **80×55 R10**, depth **2.50mm**, silicone insert **78×53 R9**, depth **2.20mm**
- Zone 2 dish: rounded rect **65×55 R10**, depth **2.50mm**, silicone insert **63×53 R9**, depth **2.20mm**
- Zone 3 pod: **Ø50** base tapering to **Ø28** top, tapered pedestal with slight concave waist, **3mm** retaining rim at top, **18mm** above plate, **30°** tilt toward front
- Zone 4 groove: **22mm** wide × **10mm** deep, silicone-lined, USB‑C interface in groove
- Zone 5 groove: **18mm** wide × **10mm** deep, silicone-lined, USB‑C port in groove
- Rear inlet: IEC C13 **28×20mm** cutout centered on rear wall, bottom at **Z=1.00mm**

## Fastening and Bottom Features

- M3 clearance holes: **Ø3.20mm** at `(-60.00,150.00)` and `(+60.00,150.00)`
- 4 rubber feet: **Ø15×3mm** at the definitive coordinates in [component-positions.md](component-positions.md)
- 8 underside vent slots: **40×4×2.5mm** at definitive coordinates

## Materials

- Base: matte ABS
- Top plate: 1.5mm aluminium (gunmetal brushed)
- Silicone contact zones: dark grey, anti-slip/anti-scratch
