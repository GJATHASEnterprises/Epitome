# Epitome Penta — Bill of Materials (BOM)

## Batch 1 Context

- **Location:** Downers Grove, IL (Chicago suburb)
- **Batch size:** 10 units (Batch 1 — US, August 2026)
- **SKU scope:** Standard SKU only (XL is Batch 2+)
- **Colour scope:** Black only
- **Budget:** $1,500
- **Sell price:** $249
- **Tariffs:** Section 301 at 25% (**Section 122 expired July 24 2026 — no longer applies**)
- **Enclosure:** Full ABS — 3D printed centre platform (school printer, own filament) + laser cut ABS panels (Pumping Station One makerspace, Chicago)
- **Batch 1 material rule:** No aluminium anywhere in Batch 1

---

## Device Size Reference

| Device | Orientation | Slot used | Slot length |
|---|---|---|---|
| Laptop (Standard) — up to 17" class | On thin edge (like book on shelf) | Zone 4 | 400mm |
| Tablet — iPad Pro 13" in case | On thin edge (like book on shelf) | Zone 5 | 290mm |

---

## Zone Sizes

| Zone | Function | Internal size (L × D × W) | Notes |
|---|---|---|---|
| Zone 1 | Phone Qi pad | 160×100mm surface | 20W, MagSafe ring |
| Zone 2 | Buds/Phone pad | 90×65mm dish | 15W |
| Zone 3 | Watch cradle | 50×50mm | Apple puck + Qi coil |
| Zone 4 | Laptop slot | **400×90×35mm** | Cable from top, device on thin edge |
| Zone 5 | iPad slot | **290×70×20mm** | Cable from top, device on thin edge |

---

## Cardboard Prototype Cut Guide

| Piece | Dimensions |
|---|---|
| Base plate | 250mm × 100mm |
| Left slot outer box | 400mm × 90mm × 35mm |
| Left slot inner cavity | 400mm × 90mm × 35mm (cardboard prototype — no wall offset) |
| Centre Step 1 block | 180mm × 100mm × 40mm |
| Centre Step 2 block | 140mm × 100mm × 40mm |
| Right slot outer box | 290mm × 70mm × 20mm |
| Right slot inner cavity | 290mm × 70mm × 20mm (cardboard prototype — no wall offset) |

---

## Production BOM — Electronics & Internals

| # | Part | Spec | Qty | Source | Unit Cost (10 units) |
|---|---|---|---|---|---|
| 1 | Qi 20W TX Module | Zone 1 phone pad | 1 | Amazon domestic | $14.00 |
| 2 | Qi 15W TX Module | Zone 2 buds/phone pad | 1 | Amazon domestic | $11.00 |
| 3 | Apple Watch Puck PCBA | Zone 3 | 1 | AliExpress + 25% tariff | $2.00 |
| 4 | Qi watch coil 5W | Zone 3 universal watch | 1 | AliExpress + 25% tariff | $6.25 |
| 5 | USB-C PD 100W trigger board | Zone 4 | 1 | AliExpress + 25% tariff | $1.88 |
| 6 | USB-C PD 20W trigger board | Zone 5 | 1 | AliExpress + 25% tariff | $1.56 |
| 7 | Captive USB-C cable 220mm 100W braided | Zone 4 | 1 | Amazon domestic | $4.00 |
| 8 | Captive USB-C cable 200mm 20W braided | Zone 5 | 1 | Amazon domestic | $3.00 |
| 9 | ESP32-C3 SuperMini | MCU | 1 | AliExpress + 25% tariff | $1.58 |
| 10 | INA3221 chip ×2 + bare breakout PCB ×2 | Monitoring | 1 lot | LCSC chips + JLCPCB PCBs | $3.40 |
| 11 | Mean Well LRS-150-24 PSU | 156W 24V internal | 1 | LCSC + 25% tariff | $17.31 |
| 12 | IEC C13 right-angle inlet | Panel mount | 1 | AliExpress + 25% tariff | $3.75 |
| 13 | WS2811 LED strip (~20 LED section) | Front diffuser | 1 | AliExpress + 25% tariff ($1.75 × 1.25) | $2.19 |
| 14 | PTC fuse + passives | Safety | 1 lot | Amazon domestic | $1.00 |
| 15 | Wiring / JST connectors / heat shrink / clips | Internal harness | 1 lot | Amazon domestic | $8.00 |
| **Electronics subtotal** | | | | | **$81.92/unit** |

---

## Enclosure

