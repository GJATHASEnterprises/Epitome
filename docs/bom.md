# Quad-Dock — Bill of Materials (BOM)

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

| # | Part | Spec | Qty | Unit Cost | Total Est. | Source |
|---|------|------|-----|-----------|------------|--------|
| 1 | Qi 15W TX Module | 50mm coil, 15W | 1 | $5–$8 | $5–$8 | LCSC (order ×10) |
| 2 | Qi 5W TX Module | Buds-friendly wireless TX | 1 | $3–$5 | $3–$5 | LCSC / AliExpress |
| 3 | Apple Watch Puck | Magnetic puck, 5W | 1 | $4–$6 | $4–$6 | Bulk ×10 order |
| 4 | USB-C PD Board | 100W capable | 1 | $8–$12 | $8–$12 | LCSC |
| 5 | USB-C PD Board | 20W capable | 1 | $5–$8 | $5–$8 | LCSC |
| 6 | ESP32-C3 Mini | RISC-V, WiFi + BLE | 1 | $2–$3 | $2–$3 | LCSC |
| 7 | INA3221 | 3-ch I2C, Zones 1–3 | 1 | $2–$4 | $2–$4 | LCSC |
| 8 | INA219 | 1-ch I2C, Zone 4 | 1 | $1–$2 | $1–$2 | LCSC |
| 9 | INA219 | 1-ch I2C, Zone 5 | 1 | $1–$2 | $1–$2 | LCSC |
| 10 | BH1750 | I2C ambient light | 1 | $0.50–$1 | $0.50–$1 | LCSC |
| 11 | WS2812B LED Strip | 20 LEDs cut from 60/m | 1 | $2–$4 | $2–$4 | LCSC |
| 12 | N52 Ring Magnets | Ring, Zone 1 alignment | 1 set | $1–$2 | $1–$2 | LCSC / AliExpress |
| 13 | Internal AC/DC PSU | 180W, 20V out | 1 | $10–$15 | $10–$15 | LCSC bulk 50+ units |
| 14 | IEC C13 Inlet | Panel mount + fuse | 1 | $2–$3 | $2–$3 | LCSC |
| 15 | 1.5m braided IEC C13 cable | Right-angle C13 end | 1 | $2.50–$3.50 | $2.50–$3.50 | AliExpress / Local bulk |
| 16 | 3.3V LDO | Shared ESP32 + sensors | 1 | $0.30–$0.60 | $0.30–$0.60 | JLCPCB basic |
| 17 | Thermistors NTC 10K | Per zone branch | 4 | $0.20–$0.40 | $0.80–$1.60 | JLCPCB basic |
| 18 | Overcurrent Protection | Polyfuse per powered zone | 5 | $0.40–$0.80 | $2.00–$4.00 | LCSC |
| 19 | Custom PCB (PCBA) | 2-layer, JLCPCB, 4/panel | 1 | $8–$12 | $8–$12 | JLCPCB |
| 20 | Capacitors / Resistors | Assorted SMD | lot | $1–$3 | $1–$3 | JLCPCB basic |
| 21 | Wiring / Connectors | JST, Dupont, misc | lot | $2–$4 | $2–$4 | LCSC |
| 22 | Silicone Lining | Sheet cut per zone pocket/groove | 1 pack | $2–$4 | $2–$4 | LCSC / Local |
| 23 | Frosted Diffuser Strip | Frosted acrylic, LED bar | 1 | $1–$2 | $1–$2 | Local |
| 24 | Aluminum Top Plate | 1.5mm sheet, Arc profile | 1 | $6–$10 | $6–$10 | Local laser cutter 50+ |
| 25 | ABS Base | Laser cut + bent (Batch 1) | 1 | $12–$18 | $12–$18 | Local fabrication |
| 26 | Rubber Feet | ×4, Quad-Dock logo emboss | 1 set | $1–$2 | $1–$2 | Local / AliExpress |
| 27 | M3 Fasteners | Screws only (snap-fit + 2) | 1 lot | $0.50–$1 | $0.50–$1 | LCSC / Local |
| 28 | Kraft Box | Rigid, structured corners | 1 | $2–$3 | $2–$3 | 100 unit MOQ |
| 29 | Die-Cut Foam Insert | Holds dock, no shift | 1 | $1.50–$2.50 | $1.50–$2.50 | Local |
| 30 | Black Tissue Paper | Wrap around dock | 1 sheet | $0.30–$0.50 | $0.30–$0.50 | Local |
| 31 | Quad-Dock Logo Sticker | On tissue wrap | 1 | $0.25–$0.50 | $0.25–$0.50 | Local |
| 32 | Warranty Registration Card | 85×55mm printed insert | 1 | $0.25 | $0.25 | Local |
| 33 | Quick Start Guide | Folded setup card | 1 | $0.15 | $0.15 | Local |

---

## Cost Totals by Volume

| Quantity | Realistic Middle | Notes |
|----------|-----------------|-------|
| 20–50 units | ~$84–$92 | Laser cut enclosure, no mold, standard sourcing |
| **50 units** | **~$79** | Includes 5-zone electronics and in-box bundle |
| 100+ units | ~$75 | Volume PCB panels, 100 unit MOQ on box |

---

## Packaging Cost Breakdown

| Item | Cost |
|------|------|
| Rigid kraft box | $2–$3 |
| Die-cut foam insert | $1.50–$2.50 |
| Black tissue paper | $0.30–$0.50 |
| Quad-Dock logo sticker | $0.25–$0.50 |
| Warranty registration card | $0.25 |
| Quick-start guide | $0.15 |
| IEC C13 braided cable | $2.50–$3.50 |
| **Total packaging** | **$6.95–$10.40** |

Bundling the IEC cable keeps the dock usable out of the box and the warranty card captures buyer emails for batch 2 follow-up.

---

## Bulk Sourcing Notes (to Hit ~$79 at 50 Units)

| Change | Saving |
|--------|--------|
| Source PSU from LCSC in bulk (50+ units) | -$3–$5 |
| Combine PCB panels (4 boards per panel at JLCPCB) | -$2–$3 |
| Aluminum top via local laser cutter at 50+ units | -$2–$4 |
| Apple Watch puck in bulk (×10 minimum order) | -$1–$2 |
| Kraft box at 100 unit MOQ | -$1–$2 |
| Qi coils from LCSC in sets of 10 | -$1–$2 |
| **Total additional savings** | **-$10–$18** |

---

## Injection Mold Note (Deferred to Batch 2)

The ABS base is laser cut + bent for Batch 1. An injection mold is planned for Batch 2 after break-even.

| | Cost |
|-|------|
| Mold tooling (one-time) | $800–$1,500 |
| Per-unit cost with mold | ~$6–$10 |
| When to order | After ~19 units sold (break-even on $1,500 investment) |

See [production-roadmap.md](production-roadmap.md).

---

## Approved Suppliers

| Supplier | Use For |
|----------|---------|
| LCSC (lcsc.com) | ICs, passives, modules, connectors, sensors |
| JLCPCB (jlcpcb.com) | Custom PCB + PCBA assembly (4 boards per panel) |
| AliExpress | Prototype breakout boards, Qi coils, magnets, packaging |
| Local laser cutter | Aluminum top plate + ABS base at 50+ units |

---

## What NOT to Source From
- Amazon (high counterfeit risk for power/PD parts)
- eBay (unverifiable sourcing)
- Unknown AliExpress stores with no trade history or reviews
