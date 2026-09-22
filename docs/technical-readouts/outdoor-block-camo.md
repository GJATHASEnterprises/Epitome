# Outdoor Block Camo — Technical Readout

## Enclosure specification
- Sealed ASA body targeting IP67 ingress performance.
- Finish stack: OD-green ASA base, masked spray camo pattern, UV matte clear coat.
- Gasket: 2 mm TPU printed gasket in perimeter groove.
- Closure hardware: M3 stainless screws ×8, cross-pattern torque sequence.
- Porting: membrane pressure vent and IP67 panel-mount USB-C with tethered TPU cap.

## Electronics BOM (Sept 2026 planning estimates, tariffed where applicable)
| Item | Unit cost |
|---|---:|
| Certified 20,000 mAh (74 Wh) PD battery module (China, +25% tariff) | $22.50 |
| 20W magnetic phone TX module (China, +25% tariff) | $7.50 |
| 5–10W buds TX module (China, +25% tariff) | $2.50 |
| USB-C PD output path (20W) + interlock control hardware | $4.50 |
| NTC on cell + NTC on phone coil + fused harness | $2.80 |
| IP67 panel-mount USB-C + tethered cap (China, +25% tariff) | $4.00 |
| Membrane vent | $1.00 |
| ASA + TPU enclosure materials and hardware | $8.00 |
| Camo finish process adder | $3.50 |
| Packaging and consumables | $0.50 |
| **Build cost** | **$56.80** |

## Firmware behavior
- Interlock: USB-C insertion disables buds charging zone within 1 second.
- Interlock restore: buds zone re-enabled on USB-C removal.
- Battery protection: if bank <10%, all zones disabled.
- LED behavior: fuel-gauge blink patterns plus low-battery cutoff indication.

## Power budget
- Battery system: 74 Wh certified module.
- Phone zone: up to 20W magnetic TX.
- Buds zone: 5–10W.
- USB-C PD output: **20W**.

## Compliance + launch gating
- Batch launch is gated by `docs/launch-plan.md` Phase 4.
- Compliance floor target: **~$1,500–3,000** when using FCC-ID'd TX modules and verified UN38.3/UL battery component docs.
- Full UL 2056 end-product listing (~$15,000–30,000) is a later distribution milestone, not required for legal direct sales.
- Hard sourcing requirement: verify module FCC IDs and battery UN38.3/UL docs before ordering production lots.

## Shipping constraints
- Ground-only shipping.
- UN3481 labeling.
- Battery installed in equipment.
- ≤100Wh per unit (74Wh module qualifies).

## QC checklist
- [ ] All Step-model QC gates (charge compatibility, thermal soak, cutoff simulation, no-brownout, cosmetic, shake).
- [ ] USB-C interlock disable/restore timing validation.
- [ ] 30-minute immersion at 30 cm with desiccant telltale pass.
- [ ] 1 m drop test, 6 faces, post-test full functionality.
- [ ] Measured runtime ≥2.5 full phone charges.
- [ ] 25-cycle battery validation.
- [ ] Wording compliance: use “IP67 — submersion-safe in shallow water”; avoid unqualified “waterproof”.

## Unit economics
- Build cost: ~$56.80.
- Customer-paid shipping required (ground service for Li-ion).
- Net per sale at $129: approximately $39.
