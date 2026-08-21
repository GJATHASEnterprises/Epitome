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
| Charging interface | **Captive braided USB-C to USB-C cable (220mm, 100W)** | **Captive braided USB-C to USB-C cable (220mm, 100W)** |
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

## Centre Platform Dimensions — 3-Step Tapered Layout

| Step | Width | Depth | Height | Zone | Content |
|---|---:|---:|---:|---|---|
| Step 3 (top) | 100mm | 80mm | 15mm | Zone 3 | Watch cradle — Apple puck + Qi coil |
| Step 2 (middle) | 140mm | 100mm | 15mm | Zone 2 | Buds/Phone pad — 15W Qi, 90×65 landscape |
| Step 1 (base) | 180mm | 110mm | 15mm | Zone 1 | Phone pad — 20W Qi, full-width silicone surface |

- Total centre platform height: **45mm**
- Taper rule: each step is **40mm narrower** than the one below
- Every riser face uses brushed aluminium + internal ribbing reinforcement

### Zone 1 (Step 1 base)

| Dimension | Value |
|---|---|
| Silicone charging area | 160 × 100mm (flat, no recessed dish) |
| Qi output | **20W** |
| Qi coil | Centered under silicone surface |
| Magnets | N52 ring magnets for alignment |
| Orientation intent | Landscape phone placement |

### Zone 2 (Step 2 middle)

| Dimension | Value |
|---|---|
| Pad dish size | **90 × 65mm**, landscape |
| Inner alignment ridge | **1mm ridge around 68 × 48mm inner zone** |
| Qi output | **15W** |
| Positioning | Front-middle of Step 2; slight phone overhang acceptable |

### Zone 3 (Step 3 top)

| Dimension | Value |
|---|---|
| Step area | 100 × 80mm |
| Cradle location | Rear of Step 3, slightly raised |
| Charging | Apple Watch magnetic puck + Qi coil |
| Policy | 5W shared, one active watch path at a time |

---

## Full Dimensions Summary Table

| Feature | Standard | XL |
|---|---|---|
| Overall dock | ~530 × 300mm | ~700 × 300mm |
| Left (laptop) slot — internal | 320 × 25mm, 28mm opening | 400 × 25mm, 28mm opening |
| Right (iPad) slot — internal | 290 × 25mm, 20mm opening | 290 × 25mm, 20mm opening |
| Centre Step 1 | 180 × 110 × 15mm | 180 × 110 × 15mm |
| Centre Step 2 | 140 × 100 × 15mm | 140 × 100 × 15mm |
| Centre Step 3 | 100 × 80 × 15mm | 100 × 80 × 15mm |
| Zone 1 silicone surface | 160 × 100mm | 160 × 100mm |
| Zone 2 dish | 90 × 65mm | 90 × 65mm |

---

## Device Sizing Reference

| Device | Model sized for | Key dimension |
|---|---|---|
| Phone | iPhone 16 Pro Max | 163mm × 77mm |
| Tablet | iPad Pro 13" in case | Up to ~20mm total thickness |
| Laptop | 15" class (Standard) / 17" class (XL) | Up to ~28mm slot clearance |
| Watch | Apple Watch Ultra 2 + Qi watches | Step 3 raised cradle zone |

---

## Zone Layout Diagram

```text
[TOP VIEW — Penta Standard ~530mm wide]

+-------------------+------------------------------+-------------------+
| Laptop Slot Z4    |    3-Step Centre Platform   | iPad Slot Z5      |
| 320×25 / 28mm     | Step 3: Watch (rear) 5W     | 290×25 / 20mm     |
| Captive USB-C     | Step 2: Buds 90×65, 15W     | Captive USB-C     |
| 220mm cable 100W  | Step 1: Phone 160×100, 20W  | 200mm cable 20W   |
| 5mm stop shelf    | 45mm total stack height      | 5mm stop shelf    |
+-------------------+------------------------------+-------------------+
Rear: right-angle IEC C13 inlet, PSU under laptop slot cavity
```

---

## Zone Specifications

### Zone 1 — Phone (Qi 20W)
- 20W Qi + MagSafe-style alignment magnets

### Zone 2 — Buds / Phone (Qi 15W)
- 90×65mm pad with 68×48mm inner ridge marker

### Zone 3 — Watch (Universal 5W)
- Apple Watch puck + Qi coil in same cradle, one device at a time

### Zone 4 — Laptop (USB-C PD 100W)
- Captive 220mm braided USB-C cable from internal PD board

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

- **PSU:** Internal 160W AC/DC, relocated under laptop slot cavity
- **Inlet:** Rear right-angle IEC C13
- **Power budget:** **155W total load, 5W headroom**
- **Firmware cap:** global soft power cap at **150W**
- **Certification planning required:** FCC, CE, UKCA, RCM before retail in target markets

---

## Manufacturing Method (Batch 1)

- 3D print ABS: centre platform only (3-step geometry)
- Laser cut + bent ABS: left/right slot walls
- Vacuum-formed ABS: base
- Laser cut + bent aluminium: top plates + step riser faces

Batch 1 enclosure target: **~$40–62 per unit**.

---

## Packaging

- Standard retail box target: **~580×340×100mm**
- XL retail box target: **~750×340×100mm**
- Moulded pulp tray replaces die-cut foam
- Warranty/setup docs provided via QR only (`epitome.io/warranty`, `epitome.io/setup`)

---

## Price

| SKU | Early Bird | Pre-Order | Retail |
|---|---:|---:|---:|
| Penta Standard | $199 | $249 | $279 |
| Penta XL | $229 | $279 | $309 |
