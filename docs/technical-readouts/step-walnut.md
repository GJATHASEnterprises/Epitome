# Step Walnut — Technical Readout

## Enclosure specification
- Two-shell stepped enclosure.
- **Base shell:** black PETG.
- **Top shell:** wood-PLA, sanded and Danish-oiled.
- Single white status LED via 3 mm light pipe.
- Wall thickness 2.4 mm; coil window ≤1.5 mm; M3 heat-set inserts ×4.

## Electronics BOM (Sept 2026, tariffed where applicable)
| Item | Unit cost |
|---|---:|
| 15–20W Qi TX module (China, +25%) | $5.63 |
| 5W buds TX module (China, +25%) | $2.50 |
| Watch TX coil (estimate, pending sourcing) | $3.50 |
| USB-C trigger/boost board (China, +25%) | $2.25 |
| 65W GaN brick (China, +25%) | $13.75 |
| USB-C cable, 1 m (China, +25%) | $3.00 |
| Digispark-style ATtiny85 USB board + easy-connect harnessing | $7.37 |
| Enclosure + inserts/feet + oil finish | $9.50 |
| Packaging (kraft box + insert) | $3.00 |
| **Build cost** | **~$50.50** |

## Firmware behavior (Digispark ATtiny85)
- Default: steady warm-white status LED during non-night hours.
- Zone detect pulse: brief brightness pulse on newly detected device presence.
- Night mode: timer-based overnight LED-off window (approximate, no RTC alignment).

## Unit economics
- Price: $99
- Customer-paid shipping target: ~$10.50 label
- Net per sale after fees/processing/defect reserve: **~$28–29**
