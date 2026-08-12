# Epitome Penta — Bill of Materials (BOM)

**Target BOM:** ~$85 per unit at 50 units with the full 5-zone / in-box bundle spec

> **Design revision:** Stepped centre platform with open-front side slots for laptop (left) and iPad (right).
> Overall footprint: ~700mm wide × ~300mm deep.

---

## Device Size Reference (Largest Models — Cardboard Prototype Guide)

| Device | Model | Key Dimension |
|---|---|---|
| Phone | iPhone 16 Pro Max | 163mm tall × 77mm wide × 8.25mm thick |
| iPad | iPad Pro 13" | 281mm tall × 215mm wide × 5.1mm thick |
| Laptop | 17" generic | 395mm wide × 270mm deep × 18mm thick |
| Watch | Apple Watch Ultra 2 | 49mm case, 51mm wide with lugs |
| Buds | AirPods Pro | 65mm × 45mm × 21mm case |

---

## Zone Sizes (Definitive)

| Zone | Location | Internal Size | Notes |
|---|---|---|---|
| Zone 1 — Phone Qi pad | Step 1 centre | 90×65mm dish, 2.5mm deep | Fits iPhone 16 Pro Max (163×77mm footprint — phone sits landscape) |
| Zone 2 — Buds Qi pad | Step 2 right | 70×50mm dish, 2.5mm deep | Fits AirPods Pro case (65×45mm) |
| Zone 3 — Watch cradle | Step 2 left | Ø55mm pod base, 30° tilt | Fits Apple Watch Ultra 2 (51mm wide) |
| Zone 4 — Laptop slot | Left slot | 400mm wide × 25mm deep × 22mm tall | Fits 17" laptop (395mm wide × 18mm thick) — open front |
| Zone 5 — iPad slot | Right slot | 290mm wide × 25mm deep × 10mm tall | Fits iPad Pro 13" (281mm tall × 5.1mm thick) — open front |

---

## Cardboard Prototype Cut Guide

| Piece | Dimensions |
|---|---|
| Base plate | 700mm × 300mm |
| Left slot outer box | 410mm × 300mm × 22mm |
| Left slot inner cavity | 400mm × 25mm × 22mm (open front) |
| Centre Step 1 block | 200mm × 300mm × 40mm |
| Centre Step 2 block | 200mm × 200mm × 40mm (rear-positioned on Step 1) |
| Right slot outer box | 300mm × 300mm × 10mm |
| Right slot inner cavity | 290mm × 25mm × 10mm (open front) |

Mark on Step 1: 90×65mm phone pad zone (centred)
Mark on Step 2: 55mm circle (watch, left side) + 70×50mm rectangle (buds, right side)

---

## Prototype BOM (Breakout Boards — No Custom PCB)

Use this for the prototype build. All breakout boards on breadboard/veroboard.

| # | Part | Spec | Qty | Unit Cost (Est.) | Source |
|---|------|------|-----|------------------|--------|
| 1 | ESP32-C3 Mini dev board | ESP32-C3 Mini, USB flashing | 2 | $3–$5 | LCSC / AliExpress |
| 2 | Qi 15W TX coil module | 50mm coil, 15W, breakout | 1 | $5–$8 | AliExpress |
| 3 | Qi 5W TX coil module | Buds pad, 5W | 1 | $4–$6 | AliExpress |
| 4 | Apple Watch charger module | Standard puck, 5W | 1 | $8–$12 | AliExpress |
| 5 | USB-C PD 100W controller board | Pre-made breakout, rear-wall mount | 1 | $8–$14 | AliExpress |
| 6 | USB-C PD 20W controller board | Pre-made breakout, rear-wall mount | 1 | $5–$8 | LCSC / AliExpress |
| 7 | INA3221 breakout board | 3-ch I2C power monitor | 1 | $2–$4 | LCSC / AliExpress |
| 8 | INA219 breakout board | 1-ch I2C power monitor | 2 | $1–$3 | LCSC / AliExpress |
| 9 | BH1750 breakout board | I2C ambient light sensor | 1 | $1–$2 | AliExpress |
| 10 | WS2812B LED strip | 1m reel (cut to 20 LEDs) | 1 | $3–$5 | AliExpress |
| 11 | N52 ring magnets (×5) | Fits 50mm Qi coil, Zone 1 alignment | 1 pk | $3–$5 | AliExpress |
| 12 | 180W AC/DC PSU module | 100–240V in, 20V out | 1 | $15–$22 | AliExpress / LCSC |
| 13 | IEC C13 inlet socket | Panel mount, rear wall | 1 | $2–$3 | AliExpress |
| 14 | IEC C13 braided power cable | 1.5m bundle cable | 1 | $2–$4 | AliExpress |
| 15 | Breadboard (full size) | 830 tie-points | 2 | $3–$5 | Local / AliExpress |
| 16 | Jumper wires | Male-male, male-female | 2 packs | $2–$4 | Local / AliExpress |
| 17 | USB-C female breakout boards | Rear-wall port for laptop + iPad slots | 2 | $1–$2 | AliExpress |
| 18 | USB-C extension cable (short) | Slot port to PD board connection | 2 | $2–$4 | AliExpress |
| 19 | Assorted resistors/capacitors | 300Ω, 100µF, 10K NTC | lot | $3–$5 | LCSC |
| 20 | Frosted acrylic strip | LED diffuser test piece | 1 | $5–$10 | Local |
| **Prototype electronics total** | | | | **$88–$150** | |

