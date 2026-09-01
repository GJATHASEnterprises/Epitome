# Epitome — Production Plan & Detailed BOMs

**Batch plan:** Step Walnut ×3, Step Obsidian ×3 (Batch 1) · Outdoor Block Camo ×2, Stone ×2 (Batch 2, gated behind Batch 1 + reserve gates).

---

## PART A — How to build the Step (both finishes)

### A1. Design / CAD
1. Two-tier stepped enclosure (existing DXF/technical drawings in `assets/`): top tier = phone coil bay, lower tier = buds coil bay, rear = recessed USB-C input + cable strain channel.
2. Wall thickness 2.4 mm; **coil windows 1.5 mm max** (wireless efficiency).
3. Internal bosses for M3 heat-set inserts ×4 (base plate), coil pockets with 0.3 mm clearance, thermistor channel touching phone-coil backside, LED light pipe hole 3 mm.
4. Walnut model: printed core + walnut veneer top wrap (or walnut-PLA if veneer too fiddly). Obsidian: matte black PETG, 0.4 nozzle, 15% gyroid infill.

### A2. Print
- PETG, 0.2 mm layers, 4 walls near inserts. Print base + top shell separately.
- Per unit: ~180 g filament, ~9 hr print. Dry filament first (stringing ruins matte finish).

### A3. Assembly order (per unit — do not deviate)
1. Heat-set inserts into bosses (soldering iron @ 220°C)
2. Seat phone TX coil module in pocket; kapton tape over rear
3. Seat buds TX module
4. Glue thermistor to phone coil back (thermal epoxy), route to board
5. Wire loom: USB-C trigger/boost board → both TX modules + polyfuse inline
6. Flash ATtiny85 (LED controller firmware in `firmware/`), test blink codes on bench
7. Route LED light pipe, hot-glue strain relief on all JST runs
8. Close shell, drive 4 screws, apply silicone feet
9. Serial sticker inside base: EPT-S-001…006

### A4. Firmware flash
- USBasp/Arduino-as-ISP → ATtiny85. Verify: breathing LED on idle, solid on charge, fast-blink on thermal fault (simulate with hairdryer on thermistor).

### A5. QC per unit (pass all or don't ship)
- [ ] Phone charges on all 3 test devices; buds charge
- [ ] 1-hr sustained charge: surface <45°C
- [ ] Thermal cutoff fires on simulated overheat and recovers
- [ ] 65W brick: both zones simultaneously, no brownout
- [ ] Cosmetic pass under raking light; shake test in packed box

## PART B — How to build the Outdoor Block (both finishes)

### B1. Design deltas vs Step
- Single sealed body, ASA (Camo: OD-green ASA + masked spray camo, clear matte UV coat; Stone: gray ASA, no paint).
- Gasket groove around lid (2 mm TPU printed gasket or 2 mm silicone cord), M3 stainless screws ×8.
- Sealed IP67 USB-C receptacle (panel-mount, rated part — do not use bare board port) + tethered TPU cap.
- Membrane vent (Gore-style adhesive patch) over 3 mm hole.
- Battery bay for certified 20,000 mAh module; foam retention; NTC on cell face AND phone coil.

### B2. Assembly order
1. Inserts → coils (phone 20W magnetic, buds 5–10W) → thermistors ×2
2. Interlock wiring: USB-C VBUS sense → MCU → MOSFET kills buds TX when port active
3. Battery module in bay, foam, connect via fused harness
4. Firmware: interlock logic + <10% cutoff + LED gauge blinks
5. Gasket in groove, torque lid screws in cross pattern, fit vent + port cap

### B3. QC per unit
- [ ] All Step QC items, plus:
- [ ] Interlock: plug USB-C → buds zone off ≤1 s; unplug → restores
- [ ] Immersion: 30 min @ 30 cm, desiccant-paper telltale inside stays dry
- [ ] 1 m drop ×6 faces onto dirt, functional after
- [ ] Measured runtime ≥2.5 full phone charges

---

## PART C — Detailed BOMs (per unit)

