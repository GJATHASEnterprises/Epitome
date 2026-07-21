# Quad-Dock — Production Roadmap

---

## Overview

| Batch | Method | Units | Investment | Status |
|-------|--------|-------|------------|--------|
| Batch 1 | Laser cut + bent enclosure | 17–19 | $1,500 | First run — proves demand |
| Batch 2 | Injection mold + JLCPCB PCBA | 50 | ~$5,000 (reinvested) | After break-even |
| Batch 3+ | Scale run | 100+ | Self-funded | Ongoing |

---

## Batch 1 — Laser Cut (17–19 Units)

### Goal
Prove demand. Sell enough to recoup the $1,500 investment and fund the injection mold for Batch 2.

### Enclosure Method
- ABS base: laser cut + hand bent sheet — no injection mold
- Aluminum top plate: laser cut to Arc profile, anodized or brushed finish
- Setup cost: ~$0 (no mold tooling)
- Per-unit enclosure cost: ~$12–$18
- Appearance: Clean and sharp; slightly more handmade character — acceptable for first batch

### Budget

| Item | Cost |
|------|------|
| PCB setup + first JLCPCB panel | $50–$80 |
| Components (electronics, all 17–19 units) | ~$1,100–$1,250 |
| Enclosure (laser cut, all 17–19 units) | ~$200–$340 |
| Packaging (17–19 units) | ~$75–$130 |
| Misc / buffer | ~$70–$100 |
| **Total** | **~$1,500** |

### Pricing and Revenue

| Metric | Value |
|--------|-------|
| Sale price per unit | $189 |
| Revenue (17 units) | $3,213 |
| Revenue (19 units) | $3,591 |
| Investment to recoup | $1,500 |
| **Break-even point** | **~13 units** |
| Profit after break-even (17 units sold) | ~$1,713 |
| Profit after break-even (19 units sold) | ~$2,091 |

### Break-Even Analysis

| Units Sold | Revenue | Investment | Profit / (Loss) |
|------------|---------|------------|-----------------|
| 1 | $189 | $1,500 | ($1,311) |
| 5 | $945 | $1,500 | ($555) |
| 10 | $1,890 | $1,500 | $390 |
| **13** | **$2,457** | **$1,500** | **$957** ← break-even zone |
| 17 | $3,213 | $1,500 | $1,713 |
| 19 | $3,591 | $1,500 | $2,091 |

*Note: Break-even is roughly at 13 units when amortizing the $1,500 investment across all 17–19 units (≈ $88/unit investment). At 13 units sold the total revenue ($2,457) covers the $1,500 investment with ~$957 to spare.*

---

## Batch 2 — Injection Mold (50 Units)

### Trigger
Order Batch 2 after Batch 1 breaks even (~13 units sold). Use Batch 1 profit to fund the mold.

### Changes from Batch 1
- ABS base switches from laser cut to injection molded — consistent Arc geometry every unit
- Mold cost: $800–$1,500 one-time
- Per-unit base cost drops to ~$6–$10

### Budget (50 Units)

| Item | Cost |
|------|------|
| Injection mold (one-time) | $800–$1,500 |
| Components per unit × 50 | ~$67 × 50 = $3,350 |
| Packaging × 50 | ~$5.50 × 50 = $275 |
| PCB panels (4/panel, 50 units = 13 panels) | ~$200–$300 |
| **Total** | **~$4,625–$5,375** |

### Revenue (50 Units at $189)

| Metric | Value |
|--------|-------|
| Revenue | $9,450 |
| Total costs | ~$5,000 |
| **Profit** | **~$4,450** |

---

## Batch 3+ — Scale Run (100+ Units)

### At 100+ Units
- BOM cost drops to ~$64/unit with volume discounts
- Kraft box at 100 unit MOQ reduces packaging cost
- JLCPCB panels more efficient at higher volume (more panels per order)
- Local laser cutter pricing improves at 50+ aluminum tops

### Revenue Projection (100 Units at $189)

| Metric | Value |
|--------|-------|
| Revenue | $18,900 |
| BOM cost (~$64 × 100) | $6,400 |
| Packaging (~$5 × 100) | $500 |
| **Gross profit** | **~$12,000** |

---

## Path Forward Summary

```
$1,500 investment
    ↓
Batch 1: 17–19 laser cut units
    ↓ sell 13+ units at $189
Break-even + ~$1,700 profit
    ↓ reinvest
Batch 2: injection mold ($800–$1,500) + 50 proper units
    ↓ sell at $189
~$4,450 profit
    ↓ reinvest
Batch 3: 100+ units at ~$64/unit
    ↓
~$12,000 gross profit per batch
```

---

## Key Milestones

| Milestone | Target |
|-----------|--------|
| Prototype complete | Before Batch 1 order |
| Batch 1 shipped | After prototype validation |
| Break-even (13 units) | Triggers Batch 2 planning |
| Mold order | After break-even confirmed |
| Batch 2 shipped | ~8–12 weeks after mold order |
| Batch 3 order | After Batch 2 sells through |
