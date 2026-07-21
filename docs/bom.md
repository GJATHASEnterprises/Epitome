# Quad-Dock — Bill of Materials (BOM)

**Target BOM:** ~$67 per unit at 50 units with smart bulk sourcing

---

## Prototype BOM (Breakout Boards — No Custom PCB)

Use this for the prototype build. No JLCPCB PCB order required — all breakout boards on breadboard.

| # | Part | Spec | Qty | Unit Cost (Est.) | Source |
|---|------|------|-----|------------------|--------|
| 1 | ESP32-C3 Mini dev board | ESP32-C3 Mini, USB flashing | 2 | $3–$5 | LCSC / AliExpress |
| 2 | Qi 15W TX coil module | 50mm coil, 15W, breakout | 2 | $5–$8 | AliExpress |
| 3 | Apple Watch charger module | Standard puck, 5W | 1 | $8–$12 | AliExpress |
| 4 | USB-C PD 100W controller board | Pre-made breakout | 1 | $8–$14 | AliExpress |
| 5 | INA3221 breakout board | 3-ch I2C power monitor | 1 | $2–$4 | LCSC / AliExpress |
| 6 | INA219 breakout board | 1-ch I2C power monitor | 1 | $1–$3 | LCSC / AliExpress |
| 7 | BH1750 breakout board | I2C ambient light sensor | 1 | $1–$2 | AliExpress |
| 8 | WS2812B LED strip | 1m reel (cut to 16 LEDs) | 1 | $3–$5 | AliExpress |
| 9 | N52 ring magnets (×5) | Fits 50mm Qi coil | 1 pk | $3–$5 | AliExpress |
| 10 | 180W AC/DC PSU module | 100–240V in, 20V out | 1 | $15–$22 | AliExpress / LCSC |
| 11 | IEC C13 inlet socket | Panel mount | 1 | $2–$3 | AliExpress |
| 12 | Breadboard (full size) | 830 tie-points | 2 | $3–$5 | Local / AliExpress |
| 13 | Jumper wires | Male-male, male-female | 2 packs | $2–$4 | Local / AliExpress |
| 14 | USB-C connectors + breakout | Breakout boards | 2 | $2–$4 | AliExpress |
| 15 | Assorted resistors/capacitors | 300Ω, 100µF, 10K NTC | lot | $3–$5 | LCSC |
| 16 | Frosted acrylic strip | LED diffuser test piece | 1 | $5–$10 | Local |
| **Prototype electronics total** | | | | **$68–$111** | |

*Order 25% extra for spares. Budget ~$80–$120 for electronics.*

---

## Production BOM (Full JLCPCB PCBA)

| # | Part | Spec | Qty | Unit Cost | Total Est. | Source |
|---|------|------|-----|-----------|------------|--------|
| 1 | Qi 15W TX Module | 50mm coil, 15W | 2 | $5–$8 | $10–$16 | LCSC (order ×10) |
| 2 | Apple Watch Puck | Magnetic puck, 5W | 1 | $4–$6 | $4–$6 | Bulk ×10 order |
| 3 | USB-C PD Board | 100W capable | 1 | $8–$12 | $8–$12 | LCSC |
| 4 | ESP32-C3 Mini | RISC-V, WiFi + BLE | 1 | $2–$3 | $2–$3 | LCSC |
| 5 | INA3221 | 3-ch I2C, Zones 1–3 | 1 | $2–$4 | $2–$4 | LCSC |
| 6 | INA219 | 1-ch I2C, Zone 4 | 1 | $1–$2 | $1–$2 | LCSC |
| 7 | BH1750 | I2C ambient light | 1 | $0.50–$1 | $0.50–$1 | LCSC |
| 8 | WS2812B LED Strip | 16 LEDs cut from 60/m | 1 | $2–$4 | $2–$4 | LCSC |
| 9 | N52 Ring Magnets | Ring, Zone 1 alignment | 1 set | $1–$2 | $1–$2 | LCSC / AliExpress |
| 10 | Internal AC/DC PSU | 180W, 20V out | 1 | $10–$15 | $10–$15 | LCSC bulk 50+ units |
| 11 | IEC C13 Inlet | Panel mount + fuse | 1 | $2–$3 | $2–$3 | LCSC |
| 12 | 3.3V LDO | Shared ESP32 + sensors | 1 | $0.30–$0.60 | $0.30–$0.60 | JLCPCB basic |
| 13 | Thermistors NTC 10K | Per coil zone | 3 | $0.20–$0.40 | $0.60–$1.20 | JLCPCB basic |
| 14 | Overcurrent Protection | Polyfuse per zone | 4 | $0.40–$0.80 | $1.60–$3.20 | LCSC |
| 15 | Custom PCB (PCBA) | 2-layer, JLCPCB, 4/panel | 1 | $8–$12 | $8–$12 | JLCPCB |
| 16 | Capacitors / Resistors | Assorted SMD | lot | $1–$3 | $1–$3 | JLCPCB basic |
| 17 | Wiring / Connectors | JST, Dupont, misc | lot | $2–$4 | $2–$4 | LCSC |
| 18 | Silicone Lining | Sheet cut per zone pocket | 1 pack | $2–$4 | $2–$4 | LCSC / Local |
| 19 | Frosted Diffuser Strip | Frosted acrylic, LED bar | 1 | $1–$2 | $1–$2 | Local |
| 20 | Aluminum Top Plate | 1.5mm sheet, Arc profile | 1 | $6–$10 | $6–$10 | Local laser cutter 50+ |
| 21 | ABS Base | Laser cut + bent (Batch 1) | 1 | $12–$18 | $12–$18 | Local fabrication |
| 22 | Rubber Feet | ×4, Quad-Dock logo emboss | 1 set | $1–$2 | $1–$2 | Local / AliExpress |
| 23 | M3 Fasteners | Screws only (snap-fit + 2) | 1 lot | $0.50–$1 | $0.50–$1 | LCSC / Local |
| 24 | Kraft Box | Rigid, structured corners | 1 | $2–$3 | $2–$3 | 100 unit MOQ |
| 25 | Die-Cut Foam Insert | Holds dock, no shift | 1 | $1.50–$2.50 | $1.50–$2.50 | Local |
| 26 | Black Tissue Paper | Wrap around dock | 1 sheet | $0.30–$0.50 | $0.30–$0.50 | Local |
| 27 | Quad-Dock Logo Sticker | On tissue wrap | 1 | $0.25–$0.50 | $0.25–$0.50 | Local |
| 28 | QR Code Card | Setup + warranty | 1 | $0.25–$0.50 | $0.25–$0.50 | Local |

---

## Cost Totals by Volume

| Quantity | Realistic Middle | Notes |
|----------|-----------------|-------|
| 20–50 units | ~$75–$85 | Laser cut enclosure, no mold, standard sourcing |
| **50 units** | **~$67** | Bulk sourcing applied (see notes below) |
| 100+ units | ~$64 | Volume PCB panels, 100 unit MOQ on box |

---

## Packaging Cost Breakdown

| Item | Cost |
|------|------|
| Rigid kraft box | $2–$3 |
| Die-cut foam insert | $1.50–$2.50 |
| Black tissue paper | $0.30–$0.50 |
| Quad-Dock logo sticker | $0.25–$0.50 |
| QR code card (setup + warranty) | $0.25–$0.50 |
| **Total packaging** | **$4.30–$7** |

No IEC cable bundled. User supplies their own standard PC power cable.

---

## Bulk Sourcing Notes (to Hit ~$67 at 50 Units)

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
| When to order | After ~13 units sold (break-even on $1,500 investment) |

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
