# Epitome Penta — Enclosure Specification

## Core Envelope

| SKU | Overall width | Overall depth | Overall height | Material system | Notes |
|---|---:|---:|---:|---|---|
| Penta Standard | ~250mm | ~100mm | ~100mm | Full ABS enclosure, no aluminium | Rear spine + front fascia unify the structure |

---

## Structural Layout

The enclosure is a compact three-zone body tied together by two continuous structural panels:

1. **Left slot** — laptop bay (**Zone 4**)
2. **Centre platform** — three-step charging platform (**Zones 1–3**) raised over the PSU cavity
3. **Right slot** — tablet bay (**Zone 5**)
4. **Rear spine plate** — full-width structural rear panel tying both slot walls and the centre platform rear together
5. **Front fascia strip** — full-width front base panel carrying the LED diffuser and visually unifying the dock

The Mean Well LRS-150-24 PSU no longer sits under the laptop slot. It now sits flat on the base plate under the centre platform footprint, with the centre platform body raised on a perimeter wall above it.

---

## Left Slot (Laptop — Zone 4)

- Entry: device slides in **on its thin edge** (screen facing forward)
- Slot length: **400mm**
- Slot width: **35mm**
- Slot depth: **90mm** (internal, front fascia to rear spine)
- Slot wall height: **95mm**
- Captive braided USB-C cable (**220mm, 100W**) hangs from the top of the slot
- No stop shelf; device rests on the lined floor and natural cable reach is validated at full insertion
- Silicone lining on floor and inner side walls

---

## Right Slot (Tablet — Zone 5)

- Entry: device slides in **on its thin edge**
- Slot length: **290mm**
- Slot width: **20mm**
- Slot depth: **70mm** (internal)
- Slot wall height: **75mm**
- Captive braided USB-C cable (**200mm, 20W**) hangs from the top of the slot
- No stop shelf; device rests on the lined floor
- Silicone lining on floor and inner side walls

---

## Centre Platform — 3-Step Tapered Geometry

| Step | Width | Depth | Height | Zone | Content |
|---|---:|---:|---:|---|---|
| Step 1 (base) | 180mm | 110mm | 15mm | Zone 1 | Phone pad, 20W Qi, 160×100mm silicone surface |
| Step 2 (middle) | 140mm | 100mm | 15mm | Zone 2 | Buds/Phone pad, 15W Qi, 90×65mm dish |
| Step 3 (top) | 100mm | 80mm | 15mm | Zone 3 | Watch cradle, Apple puck + Qi watch coil |

- Centre platform body raised on perimeter wall over PSU cavity
- Riser cavity: **20mm clearance** between PSU top and Step 1 base
- All coils are embedded in the step bodies themselves
- Wiring from all coils and watch modules routes down through the riser cavity to the PSU / PCB area
- Total centre column height from base floor: **95mm**

### Zone 1 (Step 1)

- Flat silicone charging surface: **160×100mm**
- Qi TX: **20W**, embedded inside Step 1 body directly under the silicone surface
- Magnetic alignment ring included

### Zone 2 (Step 2)

- Silicone dish: **90×65mm**
- Qi TX: **15W**, embedded inside Step 2 body and centred under the dish
- Slight phone overhang remains acceptable

### Zone 3 (Step 3)

- Apple Watch puck + Qi watch coil embedded inside Step 3 body
- Shared **5W** watch charging budget
- Rear watch presentation preserved despite the PSU move because the step dimensions remain unchanged

---

## Z Height Stack

| Z position | What is here |
|---|---|
| Z=0 | Base plate floor |
| Z=3 | Base plate top / PSU resting surface |
| Z=33 | PSU top (30mm height) |
| Z=50 | Step 1 base (20mm riser cavity above PSU) |
| Z=65 | Step 2 base / Step 1 top |
| Z=80 | Step 3 base / Step 2 top |
| Z=95 | Step 3 top (watch cradle surface) |
| Z=98 | Approximate overall dock height |

---

## PSU Cavity

