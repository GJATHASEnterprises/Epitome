# Epitome — Budget Plan (~$2,000)

## Allocation (Sept 2026)

| Item | Amount | Notes |
|---|---:|---|
| Batch 1 Step parts + packaging + build consumables | ~$451 | 3 Walnut + 3 Obsidian plan incl. estimated watch TX coils |
| LLC formation + product liability insurance | ~$500 | Required before battery products |
| Marketing (see `docs/marketing-plan.md`) | **~$400** | Reduced from ~$600 |
| CAD freelancer (production files) | **$150–250** | STEP/STL delivery from design brief |
| Measurement order (Week 1) | **~$35** | 1× each module for caliper dimensions, plus GaN brick / cable-overmold capture for rear strain-channel sizing |
| Step Go / Outdoor Block reserve (gated) | **$500** | Unchanged |
| Contingency (after tooling draw) | Remainder | Includes defects/reshipping buffer |
| **Total planning envelope** | **~$2,000** | |

## Unit economics reference (net-after-fees)

| Product | Build cost | Price | Net-after-fees |
|---|---:|---:|---:|
| Step Walnut | ~$45.93 | $99 | ~ $32–33/sale |
| Step Obsidian | ~$52.00 | $109 | ~ $36–40/sale |
| Outdoor Block Stone (gated) | ~$53.30 | $119 | ~ $34/sale |
| Outdoor Block Camo (gated) | ~$56.80 | $129 | ~ $39/sale |

## Labor & true unit economics

- Build-cost numbers above exclude labor. Real finishing/assembly/QA/packing time is expected to be roughly **45–90 minutes per unit**, especially for Walnut sanding/oil work.
- That is acceptable for Batch 1 validation, but it means the table above should not be read as final long-term margin after labor.
- Batch 1 projected profit (**~$204–219**) will **not** fully recoup the **$150–250 CAD spend**, and that is an accepted validation cost rather than a launch failure.

## Tooling draw (from contingency)

One-time tooling is **~$97** (hardened steel nozzle, insert tips, USBasp, epoxy/kapton, camo stencils, immersion test kit).

## Measurement-order reminder

- Include the 65W GaN brick, USB-C plug overmold, and cable exit/bend-relief dimensions in the same first-pass measurement set because they directly affect the rear recess and strain-channel geometry in the Step CAD brief.

## Gates on the $500 reserve

All must be true (full lists in `docs/for-later/step-go-concept.md` and `docs/for-later/outdoor-block-spec.md`):
- Batch 1 sold through (≥3 paid units), zero thermal incidents
- LLC + insurance active
- Certified battery module source ≤$25 confirmed
- Prototype passes physical test gates (immersion/drop/thermal for Outdoor Block)
