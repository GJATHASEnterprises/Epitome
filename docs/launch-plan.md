# Epitome — Master Launch Plan (Sept-2026 planning estimates)

This is the operating plan for launching Epitome with a hard capital limit of about **$2,000**.

## Core rules

- Total available capital: **~$2,000**.
- Every phase must fit inside that limit.
- Follow this order: **demand first, compliance second, inventory last**.
- Do **not** build sellable inventory before demand is proven and FCC authorization is complete.
- FCC rule reminder: advertising an unauthorized RF product as "for sale" is a violation. Waitlist pages must not take money or claim active sales.

## Phase 0 — Free verification week (~$0)

1. Ask Qi/Qi2 TX module vendors for module-level FCC IDs.
2. Verify each ID at: https://www.fcc.gov/oet/ea/fccid.
3. Ask the battery module vendor for UN38.3 + UL component docs for the future Outdoor Block.
4. Verify those battery docs directly with the issuing lab.
5. Request quotes from **3 FCC-recognized labs**.
6. Note in all quote requests: one FCC Step test covers both Walnut and Obsidian because electronics are identical; Stone and Camo can share one later test.

**Why this matters:**
- These free answers decide whether the near-term compliance bill lands around **~$1,000–1,500** (good path) or **~$4,000+** (bad path).

### Gate 0 → 1
Do not move to Phase 1 until these vendor and lab answers are documented.

## Phase 1 — Prototype + demand test (~$500–700)

1. Place a measurement order (~$35): one of each module from current docs.
2. Build only **2 prototypes total** (1 Walnut + 1 Obsidian), not 6.
3. Buy only essential setup/tooling (~$120).
4. Form LLC (~$50–150) before any selling activity.
5. Publish a free landing page + waitlist with prototype/renders.
6. Share in relevant communities (r/battlestations, r/functionalprint, etc.).
7. Waitlist page rules: no payments, no "for sale" claims.

### Gate 1 → 2
Move forward only if:
- Waitlist interest is meaningful (suggested threshold: **~100 signups**), **and**
- FCC quote path from Phase 0 remains favorable.

If demand is weak, pause. A max loss of about ~$700 means the demand test worked.

## Phase 2 — Compliance (~$1,000–2,500 if Phase 0 is favorable)

1. Run FCC verification testing for the Step platform (single test covering Walnut + Obsidian).
2. Activate year-1 general/product liability insurance (~$500–1,500).

### Gate 2 → 3
Do not proceed until FCC authorization is in hand.

## Phase 3 — Pre-order-funded production

1. Open paid pre-orders only after Phase 2 gate passes.
2. Build only what is sold.
3. Keep direct sales on own site (customer pays shipping) to avoid typical marketplace fees (~8–15% vs ~3% direct processing).

Sept-2026 planning economics after current Step optimizations:
- **Walnut build:** ~$48.63 → net about **$30–32** at $99.
- **Obsidian build:** ~$54.63 → net about **$34–38** at $109.

Compliance is a one-time toll; after prototypes, each additional unit is mostly BOM cost.

## Phase 4 — Outdoor Block (gated sequence, not cancelled)

Block remains gated until either:
- Step cumulative profit reaches **~$3,000**, or
- Block waitlist/pre-order interest reaches **~40 signups**.

Compliance floor (good path):
- **~$1,500–3,000** with FCC-ID'd modules + certified battery module docs + final FCC verification.
- Full UL 2056 end-product listing (~$15,000–30,000) is a **later scaling milestone** for Amazon/big retail, not required for legal direct sales.

Quality/failure-margin guidance:
- Keep **10–15% defect reserve**.
- Budget **1 sacrificial QC unit per batch** for destructive validation.
- Follow existing QC: immersion, 6-face drop, 25-cycle battery tests.

Li-ion shipping rules for Block:
- Ground only.
- UN3481.
- Battery installed in equipment.
- ≤100Wh (74Wh module qualifies).

## Risk register (plain-language)

1. **Cheap 65W brick risk**: the $9.50 target only stands if genuine UL/ETL/FCC docs check out and thermal-soak samples pass. If not, fall back to the $13.75 brick.
2. **Zone 2 geometry risk**: second phone/buds landing area must be validated in CAD before STL freeze.
3. **Dual-load thermal risk**: test Zone 1 + Zone 2 + USB-C use for hot spots and stability.
4. **Soft-cap firmware limitation**: current cap is heuristic detect-based behavior; no direct current measurement.
5. **Watch-zone compatibility risk**: generic watch coils do not charge Apple Watch without MFi hardware.
6. **Marketing wording risk**:
   - Say: "up to 60W total".
   - Say: "Qi2 magnetic charging — compatible with MagSafe-case iPhones".
   - Do not use bare "MagSafe" as a product claim.
   - Say: "IP67 — submersion-safe in shallow water".
   - Do not use unqualified "waterproof".
