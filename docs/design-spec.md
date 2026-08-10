# Epitome Penta — Design Specification

> **Note:** This file provides a summary of the product spec. For detailed specifications see:
> - [Enclosure Specification](enclosure.md) — Arc design, dimensions, materials, zone layout, LED system
> - [Electronics Specification](electronics.md) — ESP32-C3, all ICs, power architecture, sensors
> - [Definitive Component Positions](component-positions.md) — exact X/Y/Z coordinates for all exterior/interior features
> - [Packaging Specification](packaging.md) — in-box contents, cable bundle, warranty card
> - [Firmware Notes](firmware-notes.md) — night mode behaviour and timing source

---

## Product Name
Epitome Penta

## Color Variants
- **Black** — Gunmetal brushed aluminum top, matte black soft-touch ABS base
- **White** — Silver brushed aluminum top, matte white soft-touch ABS base

---

## Physical Dimensions

| Dimension | Value |
|-----------|-------|
| Length | 300mm |
| Width (front edge) | 110mm |
| Width (rear edge) | 140mm |
| Height (front edge) | 12mm |
| Height (rear edge) | 22mm |
| Corner radius | R20mm (all edges) |

---

## Enclosure Design ("Arc")

Smooth curved wedge — wide at rear, slightly narrower at front. Zero sharp corners. R20mm radius on all edges.

- **Top plate:** 1.5mm brushed aluminum — Gunmetal (Black model), Silver (White model). Laser-etched zone icons and Epitome Penta wordmark.
- **Base:** Soft-touch matte ABS — Black or White. Laser cut + bent for Batch 1; injection mold from Batch 2.
- **Zone pockets:** Silicone-lined recessed dishes and grooves replacing exposed accessory clutter.
- **Watch cradle:** Teardrop-shaped elevated pod, rear-left, 30° tilt toward user.
- **Laptop groove:** Right half, `X=+40`, **22mm** wide × **12mm** deep, silicone-lined.
- **iPad/phone groove:** Right half beside laptop groove, `X=+80`, **18mm** wide × **12mm** deep, silicone-lined.
- **LED system:** WS2812B strip hidden under front lip with frosted diffuser. **5 sections** divided by recessed lines. Laser-etched zone icons above each section.
- **Assembly:** Snap-fit base + 2× M3 screws only.
- **Cooling:** Vents on base.
- **Top plate:** Removable for service access.

---

## Zone Layout

Exact zone anchors:
- Zone 1: `X=-45.00, Y=60.00`
- Zone 2: `X=-45.00, Y=140.00`
- Zone 3: `X=-45.00, Y=225.00`
- Zone 4: groove centered at `X=+40.00`, `Y=15..285`
- Zone 5: groove centered at `X=+80.00`, `Y=15..285`

```
         ← 300mm →
+---------------------------------------------------------+  ← rear (140mm wide, 22mm high)
|  [⌚ ZONE 3 — Watch]   [💻 ZONE 4 — Laptop] [📱 ZONE 5 — iPad/Phone] |
|  Teardrop pod          Vertical spine        Parallel USB-C groove    |
|  30° tilt, rear-left   22mm groove           18mm groove              |
+---------------------------------------------------------+  ← arc taper
|  [📱 ZONE 1 — Phone]                [🎧 ZONE 2 — Buds]               |
|  15W Qi + magnets                   5W Qi                            |
+-[■ PHONE ■|■ BUDS ■|■ WATCH ■|■ LAPTOP ■|■ iPAD ■]------------------+
← front (110mm wide, 12mm high) →
                   IEC C13 inlet (rear centre)
```

---

## Zone Specifications

### Zone 1 — Phone (Qi 15W)
- 50mm Qi TX coil, 15W
- N52 ring magnets for phone alignment (MagSafe-style)
- Silicone-lined recessed dish

### Zone 2 — Buds / Phone (Qi 5W)
- Qi charging zone, 5W target budget
- Works for AirPods (Qi case) or a second phone
- Silicone-lined recessed dish

### Zone 3 — Apple Watch
- Apple Watch magnetic puck (wired internally)
- 5W output
- Teardrop cradle, 30° tilt, rear-left position
- Compatible: Apple Watch Series 1–9, SE, Ultra

