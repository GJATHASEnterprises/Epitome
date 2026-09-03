# Step Obsidian — Technical Readout

## Enclosure specification
- Same two-tier stepped geometry as Step Walnut.
- Material: CF-filled PETG for matte carbon-weave visual texture.
- Side RGB light channels recessed with diffuser bars (clear TPU/acrylic) to eliminate visible LED dotting.
- Requires hardened steel nozzle for abrasive filament (one-time tooling: $15).
- Core print settings: 0.2 mm layers, structural walls increased near inserts, 15% gyroid infill baseline.

## Electronics BOM (Sept 2026, tariffed where applicable)
| Item | Unit cost |
|---|---:|
| 15–20W Qi TX module (pre-certified, China, +25% tariff) | $5.63 |
| 5W buds TX module (China, +25% tariff) | $2.50 |
| USB-C trigger/boost board (China, +25% tariff) | $2.25 |
| ESP32-C3 MCU + RGB support circuitry (incl. level shifter) | $4.30 |
| WS2812B side-light system + diffusers | $2.00 |
| NTC thermistor + polyfuse + harness | $2.00 |
| 65W GaN brick (China, +25% tariff) | $13.75 |
| Braided USB-C cable, 1 m (China, +25% tariff) | $3.00 |
| CF-PETG enclosure + inserts/screws/feet + consumables/power | $10.07 |
| Packaging (kraft box + black label + insert card) | $3.00 |
| **Build cost** | **$48.50** |

## Firmware behavior (ESP32-C3)
- Charging status integrated with RGB controller.
- RGB modes: static color, breathing, charge-progress sweep, OFF.
- Last RGB mode persistence across power cycles.
- Thermal fault indication and protective cutoff logic maintained.
- Brightness cap logic active while both charging zones are at full load.

## Power budget
- Input adapter: 65W USB-C GaN brick.
- Phone zone: 15–20W.
- Buds zone: 5W.
- RGB worst case: ~3.6W.
- Firmware-limited RGB output when both charging zones peak to preserve power/thermal margin.

## Assembly order
1. Print CF-PETG parts (hardened nozzle) and prep diffuser components.
2. Install inserts and both TX modules.
3. Install NTC and route fused harness.
4. Install ESP32-C3 control board, level shifter, and RGB strip segments.
5. Validate RGB channels, mode control, and persistence behavior.
6. Validate charging behavior and thermal fault signaling.
7. Close enclosure and complete packaging with brick + cable.

## QC checklist
- [ ] All Step Walnut electrical/thermal/cosmetic/shake QC gates.
- [ ] RGB all-modes test (static, breathing, sweep, OFF).
- [ ] RGB-off persistence verified after power cycle.

## Unit economics
- Build cost: ~$48.50.
- Customer-paid shipping label target: $10.50.
- Seller-side overhead: Etsy + processing + defect reserve.
- Net per sale at $109: approximately $40–44.
