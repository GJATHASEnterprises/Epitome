# Epitome Penta — Bill of Materials (BOM)

**Target BOM:** ~$79 per unit at 50 units with the full 5-zone / in-box bundle spec

---

## Prototype BOM (Breakout Boards — No Custom PCB)

Use this for the prototype build. No JLCPCB PCB order required — all breakout boards on breadboard.

| # | Part | Spec | Qty | Unit Cost (Est.) | Source |
|---|------|------|-----|------------------|--------|
| 1 | ESP32-C3 Mini dev board | ESP32-C3 Mini, USB flashing | 2 | $3–$5 | LCSC / AliExpress |
| 2 | Qi 15W TX coil module | 50mm coil, 15W, breakout | 2 | $5–$8 | AliExpress |
| 3 | Apple Watch charger module | Standard puck, 5W | 1 | $8–$12 | AliExpress |
| 4 | USB-C PD 100W controller board | Pre-made breakout | 1 | $8–$14 | AliExpress |
| 5 | USB-C PD 20W controller board | Pre-made breakout | 1 | $5–$8 | LCSC / AliExpress |
| 6 | INA3221 breakout board | 3-ch I2C power monitor | 1 | $2–$4 | LCSC / AliExpress |
| 7 | INA219 breakout board | 1-ch I2C power monitor | 2 | $1–$3 | LCSC / AliExpress |
| 8 | BH1750 breakout board | I2C ambient light sensor | 1 | $1–$2 | AliExpress |
| 9 | WS2812B LED strip | 1m reel (cut to 20 LEDs) | 1 | $3–$5 | AliExpress |
| 10 | N52 ring magnets (×5) | Fits 50mm Qi coil | 1 pk | $3–$5 | AliExpress |
| 11 | 180W AC/DC PSU module | 100–240V in, 20V out | 1 | $15–$22 | AliExpress / LCSC |
| 12 | IEC C13 inlet socket | Panel mount | 1 | $2–$3 | AliExpress |
| 13 | IEC C13 braided power cable | 1.5m bundle cable | 1 | $2–$4 | AliExpress |
| 14 | Breadboard (full size) | 830 tie-points | 2 | $3–$5 | Local / AliExpress |
| 15 | Jumper wires | Male-male, male-female | 2 packs | $2–$4 | Local / AliExpress |
| 16 | USB-C connectors + breakout | Breakout boards | 3 | $1–$2 | AliExpress |
| 17 | Assorted resistors/capacitors | 300Ω, 100µF, 10K NTC | lot | $3–$5 | LCSC |
| 18 | Warranty registration card | Printed insert | 1 | $0.25 | Local |
| 19 | Frosted acrylic strip | LED diffuser test piece | 1 | $5–$10 | Local |
| **Prototype electronics total** | | | | **$86–$145** | |

*Order 25% extra for spares. Budget ~$95–$155 for electronics and in-box items.*

---

## Production BOM (Full JLCPCB PCBA)

### Electronics & Internals

