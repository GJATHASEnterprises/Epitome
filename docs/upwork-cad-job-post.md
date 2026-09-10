# Upwork Job Post — CAD Production Files for Epitome Step

**Copy-paste everything below the line into Upwork. Budget: fixed price $250 (accept range $150–350).**

---

## Title
CAD production files (STEP/STL) for a 2-piece 3D-printed three-tier wireless charger enclosure — full written spec provided

## Category
CAD & 3D Modeling → Product Design (Fusion 360 / SolidWorks / Onshape)

## Description

I'm building a three-tier desktop wireless charging stand ("Epitome Step") sold in two material variants that share identical geometry. It has dedicated zones for a phone, earbuds, and watch, with the top watch step set back from the front. I need production-ready CAD from a **complete written design brief** — the industrial design direction, target envelope dimensions, all engineering constraints, and caliper-measured component dimensions are already documented. This is a modeling job, not a design-from-scratch job: the added printability note and coil-pocket fit coupons are just low-cost print-validation deliverables to reduce revision rounds.

**You will receive:**
- A detailed design brief (target envelope 165 × 100 mm, three-tier layout, wall thicknesses, coil pocket rules, insert boss specs, FDM printability constraints)
- Repo-generated renders / technical diagrams showing the intended three-tier structure and proportions
- Caliper-measured dimensions for every internal component (coils, PCBs, inserts, light pipe / LED strips)
- Reference sketches of the intended look

**Deliverables:**
1. Parametric CAD (Fusion 360 preferred; native file + STEP)
2. STL exports, print-oriented, for both shells × both variants:
   - Variant A ("Walnut"): base + top shell with Ø3.2 mm front light-pipe hole
   - Variant B ("Obsidian"): base + top shell with recessed side grooves (5 × 3 × ~140 mm) for LED diffuser bars, incl. printable diffuser bar model
3. Parametric clearance variables / notes for fit tuning, including per-material offsets for PETG, wood-PLA, and CF-PETG shrinkage
4. Dimensioned drawing PDF (top, front, side, section through all three coil pockets)
5. Short printability report: part orientation, support-free confirmation, estimated print time/material per shell
6. Milestone 2 test-fit artifacts: one small coil-pocket fit coupon STL for each coil pocket (phone / earbuds / watch)
7. Exploded-view image showing assembly stack order

**Hard requirements (all specified in the brief):**
- Wall 2.4 mm; ≤1.5 mm directly above coil pockets
- Coil pockets sized from provided measurements + 0.3 mm clearance
- 4× M3 heat-set boss (Ø7.2 mm hole / Ø10 mm boss); no fasteners visible from top/sides
- Rear recessed USB-C pocket + strain channel; thermistor groove; board standoffs
- Three coil pockets total, including the watch pocket on the set-back Step 3 tier
- Both shells FDM-printable without supports (no overhangs >50° without chamfer)

**Process & milestones:**
- Milestone 1 (30%): exterior form model for approval — visually matches the repo-generated renders/technical diagrams and the brief's §2 envelope within ±10%
- Milestone 2 (70%): full internal features, all deliverables. Includes **2 revision rounds** (e.g., pocket fit adjustments after my test print), plus the three coil-pocket fit coupon STLs
- Timeline: 7–10 days preferred

## Printer / fabrication info

**To be provided to the hired freelancer before final modeling starts:**
- Printer bed size
- Nozzle size(s)
- Exact PETG / wood-PLA / CF-PETG material brands
- Preferred layer height / wall settings if they affect fit allowances

**To apply:** share 1–2 examples of enclosure/consumer-product CAD you've modeled for FDM printing, and confirm you can deliver native Fusion 360 (or state your tool).

---

## Internal notes (not part of the post)

- **Do NOT post until §5 of `design-brief-step.md` is filled in with caliper measurements** — posting before parts arrive invites guesswork and a wasted revision round.
- Send shortlisted applicants the design brief only (not the whole repo — pricing/margin docs are private).
- Scope is the **three-tier** Step enclosure only: phone + earbuds + watch, target footprint 165 × 100 mm, watch step setback preserved, exterior shape still TBD within the brief envelope.
- Screen for: FDM experience specifically (injection-molding-only folks over-design), asks about tolerances/test prints (good sign), portfolio with visible layer-line-aware design.
- Red flags: bids >$500 for this scope, "I will design your product" language (scope creep), no questions asked before bidding.
- Budget source: reallocated from marketing (see budget-plan.md). Cap: $350 including revisions.
- Payment: milestones via Upwork escrow only, no off-platform payment.
