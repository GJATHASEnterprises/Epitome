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
| USB-C trigger/boost board (China, +25%) | $2.25 |
| 65W GaN brick (China, +25%) | $13.75 |
| USB-C cable, 1 m (China, +25%) | $3.00 |
| ATtiny85 + status LED + thermals/harness | $2.80 |
| Enclosure + inserts/feet + oil finish | $9.50 |
| Packaging (kraft box + insert) | $3.00 |
| **Build cost** | **$42.43** |

## Firmware behavior (ATtiny85)
- Idle: soft breathing white status LED.
- Charging: solid white status LED.
- Thermal fault: fast-blink white + cutoff behavior.

## Unit economics
- Price: $99
- Customer-paid shipping target: ~$10.50 label
- Net per sale after fees/processing/defect reserve: **~$36**