*Order 25% extra for spares. Budget ~$100–$165 for electronics and in-box items.*

---

## Production BOM (Full JLCPCB PCBA)

### Electronics & Internals

| # | Part | Spec | Qty | Unit Cost (15 units) | Unit Cost (50 units) | Source |
|---|------|------|-----|---------------------|---------------------|--------|
| 1 | Qi 15W TX Module | 50mm coil, 15W — Zone 1 phone pad | 1 | $7 | $5–$6 | LCSC / AliExpress |
| 2 | Qi 5W TX Module | Buds-friendly wireless TX — Zone 2 | 1 | $5 | $3–$4 | LCSC / AliExpress |
| 3 | Apple Watch Puck | Magnetic puck, 5W — Zone 3 | 1 | $10 | $4–$6 | Bulk ×10 order |
| 4 | USB-C PD Board 100W | Zone 4 laptop slot rear wall | 1 | $11 | $8–$10 | LCSC |
| 5 | USB-C PD Board 20W | Zone 5 iPad slot rear wall | 1 | $7 | $5–$6 | LCSC |
| 6 | USB-C female port (panel mount) | Laptop slot rear wall | 1 | $2 | $1–$2 | LCSC |
| 7 | USB-C female port (panel mount) | iPad slot rear wall | 1 | $2 | $1–$2 | LCSC |
| 8 | ESP32-C3 Mini | RISC-V, WiFi + BLE | 1 | $4 | $2–$3 | LCSC |
| 9 | INA3221 | 3-ch I2C, Zones 1–3 | 1 | $3 | $2–$3 | LCSC |
| 10 | INA219 Zone 4 | 1-ch I2C, Zone 4 | 1 | $2 | $1–$2 | LCSC |
| 11 | INA219 Zone 5 | 1-ch I2C, Zone 5 | 1 | $2 | $1–$2 | LCSC |
| 12 | BH1750 | I2C ambient light | 1 | $1 | $0.50–$1 | LCSC |
| 13 | WS2812B LED Strip | 20 LEDs cut from 60/m | 1 | $3 | $2–$3 | LCSC |
| 14 | N52 Ring Magnets | Zone 1 alignment | 1 set | $2 | $1–$2 | LCSC / AliExpress |
| 15 | Internal AC/DC PSU | 180W, 20V out | 1 | $20 | $10–$15 | LCSC |
| 16 | IEC C13 Inlet | Panel mount + fuse, rear wall | 1 | $3 | $2–$3 | LCSC |
| 17 | 3.3V LDO | Shared ESP32 + sensors | 1 | $1 | $0.30–$0.60 | JLCPCB basic |
| 18 | Thermistors NTC 10K | Per zone branch | 5 | $1.50 | $0.80–$1.60 | JLCPCB basic |
| 19 | Overcurrent Protection | Polyfuse per powered zone | 5 | $3 | $2.00–$4.00 | LCSC |
| 20 | Custom PCB (PCBA) | 2-layer, JLCPCB | 1 | $14 | $8–$12 | JLCPCB |
| 21 | Capacitors / Resistors | Assorted SMD | lot | $5 | $1–$3 | JLCPCB basic |
| 22 | Wiring / Connectors | JST, Dupont, misc | lot | $5 | $2–$4 | LCSC |
| 23 | Silicone Lining | Sheet cut per zone — slots + pads | 1 pack | $5 | $3–$5 | LCSC / Local |
| 24 | Frosted Diffuser Strip | Frosted acrylic, LED bar | 1 | $2 | $1–$2 | Local |
| **Electronics subtotal** | | | | **~$110** | **~$72** | |

### Enclosure

