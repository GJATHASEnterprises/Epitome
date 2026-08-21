# Epitome Penta — Bill of Materials (BOM)

## Batch 1 Context

- **Location:** Downers Grove, IL (Chicago suburb)
- **Batch size:** 10 units
- **SKU scope:** Standard SKU only
- **Colour scope:** Black only
- **Budget:** $1,500
- **Sell price:** $249
- **Tariffs:** Section 301 at 25% (**Section 122 expired July 24 2026 — no longer applies**)
- **Enclosure:** Full ABS — 3D printed centre platform (school printer, own filament) + laser cut ABS panels (Pumping Station One makerspace, Chicago)
- **Batch 1 material rule:** No aluminium anywhere in Batch 1

---

## Electronics — Per Unit Costs (Verified August 2026)

### AliExpress order (apply 25% Section 301 tariff to all)

| Part | Calculation | Per Unit |
|---|---:|---:|
| ESP32-C3 SuperMini | $1.26 × 1.25 | $1.58 |
| PD 100W trigger board | $1.50 × 1.25 | $1.88 |
| PD 20W trigger board | $1.25 × 1.25 | $1.56 |
| Apple Watch puck PCBA module | $1.60 × 1.25 | $2.00 |
| Qi watch coil 5W | $5.00 × 1.25 | $6.25 |
| INA3221 chip ×2 (LCSC, raw chip for DIY breakout) | $1.20 × 2 × 1.25 | $3.00 |
| JLCPCB bare INA3221 breakout PCBs ×2 (ordered with parts) | $0.20 × 2 | $0.40 |
| Mean Well LRS-150-24 PSU (LCSC) | $13.85 × 1.25 | $17.31 |
| WS2811 LED strip section (20 LEDs, from 2× 5m rolls shared across batch) | Fixed | $1.40 |
| IEC C13 right-angle inlet (LCSC) | $3.00 × 1.25 | $3.75 |
| Wiring / JST connectors / heat shrink / cable clips | $6.50 × 1.25 | $8.13 |
| PTC resettable fuse + passives (LCSC) | $0.40 × 1.25 | $0.50 |

### Amazon US domestic order (no tariff)

| Part | Per Unit |
|---|---:|
| Qi 20W TX module (Zone 1) | $14.00 |
| Qi 15W TX module (Zone 2) | $11.00 |
| Captive USB-C cable 220mm 100W braided | $4.00 |
| Captive USB-C cable 200mm 20W braided | $3.00 |
| Wiring / connectors supplement | $8.00 |
| PTC fuse passives supplement | $1.00 |

**Electronics total per unit: $90.96**
**Electronics total ×10: $909.60**

---

## Enclosure — Per Unit Costs

### 3D printed centre platform (school printer)

- **Filament only:** 198g ABS per unit, from own $20 spool = **$2.00**
- **Print time:** ~6–8 hours per unit on school printer

### Laser cut ABS panels (Pumping Station One, Chicago — makerspace)

- Pumping Station One membership: **$50/month** (one month covers all 10 units)
- ABS sheet from Inventables (Chicago-based, fast shipping to Downers Grove): **~$50–60 for all 10 units worth**
- Machine time at member rate (~$1–2/min): **~$20–30 for all 10 units**
- **Total laser cutting all-in:** **~$120–140 for whole batch = $12–14/unit**

### Parts cut on laser

- Slot walls (both slots): tab-and-slot panels, simple rectangles
- Base plate: 530×300mm
- Top panels: left 330×300mm, right 300×300mm
- Rear wall with IEC C13 cutout
- LED diffuser strip: frosted acrylic 530×15mm

### Finishing supplies (shared across all 10 units)

- Sandpaper assortment 120–800 grit: $6
- Acetone 1 litre (Home Depot/Walmart): $8
- Rust-Oleum filler primer 1 can: $6
- Rust-Oleum matte black paint 1 can: $6
- Matte clear coat 1 can: $6
- **Total finishing supplies:** $32 = **$3.20/unit**