| # | Part | Spec | Qty | Unit Cost (15 units) | Unit Cost (50 units) | Source |
|---|------|------|-----|---------------------|---------------------|--------|
| 1 | Qi 15W TX Module | 50mm coil, 15W | 1 | $7 | $5–$6 | LCSC / AliExpress |
| 2 | Qi 5W TX Module | Buds-friendly wireless TX | 1 | $5 | $3–$4 | LCSC / AliExpress |
| 3 | Apple Watch Puck | Magnetic puck, 5W | 1 | $10 | $4–$6 | Bulk ×10 order |
| 4 | USB-C PD Board | 100W capable | 1 | $11 | $8–$10 | LCSC |
| 5 | USB-C PD Board | 20W capable | 1 | $7 | $5–$6 | LCSC |
| 6 | ESP32-C3 Mini | RISC-V, WiFi + BLE | 1 | $4 | $2–$3 | LCSC |
| 7 | INA3221 | 3-ch I2C, Zones 1–3 | 1 | $3 | $2–$3 | LCSC |
| 8 | INA219 Zone 4 | 1-ch I2C, Zone 4 | 1 | $2 | $1–$2 | LCSC |
| 9 | INA219 Zone 5 | 1-ch I2C, Zone 5 | 1 | $2 | $1–$2 | LCSC |
| 10 | BH1750 | I2C ambient light | 1 | $1 | $0.50–$1 | LCSC |
| 11 | WS2812B LED Strip | 20 LEDs cut from 60/m | 1 | $3 | $2–$3 | LCSC |
| 12 | N52 Ring Magnets | Ring, Zone 1 alignment | 1 set | $2 | $1–$2 | LCSC / AliExpress |
| 13 | Internal AC/DC PSU | 180W, 20V out | 1 | $20 | $10–$15 | LCSC |
| 14 | IEC C13 Inlet | Panel mount + fuse | 1 | $3 | $2–$3 | LCSC |
| 15 | 3.3V LDO | Shared ESP32 + sensors | 1 | $1 | $0.30–$0.60 | JLCPCB basic |
| 16 | Thermistors NTC 10K | Per zone branch | 4 | $1.50 | $0.80–$1.60 | JLCPCB basic |
| 17 | Overcurrent Protection | Polyfuse per powered zone | 5 | $3 | $2.00–$4.00 | LCSC |
| 18 | Custom PCB (PCBA) | 2-layer, JLCPCB | 1 | $14 | $8–$12 | JLCPCB |
| 19 | Capacitors / Resistors | Assorted SMD | lot | $5 | $1–$3 | JLCPCB basic |
| 20 | Wiring / Connectors | JST, Dupont, misc | lot | $5 | $2–$4 | LCSC |
| 21 | Silicone Lining | Sheet cut per zone pocket/groove | 1 pack | $3 | $2–$4 | LCSC / Local |
| 22 | Frosted Diffuser Strip | Frosted acrylic, LED bar | 1 | $2 | $1–$2 | Local |
| **Electronics subtotal** | | | | **~$104** | **~$67** | |

### Enclosure

| # | Part | Spec | Qty | Unit Cost (15 units) | Unit Cost (50 units) | Source |
|---|------|------|-----|---------------------|---------------------|--------|
| 23 | 3D Printed Shell | JLCPCB FDM, full Arc body, matte ABS — **Batch 1** | 1 | $40–$55 | — | JLCPCB 3D printing |
| 24 | Aluminum Top Plate | 1.5mm sheet, Arc profile — **Batch 2+** | 1 | — | $6–$10 | Local laser cutter 50+ |
| 25 | ABS Base | Laser cut + bent — **Batch 2+** | 1 | — | $12–$18 | Local fabrication |
| 26 | Rubber Feet | ×4, Epitome Penta logo emboss | 1 set | $2 | $1–$2 | Local / AliExpress |
| 27 | M3 Fasteners | Screws only (snap-fit + 2) | 1 lot | $1 | $0.50–$1 | LCSC / Local |
| **Enclosure subtotal** | | | | **~$45–$58** | **~$22** | |

> **Batch 1 note:** The aluminum top plate is replaced by a painted/primed matte ABS top (part of the 3D printed shell). Shape and all zones are identical. The brushed aluminum top is introduced in Batch 2 once the injection mold is funded.

### Packaging & In-Box Contents

| # | Item | Spec | Qty | Unit Cost | Source |
|---|------|------|-----|-----------|--------|
| 28 | 1.5m braided IEC C13 cable | Right-angle C13 end, braided | 1 | $2.50–$3.50 | AliExpress / Local bulk |
| 29 | Rigid kraft box | Structured corners, 340×180×90mm | 1 | $2.50–$3.50 | Local (small run) / 100 unit MOQ |
| 30 | Die-cut foam insert | Custom cut, holds dock + cable | 1 | $2–$2.50 | Local |
| 31 | Black tissue paper | Wrap around dock | 1 sheet | $0.30–$0.50 | Local |
| 32 | Epitome Penta logo sticker | On tissue wrap | 1 | $0.25–$0.50 | Local |
| 33 | Warranty registration card | 85×55mm, matte laminate, QR to registration page | 1 | $0.25 | Local print shop |
| 34 | Quick-start guide | 4-panel fold, 148×105mm, full colour | 1 | $0.15 | Local print shop |
| **Packaging subtotal** | | | | **~$8–$11** | |

---

## Cost Totals by Volume

