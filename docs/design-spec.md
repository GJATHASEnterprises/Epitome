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
- **Black** — Matte ABS, all surfaces (Batch 1)

> White and Midnight Blue are planned for a future batch. Black only for Batch 1.

---

## Overall Dimensions

| SKU | Overall width | Overall depth | Overall height | Corner radius | Top plate material | Base material |
|---|---:|---:|---:|---|---|---|
| **Penta Standard** | **~250mm** | **~100mm** | **~100mm** | R10mm | 3mm matte ABS | Matte ABS |
| **Penta XL** | ~320mm | ~100mm | ~100mm | R10mm | 3mm matte ABS | Matte ABS |

> XL is Batch 2+. Standard launches first. No aluminium anywhere in Batch 1.

---

## Slot Dimensions

### Left Slot — Laptop (Zone 4)

| Dimension | Standard |
|---|---:|
| Slot length (left to right) | 400mm |
| Slot depth (front to back, internal) | 90mm |
| Slot width (opening thickness) | **35mm** |
| Slot wall height | **95mm** |
| Entry | Device slides in on its **thin edge** (like a book on a shelf) |
| Charging interface | **Captive braided USB-C cable (220mm, 100W) hangs from top of slot** |
| Alignment | Cable at top of slot — device plugs in on insertion |
| Sized for | Any laptop up to 17" class (~28mm thick including case) |

> XL (Batch 2+) has a wider overall dock footprint (~320mm wide); the slot length remains 400mm.

### Right Slot — iPad (Zone 5)

| Dimension | Standard |
|---|---:|
| Slot length (left to right) | 290mm |
| Slot depth (front to back, internal) | 70mm |
| Slot width (opening thickness) | **20mm** |
| Slot wall height | **75mm** |
| Entry | Device slides in on its **thin edge** (like a book on a shelf) |
| Charging interface | **Captive braided USB-C cable (200mm, 20W) hangs from top of slot** |
| Alignment | Cable at top of slot — device plugs in on insertion |
| Sized for | Any tablet up to iPad Pro 13" in case (~16mm thick) |

---

## Centre Platform Dimensions — 3-Step Tapered Layout

| Step | Width | Depth | Height | Zone | Content |
|---|---:|---:|---:|---|---|
| Step 3 (top) | 100mm | 80mm | 15mm | Zone 3 | Watch cradle — Apple puck + Qi coil |
| Step 2 (middle) | 140mm | 100mm | 15mm | Zone 2 | Buds or second phone pad — 20W Qi, 120×80 landscape |
| Step 1 (base) | 180mm | 110mm | 15mm | Zone 1 | Phone pad — 20W Qi, full-width silicone surface |

- Step dimensions are unchanged.
- Centre platform body is raised over the PSU on a perimeter wall.
- **20mm riser cavity** sits between PSU top and Step 1 base for coil/logic wiring.
- Total centre column height from base floor: **95mm**.

### Zone 1 (Step 1 base)

| Dimension | Value |
|---|---|
| Silicone charging area | 160 × 100mm (flat, no recessed dish) |
| Qi output | **20W** |
| Qi coil | Embedded in Step 1 body under silicone surface |
| Magnets | N52 ring magnets for alignment |
| Orientation intent | Landscape phone placement |

### Zone 2 (Step 2 middle)

| Dimension | Value |
|---|---|
| Pad dish size | **120 × 80mm**, landscape |
| Inner alignment ridge | **1mm ridge around 68 × 48mm inner zone** |
| Qi output | **20W** |
| Positioning | Front-middle of Step 2; slight phone overhang acceptable |

### Zone 3 (Step 3 top)

| Dimension | Value |
|---|---|
| Step area | 100 × 80mm |
| Cradle location | Rear of Step 3, slightly raised |
| Charging | Apple Watch magnetic puck + Qi coil embedded in Step 3 body |
| Policy | 5W shared, one active watch path at a time |

---

## Full Dimensions Summary Table