### Assembly consumables

- Weld-On #3 ABS cement (one bottle, covers all 10): $8 total = $0.80/unit
- M3 brass heat-set inserts 50-pack: $8 total = $0.80/unit
- M3 screw assortment kit (one kit): $9 total = $0.90/unit
- Rubber feet 100-pack: $7 total = $0.70/unit
- Silicone sheet 500×500mm (one sheet cut for all 10): $13 total = $1.30/unit

**Enclosure total per unit: $21.70 (excl. makerspace membership amortised separately)**
**Makerspace membership: $50 one-time**
**Enclosure + membership total ×10: $267**

---

## Packaging — Per Unit

- Flat-pack rigid kraft box ~580×340×100mm (self-assembled): $3.50–4.00
- IEC C13 braided cable 1.5m (Amazon domestic): $3.00
- Cardboard insert (cut from offcuts): $0.50
- Felt liner (cut from $5 roll): $0.20
- Tape + label: $0.50
- **Packaging total per unit:** $7.70–8.20. Use **$8.00**.
- **Packaging total ×10:** $80.00

---

## Hidden / Operational Costs

- Single combined AliExpress/LCSC order inbound shipping (ePacket): $25 total
- Amazon order: free Prime shipping
- Inventables ABS sheet shipping (Chicago-based, fast to Downers Grove): $10–15
- Stripe US payment processing (2.9% + $0.30 on $249): $7.52/unit = $75.20 total
- UPS/FedEx Ground domestic shipping to customer (~3.5kg box, IL origin): $16.00/unit = $160.00 total
- Defect/spare buffer (1 unit parts cost ~$91): $91.00 total = $9.10/unit
- Domain (epitome.io): $15/year = $1.50/unit
- Carrd pro site: $19/year = $1.90/unit
- Wise bank transfer fee (0.45% on ~$500 AliExpress order): $2.25 total
- **Hidden costs total:** **~$385–395**

---

## Full Batch 1 Totals

| Category | Total ×10 |
|---|---:|
| Electronics | $909.60 |
| Enclosure (inc. makerspace membership + finishing + assembly consumables) | $267.00 |
| Packaging | $80.00 |
| Hidden / operational | $390.00 |
| **Grand total** | **$1,646.60** |
| **Per unit cost** | **$164.66** |

**Revenue:** 10 × $249 = **$2,490**
**Profit:** **$843.40**
**Per unit margin:** **$84.34**

**Budget note:** Total spend of **$1,646.60** exceeds the **$1,500** budget by **$146.60**. Collect **1 pre-order ($249)** before placing any parts orders. After 1 pre-order: **out-of-pocket = $1,397.60** — inside budget with **$102.40** safety net.

---

## Approved Suppliers

| Supplier | Use for |
|---|---|
| AliExpress (single combined order) | ESP32-C3, PD boards, Apple Watch puck, Qi coil, INA3221 chip, PSU, WS2811, IEC inlet, wiring |
| LCSC (combine with AliExpress order) | INA3221 chip, PSU, passives |
| Amazon US (domestic, no tariff) | Qi 20W/15W modules, USB-C cables, wiring supplements, rubber feet, M3 kit, silicone sheet, flat-pack boxes, IEC cable |
| Inventables (Chicago) | ABS sheet, frosted acrylic strip |
| JLCPCB | Bare INA3221 breakout PCBs (order with AliExpress/LCSC) |
| Pumping Station One (Chicago makerspace) | Laser cutting all ABS + acrylic panels |
| School makerspace | 3D printing centre platform ×10 |
| Home Depot / Walmart (Downers Grove) | Acetone, sandpaper, Rust-Oleum primer/paint/clear coat |
| Microcenter (Westmont, IL — 7 min away) | Backup ESP32, connectors, soldering supplies |

---

## Tariff Note (August 20 2026)

- Section 301: **25% active** on Chinese electronics
- Section 122: **EXPIRED July 24 2026** — no longer applied
- All AliExpress/LCSC costs above already include **25% Section 301**
