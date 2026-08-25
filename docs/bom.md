# Penta Dock — Bill of Materials (BOM)

## Batch 1 Context

- **Location:** Downers Grove, IL (Chicago suburb)
- **Batch size:** 10 units (Batch 1 — US, August 2026)
- **SKU scope:** Standard SKU only (XL is Batch 2+)
- **Colour scope:** Black only
- **Budget:** $1,500
- **Sell price:** $249
- **Tariffs:** Section 301 at 25% (**Section 122 expired July 24 2026 — no longer applies**)
- **Enclosure:** Full ABS — 3D printed centre platform (school printer, own filament) + laser cut ABS panels (Pumping Station One makerspace, Chicago)

---

## Zone Sizes

| Zone | Function | Internal size (L × D × W) | Notes |
|---|---|---|---|
| Zone 1 | Phone Qi2 pad | 160×100mm surface | 20W, Qi2 certified, magnetic alignment ring compatible |
| Zone 2 | Buds or second phone pad | 120×80mm dish | 20W Qi |
| Zone 3 | Watch cradle | 50×50mm | Apple puck + Qi coil |
| Zone 4 | Laptop slot | **400×90×35mm** | 95mm tall wall, cable from top, device on thin edge |
| Zone 5 | iPad slot | **290×70×20mm** | 75mm tall wall, cable from top, device on thin edge |

---

## Power Budget

| Zone | Device | Power | Method |
|---|---|---|---|
| Zone 1 | Phone | 20W | Qi2 (magnetic alignment) |
| Zone 2 | Buds or second phone | 20W | Qi |
| Zone 3 | Watch | 5W | Apple Watch puck + Qi coil |
| Zone 4 | Laptop | 100W | USB-C PD (captive braided cable) |
| Zone 5 | Tablet | 45W | USB-C PD (captive braided cable) |
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

| # | Part | Spec | Qty | Source | Unit Cost (10 units) |
|---|---|---|---|---|---|
| 1 | Qi2 20W TX Module | Zone 1 — Qi2 certified, magnetic alignment ring compatible | 1 | Amazon domestic | $14.00 |
| 2 | Qi 20W TX Module | Zone 2 buds or second phone pad | 1 | Amazon domestic | $11.00 |
| 3 | Apple Watch Puck PCBA | Zone 3 | 1 | AliExpress + 25% tariff | $2.00 |
| 4 | Qi watch coil 5W | Zone 3 universal watch | 1 | AliExpress + 25% tariff | $6.25 |
| 5 | USB-C PD 100W trigger board | Zone 4 | 1 | AliExpress + 25% tariff | $1.88 |
| 6 | USB-C PD 45W trigger board | Zone 5 | 1 | AliExpress + 25% tariff | $2.06 |
| 7 | Captive USB-C cable 220mm 100W braided | Zone 4 | 1 | Amazon domestic | $4.00 |
| 8 | Captive USB-C cable 200mm 65W braided | Zone 5 | 1 | Amazon domestic | $3.00 |
| 9 | ESP32-C3 SuperMini | MCU | 1 | AliExpress + 25% tariff | $1.58 |
| 10 | INA3221 chip ×2 + bare breakout PCB ×2 | Monitoring | 1 lot | LCSC chips + JLCPCB PCBs | $3.40 |
| 11 | Mean Well LRS-200-24 PSU | 201W 24V internal, under centre platform | 1 | LCSC + 25% tariff | $17.31 |
| 12 | IEC C13 right-angle inlet | Panel mount | 1 | AliExpress + 25% tariff | $3.75 |
| 13 | WS2811 LED strip (~20 LED section) | Front diffuser | 1 | AliExpress + 25% tariff ($1.75 × 1.25) | $2.19 |
| 14 | PTC fuse + passives | Safety | 1 lot | Amazon domestic | $1.00 |
| 15 | Wiring / JST connectors / heat shrink / clips | Internal harness | 1 lot | Amazon domestic | $8.00 |
| **Electronics subtotal** | | | | | **$82.62/unit** |

---

## Enclosure

