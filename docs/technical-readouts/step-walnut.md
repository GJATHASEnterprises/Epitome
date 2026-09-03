# Step Walnut — Technical Readout

## Enclosure specification
- Two-tier stepped enclosure for phone zone + buds zone.
- Material: wood-PLA, ~180 g per unit.
- Finish: sanding plus Danish oil.
- Wall thickness: 2.4 mm.
- Coil window thickness: ≤1.5 mm.
- Fastening: M3 heat-set inserts ×4.
- Print settings: 0.2 mm layer height, 4 walls near inserts, 15% gyroid infill.

## Electronics BOM (Sept 2026, tariffed where applicable)
| Item | Unit cost |
|---|---:|
| 15–20W Qi TX module (pre-certified, China, +25% tariff) | $5.63 |
| 5W buds TX module (China, +25% tariff) | $2.50 |
| USB-C trigger/boost board (China, +25% tariff) | $2.25 |
| ATtiny85 MCU + white status LED + 3 mm light pipe | $2.80 |
| NTC thermistor (phone coil) + polyfuse + harness | $2.00 |
| 65W GaN brick (China, +25% tariff) | $13.75 |
| Braided USB-C cable, 1 m (China, +25% tariff) | $3.00 |
| Enclosure + inserts/screws/feet + consumables/power | $7.50 |
| Packaging (kraft box + black label + insert card) | $3.00 |
| **Build cost** | **$42.43** |

## Firmware behavior (ATtiny85)
- Idle: breathing white LED.
- Charging: solid white LED.
- Thermal fault: fast-blink white LED.
- Thermal control: cutoff behavior tuned to keep measured external surface under 45°C target.

## Power budget
- Input adapter: 65W USB-C GaN brick.
- Phone zone: 15–20W.
- Buds zone: 5W.
- Control + LED + losses: remaining budget margin under adapter rating.

## Assembly order
1. Print shell components and post-finish surfaces.
2. Install M3 heat-set inserts.
3. Install phone TX and buds TX modules in coil pockets.
4. Bond NTC to phone-coil backside; route harness with polyfuse.
5. Wire USB-C trigger/boost to both TX zones and control logic.
6. Flash ATtiny85 and verify indicator state transitions.
7. Install light pipe and strain-relief points.
8. Close enclosure, torque fasteners, apply feet, package with brick + cable.

## QC checklist
- [ ] 3-device charge compatibility test (phone + buds).
- [ ] 1-hour thermal soak: measured surface <45°C.
- [ ] Thermal cutoff simulation and recovery.
- [ ] Dual-zone charge on 65W brick with no brownout.
- [ ] Cosmetic inspection under raking light.
- [ ] Packaged shake test.

## Unit economics
- Build cost: $42.43.
- Customer-paid shipping label target: $10.50.
- Seller-side overhead: Etsy ~10% + processing + 10% defect buffer.
- Net per sale at $99: approximately $36.