| # | Part | Spec | Qty | Unit Cost (15 units) | Unit Cost (50 units) | Source |
|---|------|------|-----|---------------------|---------------------|--------|
| 25 | 3D Printed Shell | JLCPCB FDM, full stepped body, matte ABS — **Batch 1** | 1 | $55–$75 | — | JLCPCB 3D printing |
| 26 | Aluminum Top Plate + Step Faces | 1.5mm sheet, stepped profile — **Batch 2+** | 1 | — | $10–$15 | Local laser cutter 50+ |
| 27 | ABS Base + Slot Walls | Laser cut + assembled — **Batch 2+** | 1 | — | $15–$22 | Local fabrication |
| 28 | Rubber Feet | ×4, logo emboss optional | 1 set | $2 | $1–$2 | Local / AliExpress |
| 29 | M3 Fasteners | Screws + inserts | 1 lot | $1 | $0.50–$1 | LCSC / Local |
| **Enclosure subtotal** | | | | **~$58–$78** | **~$28** | |

> **Batch 1 note:** Full enclosure is FDM 3D printed ABS. Brushed aluminium surfaces and slot wall reinforcements are introduced in Batch 2. Geometry is identical across batches.

### Packaging & In-Box Contents

| # | Item | Spec | Qty | Unit Cost | Source |
|---|------|------|-----|-----------|--------|
| 30 | 1.5m braided IEC C13 cable | Right-angle C13 end, braided | 1 | $2.50–$3.50 | AliExpress / Local bulk |
| 31 | Rigid kraft box | Structured corners, ~750×340×100mm | 1 | $3.50–$5.00 | Local (small run) / 100 unit MOQ |
| 32 | Die-cut foam insert | Custom cut, holds dock + cable | 1 | $3–$4 | Local |
| 33 | Black tissue paper | Wrap around dock | 1 sheet | $0.30–$0.50 | Local |
| 34 | Epitome Penta logo sticker | On tissue wrap | 1 | $0.25–$0.50 | Local |
| 35 | Warranty registration card | 85×55mm, matte laminate, QR to registration page | 1 | $0.25 | Local print shop |
| 36 | Quick-start guide | 4-panel fold, 148×105mm, full colour | 1 | $0.15 | Local print shop |
| **Packaging subtotal** | | | | **~$10–$15** | |

---

## Cost Totals by Volume

| Quantity | Enclosure Method | Per-Unit Cost | Notes |
|----------|-----------------|---------------|-------|
| **13–15 units (Batch 1)** | **3D printed ABS shell (JLCPCB FDM)** | **~$130–$155** | Larger enclosure increases print cost vs old design |
| 20–50 units | Laser cut + bent enclosure | ~$90–$100 | Volume enclosure pricing kicks in |
| **50 units** | **Laser cut + aluminum surfaces** | **~$85** | Includes full in-box bundle |
| 100+ units | Injection mold base + aluminum surfaces | ~$78 | Volume PCB panels, 100 unit MOQ on box |

---

## Batch 1 Budget (13–15 Units)

| Item | Cost (13 units) | Cost (15 units) |
|------|----------------|----------------|
| Electronics × units | ~$1,430 | ~$1,650 |
| 3D printed enclosure × units | ~$715–$975 | ~$825–$1,125 |
| Packaging × units | ~$130–$195 | ~$150–$225 |
| **Total** | **~$1,500–$1,600** | **~$1,700–$2,000** |

> **Note:** The larger enclosure (700mm wide) increases Batch 1 3D print cost significantly vs the old design.
> Get a JLCPCB FDM quote with the final dimensions before committing to batch size.

### Batch 1 Revenue & Profit (at $249/unit)

| Units Sold | Revenue | Investment | Profit / (Loss) |
|------------|---------|------------|-----------------|
| 1 | $249 | $1,550 | ($1,301) |
| 5 | $1,245 | $1,550 | ($305) |
| **7** | **$1,743** | **$1,550** | **$193** ← break-even |
| 10 | $2,490 | $1,550 | **$940** |
| 13 | $3,237 | $1,550 | **$1,687** |
| 15 | $3,735 | $1,550 | **$2,185** |

---

## Approved Suppliers

| Supplier | Use For |
|----------|---------|
| LCSC (lcsc.com) | ICs, passives, modules, connectors, sensors |
| JLCPCB (jlcpcb.com) | Custom PCB + PCBA assembly + Batch 1 3D printed enclosure |
| AliExpress | Prototype breakout boards, Qi coils, magnets, packaging items |
| Local laser cutter | Aluminum surfaces + ABS base at 50+ units (Batch 2+) |
| Local print shop | Warranty card, quick-start guide |

---

## What NOT to Source From
- Amazon (high counterfeit risk for power/PD parts)
- eBay (unverifiable sourcing)
- Unknown AliExpress stores with no trade history or reviews
