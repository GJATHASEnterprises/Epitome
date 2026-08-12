# Epitome Penta — Design Specification

> **Note:** This file provides a summary of the product spec. For detailed specifications see:
> - [Enclosure Specification](enclosure.md)
> - [Electronics Specification](electronics.md)
> - [BOM](bom.md)
> - [Packaging Specification](packaging.md)
> - [Firmware Notes](firmware-notes.md)

---

## Product Name
Epitome Penta

## Brand
Epitome

## Color Variants
- **Black** — Gunmetal brushed aluminum top, matte black soft-touch ABS base
- **White** — Silver brushed aluminum top, matte white soft-touch ABS base

---

## Overall Dimensions

| Dimension | Value |
|---|---|
| Overall width | 700mm |
| Overall depth | 300mm |
| Corner radius | R20mm (all exterior edges) |
| Top plate thickness | 1.5mm brushed aluminium |
| Base material | Matte ABS |

---

## Slot Dimensions

### Left Slot — Laptop (Zone 4)

| Dimension | Value |
|---|---|
| Slot width (internal) | 400mm |
| Slot depth (front to rear wall) | 25mm |
| Slot height (opening) | 22mm |
| Entry | Open front — laptop slides in horizontally on its side |
| USB-C port location | Rear wall of slot, centred |
| USB-C port power | 100W PD |
| Silicone lining | Floor and rear wall |
| Sized for | Up to 17" laptop (395mm wide × 18mm thick) |

### Right Slot — iPad (Zone 5)

| Dimension | Value |
|---|---|
| Slot width (internal) | 290mm |
| Slot depth (front to rear wall) | 25mm |
| Slot height (opening) | 10mm |
| Entry | Open front — iPad slides in horizontally on its side |
| USB-C port location | Rear wall of slot, centred |
| USB-C port power | 20W PD |
| Silicone lining | Floor and rear wall |
| Sized for | iPad Pro 13" (281mm tall × 5.1mm thick) and smaller |

---

## Centre Platform Dimensions

### Step 1 — Phone (Zone 1)

| Dimension | Value |
|---|---|
| Platform width | 200mm |
| Platform depth | 300mm |
| Height | Base level — 0mm above dock surface |
| Pad dish size | 90 × 65mm, R10, 2.5mm deep |
| Silicone insert | 88 × 63mm, R9, 2.2mm deep |
| Qi coil | 50mm, 15W |
| N52 ring magnets | MagSafe-style alignment |
| Sized for | iPhone 16 Pro Max (163mm × 77mm × 8.25mm) |

### Step 2 — Watch + Buds (Zones 2 & 3)

| Dimension | Value |
|---|---|
| Platform width | 200mm |
| Platform depth | 200mm (rear half of Step 1) |
| Height | +40mm above Step 1 |
| Step riser height | 40mm |
| Step riser face | Brushed aluminium, front-facing |
| Total centre platform height | 40mm at Step 2 |

#### Watch Cradle (Zone 3) — left side of Step 2

| Dimension | Value |
|---|---|
| Pod base diameter | Ø55mm |
| Tilt | 30° toward user |
| Location | Left side of Step 2 surface |
| Charging | Apple Watch magnetic puck, 5W |
| Compatible | Apple Watch Series 1–9, SE, Ultra 2 |

#### Buds Pad (Zone 2) — right side of Step 2

| Dimension | Value |
|---|---|
| Pad dish size | 70 × 50mm, R10, 2.5mm deep |
| Silicone insert | 68 × 48mm, R9, 2.2mm deep |
| Location | Right side of Step 2 surface |
| Qi output | 5W |
| Sized for | AirPods Pro case (65mm × 45mm × 21mm) |
| Also fits | Phone as alternative |

---

## Full Dimensions Summary Table

| Feature | Width | Depth | Height / Thickness |
|---|---|---|---|
| Overall dock | 700mm | 300mm | 40mm (at Step 2) |
| Left (laptop) slot — internal | 400mm | 25mm | 22mm opening |
| Right (iPad) slot — internal | 290mm | 25mm | 10mm opening |
| Centre Step 1 platform | 200mm | 300mm | base level |
| Centre Step 2 platform | 200mm | 200mm | +40mm |
| Phone dish (Step 1) | 90mm | 65mm | 2.5mm deep |
| Buds dish (Step 2) | 70mm | 50mm | 2.5mm deep |
| Watch cradle pod base | Ø55mm | — | 30° tilt |
| Top plate | Full surface | Full surface | 1.5mm |
| Rubber feet | Ø15mm | — | 3mm |
| IEC C13 inlet cutout | 28mm | — | 20mm tall |

