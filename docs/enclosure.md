# Epitome Penta — Enclosure Specification

## Core Envelope

| SKU | Overall width | Overall depth | Corner radius | Base material |
|---|---:|---:|---|---|
| Penta Standard | ~250mm | ~100mm | R10mm | Matte ABS |
| Penta XL | ~320mm | ~100mm | R10mm | Matte ABS |

---

## Structural Layout

The enclosure remains split into three sections left to right:

1. **Left slot** — laptop bay (Zone 4)
2. **Centre platform** — **Step 1 + Step 2 + Step 3** (Zones 1–3)
3. **Right slot** — tablet bay (Zone 5)

Launch sequence: Standard first, XL second.

---

## Left Slot (Laptop — Zone 4)

- Entry: device slides in **on its thin edge** (screen facing forward), charges from cable at top
- Slot length: **400mm** (fits any laptop up to 17" class)
- Slot width: **35mm** (fits laptops up to ~28mm thick including case)
- Slot depth: **90mm** (front to back, for stability)
- Captive braided USB-C cable (220mm, 100W) hangs from top of slot
- Silicone lining on floor and side walls
- 5mm silicone-covered floor pad supports device edge

---

## Right Slot (Tablet — Zone 5)

- Entry: device slides in **on its thin edge**, charges from cable at top
- Slot length: **290mm** (fits any tablet up to iPad Pro 13" in case)
- Slot width: **20mm** (fits tablets up to ~16mm thick including case)
- Slot depth: **70mm** (front to back, for stability)
- Captive braided USB-C cable (200mm, 20W) hangs from top of slot
- Silicone lining on floor and side walls
- 5mm silicone-covered floor pad supports device edge

---

## Centre Platform — 3-Step Tapered Geometry

| Step | Width | Depth | Height | Zone | Content |
|---|---:|---:|---:|---|---|
| Step 3 (top) | 100mm | 80mm | 15mm | Zone 3 | Watch cradle — Apple puck + Qi coil |
| Step 2 (middle) | 140mm | 100mm | 15mm | Zone 2 | Buds/Phone pad — 15W Qi, 90×65mm landscape |
| Step 1 (base) | 180mm | 110mm | 15mm | Zone 1 | Phone pad — 20W Qi, full-width silicone surface |

- Total centre platform height: **45mm** (3 × 15mm)
- Taper rule: each step is **40mm narrower** than the one below
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
- Rear wiring channel carries all internal harnesses
- Separate inlet fuse holder removed from rear wall (protection moved to PCB PTC)

---

## Fastening and Base Features

- M3 clearance holes: Ø3.20mm, left/right symmetry on centre platform
- 4× rubber feet: Ø15×3mm at corners
- 8× underside vent slots: 40×4×2.5mm
- Snap-fit base + M3 screws for service access
- **PSU cavity moved under laptop slot** for thermal isolation from centre Qi zones

---

## Materials

| Part | Material | Finish |
|---|---|---|
| Top surface + step faces | 3mm ABS sheet | Primed + Rust-Oleum 2X Matte Black |
| Base | 3mm ABS sheet | Primed + Matte Black |
| Slot walls | 3mm ABS sheet | Primed + Matte Black |
| Centre platform | 3D printed ABS | Primed + Matte Black |
| Slot/pad lining | Silicone sheet | Dark grey anti-slip |
| Front LED diffuser | Frosted acrylic 3mm | Diffused |
| Feet | Rubber adhesive | Matte black |

---

## Assembly Method

**Tools needed:**
- Soldering iron (for heat-set inserts)
- Weld-On #3 ABS cement
- M3 screwdriver
- Wire stripper / crimper

**Step 1 — Slot boxes**
Laser cut slot wall panels use tab-and-slot joints. Dry fit first, then bond all joints with Weld-On #3 ABS cement. Hold 60 seconds per joint. Full cure: 24 hours.

**Step 2 — Base plate**
Slot boxes sit on base plate and are cemented down. Centre platform sits between them, located by 4× M3 screws through base into brass heat-set inserts in platform bottom.

**Step 3 — Electronics installation**
Install PSU in cavity under laptop slot. Route all wiring through rear channel. Install all charging modules per component-positions.md. Captive cables routed through top of each slot.

**Step 4 — Top panels**
Cemented to slot box top edges + 2× M3 screws per panel from underneath.

**Step 5 — Rear wall**
Cemented to back of both slot boxes. IEC C13 inlet installed in cutout.

**Step 6 — Base close**
4× M3 screws at corners. Rubber feet press-fit over screw heads.

**Time per unit:** ~45–60 minutes once experienced.
