# Epitome Outdoor Block — Concept Spec (FOR LATER)

**Status:** Concept. Gated behind Step Batch 1 success + $500 reserve. Plausibility: 7/10 with certified-module architecture and IP67 target; 4/10 if custom cells or "completely waterproof" absolutism.

**One-liner:** A rugged, IP67 battery-powered wireless charging block for camping/outdoors. Phone + buds zones, one USB-C output, ~3 full phone charges per bank.

---

## Models

| | **Outdoor Block Camo** | **Outdoor Block Stone** |
|---|---|---|
| Finish | Matte OD green + black camo accents | Matte stone gray + charcoal accents |
| Target price | $129 | $119 |
| Electronics | Identical | Identical |

## Charging zones & interlock logic

| Zone | Spec | Notes |
|---|---|---|
| Zone 1 — Phone | Magnetic wireless, up to 20W | Always on unless thermal/power-limited |
| Zone 2 — Buds | Wireless, engineered 5–10W actual | Market as "optimized earbuds charging" — buds only draw ~5W; higher power = heat in sealed housing |
| Zone 3 — USB-C output | Wired PD output | **When active, Zone 2 auto-disables** (firmware + hardware interlock) |

### Mode table
| USB-C plugged in? | Phone zone | Buds zone |
|---|---|---|
| No | ON | ON |
| Yes | ON | OFF (forced) |
| Bank <10% | OFF | OFF (prevent brownout loops) |

## Waterproofing (IP67 target — not "completely waterproof")

- Enclosure: **ASA or PC-ABS** (not plain ABS — UV/weather resistance)
- Gasketed split line, membrane pressure-equalization vent
- Sealed USB-C receptacle + tethered cap; potted cable glands
- External button via sealed tact dome
- Top shell over coils: 1.2–1.8 mm non-metallic max (wireless efficiency)
- Marketing language: "IP67 — submersion-safe in shallow water" — never claim "waterproof" unqualified

## Battery architecture (same rule as Step Go)

- **Docked/integrated CERTIFIED battery module** (UL 2056 / UN38.3 pre-certified pack), never loose cells
- 20,000mAh class (~74Wh) — under 100Wh airline carry-on limit
- Mandatory: BMS with short-circuit protection, thermal sensor + cutoff, fuse
- Real-world claim: ~3 phone charges (wireless, mixed usage) or 2 charges + buds top-ups

## Draft BOM (rough v1)

| Part | Est. cost |
|---|---:|
| Certified 20,000mAh PD battery module | $22–25 |
| 20W magnetic wireless TX (pre-certified Qi) | $6.50 |
| 5–10W buds TX module | $2.50 |
| Sealed USB-C receptacle + cap | $3.00 |
| Interlock circuit + MCU (ATtiny85) + sensors | $4.00 |
| ASA/PC-ABS printed enclosure + gaskets + vent | $7.00 |
| Fasteners, silicone, misc | $2.50 |
| Packaging | $6.00 |
| **Build cost estimate** | **~$54–57** |

Margin at $119: ~45%. At $129 (Camo): ~48%. Viable.

## Go / No-Go gates (all must pass before spending the $500 reserve)

- [ ] Step Batch 1 sold through (≥3 paid units shipped, zero thermal incidents)
- [ ] LLC + product liability insurance active
- [ ] Certified battery module source confirmed ≤$25
- [ ] Prototype passes: 30 min immersion @ 30 cm (IP67), no ingress
- [ ] Prototype passes: 1 m drop × 6 faces onto packed dirt, functional after
- [ ] Thermal: phone zone sustained 20W for 1 hr in 35°C ambient, coil surface <45°C
- [ ] Runtime: ≥2.5 full phone charges measured (not calculated)
- [ ] 25 charge/discharge cycles, no capacity anomaly, no swelling
- [ ] Interlock verified: USB-C insertion kills buds zone within 1 s, restores on removal
