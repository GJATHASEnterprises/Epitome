# Epitome — Production Plan (Sept 2026 Canon)

## 1) Product lineup and build materials

- **Step Walnut ($99):** minimalist / wood-desk buyer. Black PETG base shell + wood-PLA top shell, sanded and Danish-oiled. ATtiny85. Single white status LED via 3 mm light pipe.
- **Step Obsidian ($109):** gamer / battlestation buyer. Full CF-PETG shells (carbon-weave matte). ESP32-C3. WS2812B RGB glow lines in recessed side grooves behind flush diffusers, 8–12 LEDs per side, no visible LED dots.
- **Outdoor Block Stone ($119) / Camo ($129):** unchanged architecture from technical readouts (Batch 2 gated).

Authoritative per-model BOMs and QC gates live in `docs/technical-readouts/`.

## 2) Unit economics (customer pays shipping)

| Model | Build cost | Price | Net after fees/processing/defect reserve |
|---|---:|---:|---:|
| Step Walnut | $42.43 | $99 | ~ $36 / sale |
| Step Obsidian | ~$48.50 | $109 | ~ $40–44 / sale |
| Outdoor Block Stone | ~$53.30 | $119 | ~ $34 / sale |
| Outdoor Block Camo | ~$56.80 | $129 | ~ $39 / sale |

Batch 1 build plan: **3 Walnut + 3 Obsidian**, projected profit **~$225–240**.

## 3) Sept-2026 tariffed reference prices (25% Section 301 on China-sourced electronics)

- Qi TX: **$5.63**
- Buds TX: **$2.50**
- Trigger board: **$2.25**
- 65W GaN brick (included with Step): **$13.75**
- Cable (included with Step): **$3.00**
- 20W magnetic TX: **$7.50**
- IP67 USB-C: **$4.00**
- 20,000 mAh certified PD bank: **$22.50**
- Enclosure cost targets: Walnut **$9.50** (wood-PLA + oil), Obsidian **$11.00** ($7.50 + $3.50 CF premium)
- Packaging target: kraft box **$3.00**

## 4) One-time tooling/setup

| Item | Cost |
|---|---:|
| Hardened steel nozzle (CF-PETG) | $15 |
| Heat-set insert tips | $12 |
| USBasp programmer | $10 |
| Thermal epoxy + kapton + flux stock | $15 |
| Camo stencil/paint supplies | $30 |
| Immersion test kit | $15 |
| **Total** | **~$97** |

## 5) Schedule updates

1. **Week 1:** place a **measurement order (~$35)**: one of each electronics module for caliper capture (`docs/design-brief-step.md` §5).
2. **Week 1:** place consolidated parts order after measurement order confirmation (same-week confirmation target):
   - **Immediate Batch 1 purchase (3 Walnut + 3 Obsidian): ~ $430 Step-only**
   - **Optional full 10-unit planning envelope (if buying all modules up front): ~ $740 total**
3. **Before prototype printing:** produce CAD production files (friend sketches + dimensional spec, or Upwork CAD freelancer delivery of STEP/STL).
4. **Week 2–3:** first Step prototype and QC gauntlet.
5. **Week 3–5:** build/ship remaining Step units.
6. **Batch 2 gated:** Outdoor Block only after reserve + safety gates pass.
