# Epitome — Production Plan (Sept 2026 planning estimates)

## 1) Product lineup and build materials

- **Step Walnut ($99):** minimalist / wood-desk buyer. Black PETG base + wood-PLA top. Digispark-style ATtiny85. Single white status LED.
- **Step Obsidian ($109):** gamer / battlestation buyer. Full CF-PETG shells. Digispark-style ATtiny85. WS2812B RGB glow lines.
- **Outdoor Block Stone ($119) / Camo ($129):** 20W magnetic phone + 5–10W buds + 20W USB-C output (Batch 2 gated).

Authoritative per-model BOMs and QC gates live in `docs/technical-readouts/`.

## 2) Unit economics (customer pays shipping)

| Model | Build cost | Price | Net after fees/processing/defect reserve |
|---|---:|---:|---:|
| Step Walnut | ~$48.63 | $99 | ~ $30–32 / sale |
| Step Obsidian | ~$54.63 | $109 | ~ $34–38 / sale |
| Outdoor Block Stone | ~$53.30 | $119 | ~ $34 / sale |
| Outdoor Block Camo | ~$56.80 | $129 | ~ $39 / sale |

## 3) Sept-2026 tariffed reference prices (25% Section 301 on China-sourced electronics)

- Step Zone 1 TX: **$5.63**
- Step Zone 2 TX (same SKU class): **$5.63**
- Watch TX coil (generic): **$3.50 estimate**
- Step USB-C output trigger board (15W class): **$1.50**
- Step 65W GaN brick target: **$9.50** *(fallback $13.75 if cert docs fail checks)*
- Step cables (1 input + 1 output): **$3.00**
- Outdoor Block 20W magnetic TX: **$7.50**
- Outdoor Block IP67 USB-C: **$4.00**
- Outdoor Block 20,000 mAh certified PD bank: **$22.50**

## 4) Compliance and sourcing rules

- Every wireless TX module must have a verifiable module-level FCC ID.
- Outdoor Block battery modules must provide verifiable UN38.3 and UL component docs.
- Step Walnut + Obsidian share one FCC test path because electronics are identical.
- Outdoor Block Stone + Camo also share one test path later because electronics are identical.

## 5) Build sequence rules

- Do not build sellable inventory before demand is proven and FCC authorization is complete.
- Waitlist can be used before authorization, but must not collect payment or claim live sales.
- Operating gates and phase order are defined in `docs/launch-plan.md`.
