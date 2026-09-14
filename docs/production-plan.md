# Epitome — Production Plan (Sept 2026 Canon)

## 1) Product lineup and build materials

- **Step Walnut ($99):** minimalist / wood-desk buyer. Black PETG base shell + wood-PLA top shell, sanded and Danish-oiled. Digispark-style ATtiny85 USB board. Single white status LED via 3 mm light pipe.
- **Step Obsidian ($109):** gamer / battlestation buyer. Full CF-PETG shells (carbon-weave matte). Digispark-style ATtiny85 USB board. WS2812B RGB glow lines in recessed side grooves behind flush diffusers, 8 LEDs per side (16 total), no visible LED dots.
- **Outdoor Block Stone ($119) / Camo ($129):** unchanged architecture from technical readouts (Batch 2 gated).

Authoritative per-model BOMs and QC gates live in `docs/technical-readouts/`.

## 2) Unit economics (customer pays shipping)

| Model | Build cost | Price | Net after fees/processing/defect reserve |
|---|---:|---:|---:|
| Step Walnut | ~$50.50 | $99 | ~ $28–29 / sale |
| Step Obsidian | ~$56.50 | $109 | ~ $32–36 / sale |
| Outdoor Block Stone | ~$53.30 | $119 | ~ $34 / sale |
| Outdoor Block Camo | ~$56.80 | $129 | ~ $39 / sale |

Batch 1 build plan: **3 Walnut + 3 Obsidian**, projected profit **~$180–195**.
That profit is not expected to recoup the one-time **$150–250 CAD spend** during Batch 1; the CAD spend is treated as validation/tooling cost.

## 3) Sept-2026 tariffed reference prices (25% Section 301 on China-sourced electronics)

- Qi TX: **$5.63**
- Buds TX: **$2.50**
- Watch TX coil: **$3.50 estimate**
- Trigger board: **$2.25**
- 65W GaN brick (included with Step): **$13.75**
- Cable (included with Step): **$3.00**
- 20W magnetic TX: **$7.50**
- IP67 USB-C: **$4.00**
- 20,000 mAh certified PD bank: **$22.50**
- Enclosure cost targets: Walnut **$9.50** (wood-PLA + oil), Obsidian **$11.00** ($7.50 + $3.50 CF premium)
- Packaging target: kraft box **$3.00**
- Easy-connect delta target: **~$6–12 / unit, plan at ~$8**

## 4) One-time tooling/setup

| Item | Cost |
|---|---:|
| Hardened steel nozzle (CF-PETG) | $15 |
| Heat-set insert tips | $12 |
| Multimeter | $10 |
| Wire stripper | $8 |
| Heat gun | $15 |
| Thermal epoxy + kapton | $15 |
| Camo stencil/paint supplies | $30 |
| Immersion test kit | $15 |
| **Total cash draw** | **~$105 if bought from zero; roughly flat to -$10 versus the older solder-based plan if common hand tools are already on hand** |

## 5) Schedule updates

1. **Week 1:** place a **measurement order (~$35)**: one of each electronics module, plus the 65W GaN brick / USB-C plug-overmold reference, Digispark board, screw-terminal DC jack, and distribution PCB for caliper capture (`docs/design-brief-step.md` §5).
2. **Week 1:** place consolidated parts order after measurement order confirmation (same-week confirmation target):
   - **Immediate Batch 1 purchase (3 Walnut + 3 Obsidian): ~ $501 Step-only**
   - **Optional full 10-unit planning envelope (if buying all modules up front): adjust from the earlier plan by roughly +$8 per Step unit**
3. **Before prototype printing:** produce CAD production files (friend sketches + dimensional spec, or Upwork CAD freelancer delivery of STEP/STL).
4. **Week 2–3:** first Step prototype and QC gauntlet.
5. **Week 3–5:** build/ship remaining Step units.
6. **Batch 2 gated:** Outdoor Block only after reserve + safety gates pass.
