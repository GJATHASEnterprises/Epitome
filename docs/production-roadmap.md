# Epitome Step — Production Roadmap

---

## Batch 1 — 10 units (5 Walnut + 5 Obsidian)

### Goal
Prove the product works. Learn what's hard to build. Get 10 real units into real customers' hands. Collect feedback.

### Timeline
| Week | Task |
|---|---|
| Week 1 | Order all parts. Set up Shopify pre-order page. Post on Reddit/Etsy. |
| Week 2 | Parts arrive. Program ATtiny85 chips. Confirm school makerspace bookings. |
| Week 3 | Build weekend — 3D prints, laser cuts, electronics assembly, finishing |
| Week 4 | QC all 10 units. Photography. Pack boxes. |
| Week 5 | Ship to pre-order customers. Post "Batch 1 shipped" update. |

### Build schedule (Week 3)
- 3D prints: 4 h Friday evening + 4 h Saturday morning (2 prints per session)
- Laser cuts: Saturday morning alongside prints
- Electronics assembly: Saturday afternoon (4 h, 2 people)
- Per-zone testing: Saturday evening (2 h)
- Finishing: Sunday morning (walnut oil cure + obsidian spray cure in parallel)
- Final assembly + QC: Sunday afternoon
- Photography + packaging: Sunday evening

### School makerspace requirements
- Book FDM printer: 2 × 4-hour blocks (Friday evening + Saturday morning)
- Book laser cutter: 1 × 2-hour block (Saturday morning)
- Book spray booth: 1 × 2-hour block (Sunday morning, for Obsidian finishing only)
- Confirm enclosure and table space for 2 days

---

## What to learn from Batch 1

1. How long does actual build time take? (Target: 18 h for 10 units. Reality may differ.)
2. Which zone gives the most trouble? (Watch relay expected to be fiddly.)
3. Are the walnut faces robust enough? (Watch for delamination if veneer MDF is used.)
4. Do customers understand the BYOC (Bring Your Own Cable) model?
5. What do customers say about the LED colour/brightness?
6. Any thermal issues with Qi2 TX at 20W? (NTC monitoring is there for this.)
7. Any issues with the 100W brick / barrel adapter combo?

---

## Batch 2 — target 25 units (suggest 10 Walnut + 15 Obsidian)

### Targets informed by Batch 1
- Refine build process based on Batch 1 learnings
- Investigate custom PCB to combine relay, ATtiny85, and buck converters on one board
- Evaluate whether walnut step faces can be sourced pre-cut from a supplier
- Evaluate adding a third USB-C port if customers request it

### Timeline
- Start planning after Batch 1 ships
- Target: 6 weeks after Batch 1 ships, Batch 2 opens for pre-order
- Target: 4 weeks after pre-order closes, Batch 2 ships

### Revenue targets
- Batch 1 (5+5): ~$174 profit
- Batch 2 (10+15): target $600–800 profit depending on mix

---

## Future (Batch 3+)

- Consider dedicated manufacturing run instead of school makerspace
- Evaluate custom injection-moulded base (reduces ABS print time from 4h to ~15 min)
- Evaluate Obsidian RGB app control (see `docs/app-spec.md`)
- International shipping (Etsy handles this reasonably)

---

## Price review

Review pricing after Batch 1 based on:
- Actual build time (labour cost if you value your time)
- Customer willingness to pay
- Competitor price changes
- Whether the 100W brick + 3 USB-C cables should remain bundled or become add-ons

The Obsidian model has thin margin (~10%) at $79 with the current packaging. A $5 price increase to $84 would improve margin to ~16% with minimal impact on conversion.

