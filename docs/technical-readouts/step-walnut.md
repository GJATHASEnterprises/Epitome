# Step Walnut — Technical Readout

## Enclosure specification
- Two-shell stepped enclosure.
- **Base shell:** black PETG.
- **Top shell:** wood-PLA, sanded and Danish-oiled.
- Single white status LED via 3 mm light pipe.
- Wall thickness 2.4 mm; coil window ≤1.5 mm; M3 heat-set inserts ×4.

## Electronics BOM (Sept 2026 planning estimates; tariffed where applicable)
| Item | Unit cost |
|---|---:|
| Zone 1 Qi2 magnetic TX module (China, +25%) | $5.63 |
| Zone 2 Qi TX module up-to-15W (same SKU class, China, +25%) | $5.63 |
| Watch TX coil (generic estimate, pending sourcing) | $3.50 |
| USB-C output trigger board (15W class, China, +25%) | $1.50 |
| 65W GaN brick target (China, +25%) | $9.50 |
| USB-C cables (1 input + 1 output) | $3.00 |
| Digispark-style ATtiny85 USB board + easy-connect harnessing | $7.37 |
| Enclosure + inserts/feet + oil finish | $9.50 |
| Packaging (kraft box + insert) | $3.00 |
| **Build cost** | **~$48.63** |

## Firmware behavior (Digispark ATtiny85)
- Default: steady warm-white status LED during non-night hours.
- Zone detect pulse: brief brightness pulse on newly detected device presence.
- Night mode: timer-based overnight LED-off window (approximate, no RTC alignment).
- Soft cap behavior: when all zones are active, Zone 2 shifts to low-power profile.

## Unit economics
- Price: $99
- Customer-paid shipping target: ~$10.50 label
- Net per sale after fees/processing/defect reserve: **~$30–32**

## Compatibility wording constraints
- Zone 1 wording: "Qi2 magnetic charging — compatible with MagSafe-case iPhones and Qi2 Android phones."
- Zone 3 generic watch coil does **not** support Apple Watch unless an MFi-certified module is used.
