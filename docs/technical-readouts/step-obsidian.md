# Step Obsidian — Technical Readout

## Enclosure specification
- Same stepped geometry as Walnut.
- **Both shells:** CF-PETG (carbon-weave matte).
- Side RGB grooves with flush diffuser bars (glow lines only, no visible LED dots).
- WS2812B count target: **8 LEDs per side (16 total)** on 60 LED/m strip.
- Hardened steel nozzle required for CF-PETG.

## Electronics BOM (Sept 2026 planning estimates; tariffed where applicable)
| Item | Unit cost |
|---|---:|
| Zone 1 Qi2 magnetic TX module (China, +25%) | $5.63 |
| Zone 2 Qi TX module up-to-15W (same SKU class, China, +25%) | $5.63 |
| Watch TX coil (generic estimate, pending sourcing) | $3.50 |
| USB-C output trigger board (15W class, China, +25%) | $1.50 |
| 65W GaN brick target (China, +25%) | $9.50 |
| USB-C cables (1 input + 1 output) | $3.00 |
| Digispark-style ATtiny85 USB board + RGB/easy-connect harnessing | $9.80 |
| WS2812B strips + diffuser bars | $2.00 |
| CF-PETG enclosure + inserts/feet | $11.07 |
| Packaging (kraft box + insert) | $3.00 |
| **Build cost** | **~$54.63** |

## Firmware behavior (Digispark ATtiny85)
- RGB modes: rear-button colour cycling across documented preset colours plus OFF.
- RGB brightness is trimmed when wireless load is fully active.
- Soft cap behavior: when all zones are active, Zone 2 shifts to low-power profile.
- Thermal cutoff behavior retained through the Qi module / hardwired thermal chain.

## Unit economics
- Price: $109
- Customer-paid shipping target: ~$10.50 label
- Net per sale after fees/processing/defect reserve: **~$34–38**

## Compatibility wording constraints
- Zone 1 wording: "Qi2 magnetic charging — compatible with MagSafe-case iPhones and Qi2 Android phones."
- Zone 3 generic watch coil does **not** support Apple Watch unless an MFi-certified module is used.
