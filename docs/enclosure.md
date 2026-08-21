# Epitome Penta — Enclosure Specification

## Core Envelope

| SKU | Overall width | Overall depth | Corner radius | Top plate thickness | Base material |
|---|---:|---:|---|---|---|
| Penta Standard | ~530mm | ~300mm | R20mm | 1.5mm aluminium | Matte ABS |
| Penta XL | ~700mm | ~300mm | R20mm | 1.5mm aluminium | Matte ABS |

---

## Structural Layout

The enclosure remains split into three sections left to right:

1. **Left slot** — laptop bay (Zone 4)
2. **Centre platform** — **Step 1 + Step 2 + Step 3** (Zones 1–3)
3. **Right slot** — tablet bay (Zone 5)

Launch sequence: Standard first, XL second.

---

## Left Slot (Laptop — Zone 4)

- Entry: open front, laptop slides in horizontally on its side
- Slot width: **320mm (Standard)** / **400mm (XL)**
- Slot depth: **25mm**
- Slot opening: **28mm**
- Silicone lining on floor and rear wall
- **5mm silicone-covered rear stop shelf** supports device edge
- **Captive braided USB-C to USB-C cable (220mm, 100W)**, fixed internally to PD board
- Cable free end stores coiled on rear wall via silicone clip (above stop shelf)

---

## Right Slot (iPad — Zone 5)

- Entry: open front, iPad/tablet slides in horizontally on its side
- Slot width: **290mm**
- Slot depth: **25mm**
- Slot opening: **20mm**
- Silicone lining on floor and rear wall
- **5mm silicone-covered rear stop shelf** supports device edge
- **Captive braided USB-C to USB-C cable (200mm, 20W)**, fixed internally to PD board
- Cable free end stores coiled on rear wall via silicone clip (above stop shelf)

---

## Centre Platform — 3-Step Tapered Geometry

| Step | Width | Depth | Height | Zone | Content |
|---|---:|---:|---:|---|---|
| Step 3 (top) | 100mm | 80mm | 15mm | Zone 3 | Watch cradle — Apple puck + Qi coil |
| Step 2 (middle) | 140mm | 100mm | 15mm | Zone 2 | Buds/Phone pad — 15W Qi, 90×65mm landscape |
| Step 1 (base) | 180mm | 110mm | 15mm | Zone 1 | Phone pad — 20W Qi, full-width silicone surface |

- Total centre platform height: **45mm** (3 × 15mm)
- Taper rule: each step is **40mm narrower** than the one below
- Riser faces: brushed aluminium
- Each riser requires **internal ribbing reinforcement**

### Step 1 (Zone 1 — Phone)

- Full-width flat silicone wireless surface (no recessed dish)
- Silicone area: **160mm × 100mm**
- Qi TX: **20W**, centred coil under surface
- Magnetic alignment: N52 MagSafe-style ring
- Phone orientation target: **landscape**

### Step 2 (Zone 2 — Buds/Phone)

- 90×65mm landscape silicone dish
- 15W Qi coil centred
- 1mm subtle silicone ridge defining **68×48mm** inner buds zone
- Slight phone side overhang on this step is acceptable and expected

### Step 3 (Zone 3 — Watch)

- Rear-position watch cradle on Step 3 top
- Slight raised profile for premium visibility
- Apple Watch magnetic puck + Qi watch coil
- Shared 5W budget, one watch charging path active at a time

---

## Rear Wall Features

- **Right-angle IEC C13 inlet:** 28×20mm cutout, cable routed downward
- Captive cable clips for Zones 4 and 5 mounted above slot stop shelves
- Rear wiring channel continues to carry all internal harnesses
- Separate inlet fuse holder removed from rear wall (protection moved to PCB PTC)

---

## Fastening and Base Features

- M3 clearance holes: Ø3.20mm, left/right symmetry on centre platform
- 4× rubber feet: Ø15×3mm at corners
- 8× underside vent slots: 40×4×2.5mm
- Snap-fit base + M3 screws for service access
- **PSU cavity moved under laptop slot** for thermal isolation from centre Qi zones

---

## Manufacturing Method (Batch 1 Cost-Optimized Hybrid)

- **Centre platform (3-step):** 3D printed ABS (complex geometry only)
- **Slot walls (left + right):** laser cut + bent ABS sheet
- **Top aluminium plates + step riser faces:** laser cut 1.5mm aluminium sheet, bent
- **Base:** vacuum-formed ABS sheet

### Batch 1 Enclosure Cost Targets (15 units)

- 3D print centre platform only (~120mm × 120mm × 45mm volume): **$18–28 / unit**
- Laser cut ABS slot walls: **$8–12 / unit**
- Vacuum-formed base: **$6–10 / unit**
- Aluminium laser cut + bend set: **$8–12 / unit**
- **Total enclosure Batch 1:** **~$40–62 / unit** (down from ~$45–65 full 3D print)

---

## Materials

| Part | Material | Finish |
|---|---|---|
| Top plate / step faces | 1.5mm aluminium | Gunmetal (Black), Silver (White), Midnight Blue |
| Base and slot walls | Matte ABS | Black, White, Navy-black |
| Slot/pad lining | Silicone elastomer | Dark grey anti-slip |
| Front LED diffuser | Frosted acrylic | Diffused |
| Feet | Moulded rubber | Matte black |
