# Epitome Penta — Bill of Materials (BOM)

**Target BOM:** ~$92–$99 per unit at 50 units with full universal 5-zone spec

> **Design revision:** Captive slot cables, universal watch charging on Zone 3, two SKU widths (Standard + XL).

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
| Zone 1 — Phone Qi pad | Step 1 centre | 90×65mm dish | 15W |
| Zone 2 — Buds/Phone Qi pad | Step 2 front | 90×65mm dish + 68×48 inner ridge | 15W |
| Zone 3 — Watch cradle | Step 2 rear | Ø55mm pod | Apple puck + Qi watch coil, 5W shared |
| Zone 4 — Laptop slot | Left slot | 320×25×28 (Std) / 400×25×28 (XL) | Captive USB-C cable, 100W |
| Zone 5 — iPad slot | Right slot | 290×25×20 | Captive USB-C cable, 20W |

---

## Cardboard Prototype Cut Guide

| Piece | Standard Dimensions |
|---|---|
| Base plate | 530mm × 300mm |
| Left slot outer box | 330mm × 300mm × 28mm |
| Left slot inner cavity | 320mm × 25mm × 28mm |
| Centre Step 1 block | 200mm × 300mm × 40mm |
| Centre Step 2 block | 200mm × 200mm × 40mm |
| Right slot outer box | 300mm × 300mm × 20mm |
| Right slot inner cavity | 290mm × 25mm × 20mm |

---

## Prototype BOM (Breakout Boards — No Custom PCB)

| # | Part | Spec | Qty | Unit Cost (Est.) | Source |
|---|------|------|-----|------------------|--------|
| 1 | ESP32-C3 Mini dev board | ESP32-C3 Mini, USB flashing | 2 | $3–$5 | LCSC / AliExpress |
| 2 | Qi 15W TX coil module | Zone 1 | 1 | $5–$8 | AliExpress |
| 3 | Qi 15W TX coil module | Zone 2 | 1 | $5–$8 | AliExpress |
| 4 | Apple Watch charger module | Zone 3 puck | 1 | $8–$12 | AliExpress |
| 5 | Qi watch coil 5W module | Zone 3 universal watch support | 1 | $4–$7 | AliExpress |
| 6 | USB-C PD 100W controller board | Zone 4 | 1 | $8–$14 | AliExpress |
| 7 | USB-C PD 20W controller board | Zone 5 | 1 | $5–$8 | LCSC / AliExpress |
| 8 | Captive USB-C cable 300mm | Braided, 100W rated, Zone 4 | 1 | $3–$5 | AliExpress / LCSC |
| 9 | Captive USB-C cable 200mm | Braided, 20W rated, Zone 5 | 1 | $2–$4 | AliExpress / LCSC |
| 10 | Right-angle IEC C13 inlet socket | Panel mount | 1 | $2–$4 | LCSC |
| 11 | Reinforcement insert/rib material | Step riser support | 1 set | $1–$3 | Local |
| 12 | 180W AC/DC PSU module | 100–240V in, 20V out | 1 | $15–$22 | LCSC |
| **Prototype electronics total** | | | | **$95–$165** | |

---

## Production BOM (Full JLCPCB PCBA)

### Electronics & Internals

| # | Part | Spec | Qty | Unit Cost (15 units) | Unit Cost (50 units) |
|---|------|------|-----|---------------------|---------------------|
| 1 | Qi 15W TX Module | Zone 1 phone pad | 1 | $7 | $5–$6 |
| 2 | Qi 15W TX Module | Zone 2 buds/phone pad | 1 | $7 | $5–$6 |
| 3 | Apple Watch Puck | Zone 3 | 1 | $10 | $4–$6 |
| 4 | Qi watch coil 5W | Zone 3 universal watch support | 1 | $6 | $4–$5 |
| 5 | USB-C PD Board 100W | Zone 4 | 1 | $11 | $8–$10 |
| 6 | USB-C PD Board 20W | Zone 5 | 1 | $7 | $5–$6 |
| 7 | Captive USB-C cable 300mm, braided | 100W rated | 1 | $4 | $2–$3 |
| 8 | Captive USB-C cable 200mm, braided | 20W rated | 1 | $3 | $1.5–$2.5 |
| 9 | ESP32-C3 Mini | MCU | 1 | $4 | $2–$3 |
| 10 | INA3221 + INA219x2 + BH1750 | Monitoring + ambient | 1 lot | $8 | $4–$6 |
| 11 | Internal AC/DC PSU | 180W, 20V out | 1 | $20 | $10–$15 |
| 12 | Right-angle IEC C13 inlet | Panel mount + fuse | 1 | $4 | $2.5–$3.5 |
| 13 | Reinforcement insert / rib kit | Step riser anti-crack support | 1 set | $3 | $1.5–$2.5 |
| 14 | Custom PCB (PCBA) | 2-layer, JLCPCB | 1 | $14 | $8–$12 |
| 15 | Wiring / connectors / strain relief | Includes cable clips | 1 lot | $6 | $3–$5 |
| **Electronics subtotal** | | | | **~$114** | **~$76–$88** |