### Zone 4 — Laptop / USB-C PD (100W)
- USB-C PD, up to 100W
- Laptop groove: 22mm wide × 12mm deep, silicone-lined
- Laptop stands vertically on its spine
- Compatible: any USB-C laptop (2018+)

### Zone 5 — iPad / Phone / USB-C PD (20W)
- USB-C PD 2.0, up to 20W
- Groove: 18mm wide × 12mm deep, silicone-lined
- Intended for iPad, Android phone, or secondary USB-C device
- Protected by dedicated INA219 + polyfuse + NTC branch

---

## LED Status System

| State | Color | Meaning |
|-------|-------|---------|
| Charging | Red | Device charging on that zone |
| Full | Green | Device fully charged |
| Empty | Off | No device detected |

Night mode turns all zone LEDs off between 23:00–07:00 unless a zone is actively drawing more than 0.5W.

---

## Electronics Summary

See [electronics.md](electronics.md) for full spec.

- **MCU:** ESP32-C3 Mini (WiFi + BLE, flashed via onboard USB)
- **Power monitors:** INA3221 (Zones 1–3), INA219 (Zone 4), INA219 (Zone 5)
- **Ambient light:** BH1750 (I2C)
- **LED:** WS2812B strip (20 LEDs, 4 per zone)
- **Charging:** 2× Qi (Zones 1–2), Watch puck 5W (Zone 3), USB-C PD 100W (Zone 4), USB-C PD 20W (Zone 5)
- **PSU:** Internal 180W AC/DC (IEC C13 inlet, no external power brick)
- **No USB-A port**
- **No physical buttons**

---

## Packaging

- Rigid kraft or matte-black retail box
- Die-cut foam insert
- Black tissue paper wrap
- Epitome Penta logo sticker on tissue
- Quick-start guide
- Warranty registration card
- 1.5m braided IEC C13 cable bundled in-box

---

## Price

**$189** — Black or White

---

## Comprehensive Engineering Expansion (Revision A)

This section expands the base product summary into a manufacturing-grade reference.

### Reference Documents

- Mechanical coordinate source of truth: [component-positions.md](component-positions.md)
- Enclosure and material baseline: [enclosure.md](enclosure.md)
- Electrical architecture and limits: [electronics.md](electronics.md)
- Wiring implementation details: [wiring.md](wiring.md)
- Firmware timing and night mode behavior: [firmware-notes.md](firmware-notes.md)
- Cost and sourcing context: [bom.md](bom.md)

### Complete Physical Dimensions Table

| Parameter | Value | Notes |
|---|---:|---|
| Overall length (Y) | 300.00 mm | Front edge at Y=0.00, rear edge at Y=300.00 |
| Front width | 110.00 mm | X = -55.00..+55.00 at Y=0 |
| Rear width | 140.00 mm | X = -70.00..+70.00 at Y=300 |
| Front height | 12.00 mm | At Y=0 |
| Rear height | 22.00 mm | At Y=300 |
| Corner radius | R20.00 mm | All exterior corners |
| Top plate thickness | 1.50 mm | Brushed aluminum |
| Width taper function | W(Y)=110+30×(Y/300) | mm, linear taper front→rear |
| Height taper function | H(Y)=12+10×(Y/300) | mm, linear rise front→rear |
| Zone 1 dish | 80×55 mm, R10, depth 2.50 mm | Silicone insert 78×53 mm, R9, depth 2.20 mm |
| Zone 2 dish | 65×55 mm, R10, depth 2.50 mm | Silicone insert 63×53 mm, R9, depth 2.20 mm |
| Zone 3 watch pod | Ø50 mm footprint, 18 mm tall | 30° forward tilt |
| Zone 4 groove | 22 mm wide × 12 mm deep | Span Y=15..285 |
| Zone 5 groove | 18 mm wide × 12 mm deep | Span Y=15..285 |
| IEC C13 cutout | 28×20 mm | Rear centered; cutout bottom Z=1.00 |
| M3 top plate holes | Ø3.20 mm | 2 locations, left/right symmetry |
| Rubber feet | Ø15×3 mm | 4 feet |
| Underside vent slots | 40×4×2.5 mm each | 8 slots total |
| LED diffuser strip | 290×8×3 mm | Frosted strip under front lip |
| LED zone window | 56×8×3 mm each | 5 optical sections |

### Full Zone Layout With Coordinates and Intended Use

#### Coordinate and Occupancy Map

