# Penta Dock — Bill of Materials (BOM)

## Batch 1 Context

- **Location:** Downers Grove, IL (Chicago suburb)
- **Batch size:** 10 units (Batch 1 — US, August 2026)
- **SKU scope:** Standard SKU only (XL is Batch 2+)
- **Colour scope:** Obsidian (matte black) — Batch 1 only
- **Budget:** $1,500
- **Sell price:** $249
- **Tariffs:** Section 301 at 25% (**Section 122 expired July 24 2026 — no longer applies**)
- **Enclosure:** Full ABS — 3D printed centre platform (school printer, own filament) + laser cut ABS panels (Pumping Station One makerspace, Chicago)
- **Shipping:** NOT included in build cost. Charge actual shipping at checkout via Shopify/Pirateship.
- **Option A pricing note:** All costs are based on Option A (AliExpress modules where cheaper, Amazon for domestic parts).

---

## Device Size Reference

| Device | Model sized for | Key dimension |
|---|---|---|
| Phone | iPhone 16 Pro Max | 163mm × 77mm |
| Tablet | iPad Pro 13" in case | Up to ~16mm total thickness |
| Laptop | 17" class (Standard slot 400mm) | Up to ~28mm slot clearance |
| Watch | Apple Watch Ultra 2 + Qi watches | Step 3 raised cradle zone |

---

## Zone Sizes

| Zone | Function | Internal size (L × D × W) | Notes |
|---|---|---|---|
| Zone 1 | Phone Qi2 pad | 160×100mm surface | 20W, Qi2 certified, magnetic alignment N52 ring, recessed 1mm dish |
| Zone 2 | Buds or second phone pad | 90×70mm dish | 20W Qi |
| Zone 3 | Watch cradle | 50×50mm | Apple puck + Qi coil, hardware relay mutual exclusion |
| Zone 4 | Laptop slot | **400×90×35mm** | 95mm tall wall, captive 220mm 100W braided cable, 90° angled dock-end |
| Zone 5 | iPad slot | **290×70×20mm** | 80mm tall wall, captive 200mm 65W braided cable, 90° angled dock-end |

---

## Power Budget

| Zone | Device | Power | Method |
|---|---|---|---|
| Zone 1 | Phone | 20W | Qi2 (magnetic alignment, N52 ring, recessed 1mm dish) |
| Zone 2 | Buds or second phone | 20W | Qi (90×70mm dish) |
| Zone 3 | Watch | 5W | Apple Watch puck + universal Qi coil, hardware relay |
| Zone 4 | Laptop | 100W | USB-C PD, captive 220mm 100W braided cable, 90° angled dock-end |
| Zone 5 | Tablet | 45W | USB-C PD, captive 200mm 65W braided cable, 90° angled dock-end |
| **Total worst case** | | **190W** | |
| **PSU rated** | | **201W (Mean Well LRS-200-24)** | |
| **Headroom** | | **11W** | |
| **ATtiny85 soft cap** | | **185W** | |

## Wattage Etch Labels

```
PHONE    20W  Qi2
BUDS     20W  Qi
WATCH     5W
LAPTOP  100W  USB-C
TABLET   45W  USB-C
```

---

## Production BOM — Electronics & Internals

| # | Part | Source | Unit Cost |
|---|---|---|---:|
| 1 | Qi2 20W TX module | AliExpress +25% | $6.25 |
| 2 | Qi 20W TX module | AliExpress +25% | $5.50 |
| 3 | Apple Watch puck PCBA | AliExpress +25% | $2.00 |
| 4 | Qi watch coil 5W | AliExpress +25% | $6.25 |
| 5 | USB-C PD 100W trigger board | AliExpress +25% | $1.88 |
| 6 | USB-C PD 45W trigger board | AliExpress +25% | $2.00 |
| 7 | Captive USB-C 220mm 100W braided 90° | Amazon | $4.00 |
| 8 | Captive USB-C 200mm 65W braided 90° | Amazon | $3.00 |
| 9 | Mean Well LRS-200-24 PSU | LCSC +25% | $22.00 |
| 10 | IEC C13 right-angle inlet | AliExpress +25% | $3.75 |
| 11 | ATtiny85 | Amazon | $1.50 |
| 12 | WS2811 LED strip ~15 LED 250mm | AliExpress +25% | $2.19 |
| 13 | 12V buck converter ×2 (Qi zones) | AliExpress +25% | $2.50 |
| 14 | 5V buck converter ×1 (watch zone + ATtiny85) | AliExpress +25% | $1.25 |
| 15 | Hardware relay (Zone 3 mutual exclusion) | Amazon | $1.50 |
| 16 | PTC fuse + polyfuses ×5 + TVS ×2 | Amazon | $2.50 |
| 17 | NTC thermistors ×2 + thermal cutoff | Amazon | $1.50 |
| 18 | Wiring / JST / heat shrink (bulk) | Amazon | $2.60 |
| **Electronics subtotal** | | | **$72.17** |