| Quantity | Enclosure Method | Per-Unit Cost | Notes |
|----------|-----------------|---------------|-------|
| **13–15 units (Batch 1)** | **3D printed ABS shell (JLCPCB FDM)** | **~$115–$125** | No mold, no laser cut — fits $1,500 budget |
| 20–50 units | Laser cut + bent enclosure | ~$84–$92 | Volume enclosure pricing kicks in |
| **50 units** | **Laser cut + aluminum top plate** | **~$79** | Includes full in-box bundle |
| 100+ units | Injection mold base + aluminum top | ~$75 | Volume PCB panels, 100 unit MOQ on box |

---

## Batch 1 Budget (13–15 Units at ~$120/unit)

| Item | Cost (13 units) | Cost (15 units) |
|------|----------------|----------------|
| Electronics × units | ~$1,352 | ~$1,560 |
| 3D printed enclosure × units | ~$585–$715 | ~$675–$825 |
| Packaging × units | ~$104–$143 | ~$120–$165 |
| **Total** | **~$1,350–$1,450** | **~$1,500–$1,600** |

> **Target: 13 units = ~$1,400 total — fits within $1,500 budget with ~$100 buffer.**
> 15 units pushes to ~$1,550 — only viable if packaging is sourced cheaply or 3D print quote comes in at the low end.

### Batch 1 Revenue & Profit (at $189/unit)

| Units Sold | Revenue | Investment | Profit / (Loss) |
|------------|---------|------------|-----------------|
| 1 | $189 | $1,400 | ($1,211) |
| 5 | $945 | $1,400 | ($455) |
| 8 | $1,512 | $1,400 | $112 |
| **10** | **$1,890** | **$1,400** | **$490** |
| 13 | $2,457 | $1,400 | **$1,057** ← break-even + profit |
| 15 | $2,835 | $1,400 | **$1,435** |

---

## Packaging Cost Breakdown

| Item | Unit Cost |
|------|-----------|
| 1.5m braided IEC C13 cable | $2.50–$3.50 |
| Rigid kraft box | $2.50–$3.50 |
| Die-cut foam insert | $2.00–$2.50 |
| Black tissue paper | $0.30–$0.50 |
| Epitome Penta logo sticker | $0.25–$0.50 |
| Warranty registration card | $0.25 |
| Quick-start guide | $0.15 |
| **Total packaging** | **~$8–$11** |

Bundling the IEC cable keeps the dock usable out of the box — this is the single most common source of 1-star reviews for desktop power products. Bundling it eliminates that entirely.

---

## Bulk Sourcing Notes (to Hit ~$79 at 50 Units)

| Change | Saving |
|--------|--------|
| Source PSU from LCSC in bulk (50+ units) | -$3–$5 |
| Combine PCB panels (4 boards per panel at JLCPCB) | -$2–$3 |
| Aluminum top via local laser cutter at 50+ units | replaces 3D print (-$30–$40/unit) |
| Apple Watch puck in bulk (×10 minimum order) | -$1–$2 |
| Kraft box at 100 unit MOQ | -$1–$2 |
| Qi coils from LCSC in sets of 10 | -$1–$2 |
| **Total additional savings vs Batch 1** | **-$38–$54/unit** |

---

## Injection Mold Note (Deferred to Batch 2)

The Batch 1 enclosure is a JLCPCB FDM 3D printed ABS shell. An injection mold for the ABS base is planned for Batch 2 after break-even, combined with switching to a proper laser-cut brushed aluminum top plate.

| | Cost |
|-|------|
| Mold tooling (one-time) | $800–$1,500 |
| Per-unit base cost with mold | ~$6–$10 |
| When to order | After Batch 1 sells through and profit is confirmed |

See [production-roadmap.md](production-roadmap.md).

---

## Approved Suppliers

| Supplier | Use For |
|----------|---------|
| LCSC (lcsc.com) | ICs, passives, modules, connectors, sensors |
| JLCPCB (jlcpcb.com) | Custom PCB + PCBA assembly + Batch 1 3D printed enclosure |
| AliExpress | Prototype breakout boards, Qi coils, magnets, packaging items |
| Local laser cutter | Aluminum top plate + ABS base at 50+ units (Batch 2+) |
| Local print shop | Warranty card, quick-start guide |

---

## What NOT to Source From
- Amazon (high counterfeit risk for power/PD parts)
- eBay (unverifiable sourcing)
- Unknown AliExpress stores with no trade history or reviews