| Zone | Anchor / Range | Purpose | Primary Device Class |
|---|---|---|---|
| Zone 1 | X=-45.00, Y=60.00 | Main phone wireless fast charge bay | iPhone/Android phone |
| Zone 2 | X=-45.00, Y=140.00 | Secondary low-power wireless bay | Earbuds or second phone |
| Zone 3 | X=-45.00, Y=225.00 | Elevated watch magnetic cradle | Apple Watch |
| Zone 4 | X=+40.00, Y=15..285 | High-power USB-C spine groove | Laptop / ultrabook |
| Zone 5 | X=+80.00, Y=15..285 | Medium-power USB-C spine groove | iPad / phone / accessory |

#### Zone Intent Summary

- **Zone 1** prioritizes alignment and user experience for everyday phone charging, using a 50 mm Qi transmitter and N52 ring magnets.
- **Zone 2** is intentionally lower-power to minimize thermal interaction with adjacent zones while still supporting earbuds and secondary-device topping.
- **Zone 3** is physically elevated to improve watch readability and strap clearance.
- **Zone 4** is current-dominant and mechanically reinforced for high-power USB-C cable insertion/removal cycles.
- **Zone 5** provides separate regulated USB-C power for tablet/phone-class loads without competing with the Zone 4 power branch.

### Enclosure Materials Breakdown

| Subsystem | Material | Finish | Functional Reason |
|---|---|---|---|
| Top plate | 1.5 mm aluminum sheet | Brushed (Gunmetal Black SKU / Silver White SKU) | Stiffness, premium touch, EMI shielding contribution |
| Main base | ABS (soft-touch matte) | Black or White matte | Impact resistance, manufacturability, tactile quality |
| Pocket/groove lining | Silicone elastomer | Dark grey anti-slip | Scratch protection + friction hold + vibration damping |
| Front LED diffuser | Frosted acrylic/polycarbonate strip | Diffused/frosted | Homogeneous optical blending of WS2812 emitters |
| Fasteners | M3 machine screws + matching inserts/bosses | Zinc/black oxide acceptable | Serviceability and controlled clamp load |
| Feet | Molded rubber, logo emboss optional | Matte black | Anti-slip + gap for underside airflow |

### Color Variants (Black / White)

| Variant | Top Plate | Base | Silicone | Visual Identity |
|---|---|---|---|---|
| Black | Gunmetal brushed aluminum | Matte black soft-touch ABS | Dark grey | Low-contrast technical look |
| White | Silver brushed aluminum | Matte white soft-touch ABS | Dark grey (or light grey optional) | High-contrast minimal look |

Only cosmetics change by color variant; geometry, electronics, thermal envelope, and port placement remain identical.

### LED System Definition

| Item | Specification |
|---|---|
| LED type | WS2812B individually addressable RGB |
| Total emitters | 20 LEDs |
| Allocation | 4 LEDs per zone × 5 zones |
| Strip source | 60 LED/m reel, cut to length |
| Optical architecture | Hidden under front lip behind frosted diffuser |
| Mechanical segmentation | 5 front sections divided by recessed lines |
| Normal status colors | Red=charging, Green=full, Off=idle |
| Night mode behavior | 23:00–07:00 LEDs off unless active load >0.5 W |
| Night-mode entry/exit cues | New-load override flash for 3 s before returning dark |

### Zone-by-Zone Detailed Specification Table

| Zone | Charging Method | Max Power Budget | Connector/Interface | Pocket/Groove Geometry | Silicone Lining | Typical Compatible Devices |
|---|---|---:|---|---|---|---|
| Zone 1 | Qi wireless TX + magnetic alignment | 15 W | No user cable required | Dish 80×55 R10, 2.50 mm deep | Yes (78×53 R9, 2.20 mm deep) | iPhone (MagSafe-style alignment), Android phones with Qi |
| Zone 2 | Qi wireless TX | 5 W | No user cable required | Dish 65×55 R10, 2.50 mm deep | Yes (63×53 R9, 2.20 mm deep) | Earbuds case, secondary phone |
| Zone 3 | Apple Watch magnetic puck | 5 W | Integrated puck | Teardrop pod Ø50 base, 18 mm tall, 30° tilt | Local contact support as needed | Apple Watch Series 1–9, SE, Ultra |
| Zone 4 | USB-C Power Delivery | 100 W | USB-C female in groove | Groove 22 mm wide × 12 mm deep, Y=15..285 | Yes | USB-C laptops (2018+ class devices) |
| Zone 5 | USB-C Power Delivery | 20 W | USB-C female in groove | Groove 18 mm wide × 12 mm deep, Y=15..285 | Yes | iPad, phones, handheld accessories |

