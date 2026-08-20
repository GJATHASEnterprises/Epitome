# Epitome Penta — Bill of Materials (BOM)

**Target BOM:** ~**$80–95** per unit at 50 units with the updated 3-step centre platform and hybrid enclosure.

> **Design revision:** 3-step tapered centre platform, 160W PSU, captive slot cables, dual INA3221 monitoring, WS2811 lighting, QR-only printed collateral.

---

## Device Size Reference (Largest Models — Cardboard Prototype Guide)

| Device | Model | Key Dimension |
|---|---|---|
| Phone | iPhone 16 Pro Max | 163mm × 77mm |
| Tablet | iPad Pro 13" + case | up to ~20mm thick stack |
| Laptop (Standard) | 15" class | up to 320mm slot width fit |
| Laptop (XL) | 17" class | up to 400mm slot width fit |
| Watch | Apple Watch Ultra 2 / Qi watch | Ø55mm cradle region |

---

## Zone Sizes (Definitive)

| Zone | Location | Internal Size | Notes |
|---|---|---|---|
| Zone 1 — Phone Qi pad | Step 1 base | 160×100mm full-width silicone surface | 20W, landscape phone orientation |
| Zone 2 — Buds/Phone Qi pad | Step 2 middle | 90×65mm dish + 68×48mm inner ridge | 15W |
| Zone 3 — Watch cradle | Step 3 top rear | 100×80mm step with raised cradle | Apple puck + Qi watch coil, 5W shared |
| Zone 4 — Laptop slot | Left slot | 320×25×28 (Std) / 400×25×28 (XL) | Captive USB-C cable, 100W, 220mm |
| Zone 5 — iPad slot | Right slot | 290×25×20 | Captive USB-C cable, 20W, 200mm |

---

## Cardboard Prototype Cut Guide

| Piece | Standard Dimensions |
|---|---|
| Base plate | 530mm × 300mm |
| Left slot outer box | 330mm × 300mm × 28mm |
| Left slot inner cavity | 320mm × 25mm × 28mm |
| Centre Step 1 block | 180mm × 110mm × 15mm |
| Centre Step 2 block | 140mm × 100mm × 15mm |
| Centre Step 3 block | 100mm × 80mm × 15mm |
| Right slot outer box | 300mm × 300mm × 20mm |
| Right slot inner cavity | 290mm × 25mm × 20mm |

---

## Prototype BOM (Breakout Boards — No Custom PCB)

| # | Part | Spec | Qty | Unit Cost (Est.) | Source |
|---|------|------|-----|------------------|--------|
| 1 | ESP32-C3 Mini dev board | ESP32-C3 Mini, USB flashing | 2 | $3–$5 | LCSC / AliExpress |
| 2 | Qi 20W TX coil module | Zone 1 | 1 | $8–$10 | AliExpress |
| 3 | Qi 15W TX coil module | Zone 2 | 1 | $5–$8 | AliExpress |
| 4 | Apple Watch charger module | Zone 3 puck | 1 | $8–$12 | Verified Shenzhen supplier |
| 5 | Qi watch coil 5W module | Zone 3 universal watch support | 1 | $4–$7 | AliExpress |
| 6 | USB-C PD 100W controller board | Zone 4 | 1 | $8–$14 | AliExpress |
| 7 | USB-C PD 20W controller board | Zone 5 | 1 | $5–$8 | LCSC / AliExpress |
| 8 | Captive USB-C cable 220mm | Braided, 100W rated, Zone 4 | 1 | $3–$5 | AliExpress / LCSC |
| 9 | Captive USB-C cable 200mm | Braided, 20W rated, Zone 5 | 1 | $2–$4 | AliExpress / LCSC |
| 10 | Right-angle IEC C13 inlet socket | Panel mount | 1 | $2–$4 | LCSC |
| 11 | Internal AC/DC PSU 160W | 100–240V in, ~20V out | 1 | $14–$18 | LCSC |
| 12 | Reinforcement rib kit ×3 | One set for 3 step risers | 1 set | $2–$4 | Local |
| **Prototype electronics total** | | | | **$93–$177** | |

> **Fuse protection note:** dedicated rear inlet fuse holder removed; overcurrent protection moved to PCB PTC resettable fuse design.

---

## Production BOM (Full JLCPCB PCBA)

### Updated Electronics BOM (50 units target)

