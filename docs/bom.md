# Epitome — BOM & Economics Snapshot (Sept 2026 planning estimates)

Canonical detailed BOMs are in `docs/technical-readouts/`.

## Tariffed key part prices (China-sourced electronics, +25%)

| Part | Price |
|---|---:|
| Qi2 / Qi TX module (used for Zone 1 and Zone 2 on Step) | $5.63 |
| Watch TX coil (generic) | $3.50 *(estimate; pending sourcing)* |
| USB-C trigger board (Step output, 15W class) | $1.50 |
| 65W GaN brick (Step models, budget source target) | $9.50 |
| 65W GaN brick fallback price (if cert docs fail review) | $13.75 |
| USB-C cable (Step models, two cables total) | $3.00 |
| 20W magnetic TX (Outdoor Block) | $7.50 |
| IP67 USB-C (Outdoor Block) | $4.00 |
| 20,000 mAh certified PD bank | $22.50 |

## Enclosure + packaging cost targets

| Item | Cost |
|---|---:|
| Walnut enclosure (black PETG base + wood-PLA top + oil) | $9.50 |
| Obsidian enclosure (CF-PETG shells incl. premium) | $11.07 |
| Kraft packaging box set | $3.00 |

## Hard sourcing rules

- All wireless TX modules must have verifiable module-level FCC IDs.
- Outdoor Block battery modules must have verifiable UN38.3 and UL component documentation.

## Model economics (net-after-fees)

| Model | Build cost | Price | Net-after-fees |
|---|---:|---:|---:|
| Step Walnut | ~$48.63 | $99 | ~ $30–32/sale |
| Step Obsidian | ~$54.63 | $109 | ~ $34–38/sale |
| Outdoor Block Stone | ~$53.30 | $119 | ~ $34/sale |
| Outdoor Block Camo | ~$56.80 | $129 | ~ $39/sale |

## Watch-zone compatibility note

The generic ~$3.50 watch coil does **not** support Apple Watch (Apple uses a proprietary protocol). Open decision:
1. Add MFi module (+$8–11),
2. Keep generic coil and clearly state "not compatible with Apple Watch", or
3. Drop Zone 3 on Step.

Do not show Apple Watch in Step watch-zone marketing unless option 1 is selected.