### Watch Cradle Detail (Zone 3)

- Geometry: teardrop pod based on Ø50 mm footprint.
- Vertical rise: 18 mm from top plate reference.
- Tilt: 30° toward the user/front.
- Internal component: magnetic puck module centered at X=-45.00, Y=225.00 (see [component-positions.md](component-positions.md)).
- Design purpose: raises watch face for glanceability while keeping strap contact clear of top plate.

### Rear Power Inlet (IEC C13)

| Item | Value |
|---|---|
| Inlet type | IEC C13 panel mount |
| Exterior coordinate | X=0.00, Y=298.50, Z=6.00 |
| Cutout | 28×20 mm |
| Cutout floor reference | Bottom at Z=1.00 |
| Location rationale | Rear-centered cable routing and balanced strain path |

### Rubber Feet Specification and Positions

| Foot | X (mm) | Y (mm) | Z centroid (mm) | Size |
|---|---:|---:|---:|---|
| Front-left | -39.17 | 15.00 | -1.50 | Ø15×3 mm |
| Front-right | +39.17 | 15.00 | -1.50 | Ø15×3 mm |
| Rear-left | -53.50 | 285.00 | -1.50 | Ø15×3 mm |
| Rear-right | +53.50 | 285.00 | -1.50 | Ø15×3 mm |

### M3 Fastener Positions

| Fastener | X (mm) | Y (mm) | Hole Diameter | Function |
|---|---:|---:|---:|---|
| Left top-plate screw | -60.00 | 150.00 | Ø3.20 mm | Top plate retention and service access |
| Right top-plate screw | +60.00 | 150.00 | Ø3.20 mm | Top plate retention and service access |

### Ventilation Features (8× Underside Slots)

| Slot Row | Slot | X (mm) | Y (mm) | Size |
|---|---|---:|---:|---|
| Left row | 1 | -20.00 | 25.00 | 40×4×2.5 mm |
| Left row | 2 | -20.00 | 45.00 | 40×4×2.5 mm |
| Left row | 3 | -20.00 | 65.00 | 40×4×2.5 mm |
| Left row | 4 | -20.00 | 85.00 | 40×4×2.5 mm |
| Right row | 1 | +20.00 | 25.00 | 40×4×2.5 mm |
| Right row | 2 | +20.00 | 45.00 | 40×4×2.5 mm |
| Right row | 3 | +20.00 | 65.00 | 40×4×2.5 mm |
| Right row | 4 | +20.00 | 85.00 | 40×4×2.5 mm |

### Night Mode Functional Behavior (Product-Level View)

| Behavior | Value |
|---|---|
| Active window | 23:00–07:00 local time |
| Default state | Enabled |
| Light suppression rule | Zone LEDs remain off while that zone draw ≤0.5 W |
| Charge-confirmation override | 3 s brief flash when a new night-time load is detected |
| Time source priority | SNTP over WiFi first, BLE time sync fallback |
| Notification behavior | Theft-alert push notifications can be silenced during night window |

Implementation details are documented in [firmware-notes.md](firmware-notes.md).

### App Feature Summary (Engineer-Facing)

| Feature | Transport | Engineering Function |
|---|---|---|
| Device control and setup | BLE 5.0 | Pairing, zone status readout, control flags |
| Theft alert logic | BLE + app backend behavior | Alert generation when expected dock/device relationship changes |
| Ambient dimming control | BLE config + BH1750 feedback | Set dimming preferences and thresholds |
| Weekly energy/usage reports | Telemetry aggregation | Zone-level usage trend reporting |
| Home-screen widget | Mobile OS widget APIs | Quick glance: zone state, night mode, total activity |

### Pricing and Variants

| SKU | Colorway | MSRP |
|---|---|---:|
| Epitome Penta Black | Gunmetal top + black base | $189 |
| Epitome Penta White | Silver top + white base | $189 |

Cost and sourcing breakdown supporting this price target are in [bom.md](bom.md).