---

## Device Sizing Reference

| Device | Model sized for | Key dimension |
|---|---|---|
| Phone | iPhone 16 Pro Max | 163mm tall × 77mm wide × 8.25mm thick |
| iPad | iPad Pro 13" | 281mm tall × 215mm wide × 5.1mm thick |
| Laptop | 17" generic | 395mm wide × 270mm deep × 18mm thick |
| Watch | Apple Watch Ultra 2 | 49mm case, 51mm wide with lugs |
| Buds | AirPods Pro | 65mm × 45mm × 21mm case |

---

## Zone Layout Diagram

```
[TOP VIEW — 700mm wide × 300mm deep]

+---------------------+--------------------+---------------------+
|                     |   STEP 2 (+40mm)   |                     |
|    LAPTOP SLOT      |--------------------|    iPAD SLOT        |
|    400mm × 25mm     | WATCH  |   BUDS    |    290mm × 25mm     |
|    22mm opening     | Ø55mm  | 70×50mm   |    10mm opening     |
|    USB-C 100W       | 30°tilt|  Qi 5W    |    USB-C 20W        |
|    rear wall        |--------------------|    rear wall        |
|                     |   STEP 1 (base)    |                     |
|                     |--------------------|                     |
|                     |  PHONE 90×65mm     |                     |
|                     |  Qi 15W MagSafe    |                     |
+---------------------+--------------------+---------------------+
[FRONT — user faces this edge]
[LED strip runs full width across front face — 5 zones]
                     IEC C13 inlet — rear wall centre
```

---

## Zone Specifications

### Zone 1 — Phone (Qi 15W)
- 50mm Qi TX coil, 15W MagSafe-compatible
- N52 ring magnets for phone alignment
- Silicone-lined recessed dish: 90×65mm, 2.5mm deep
- Location: Step 1, centre platform

### Zone 2 — AirPods Pro (Qi 5W)
- Qi wireless TX, 5W
- Silicone-lined dish: 70×50mm, 2.5mm deep
- Location: Step 2 right side
- Also accepts a phone as secondary use

### Zone 3 — Apple Watch
- Apple Watch magnetic puck, wired internally, 5W
- Pod: Ø55mm base, 30° tilt toward user
- Location: Step 2 left side
- Compatible: Apple Watch Series 1–9, SE, Ultra 2

### Zone 4 — Laptop (USB-C PD 100W)
- USB-C PD up to 100W
- Slot: 400mm wide × 25mm deep × 22mm tall, open front
- USB-C female port in rear wall, centred
- Compatible: any USB-C laptop up to 17"

### Zone 5 — iPad (USB-C PD 20W)
- USB-C PD 2.0 up to 20W
- Slot: 290mm wide × 25mm deep × 10mm tall, open front
- USB-C female port in rear wall, centred
- Compatible: iPad Pro 13" and any smaller USB-C tablet

---

## LED Status System

| State | Colour | Meaning |
|---|---|---|
| Charging | Red | Device actively charging |
| Full | Green | Device fully charged |
| Idle | Off | No device detected |

Night mode: all LEDs off 23:00–07:00 unless zone draws >0.5W.

---

## Electronics Summary

See [electronics.md](electronics.md) for full spec.

- **MCU:** ESP32-C3 Mini (WiFi + BLE)
- **Power monitors:** INA3221 (Zones 1–3), INA219 (Zone 4), INA219 (Zone 5)
- **Ambient light:** BH1750 (I2C)
- **LED:** WS2812B strip (20 LEDs, 4 per zone), full front face
- **PSU:** Internal 180W AC/DC (IEC C13 inlet, no external brick)
- **No USB-A port**
- **No physical buttons**
- **Power budget:** 145W total load, 35W headroom

---

## Packaging

- Rigid kraft or matte-black retail box (~750×340×100mm)
- Die-cut foam insert
- Black tissue paper wrap
- Epitome Penta logo sticker
- Quick-start guide (4-panel fold, 148×105mm)
- Warranty registration card (85×55mm)
- 1.5m braided IEC C13 cable in-box

---

## Price

**$249** — Black or White
Early bird: **$199** (first 20 pre-orders)
Retail post-launch: **$279**