---

## Enclosure BOM

| # | Part | Unit Cost |
|---|---|---:|
| 1 | 3D printed centre platform (school, own filament) | $2.00 |
| 2 | Laser cut ABS base plate 250×100mm | $1.35 |
| 3 | Laser cut ABS top panels ×2 | $1.35 |
| 4 | Laser cut ABS laptop slot walls 400mm 95mm tall | $7.84 |
| 5 | Laser cut ABS tablet slot walls 290mm 80mm tall | $5.35 |
| 6 | Laser cut ABS rear spine plate 250×100mm | $1.50 |
| 7 | Laser cut ABS front fascia strip 250×20mm | $0.70 |
| 8 | Frosted acrylic LED diffuser 250×15mm | $0.80 |
| 9 | Silicone sheet textured dot ~1,150cm² | $3.70 |
| 10 | 3M Bumpons SJ5023 ×4 | $0.60 |
| 11 | Physical power button rear rail | $1.50 |
| 12 | M3 fasteners + heat-set inserts + grommets | $2.00 |
| 13 | Laser cutting setup fee ÷10 | $1.50 |
| 14 | ABS cement + primer + matte black paint + sandpaper | $2.50 |
| 15 | Strain relief silicone boots ×2 (captive cables) | $0.60 |
| 16 | Microfibre slot lining (Zones 4+5 inner walls) | $1.30 |
| **Enclosure subtotal** | | **$34.09** |

---

## Packaging BOM

| # | Item | Unit Cost |
|---|---|---:|
| 1 | Magnetic closure rigid box ~300×160×130mm matte black | $5.50 |
| 2 | Black foam insert — dock shape | $1.50 |
| 3 | Black foam insert — cables | $0.80 |
| 4 | Braided fabric IEC C13 cable 1.5m matte black | $5.50 |
| 5 | Setup card 85×55mm matte black (Moo.com) | $0.35 |
| 6 | Belly band "Penta Dock — One dock. Every device." | $0.50 |
| 7 | Printed inner lid insert (home laser printer on card) | $0.20 |
| 8 | Velcro cable tie matte black | $0.10 |
| 9 | Tape + shipping label | $0.50 |
| **Packaging subtotal** | | **$14.95** |

---

## Build Cost Summary

| Category | Per Unit |
|---|---:|
| Electronics | $72.17 |
| Enclosure | $34.09 |
| Packaging | $14.95 |
| **Total build cost per unit** | **$121.21** |

---

## Full Per-Unit Cost (no shipping — charged to customer at checkout)

| Item | Cost |
|---|---:|
| Build cost | $121.21 |
| Stripe fees (2.9% + $0.30 on $249) | $7.52 |
| Defect buffer (10% of build cost) | $12.09 |
| Domain epitomecharge.com ÷10 | $1.10 |
| **Total per unit** | **$141.92** |
| **Total ×10 units** | **$1,419.20** |

---

## Profit Table

| Units Sold | Revenue @ $249 | Total Cost | Profit/(Loss) |
|---|---:|---:|---:|
| 5 | $1,245 | $1,419 | ($174) |
| 6 | $1,494 | $1,419 | $75 ← break-even |
| 7 | $1,743 | $1,419 | $324 |
| 8 | $1,992 | $1,419 | $573 |
| 10 | $2,490 | $1,419 | **$1,071** |

**Break-even: 6 units**
**Profit at full batch (10 units): $1,074**
**Margin: 43%**

**Budget note:** Budget $1,500 — total batch cost $1,419 — **$81 safety net without any pre-order.**

---

## Approved Suppliers

| Supplier | Use For |
|---|---|
| AliExpress (verified sellers) | Qi2 module, Qi module, Apple Watch puck, Qi watch coil, PD boards, WS2811, IEC inlet, buck converters |
| LCSC | Mean Well LRS-200-24 PSU |
| Amazon US (Prime, US warehouse) | ATtiny85, captive cables, hardware relay, fuses/TVS, thermistors, wiring/JST, Bumpons, power button |
| Inventables (Chicago) | ABS sheet 3mm, frosted acrylic strip |
| Pumping Station One (Chicago) | Laser cutting all ABS panels and acrylic diffuser |
| School makerspace | 3D printing centre platform ×10 |
| Home Depot / Walmart (Downers Grove) | Acetone, primer, paint, sandpaper |
| Microcenter (Westmont IL) | Backup electronics, soldering supplies |
| Moo.com | Setup cards 85×55mm matte black |
| Wise.com | International transfers to AliExpress/LCSC |

---

## Tariff Note (August 2026)

- Section 301: **25% active** on Chinese electronics
- Section 122: **EXPIRED July 24 2026** — no longer applied
- All AliExpress/LCSC costs above already include **25% Section 301**
