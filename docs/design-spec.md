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
- **Midnight Blue (Limited Launch SKU)** — Deep navy brushed aluminum top, matte navy-black ABS base

---

## Overall Dimensions

| SKU | Overall width | Overall depth | Corner radius | Top plate thickness | Base material |
|---|---:|---:|---|---|---|
| **Penta Standard** | **~530mm** | 300mm | R20mm | 1.5mm brushed aluminium | Matte ABS |
| **Penta XL** | **~700mm** | 300mm | R20mm | 1.5mm brushed aluminium | Matte ABS |

Launch sequence: **Standard first**, then XL.

---

## Slot Dimensions

### Left Slot — Laptop (Zone 4)

| Dimension | Standard | XL |
|---|---:|---:|
| Slot width (internal) | 320mm | 400mm |
| Slot depth (front to rear wall) | 25mm | 25mm |
| Slot height (opening) | **28mm** | **28mm** |
| Entry | Open front — laptop slides in on side | Open front — laptop slides in on side |
| Charging interface | **Captive braided USB-C to USB-C cable (300mm, 100W)** | **Captive braided USB-C to USB-C cable (300mm, 100W)** |
| Rear alignment | 5mm silicone-covered stop shelf + cable clip above shelf | 5mm silicone-covered stop shelf + cable clip above shelf |
| Sized for | Up to 15" laptops | Up to 17" laptops |

### Right Slot — iPad (Zone 5)

| Dimension | Standard | XL |
|---|---:|---:|
| Slot width (internal) | 290mm | 290mm |
| Slot depth (front to rear wall) | 25mm | 25mm |
| Slot height (opening) | **20mm** | **20mm** |
| Entry | Open front — tablet slides in on side | Open front — tablet slides in on side |
| Charging interface | **Captive braided USB-C to USB-C cable (200mm, 20W)** | **Captive braided USB-C to USB-C cable (200mm, 20W)** |
| Rear alignment | 5mm silicone-covered stop shelf + cable clip above shelf | 5mm silicone-covered stop shelf + cable clip above shelf |
| Sized for | iPad/tablets with cases up to ~20mm | iPad/tablets with cases up to ~20mm |

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

### Step 2 — Watch + Buds (Zones 2 & 3)

| Dimension | Value |
|---|---|
| Platform width | 200mm |
| Platform depth | 200mm (rear half of Step 1) |
| Height | +40mm above Step 1 |
| Step riser | Internal ribbing or metal insert reinforcement required |
| Total centre platform height | 40mm at Step 2 |

#### Watch Cradle (Zone 3) — rear of Step 2

| Dimension | Value |
|---|---|
| Pod base diameter | Ø55mm |
| Tilt | 30° toward user |
| Location | Rear edge of Step 2 against rear wall (slightly raised) |
| Charging | Apple Watch magnetic puck + Qi coil (5W shared budget) |
| Compatible | Apple Watch + Qi-enabled watches (Galaxy/Pixel/Garmin Qi models) |

#### Buds Pad (Zone 2) — front edge of Step 2

| Dimension | Value |
|---|---|
| Pad dish size | **90 × 65mm**, R10, 2.5mm deep |
| Silicone insert | 88 × 63mm |
| Inner alignment ridge | **1mm ridge around 68 × 48mm inner zone** |
| Location | Front edge of Step 2 |
| Qi output | **15W** |
| Sized for | Earbuds and full-size phones |

---

## Full Dimensions Summary Table

| Feature | Standard | XL |
|---|---|---|
| Overall dock | ~530 × 300mm | ~700 × 300mm |
| Left (laptop) slot — internal | 320 × 25mm, 28mm opening | 400 × 25mm, 28mm opening |
| Right (iPad) slot — internal | 290 × 25mm, 20mm opening | 290 × 25mm, 20mm opening |
| Centre Step 2 | 200 × 200mm, +40mm | 200 × 200mm, +40mm |
| Zone 2 dish | 90 × 65mm | 90 × 65mm |
| Watch cradle | Ø55mm, rear Step 2 | Ø55mm, rear Step 2 |

---

## Device Sizing Reference

| Device | Model sized for | Key dimension |
|---|---|---|
| Phone | iPhone 16 Pro Max | 163mm × 77mm |
| Tablet | iPad Pro 13" in case | Up to ~20mm total thickness |
| Laptop | 15" class (Standard) / 17" class (XL) | Up to ~28mm slot clearance |
| Watch | Apple Watch Ultra 2 + Qi watches | Ø55mm cradle zone |

---

## Zone Layout Diagram

```
[TOP VIEW — Penta Standard ~530mm wide]

+-------------------+--------------------+-------------------+
| Laptop Slot Z4    |   STEP 2 (+40mm)   | iPad Slot Z5      |
| 320×25 / 28mm     | Watch (rear) 5W    | 290×25 / 20mm     |
| Captive USB-C     | Buds/Phone (front) | Captive USB-C     |
| 300mm cable 100W  | 90×65 Qi 15W       | 200mm cable 20W   |
| 5mm stop shelf    |                    | 5mm stop shelf    |
+-------------------+--------------------+-------------------+
|                   STEP 1 (base): Phone 90×65 Qi 15W          |
+---------------------------------------------------------------+
Rear: right-angle IEC C13 inlet, PSU under laptop slot cavity
```

---

## Zone Specifications

### Zone 1 — Phone (Qi 15W)
- 15W Qi + MagSafe alignment magnets

### Zone 2 — Buds / Phone (Qi 15W)
- 90×65mm pad with 68×48mm inner ridge marker

### Zone 3 — Watch (Universal 5W)
- Apple Watch puck + Qi coil in same cradle, one device at a time

### Zone 4 — Laptop (USB-C PD 100W)
- Captive 300mm braided USB-C cable from internal PD board

### Zone 5 — Tablet (USB-C PD 20W)
- Captive 200mm braided USB-C cable from internal PD board

---

## LED Status System

| State | Colour | Meaning |
|---|---|---|
| Charging | Red | Device actively charging |
| Full | Green | Device fully charged |
| Idle | Off | No device detected |

---

## Electronics Summary

See [electronics.md](electronics.md) for full spec.

- **PSU:** Internal 180W AC/DC, relocated under laptop slot cavity
- **Inlet:** Rear right-angle IEC C13
- **Power budget:** **155W total load, 25W headroom**
- **Certification planning required:** FCC, CE, UKCA, RCM before retail in target markets

---

## Packaging

- Standard retail box target: **~580×340×100mm**
- XL retail box target: **~750×340×100mm**
- Quick-start guide must explain captive cable pull-out/coil-back usage

---

## Price

| SKU | Early Bird | Pre-Order | Retail |
|---|---:|---:|---:|
| Penta Standard | $199 | $249 | $279 |
| Penta XL | $229 | $279 | $309 |