| # | Part | Spec | Qty | Unit Cost (10 units) |
|---|---|---|---|---|
| 16 | 3D printed centre platform | ABS, school printer, own filament | 1 | $2.00 |
| 17 | Laser cut ABS base plate | 250×100mm, 3mm ABS | 1 | $1.35 |
| 18 | Laser cut ABS top panels | 2× panels, 3mm ABS | 1 set | $1.35 |
| 19 | Laser cut ABS laptop slot walls | 400mm length, 3mm ABS | 1 set | $7.84 |
| 20 | Laser cut ABS tablet slot walls | 290mm length, 3mm ABS | 1 set | $5.05 |
| 21 | Frosted acrylic LED diffuser strip | 250×15mm, 3mm | 1 | $0.80 |
| 22 | Silicone sheet lining | All slots + pad surfaces, ~1,111cm² | 1 lot | $3.50 |
| 23 | Rubber feet ×4 + M3 fasteners + grommets | Base hardware | 1 set | $2.60 |
| 24 | Cardboard insert + felt liner | Packaging inner | 1 | $0.70 |
| 25 | Laser cutting setup fee (amortised over 10) | One-time job setup | 1 | $1.50 |
| 26 | ABS cement + finishing consumables | Primer, paint, sandpaper | 1 lot | $2.00 |
| **Enclosure subtotal** | | | | **$28.69/unit** |

---

## Packaging

| # | Item | Spec | Qty | Unit Cost |
|---|---|---|---|---|
| 27 | Rigid kraft box | ~300×150×120mm (new compact size) | 1 | $3.00 |
| 28 | IEC C13 braided cable 1.5m | Right-angle C13 end | 1 | $3.00 |
| 29 | Warranty card | 12-month + QR | 1 | $0.25 |
| 30 | Quick-start guide | 4-panel fold | 1 | $0.15 |
| 31 | Tape + shipping label | Per unit | 1 | $0.50 |
| **Packaging subtotal** | | | | **$6.90/unit** |

---

## Cost Totals by Volume

| Quantity | Method | Per-Unit Build Cost | Notes |
|---|---|---|---|
| **10 units (Batch 1)** | School 3D print + local laser cut ABS | **~$117.51** | Build cost only, excl. shipping/fees |
| 50 units (Batch 2) | Local laser cut + volume electronics | ~$92–99 | After supplier relationships established |

---

## Batch 1 — 10 Units, US (Downers Grove IL), August 2026

| Category | Per Unit | ×10 Total |
|---|---|---|
| Electronics | $81.92 | $819.20 |
| Enclosure (school print + local laser) | $28.69 | $286.90 |
| Packaging | $6.90 | $69.00 |
| UPS/FedEx Ground to customer (~2kg box) | $11.00 | $110.00 |
| Stripe fees (2.9% + $0.30 on $249) | $7.52 | $75.20 |
| Defect/spare buffer (1 unit parts cost) | $9.19 | $91.90 |
| Domain + Carrd landing page | $1.50 | $15.00 |
| **Total real cost** | **$146.72** | **$1,467.20** |

**Revenue & Profit:**

| Units Sold | Revenue @ $249 | Total Cost | Profit / (Loss) |
|---|---|---|---|
| 1 | $249 | $1,467 | ($1,218) |
| 5 | $1,245 | $1,467 | ($222) |
| 7 | $1,743 | $1,467 | $276 |
| **10** | **$2,490** | **$1,467** | **$1,023** |

**Break-even: 6 units sold.**
**Budget note: $1,467 total spend is within the $1,500 build budget with $33 safety net. Take 1 pre-order before ordering parts to create a comfortable $282 safety net.**

---

## Approved Suppliers

| Supplier | Use For |
|---|---|
| AliExpress (verified sellers) | ESP32, PD boards, Apple Watch puck, Qi coil, WS2811, IEC inlet |
| LCSC | Mean Well PSU, INA3221 chips, passives |
| JLCPCB | Bare INA3221 breakout PCBs |
| Amazon US (Prime, US warehouse) | Qi modules, cables, wiring, rubber feet, M3 hardware, silicone sheet |
| Inventables (Chicago) | ABS sheet 3mm, frosted acrylic strip |
| Pumping Station One (Chicago) | Laser cutting all ABS panels and acrylic diffuser |
| School makerspace | 3D printing centre platform ×10 |
| Home Depot / Walmart (Downers Grove) | Acetone, primer, paint, sandpaper |
| Microcenter (Westmont IL) | Backup ESP32, soldering supplies |
| Wise.com | International transfers to AliExpress/LCSC |

---

## Tariff Note (August 2026)

- Section 301: **25% active** on Chinese electronics
- Section 122: **EXPIRED July 24 2026** — no longer applied
- All AliExpress/LCSC costs above already include **25% Section 301**
