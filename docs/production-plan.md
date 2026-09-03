# Epitome — Production Plan & Detailed BOMs

**Batch plan:** Step Walnut ×3, Step Obsidian ×3 (Batch 1) · Outdoor Block Camo ×2, Stone ×2 (Batch 2, gated behind Batch 1 + reserve gates).

---

## PART A — How to build the Step line

### A1. Product positioning and design baseline
1. **Step Walnut** = minimalist / wood-desk buyer.
2. **Step Obsidian** = gamer / battlestation buyer.
3. Shared geometry: two-tier stepped enclosure; top tier phone zone, lower tier buds zone, rear recessed USB-C input + strain channel.
4. Authoritative technical specs and BOMs live in `docs/technical-readouts/`:
   - `step-walnut.md`
   - `step-obsidian.md`
   - `outdoor-block-camo.md`
   - `outdoor-block-stone.md`

### A2. Print and assembly summary
- Wall thickness 2.4 mm, coil windows ≤1.5 mm, M3 insert architecture.
- Print baseline: 0.2 mm layers, strengthened walls at inserts, 15% gyroid infill.
- Walnut finish path: wood-PLA with sanded + Danish oil process.
- Obsidian finish path: CF-filled PETG + recessed side RGB diffusers.

### A3. Firmware summary
- Walnut controller: ATtiny85 status LED logic.
- Obsidian controller: ESP32-C3 with RGB mode control and persistence.
- Both Step models enforce thermal-protection behavior to maintain <45°C surface target.

### A4. QC summary
- 3-device charge compatibility.
- 1-hour thermal soak with <45°C external surface.
- Cutoff simulation/recovery.
- 65W dual-zone no-brownout validation.
- Cosmetic raking-light inspection and shake test.
- Obsidian additional gates: RGB all-modes test + RGB-off persistence across power cycles.

## PART B — How to build the Outdoor Block line

### B1. Mechanical/electrical summary
- IP67-target ASA enclosure with TPU gasket, M3 stainless screw pattern, membrane vent, and IP67 panel-mount USB-C + tethered cap.
- Certified 20,000 mAh (74 Wh) PD battery module only (no loose cells).
- Dual wireless zones plus USB-C PD output with hardware + firmware interlock.

### B2. Firmware summary
- USB-C insertion disables buds zone within 1 second.
- USB-C removal restores buds zone.
- Battery <10% disables all zones.
- Fuel-gauge blink behavior and low-battery cutoff.

### B3. QC summary
- Includes all Step QC gates plus:
- Interlock timing verification.
- 30-minute immersion at 30 cm with desiccant telltale.
- 1 m drop test across 6 faces.
- Runtime verification (≥2.5 phone charges).
- 25-cycle battery check.
- Wording control: use “IP67 — submersion-safe in shallow water”; do not use unqualified “waterproof”.

---

## PART C — Unit economics (authoritative values)

### C1. Step Walnut
- Price: **$99**
- Build: **$42.43**
- Shipping: customer-paid (~$10.50 target)
- Net: **~$36/sale**

### C2. Step Obsidian
- Price: **$109**
- Build: **~$48.50**
- Controller: **ESP32-C3**
- Shipping: customer-paid (~$10.50 target)
- Net: **~$40–44/sale**

### C3. Outdoor Block Stone
- Price: **$119**
- Build: **~$53.30**
- Shipping: customer-paid (ground service for Li-ion)
- Net: **~$34/sale**

### C4. Outdoor Block Camo
- Price: **$129**
- Build: **~$56.80**
- Shipping: customer-paid (ground service for Li-ion)
- Net: **~$39/sale**

### C5. One-time tooling/setup (not per-unit)
| Item | Cost |
|---|---:|
| Heat-set insert tips | $12 |
| USBasp programmer + clips | $10 |
| Thermal epoxy, kapton, flux stock | $15 |
| Camo stencils + rattle cans + clear coat | $30 |
| Immersion test tub + desiccant papers | $15 |
| Hardened steel nozzle (CF-PETG requirement) | $15 |
| **Total one-time** | **~$97** |

## PART D — Schedule
- **Wk 1:** order everything (one pass); print while waiting
- **Wk 2–3:** Step prototype → full QC gauntlet → fix → freeze design
- **Wk 3–5:** build remaining 5 Step units, photograph, list
- **Batch 2 (Blocks):** only after reserve gates pass (see budget-plan.md); prototype 1 Stone first, immersion-test before building the other 3.

## PART E — Margin note
- Corrected positioning and revised costs make Obsidian the higher-margin Step model.
- Use the four technical readouts in `docs/technical-readouts/` as the source of truth for per-model BOM detail and QC execution.
