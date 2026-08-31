# Step — Enclosure Specification

---

## Overview

The enclosure consists of a 3D printed matte black ABS structural base/riser and laser-cut walnut faces and top surfaces for each of the three steps. The stepped geometry is the defining visual feature of the product.

---

## 3D Printed ABS Base / Riser

- **Material:** ABS (matte black)
- **Print method:** FDM at school makerspace
- **Dimensions:** 165mm wide × 100mm deep × 25mm tall (base plate Z=0–3 + riser cavity Z=3–25)
- **Riser cavity:** 165 × 100 × 22mm internal void (Z=3 to Z=25) — houses all wiring and PCBs
- **Clearance:** 22mm maximum component height in riser; flat-mount all boards
- **Wall thickness:** ≥3mm all external walls; ≥3mm internal ribs
- **Finish:** Sanded to 220 grit, acetone-smoothed for matte texture

### Print Settings (ABS)
- Layer height: 0.2mm
- Infill: 30% gyroid
- Perimeters: 3 shells
- Bed: 90°C, enclosure required
- Nozzle: 240°C
- Support: Yes on overhang areas

---

## Walnut Step Faces

- **Material:** Walnut, 4mm nominal thickness
- **Cut method:** Laser cut (Pumping Station One)
- **Pieces:** ×3 step front faces
  - Step 1 face: 165mm wide × 15mm tall
  - Step 2 face: 130mm wide × 15mm tall
  - Step 3 face: 95mm wide × 15mm tall
- **Finish:** Rubio Monocoat — thin coat, buffed, 1hr cure minimum

---

## Walnut Step Top Surfaces

- **Material:** Walnut, 4mm nominal thickness
- **Cut method:** Laser cut (Pumping Station One)
- **Pieces:** ×3 step tops
  - Step 1 top: 165mm wide × 100mm deep (full step top)
  - Step 2 top: 130mm wide × 100mm deep
  - Step 3 top: 95mm wide × 80mm deep (setback piece)
- **Cutouts:** Silicone charging pad recesses on each top
- **Finish:** Rubio Monocoat — thin coat, buffed, 1hr cure minimum

---

## Step Geometry

```
Step 1 (bottom): 165mm wide × 100mm deep × 15mm tall  (top surface Z=40)
Step 2 (middle): 130mm wide × 100mm deep × 15mm tall  (top surface Z=55)
Step 3 (top):     95mm wide ×  80mm deep × 15mm tall  (top surface Z=70)
```

Step widths centred at X=82.5:
- Step 1: X=0 to X=165
- Step 2: X=17.5 to X=147.5
- Step 3: X=35 to X=130

Step 3 is set back 20mm from the front: Y=20 to Y=100. This exposes the front face of Step 2 and creates the staircase visual.

### Step 3 Lateral Support Note

Step 3 is narrower (95mm) and elevated (Z=70). The internal ABS rib supporting Step 3 must be ≥3mm wall thickness to prevent flex under watch cradle load. Add vertical ribs at X=35 and X=130 in the ABS print.

---

## Riser Cavity

- **Dimensions:** 165 × 100 × 22mm (Z=3 to Z=25)
- **Purpose:** Houses all PCBs, wiring, JST connectors, and buck converters
- **Rule:** All components must be flat-mounted (no upright components over 22mm tall)
- **Access:** Removable base plate secured with M3 heat-set inserts ×4

---

## Rear Spine

- **Material:** Laser cut ABS, 165×35mm
- **Cutouts:** DC barrel jack (X=40), USB-C Port A (X=120), USB-C Port B (X=140)
- **Port positions (all at Z=15):**
  - DC barrel jack: X=40, Y=100, Z=15
  - USB-C Port A: X=120, Y=100, Z=15
  - USB-C Port B: X=140, Y=100, Z=15

---

## LED Diffuser

- **Material:** Frosted acrylic, 130mm × 10mm × 2mm
- **Position:** Front face of Step 1 riser, 130mm wide × 8mm tall slot
- **Purpose:** Diffuses WS2811 LED strip glow across front fascia

---

## Silicone Pads

- **Material:** 1mm silicone sheet, ~500cm² total
- **Pieces:**
  - Zone 1: 75×90mm portrait pad with 1mm recess on Step 1 top
  - Zone 2: 65×50mm pad on Step 2 top
  - Zone 3: 55×55mm cradle on Step 3 top

---

## Feet

- 3M Bumpons ×4, placed at corners of base plate underside

---

## Fasteners

- M3 screws + heat-set inserts for base plate removal and rear spine attachment

---

## Walnut Finishing Instructions

1. Sand walnut pieces to 220 grit along grain direction
2. Wipe clean with tack cloth
3. Apply thin coat of Rubio Monocoat oil with lint-free cloth — use less than you think you need
4. Work into grain, wipe off excess within 3 minutes
5. Buff with clean cloth until no residue
6. Allow 1 hour minimum cure before assembly
7. Do not apply heat or water for 24 hours after finishing

---

## Assembly Notes

1. Press heat-set inserts into ABS riser with soldering iron
2. Mount all PCBs and wiring in riser cavity (flat-mount, max 22mm height)
3. Route cables through internal channels before closing
4. Attach walnut faces to step fronts with a thin bead of wood glue and M3 screws from inside
5. Install LED diffuser strip in front fascia slot
6. Attach rear spine with M3 screws — verify port alignment before tightening
7. Apply feet to base corners
8. Final test all zones before boxing