### C1. Step Walnut — build $54.05 · sell $99
| Item | Cost |
|---|---:|
| 20W Qi TX module (pre-cert) | $6.25 |
| 5W buds TX module | $2.50 |
| USB-C trigger/boost board | $2.00 |
| ATtiny85 + LED + light pipe | $2.80 |
| NTC thermistor + polyfuse + JST/wiring | $2.00 |
| Heat-set inserts + screws + feet | $1.50 |
| PETG filament (180 g) | $4.00 |
| Walnut veneer + adhesive + finish oil | $6.00 |
| 65W GaN brick (wholesale) | $14.00 |
| Braided USB-C cable 1 m | $3.00 |
| Box + insert + card + band | $6.00 |
| Kapton/epoxy/glue/misc consumables | $2.00 |
| Print electricity + wear amortized | $2.00 |
| **Build cost** | **$54.05** |

**Cost to get to customer (on top of build):**
| Item | Cost |
|---|---:|
| Shipping (USPS Priority, ~2 lb) | $10.50 |
| Ship box + void fill | $1.50 |
| Etsy fees (~10% avg incl. offsite-ads risk) | $9.90 |
| Payment processing (3% + $0.25) | $3.22 |
| Defect/return buffer (10% of build) | $5.40 |
| **Fully loaded delivered cost** | **~$84.57** |
| **Net per $99 sale** | **≈ $14–19** |

Labor = unpaid founder time (tracked, not costed). Free-shipping-in-price recommended.

### C2. Step Obsidian — build $48.05 · sell $89
Same as Walnut minus veneer/oil (−$6.00). Shipping $12.00, Etsy ~$8.90, processing ~$2.92, buffer $4.80. **Fully loaded ≈ $76.67 → net ≈ $12–17.**

### C3. Outdoor Block Stone — build $57.80 · sell $119
| Item | Cost |
|---|---:|
| Certified 20,000 mAh PD module | $24.00 |
| 20W magnetic TX (pre-cert) | $6.50 |
| 5–10W buds TX | $2.50 |
| MCU + interlock MOSFET + sense circuit | $3.00 |
| NTC ×2 + fuse + harness | $2.80 |
| IP67 panel-mount USB-C + tethered cap | $4.00 |
| Membrane vent patch | $1.00 |
| ASA filament (220 g) + TPU gasket | $6.00 |
| Stainless screws + inserts + foam | $2.00 |
| Packaging (no brick — short cable included) | $6.00 |
| Consumables + electricity/wear | $2.50 |
| **Build cost** | **$57.80** |

**To customer:** shipping ~$12.00 (ground — Li-ion in equipment), materials $1.50, fees @ $119 ≈ $15.72, buffer $5.80. **Fully loaded ≈ $92.82 → net ≈ $26.**

### C4. Outdoor Block Camo — build $61.30 · sell $129
Stone BOM + camo masking/spray/UV matte clear (+$3.50). Fees scale to $129. **Fully loaded ≈ $97.50 → net ≈ $31.**

### C5. One-time tooling/setup (not per-unit — from contingency)
| Item | Cost |
|---|---:|
| Heat-set insert tips | $12 |
| USBasp programmer + clips | $10 |
| Thermal epoxy, kapton, flux stock | $15 |
| Camo stencils + rattle cans + clear coat | $30 |
| Immersion test tub + desiccant papers | $15 |
| **Total one-time** | **~$82** |

## PART D — Schedule
- **Wk 1:** order everything (one pass); print while waiting
- **Wk 2–3:** Step prototype → full QC gauntlet → fix → freeze design
- **Wk 3–5:** build remaining 5 Step units, photograph, list
- **Batch 2 (Blocks):** only after reserve gates pass (see budget-plan.md); prototype 1 Stone first, immersion-test before building the other 3.

## PART E — Key margin warning
At real fees + shipping, Step nets **$13–19/unit, not $45**. Earlier "margin" figures were gross build margin only. 6 Step units ≈ **~$90–110 total profit** — Batch 1 is a *learning* batch (proof, reviews, photos), not a payday. The Outdoor Block (~$26–31 net) is the money product. Test Walnut at $109 in Batch 2.