PSU (**Mean Well LRS-150-24, 159×97×30mm**) sits flat on the base plate under the centre platform. The centre platform perimeter wall creates an enclosed PSU cavity, and the **20mm riser cavity above the PSU** carries all wiring to the coils and logic board.

Fit check:
- PSU width: **159mm < 180mm** centre platform base footprint ✅
- PSU depth: **97mm < 100mm** base footprint ✅
- PSU height: **30mm**, leaving **20mm** wiring cavity before Step 1 base ✅

---

## Rear Spine Plate

- Continuous rear ABS structural panel running the full dock width
- Material: **3mm ABS sheet**, laser cut at Pumping Station One
- Size: **~250mm wide × ~100mm tall**
- Bonded to the rear edges of the laptop slot wall set, centre platform rear, and tablet slot wall set with Weld-On #3 ABS cement
- Carries the **28×20mm right-angle IEC C13 inlet cutout**, centred horizontally
- Together with the base plate, this rear spine forms the primary anti-racking frame of the dock

---

## Front Fascia Strip

- Continuous front ABS panel running the full dock width at the front base
- Material: **3mm ABS sheet**, laser cut at Pumping Station One
- Size: **~250mm wide × 20mm tall**
- Bonded across the front of the laptop slot base, centre platform base, and tablet slot base
- Contains the routed channel for the **250×15mm frosted acrylic LED diffuser strip**
- WS2811 LED strip runs behind the diffuser to create a single unified front light band

---

## Rear Wall Features

- **IEC C13 right-angle inlet:** 28×20mm cutout in the rear spine plate, centred horizontally
- Rear spine doubles as the main rear wiring exit plane
- Rear panel ties the laptop slot, centre platform, and tablet slot into one rigid body

---

## Fastening and Base Features

- 4× rubber feet at the base corners
- M3 screws secure serviceable joins and centre platform mounting points
- Snap-fit locating features used where possible, then reinforced with ABS cement
- Base plate + rear spine provide the primary structural frame
- Silicone-lined slot floors support devices directly; no separate stop shelves

---

## Manufacturing Method

- **3D printed centre platform:** school makerspace printer, ABS only
- **Laser cut ABS panels:** base plate, top panels, laptop slot walls, tablet slot walls, rear spine plate, and front fascia strip at Pumping Station One
- **LED front detail:** frosted acrylic diffuser strip laser cut to match fascia opening
- **Finish:** sand, prep, prime, and matte black finish across the full ABS enclosure
- **Assembly:** dry-fit tabs, bond structural seams with Weld-On #3 ABS cement, then install screws/feet after cure

---

## Batch 1 Enclosure Cost

| Part | Unit cost |
|---|---:|
| 3D printed centre platform | $2.00 |
| Laser cut ABS base plate 250×100mm | $1.35 |
| Laser cut ABS top panels | $1.35 |
| Laser cut ABS laptop slot walls | $7.84 |
| Laser cut ABS tablet slot walls | $5.05 |
| Laser cut ABS rear spine plate 250×100mm | $1.50 |
| Laser cut ABS front fascia strip 250×20mm | $0.70 |
| Frosted acrylic LED diffuser strip 250×15mm | $0.80 |
| Silicone sheet lining | $3.50 |
| Rubber feet + M3 + grommets | $2.60 |
| Cardboard insert + felt liner | $0.70 |
| Laser cutting setup fee amortised | $1.50 |
| ABS cement + finishing consumables | $2.50 |
| **Enclosure total** | **$31.39/unit** |

---

## Materials

| Part | Material | Finish |
|---|---|---|
| Base plate | 3mm ABS sheet | Matte black |
| Top panels | 3mm ABS sheet | Matte black |
| Slot walls | 3mm ABS sheet | Matte black |
| Rear spine plate | 3mm ABS sheet | Matte black |
| Front fascia strip | 3mm ABS sheet | Matte black |
| Centre platform | 3D printed ABS | Matte black |
| Slot and pad lining | Silicone sheet | Dark grey anti-slip |
| LED diffuser | Frosted acrylic | Diffused |
| Feet | Rubber | Matte black |

No aluminium is used anywhere in the Batch 1 enclosure.
