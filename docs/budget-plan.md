# Epitome — Budget Plan (~$2,000)

## Allocation (Sept 2026)

| Item | Amount | Notes |
|---|---:|---|
| Batch 1 Step parts + packaging + build consumables | ~$501 | 3 Walnut + 3 Obsidian plan incl. watch TX coils + easy-connect parts |
| LLC formation + product liability insurance | ~$500 | Required before battery products |
| Marketing (see `docs/marketing-plan.md`) | **~$400** | Reduced from ~$600 |
| CAD freelancer (production files) | **$150–250** | STEP/STL delivery from design brief |
| Measurement order (Week 1) | **~$35** | 1× each module for caliper dimensions, plus GaN brick / cable-overmold capture for rear strain-channel sizing |
| Step Go / Outdoor Block reserve (gated) | **$500** | Unchanged |
| Contingency (after tooling draw) | Remainder | Absorbs the Batch 1 easy-connect delta; reserve stays untouched |
| **Total planning envelope** | **~$2,000** | |

## Unit economics reference (net-after-fees)

| Product | Build cost | Price | Net-after-fees |
|---|---:|---:|---:|
| Step Walnut | ~$50.50 | $99 | ~ $28–29/sale |
| Step Obsidian | ~$56.50 | $109 | ~ $32–36/sale |
| Outdoor Block Stone (gated) | ~$53.30 | $119 | ~ $34/sale |
| Outdoor Block Camo (gated) | ~$56.80 | $129 | ~ $39/sale |

## Labor & true unit economics

- Build-cost numbers above exclude labor. Real finishing/assembly/QA/packing time is expected to be roughly **45–90 minutes per unit**, especially for Walnut sanding/oil work.
- That is acceptable for Batch 1 validation, but it means the table above should not be read as final long-term margin after labor.
- Batch 1 projected profit (**~$180–195**) will **not** fully recoup the **$150–250 CAD spend**, and that is an accepted validation cost rather than a launch failure.
- The beginner-friendly easy-connect architecture adds **~$50** to the first 6-unit parts order and is expected to be absorbed by contingency; the **$500 reserve remains untouched**.

## Tooling draw (from contingency)

| Item | Cost | Notes |
|---|---:|---|
| Hardened steel nozzle (CF-PETG) | $15 | Still required |
| Heat-set insert tips | $12 | Still required |
| Multimeter | $10 | Required for buck-voltage verification |
| Wire stripper | $8 | Makes screw-terminal prep repeatable |
| Heat gun | $15 | For solder-seal fallback + insert work assist |
| Thermal epoxy + kapton | $15 | Still required |
| Camo stencil/paint supplies | $30 | Outdoor Block reserve path |
| Immersion test kit | $15 | Outdoor Block reserve path |

Removing the USBasp and any solder-only workflow keeps the tooling mix roughly neutral to slightly lower overall (**about flat to -$10**, depending on which hand tools are already on hand).

## Measurement-order reminder

- Include the 65W GaN brick, USB-C plug overmold, Digispark board, screw-terminal DC jack, and power-distribution PCB in the same first-pass measurement set because they directly affect the rear recess, board bay, and strain-channel geometry in the Step CAD brief.

## Gates on the $500 reserve

All must be true (full lists in `docs/for-later/step-go-concept.md` and `docs/for-later/outdoor-block-spec.md`):
- Batch 1 sold through (≥3 paid units), zero thermal incidents
- LLC + insurance active
- Certified battery module source ≤$25 confirmed
- Prototype passes physical test gates (immersion/drop/thermal for Outdoor Block)