| # | Part | Spec | Qty | Unit Cost (10 units) |
|---|---|---|---|---|
| 16 | 3D printed centre platform | ABS, school printer, own filament | 1 | $2.00 |
| 17 | Laser cut ABS base plate | 250×100mm, 3mm ABS | 1 | $1.35 |
| 18 | Laser cut ABS top panels | 2× panels, 3mm ABS | 1 set | $1.35 |
| 19 | Laser cut ABS laptop slot walls | 400mm length, 95mm tall, 3mm ABS | 1 set | $7.84 |
| 20 | Laser cut ABS tablet slot walls | 290mm length, 75mm tall, 3mm ABS | 1 set | $5.05 |
| 21 | Laser cut ABS rear spine plate | 250×100mm, 3mm ABS | 1 | $1.50 |
| 22 | Laser cut ABS front fascia strip | 250×20mm, 3mm ABS | 1 | $0.70 |
| 23 | Frosted acrylic LED diffuser strip | 250×15mm, 3mm | 1 | $0.80 |
| 24 | Silicone sheet lining | All slots + pad surfaces, enlarged Zone 2 area | 1 lot | $3.70 |
| 25 | Rubber feet ×4 + M3 fasteners + grommets | Base hardware | 1 set | $2.60 |
| 26 | Cardboard insert + felt liner | Packaging inner | 1 | $0.70 |
| 27 | Laser cutting setup fee (amortised over 10) | One-time job setup | 1 | $1.50 |
| 28 | ABS cement + finishing consumables | Primer, paint, sandpaper | 1 lot | $2.50 |
| **Enclosure subtotal** | | | | **$31.59/unit** |

---

## Packaging

| # | Item | Spec | Qty | Unit Cost |
|---|---|---|---|---|
| 29 | Rigid kraft box | ~300×150×120mm (new compact size) | 1 | $3.00 |
| 30 | IEC C13 braided cable 1.5m | Right-angle C13 end | 1 | $3.00 |
| 31 | Warranty card | 12-month + QR | 1 | $0.25 |
| 32 | Quick-start guide | 4-panel fold | 1 | $0.15 |
| 33 | Tape + shipping label | Per unit | 1 | $0.50 |
| **Packaging subtotal** | | | | **$6.90/unit** |

---

## Cost Totals by Volume

| Quantity | Method | Per-Unit Build Cost | Notes |
|---|---|---|---|
| **10 units (Batch 1)** | School 3D print + local laser cut ABS | **~$121.11** | Build cost only, excl. shipping/fees |
| 50 units (Batch 2) | Local laser cut + volume electronics | ~$92–99 | After supplier relationships established |

---

## Batch 1 — 10 Units, US (Downers Grove IL), August 2026

| Category | Per Unit | ×10 Total |
|---|---|---|
| Electronics | $82.62 | $826.20 |
| Enclosure (school print + local laser) | $31.59 | $315.90 |
| Packaging | $6.90 | $69.00 |
| UPS/FedEx Ground to customer (~2kg box) | $11.00 | $110.00 |
| Stripe fees (2.9% + $0.30 on $249) | $7.52 | $75.20 |
| Defect/spare buffer (10% of build subtotal, rounded) | $12.10 | $121.00 |
| Domain + Carrd landing page | $1.50 | $15.00 |
| **Total real cost** | **$153.23** | **$1,532.30** |

**Revenue & Profit (Sell price: $249):**

| Units Sold | Revenue @ $249 | Total Cost | Profit / (Loss) |
|---|---|---|---|
| 1 | $249 | $1,532.30 | ($1,283.30) |
| 5 | $1,245 | $1,532.30 | ($287.30) |
| 6 | $1,494 | $1,532.30 | ($38.30) |
| 7 | $1,743 | $1,532.30 | $210.70 |
| **10** | **$2,490** | **$1,532.30** | **$957.70** |

**Break-even: 7 units sold.**
**Budget note: $1,532.30 is $32.30 above the $1,500 target budget; secure at least one pre-order before purchasing to maintain margin safety.**
