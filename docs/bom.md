# Epitome — BOM & Economics Snapshot (Sept 2026)

Canonical detailed BOMs are in `docs/technical-readouts/`.

## Tariffed key part prices (China-sourced electronics, +25%)

| Part | Price |
|---|---:|
| Qi TX module | $5.63 |
| Buds TX module | $2.50 |
| Watch TX coil | $3.50 *(estimate; pending sourcing)* |
| USB-C trigger board | $2.25 |
| 65W GaN brick (Step models) | $13.75 |
| USB-C cable (Step models) | $3.00 |
| 20W magnetic TX (Outdoor Block) | $7.50 |
| IP67 USB-C (Outdoor Block) | $4.00 |
| 20,000 mAh certified PD bank | $22.50 |

## Enclosure + packaging cost targets

| Item | Cost |
|---|---:|
| Walnut enclosure (black PETG base + wood-PLA top + oil) | $9.50 |
| Obsidian enclosure (CF-PETG shells incl. premium) | $11.00 |
| Kraft packaging box set | $3.00 |

## Easy-connect (no-solder) BOM deltas

| Part / change | Added cost |
|---|---:|
| 2× screw-terminal buck converters (pair total over bare modules) | +$1.50–3.00 / finished unit |
| USB-C PD input trigger board (~$3.00) + panel-mount USB-C receptacle (~$2.00) | ~+$0 net change / unit *(replaces prior DC jack / barrel-input hardware at roughly the same total cost)* |
| Pre-wired LED strip (factory JST-SM leads) | +$0.35–1.10 / unit |
| Digispark-style ATtiny85 USB board | +$0.70–2.20 / unit |
| Pre-crimped JST-XH pigtail set | +$0.90–1.40 / unit |
| Pre-crimped NTC | +$0.30 / unit |
| Solder-seal connector allowance | +$0.20 / unit |
| **Total easy-connect delta** | **~$6–12 / unit (plan at ~$8)** |

**Bench simplification to verify:** if the chosen input trigger can negotiate **12V directly** with enough current for the intended load, the dedicated 12V buck for Zone 1 may be removable (**–$2.50, one less module**). Mark this as **verify on bench** before changing the architecture.

## Model economics (net-after-fees)

| Model | Build cost | Price | Net-after-fees |
|---|---:|---:|---:|
| Step Walnut | ~$50.50 | $99 | ~ $28–29/sale |
| Step Obsidian | ~$56.50 | $109 | ~ $32–36/sale |
| Outdoor Block Stone | ~$53.30 | $119 | ~ $34/sale |
| Outdoor Block Camo | ~$56.80 | $129 | ~ $39/sale |

## Batch 1 projection

- Mix: 3 Walnut + 3 Obsidian
- Easy-connect parts add **~$50 total** versus the earlier 6-unit Step plan.
- Projected profit after fees/processing/defect reserve: **~$180–195**
- The watch TX coil estimate is already reflected in the Step build-cost / profit figures above; current sell prices remain unchanged pending final sourcing confirmation.
