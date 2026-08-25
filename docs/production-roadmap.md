# Penta Dock — Production Roadmap

## Batch 1 — Standard SKU Pilot, 10 Units

**Goal:** Launch, validate demand, prove the 5-zone UVP, and build 10 units with the revised enclosure inside the $1,500 budget.

## Budget Summary

- **Total batch cost:** $1,416.20
- **Budget:** $1,500
- **Safety net without any pre-order:** $83.80
- **Revenue (10 units × $249):** $2,490
- **Profit at full batch (10 units):** $1,073.80

## Pricing

- **$249 flat**
- No discounts
- Shipping calculated at checkout — charge actual shipping via Shopify/Pirateship

## Per-Unit Economics

| Item | Cost |
|---|---:|
| Build cost (electronics + enclosure + packaging) | $120.91 |
| Stripe fees (2.9% + $0.30 on $249) | $7.52 |
| Defect buffer (10% of build cost) | $12.09 |
| Domain epitomecharge.com ÷10 | $1.10 |
| **Total per unit** | **$141.62** |

## Break-Even

| Units Sold | Revenue | Total Cost | Profit/(Loss) |
|---|---:|---:|---:|
| 5 | $1,245 | $1,416 | ($171) |
| **6** | **$1,494** | **$1,416** | **$78** ← break-even |
| 7 | $1,743 | $1,416 | $327 |
| 10 | $2,490 | $1,416 | **$1,074** |

**Break-even: 6 units. Margin at full batch: 43%.**

## Pre-order Strategy

Collect at least **1 pre-order at $249** before ordering any parts. Total batch cost is $1,416.20 — one pre-order covers most of the safety net requirement.

## Build Sequence

1. Collect at least 1 pre-order
2. Place single combined AliExpress order (Qi2 module, Qi module, PD boards, Apple Watch puck, Qi watch coil, WS2811, IEC inlet, buck converters)
3. Place LCSC order (Mean Well LRS-200-24 PSU ×10)
4. Place Amazon order (ATtiny85, captive cables, hardware relay, fuses/TVS, thermistors, wiring/JST, Bumpons, power button, strain relief boots)
5. Order packaging from Amazon + Moo.com (magnetic box, foam, braided IEC cable, setup cards, belly band)
6. Order ABS sheet from Inventables
7. Confirm school printer access + buy 1 spool ABS filament
8. Get Pumping Station One membership ($50)
9. Print centre platforms at school (6–8 hrs each, run in parallel if possible)
10. Laser cut all panels at Pumping Station One
11. Finish 3D printed parts (sand → acetone → prime → paint → clear coat)
12. Apply microfibre lining to slot inner walls
13. Assemble units (45–60 min each)
14. Fit strain relief boots at cable exit points
15. QC each unit (power on, test all 5 zones, check all LEDs, visual inspection)
16. Pack and ship as orders come in

## Key Milestones

| Milestone | When |
|---|---|
| 1 pre-order collected | Before any spending |
| Parts ordered | After pre-order |
| School printer access confirmed | Week 1 |
| Pumping Station One membership | Week 1 |
| All parts received | Week 2–3 |
| All prints complete | Week 3–4 |
| All laser cutting complete | Week 3–4 |
| All units assembled + QC'd | Week 4–5 |
| All units shipped | Week 5–6 |

## App / Firmware (Shelved — Batch 2+ Consideration)

Companion app with BLE zone monitoring, per-zone power data, night mode scheduling, and theft alerts is NOT part of Batch 1. ATtiny85 handles all Batch 1 LED logic. App development is preserved as a Batch 2+ consideration. See [app-spec.md](app-spec.md) for future reference.

## Batch 2 Trigger

After all 10 units are sold and customer feedback is collected. Do not start Batch 2 planning until Batch 1 is fully sold through. Estimated Batch 2 cost: ~$95–105/unit at 20–25 units.