| Feature | Standard |
|---|---|
| Overall dock | ~250 × 100 × 100mm |
| Left (laptop) slot | 400mm long × 90mm deep × 35mm wide × 95mm tall |
| Right (iPad) slot | 290mm long × 70mm deep × 20mm wide × 75mm tall |
| Centre Step 1 | 180 × 110 × 15mm |
| Centre Step 2 | 140 × 100 × 15mm |
| Centre Step 3 | 100 × 80 × 15mm |
| Centre column height | 95mm from base floor |
| Zone 1 silicone surface | 160 × 100mm |
| Zone 2 dish | 120 × 80mm |

> XL (Batch 2+): ~320mm wide × ~100mm deep × ~100mm tall, with the same 400mm slot length and platform geometry as Standard.

---

## Device Sizing Reference

| Device | Model sized for | Key dimension |
|---|---|---|
| Phone | iPhone 16 Pro Max | 163mm × 77mm |
| Tablet | iPad Pro 13" in case | Up to ~16mm total thickness |
| Laptop | 17" class (Standard slot 400mm) | Up to ~28mm slot clearance |
| Watch | Apple Watch Ultra 2 + Qi watches | Step 3 raised cradle zone |

---

## Zone Layout Diagram

```text
[TOP VIEW — Penta Standard ~250mm wide × ~100mm deep × ~100mm tall]

+------------------+------------------------------+------------------+
| Laptop Slot Z4   |   3-Step Centre Platform    | iPad Slot Z5     |
| 400mm long       | Step 3: Watch (rear) 5W     | 290mm long       |
| 90mm deep        | Step 2: Buds 120×80, 20W     | 70mm deep        |
| 35mm wide        | Step 1: Phone 160×100, 20W  | 20mm wide        |
| 95mm tall wall   | Raised over PSU cavity       | 75mm tall wall   |
| cable from top   | coils embedded in step body  | cable from top   |
+------------------+------------------------------+------------------+
Rear: full-width rear spine with centred IEC C13 cutout
Front: full-width fascia strip with LED diffuser channel
```

---

## Zone Specifications

### Zone 1 — Phone (Qi 20W)
- 20W Qi + MagSafe-style alignment magnets

### Zone 2 — Buds / Phone (Qi 20W)
- 120×80mm pad with 68×48mm inner ridge marker

### Zone 3 — Watch (Universal 5W)
- Apple Watch puck + Qi coil in same cradle, one device at a time

### Zone 4 — Laptop (USB-C PD 100W)
- Captive 220mm braided USB-C cable hangs from top of slot; device plugs in on insertion

### Zone 5 — Tablet (USB-C PD 45W)
- Captive 200mm braided USB-C cable hangs from top of slot; device plugs in on insertion

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

- **PSU:** Mean Well LRS-200-24 (201W, 24V, trim-adjusted to ~20V output), under centre platform cavity
- **Inlet:** Rear right-angle IEC C13 in rear spine plate
- **Power budget:** **190W total load, 11W headroom**
- **ATtiny85 soft cap:** global soft power cap at **185W**
- **Certification planning required:** FCC, CE, UKCA, RCM before retail in target markets

---

## Manufacturing Method (Batch 1)

- 3D print ABS: centre platform only (raised 3-step geometry, school makerspace printer, own filament)
- Laser cut ABS: slot walls, base plate, top panels, rear spine plate, front fascia strip (Pumping Station One, Chicago)
- All surfaces: sand → acetone vapour smooth → primer → Rust-Oleum 2X Matte Black → clear coat
- No vacuum-formed parts. No aluminium. All ABS.

Batch 1 enclosure target: **~$31.39/unit**.

---

## Packaging

- Standard retail box target: **~300×150×120mm** rigid kraft
- Insert: cardboard offcut + felt liner
- Warranty/setup docs provided via QR only (`epitome.io/warranty`, `epitome.io/setup`)

---

## Price

| SKU | Price |
|---|---:|
| Penta Standard | **$249** |

> $249 flat — no early bird pricing, no retail tier. XL is Batch 2+ and not priced for Batch 1.