| # | Part | Qty | Unit Cost (15 units) | Unit Cost (50 units) |
|---|---|---|---|---|
| 1 | Qi 20W TX Module | 1 | $8 | $6–7 |
| 2 | Qi 15W TX Module | 1 | $7 | $5–6 |
| 3 | Apple Watch Puck | 1 | $10 | $4–6 (MOQ 50 direct) |
| 4 | Qi watch coil 5W | 1 | $6 | $4–5 |
| 5 | USB-C PD Board 100W | 1 | $11 | $8–10 |
| 6 | USB-C PD Board 20W | 1 | $7 | $5–6 |
| 7 | Captive USB-C cable 220mm braided 100W | 1 | $3 | $2–3 |
| 8 | Captive USB-C cable 200mm braided 20W | 1 | $3 | $1.50–2.50 |
| 9 | ESP32-C3 Mini | 1 | $4 | $2–3 |
| 10 | INA3221 ×2 | 2 | $6 | $3–4 |
| 11 | Internal AC/DC PSU 160W | 1 | $14–18 | $8–12 |
| 12 | Right-angle IEC C13 inlet | 1 | $4 | $2.50–3.50 |
| 13 | Reinforcement rib kit ×3 (one per step) | 1 set | $4 | $2–3 |
| 14 | Custom PCB (PCBA) 2-layer | 1 | $14 | $8–12 |
| 15 | Wiring / connectors / strain relief | 1 lot | $6 | $3–5 |
| 16 | WS2811 LED strip | 1 | $4 | $2–3 |
| **Electronics subtotal** |  |  | **~$111–125** | **~$69–84** |

### Updated Enclosure BOM

| # | Part | Qty | Unit Cost (15 units) | Unit Cost (50 units) |
|---|---|---|---|---|
| 17 | 3D printed centre platform | 1 | $18–28 | $10–15 |
| 18 | Laser cut + bent ABS slot walls | 1 set | $8–12 | $5–8 |
| 19 | Vacuum-formed ABS base | 1 | $6–10 | $4–6 |
| 20 | Laser cut + bent aluminium top + risers | 1 set | $8–12 | $6–10 |
| 21 | Rubber feet + M3 fasteners | 1 set | $3 | $1.50–2.50 |
| **Enclosure subtotal** |  |  | **~$43–65** | **~$26–42** |

### Updated Packaging BOM

| # | Part | Qty | Unit Cost |
|---|---|---|---|
| 22 | 1.5m braided IEC C13 cable | 1 | $2.50–3.50 |
| 23 | Rigid kraft box (Standard) | 1 | $3.20–4.50 |
| 24 | Rigid kraft box (XL) | 1 | $4.20–5.60 |
| 25 | Moulded pulp tray | 1 | $1.50–2.50 |
| **Packaging subtotal** |  |  | **~$7–11** |

> **Packaging print reduction:** printed warranty card and quick-start guide removed. Box base and dock base now carry QR codes for `epitome.io/warranty` and `epitome.io/setup`.

---

## Updated Cost Totals

| Quantity | Per-Unit Cost | Notes |
|---|---|---|
| 15 units (Batch 1) | **~$131–161** | Hybrid enclosure: 3D centre + laser slots + vacuum base |
| 50 units (Batch 2) | **~$80–95** | Full production run |

---

## Updated Break-Even Table (Batch 1, Standard @ $249)

| Units Sold | Revenue | Build Investment (midpoint $146) × 15 units = $2,190 | Profit / (Loss) |
|---|---|---|---|
| 1 | $249 | $2,190 | ($1,941) |
| 5 | $1,245 | $2,190 | ($945) |
| 9 | $2,241 | $2,190 | $51 |
| **10** | **$2,490** | **$2,190** | **$300** |
| 15 | $3,735 | $2,190 | $1,545 |

Break-even improves from 13 units to **9 units**.

---

## Approved Suppliers

| Supplier | Use For |
|----------|---------|
| LCSC | ICs, passives, connectors, right-angle C13 inlets |
| JLCPCB | Custom PCB + PCBA assembly |
| Verified Shenzhen suppliers | Apple Watch puck sourcing at MOQ 50 target |
| AliExpress (verified) | Qi/watch coils, captive braided cables, prototype modules |
| Local vacuum-form + laser vendors | ABS base + slot walls + aluminium cuts/bends |
| Certification labs | FCC / CE / UKCA / RCM testing |

---

## Certification Budget Notes

- Required pre-retail certifications by market: **FCC (US), CE (EU), UKCA (UK), RCM (Australia)**
- Typical cost estimate: **$2,000–$8,000 per certification**
- Typical lead time: **8–16 weeks per certification program**
- Plan and reserve this budget in Batch 2+ rollout before retail sales in each region

---

## What NOT to Source From
- Amazon/eBay for critical PD or power-path parts (counterfeit risk)
- Unknown AliExpress stores without verified ratings/history
