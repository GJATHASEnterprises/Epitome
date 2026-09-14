# Step Obsidian — Technical Readout

## Enclosure specification
- Same stepped geometry as Walnut.
- **Both shells:** CF-PETG (carbon-weave matte).
- Side RGB grooves with flush diffuser bars (glow lines only, no visible LED dots).
- WS2812B count target: **8 LEDs per side (16 total)** on 60 LED/m strip.
- Hardened steel nozzle required for CF-PETG.

## Electronics BOM (Sept 2026, tariffed where applicable)
| Item | Unit cost |
|---|---:|
| 15–20W Qi TX module (China, +25%) | $5.63 |
| 5W buds TX module (China, +25%) | $2.50 |
| Watch TX coil (estimate, pending sourcing) | $3.50 |
| USB-C trigger/boost board (China, +25%) | $2.25 |
| 65W GaN brick (China, +25%) | $13.75 |
| USB-C cable, 1 m (China, +25%) | $3.00 |
| Digispark-style ATtiny85 USB board + RGB/easy-connect harnessing | $9.80 |
| WS2812B strips + diffuser bars | $2.00 |
| CF-PETG enclosure + inserts/feet | $11.07 |
| Packaging (kraft box + insert) | $3.00 |
| **Build cost** | **~$56.50** |

## Firmware behavior (Digispark ATtiny85)
- RGB modes: rear-button colour cycling across the documented preset colours plus OFF.
- RGB brightness is soft-capped when estimated load approaches the 60W ATtiny85 limit.
- Thermal cutoff behavior retained through the Qi module / hardwired thermal chain.

## Unit economics
- Price: $109
- Customer-paid shipping target: ~$10.50 label
- Net per sale after fees/processing/defect reserve: **~$32–36**
