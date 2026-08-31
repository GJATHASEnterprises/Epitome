# Step — Prototype Build Guide (Batch 1, 10 Units)

School makerspace build guide.

---

## Materials List

### Per Unit
- ABS filament (matte black): ~180g
- Walnut sheet 4mm: ~600cm²
- Silicone sheet 1mm: ~500cm²
- Frosted acrylic 2mm: 130×10mm strip
- Electronics (see BOM)
- Fasteners: M3 screws ×8, M3 heat-set inserts ×8
- Wood glue
- Rubio Monocoat oil (shared between units)

### For Batch (10 units, ordered once)
- 1.8kg ABS filament
- 6000cm² walnut sheet (order extra for waste)
- 5000cm² silicone sheet
- 1300×100mm frosted acrylic strip (cut per unit)
- Rubber feet (3M Bumpons ×40)
- Sandpaper 120, 180, 220 grit

---

## Step 1: 3D Print ABS Base

### Print Settings
- Slicer: PrusaSlicer or Cura
- Material: ABS
- Layer height: 0.2mm
- Infill: 30% gyroid
- Perimeters: 3 shells
- Bed temp: 90°C
- Nozzle temp: 240°C
- Enclosure: required (ABS warps without it)
- Support: yes on overhangs >45°
- Estimated print time: ~4 hours per unit

### Print Notes
- Print base/riser as one part
- Do not print walnut faces — these are laser cut separately
- Check all wall thicknesses ≥3mm, especially at Step 3 lateral ribs
- Acetone-smooth after print for matte surface

---

## Step 2: Laser Cut Walnut (Pumping Station One)

### Walnut Laser Settings (4mm walnut)
- Speed: 15mm/s
- Power: 80%
- Passes: 2–3 (test on scrap first)
- Air assist: on
- Focus: set for 4mm material

### Parts to Cut
Per unit:
- Step 1 face: 165×15mm
- Step 2 face: 130×15mm
- Step 3 face: 95×15mm
- Step 1 top: 165×100mm (with pad recess cutout)
- Step 2 top: 130×100mm (with pad recess cutout)
- Step 3 top: 95×80mm (with pad recess cutout)

Per unit (ABS rear spine):
- Rear spine: 165×35mm with port cutouts (DC jack, USB-C ×2)

### Laser Notes
- Always do test cut on offcut first
- Walnut grain should run along the long axis of each piece
- Clean laser bed before walnut cuts to prevent scorching
- Wipe cut edges with damp cloth before finishing

---

## Step 3: Walnut Finishing

1. Sand all walnut pieces: 120 → 180 → 220 grit, with grain
2. Blow dust off with compressed air, wipe with tack cloth
3. Apply Rubio Monocoat oil with lint-free cloth — very thin coat
4. Work into grain, wipe off all excess within 3 minutes
5. Buff dry with clean cloth
6. Allow 1 hour minimum cure before assembly
7. Do not get oil on mating/glue surfaces

---

## Step 4: Electronics Assembly

Assembly order:
1. Solder polyfuses and TVS diodes to PD boards
2. Install heat-set inserts into ABS riser base (soldering iron method)
3. Mount 12V buck converter in riser cavity (flat-mount, hot glue or M3)
4. Mount 5V buck converter next to 12V buck
5. Mount ATtiny85 board in riser cavity
6. Install USB-C PD 60W board and 30W board near rear spine
7. Install hardware relay (Zone 3)
8. Route wiring using JST connectors per wiring guide
9. Feed Zone 3 wiring up through Zone 2 step before mounting Step 3 electronics
10. Mount Qi2 TX board under Step 1 top surface
11. Mount Qi 5W TX board under Step 2 top surface
12. Mount Apple Watch puck PCBA + Qi coil under Step 3 top surface
13. Install WS2811 LED strip behind frosted acrylic diffuser slot
14. Connect LED strip to ATtiny85

### Flat-Mount Rule
All boards in the riser cavity must be flat. Maximum height: 22mm. Check every component before closing the cavity.

### Step 3 Wall Thickness Note
Verify the ABS ribs at X=35 and X=130 are ≥3mm. These support Step 3 laterally. If thinner, do not proceed — reprint that unit.

---

## Step 5: Testing Checklist (per unit)

Run all tests before assembly of walnut faces.

### Power-on test
- [ ] Connect 65W brick + barrel cable
- [ ] No smoke, sparks, or excessive heat
- [ ] LED strip illuminates on power-on sequence

### Zone 1 — Phone
- [ ] Place Qi2 phone on Zone 1 pad
- [ ] Phone charges (verify on phone screen)
- [ ] Zone 1 LED (blue) illuminates
- [ ] Remove phone — LED extinguishes

### Zone 2 — Buds
- [ ] Place AirPods case on Zone 2 pad
- [ ] Case charges
- [ ] Zone 2 LED (purple) illuminates

### Zone 3 — Watch (Apple Watch)
- [ ] Place Apple Watch on Zone 3 cradle
- [ ] Watch charges
- [ ] Zone 3 LED (green) illuminates
- [ ] Relay switches to Apple Watch puck mode

### Zone 3 — Watch (Qi)
- [ ] Place Qi-compatible watch on Zone 3
- [ ] Watch charges via Qi coil
- [ ] Relay mutual exclusion: only one coil active at a time

### USB-C Port A
- [ ] Connect USB-C device to Port A
- [ ] Device charges at 60W (verify with USB meter)
- [ ] Port A LED (orange) illuminates

### USB-C Port B
- [ ] Connect USB-C device to Port B
- [ ] Device charges at 30W (verify with USB meter)
- [ ] Port B LED (teal) illuminates

### Soft cap test
- [ ] Load all zones simultaneously
- [ ] Monitor total draw — verify ATtiny85 caps at 60W by disabling low-priority zones

---

## Step 6: Final Assembly

1. Glue walnut top surfaces onto step tops with wood glue + M3 screws from inside
2. Press silicone charging pads into recesses
3. Attach walnut step faces
4. Install frosted acrylic LED diffuser in front slot
5. Attach rear ABS spine with port cutouts aligned to PD boards
6. Close base plate with M3 screws
7. Apply 3M Bumpons to base corners
8. Final visual inspection

---

## Packaging

1. Place unit in foam insert
2. Place in rigid matte black box
3. Include: 65W USB-C brick + USB-C to barrel cable (1m)
4. Include: setup card + belly band
5. Box closed and banded
