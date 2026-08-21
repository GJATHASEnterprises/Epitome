# Epitome Penta — Prototype Guide

---

## Goal of the Prototype

Not a sellable unit — a functional proof of concept to verify:

- ✅ All 5 zones charge correctly
- ✅ Captive cable slot UX works naturally for laptop/tablet
- ✅ Zone 3 dual watch mode (Apple puck + Qi) behaves correctly
- ✅ Standard SKU footprint is desk-friendly
- ✅ Thermal behavior remains stable with PSU under laptop slot cavity and 150W firmware soft cap

Definitive placement coordinates are in [component-positions.md](component-positions.md).

---

## Budget: $500

| Category | Low | High |
|----------|-----|------|
| Electronics (breakout boards + new cable/Qi parts) | $93 | $177 |
| Enclosure (hybrid prototype parts) | $40 | $62 |
| Shipping / process overhead | $15 | $35 |
| Tools (if needed) | $51 | $84 |
| Buffer for mistakes + spares | $50 | $80 |
| **Total** | **~$249** | **~$438** |

> Electronics high-end estimate reflects wide vendor spread for PSU, watch modules, and early-batch shipping-loaded breakout sourcing.

---

## Tools Needed

Soldering iron, multimeter, wire strippers, hot glue gun, cutters, helping hands.

---

## Prototype BOM (AliExpress + LCSC)

Use [bom.md](bom.md) as the source-of-truth list and pricing.

Additions for this revision:
- Captive braided USB-C cable **220mm** (100W)
- Captive braided USB-C cable 200mm (20W)
- Qi watch coil 5W for Zone 3
- Right-angle IEC C13 inlet
- Step-riser reinforcement insert/rib material (3 risers)
- Dual INA3221 monitor layout (INA219 removed)

---

## 4-Week Build Plan

### Week 1 — Order Everything
- Order all electronics and mechanical parts
- Order Standard enclosure parts with hybrid method (3D centre + laser slots + vacuum base)

### Week 2 — Cardboard Mock

**Goal:** Validate ergonomics and slot clearances before fabrication.

Standard mock dimensions:
- Base: **530×300mm**
- Laptop slot: **320×25×28mm opening**
- Tablet slot: **290×25×20mm opening**
- Step 1: **180×110×15mm**
- Step 2: **140×100×15mm**
- Step 3: **100×80×15mm**

Placement checks:
- Step 1 full-width 160×100 phone surface (20W)
- Step 2 buds pad centred (90×65, 15W)
- Watch cradle at rear of Step 3
- 5mm stop shelf + cable clip in each slot

### Week 3 — Electronics Bench Test

- [ ] Verify Zone 1 at 20W
- [ ] Verify Zone 2 at 15W
- [ ] Verify Zone 3 puck mode charges Apple Watch
- [ ] Verify Zone 3 Qi mode charges supported non-Apple watch
- [ ] Verify only one Zone 3 path is active at a time
- [ ] Verify Zone 4 captive cable delivers up to 100W (220mm lead)
- [ ] Verify Zone 5 captive cable delivers up to 20W
- [ ] Validate full-load envelope at 155W total and firmware soft cap at 150W

### Week 4 — Full Assembly

- [ ] Mount PSU under laptop slot cavity
- [ ] Install right-angle C13 inlet
- [ ] Populate PCB PTC resettable fuse protection
- [ ] Install slot stop shelves + silicone clips
- [ ] Confirm captive cable pull/retract usability
- [ ] Confirm thermal stability under simultaneous high-load test

---

## Full Assembly Checklist (Quick Reference)

- [ ] PSU wired and outputting ~20V
- [ ] Zone 1 Qi charging at 20W
- [ ] Zone 2 Qi charging at 15W
- [ ] Zone 3 puck + Qi watch modes validated
- [ ] Zone 4 captive cable charging laptop
- [ ] Zone 5 captive cable charging tablet/phone
- [ ] ESP32 telemetry + app BLE functional

---

## Budget Breakdown

Use [bom.md](bom.md) cost tables as the latest baseline.