### Enclosure

| # | Part | Spec | Qty | Unit Cost (15 units) | Unit Cost (50 units) |
|---|------|------|-----|---------------------|---------------------|
| 16 | 3D Printed Shell (Batch 1) | Standard SKU geometry | 1 | $45–$65 | — |
| 17 | Aluminum Top Plate + Step Faces | 1.5mm sheet | 1 | — | $10–$15 |
| 18 | ABS Base + Slot Walls | Batch 2+ | 1 | — | $15–$22 |
| 19 | Rubber Feet + M3 Fasteners | Serviceable base | 1 set | $3 | $1.5–$2.5 |
| **Enclosure subtotal** | | | | **~$48–$68** | **~$27–$40** |

### Packaging & In-Box Contents

| # | Item | Spec | Qty | Unit Cost |
|---|------|------|-----|-----------|
| 20 | 1.5m braided IEC C13 cable | Right-angle C13 end | 1 | $2.50–$3.50 |
| 21 | Rigid kraft box (Standard) | **~580×340×100mm** | 1 | $3.20–$4.50 |
| 22 | Rigid kraft box (XL) | **~750×340×100mm** | 1 | $4.20–$5.60 |
| 23 | Die-cut foam insert | Dock + cable | 1 | $3–$4 |
| 24 | Warranty card | 12-month summary + QR | 1 | $0.25 |
| 25 | Quick-start guide | Includes captive-cable instructions | 1 | $0.15 |
| **Packaging subtotal** | | | | **~$9–$14** |

---

## Cost Totals by Volume

| Quantity | Enclosure Method | Per-Unit Cost | Notes |
|----------|-----------------|---------------|-------|
| **13–15 units (Batch 1, Standard)** | 3D printed ABS shell | **~$145–$170** | Includes new universal watch + captive cable parts |
| 20–50 units | Laser cut + bent enclosure | ~$102–$118 | Pre-tooling scale step |
| **50 units (Batch 2)** | Molded/laser hybrid | **~$92–$99** | Includes full in-box bundle |

---

## Batch 1 Budget (13–15 Units)

| Item | Cost (13 units) | Cost (15 units) |
|------|----------------|----------------|
| Electronics × units | ~$1,480 | ~$1,710 |
| Enclosure × units | ~$585–$845 | ~$675–$975 |
| Packaging × units | ~$120–$180 | ~$140–$205 |
| Certification reserve planning | ~$8,000–$20,000* | ~$8,000–$20,000* |
| **Total build-only (excl certs)** | **~$2,185–$2,735** | **~$2,525–$2,890** |

\*Certification is often amortized over larger runs, but reserve line is included for planning visibility.

### Batch 1 Revenue & Profit (launch pricing)

| Units Sold | Revenue (Standard @ $249) | Build Investment (midpoint $2,450) | Profit / (Loss) |
|------------|---------------------------|------------------------------------|-----------------|
| 1 | $249 | $2,450 | ($2,201) |
| 5 | $1,245 | $2,450 | ($1,205) |
| 10 | $2,490 | $2,450 | $40 |
| **13** | **$3,237** | **$2,450** | **$787** |
| 15 | $3,735 | $2,450 | $1,285 |

---

## Approved Suppliers

| Supplier | Use For |
|----------|---------|
| LCSC | ICs, passives, connectors, right-angle C13 inlets |
| JLCPCB | Custom PCB + PCBA assembly + Batch 1 prototype enclosure |
| AliExpress (verified) | Qi/watch coils, captive braided cables, prototype modules |
| Local laser cutter | Aluminum surfaces + ABS base at volume |
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
