# Step Obsidian — Technical Readout

## Enclosure specification
- Same stepped geometry as Walnut.
- **Both shells:** CF-PETG (carbon-weave matte).
- Side RGB grooves with flush diffuser bars (glow lines only, no visible LED dots).
- WS2812B count target: **8–12 LEDs per side**.
- Hardened steel nozzle required for CF-PETG.

## Electronics BOM (Sept 2026, tariffed where applicable)
| Item | Unit cost |
|---|---:|
| 15–20W Qi TX module (China, +25%) | $5.63 |
| 5W buds TX module (China, +25%) | $2.50 |
| USB-C trigger/boost board (China, +25%) | $2.25 |
| 65W GaN brick (China, +25%) | $13.75 |
| USB-C cable, 1 m (China, +25%) | $3.00 |
| ESP32-C3 + RGB support circuitry + harness | $4.30 |
| WS2812B strips + diffuser bars | $2.00 |
| CF-PETG enclosure + inserts/feet | $11.07 |
| Packaging (kraft box + insert) | $3.00 |
| **Build cost** | **~$48.50** |

## Firmware behavior (ESP32-C3)
- RGB modes: static, breathing, charge-progress sweep, OFF.
- Mode persistence across power cycles.
- RGB brightness capped when both charging coils are at full load.
- Thermal cutoff behavior retained.

## Unit economics
- Price: $109
- Customer-paid shipping target: ~$10.50 label
- Net per sale after fees/processing/defect reserve: **~$40–44**
