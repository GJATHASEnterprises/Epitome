# Epitome Step — Enclosure Specification

---

## Shared base and riser — 3D print spec

The base plate and riser/wiring cavity are identical across both models.

| Parameter | Value |
|---|---|
| Material | ABS (not PLA — dimensional stability needed) |
| Infill | 40% |
| Wall perimeters | 3 (minimum 1.2 mm wall thickness) |
| Layer height | 0.2 mm |
| Colour | Matte black filament |
| Printer | School FDM printer (Bambu, Prusa, or equivalent) |
| Print time estimate | ~4 h per unit |
| Post-processing | Light sanding (220 grit), no paint needed (already matte black) |

### Base plate (Z = 0 to Z = 3)
- 165 × 100 × 3 mm
- Four 3M Bumpon recesses in corners (underside)
- Single cable channel at rear (X = 0 to X = 165, Z = 3)

### Riser / wiring cavity (Z = 3 to Z = 25)
- Internal cavity: 159 × 94 × 18 mm (6 mm wall all sides)
- All boards flat-mounted, max component height 18 mm
- Rear wall has three cutouts: barrel jack X = 40, USB-C A X = 120, USB-C B X = 140
- Front face of riser: 130 × 10 mm slot for frosted acrylic LED diffuser (Z = 26 to Z = 36)
- Two M3 heat-set inserts per side for step face attachment

---

## Step 1 — Phone (Z = 25 to Z = 40)

- 165 × 100 × 15 mm outer dimensions
- Top surface: 75 × 90 mm silicone pad recess, 1 mm deep, centred
- Qi2 coil pocket: 60 × 60 mm, 8 mm deep, beneath pad recess
- Wire chase through riser via JST connector
- **Walnut:** walnut face + top panels, ABS internal block
- **Obsidian:** ABS face + top panels

---

## Step 2 — Buds (Z = 40 to Z = 55)

- 130 × 100 × 15 mm outer
- Centred at X = 82.5 (X = 17.5 to X = 147.5)
- Top surface: 65 × 50 mm silicone pad, no recess
- Qi 5W coil pocket, 6 mm deep

---

## Step 3 — Watch (Z = 55 to Z = 70)

- 95 × 80 × 15 mm outer
- Centred at X = 82.5 (X = 35 to X = 130), Y = 20 to Y = 100
- **Minimum 3 mm wall thickness on front face** (above Step 2 level) for lateral support
- Top surface: 55 × 55 mm watch cradle with raised 3 mm lip
- Apple Watch puck pocket + Qi watch coil pocket side-by-side (relay selects active coil)
- Set-back 20 mm from front provides structural shelf and conceals wiring

---

## Walnut model — step face spec

### Material
- Sheet: 4 mm Baltic birch plywood or walnut veneer MDF, min 4 mm
- Preferred: solid walnut 4 mm sheet (Woodcraft / school laser)
- Grain direction: horizontal (grain runs left-right)

### Laser cut settings (walnut)
- Power: 70–80% (vary by laser — test cut first)
- Speed: 15 mm/s
- Passes: 2–3 until clean cut
- Kerf allowance: 0.1 mm

### Finishing — Rubio Monocoat
1. Sand all faces to 180 grit, then 220 grit (with grain)
2. Wipe clean, no dust
3. Apply thin coat of Rubio Monocoat Pure with lint-free cloth
4. Work into grain, remove excess immediately — do not let pool
5. Cure 1 hour at room temperature (20°C+)
6. Buff lightly with clean cloth
7. Do not apply second coat — single coat saturates walnut fully
8. Curing fully hardens in 24 hours; handle carefully during first hour

### Edge profile — Walnut
- Front face of each step: **hand-sand to soft radius**, ~1.5 mm radius
- Rear and side edges: 0.5 mm break (single sanding pass)
- Top surface edges: soft radius 1 mm

---

## Obsidian model — step face spec

### Material
- Sheet: 4 mm matte black ABS sheet
- Same dimensions as walnut faces

### Laser cut settings (ABS)
- Power: 60–70%
- Speed: 20 mm/s
- Passes: 1–2
- **Ventilate well** — ABS fumes are irritating
- Kerf allowance: 0.1 mm

### Finishing — matte black paint
1. Light sanding of cut edges with 320 grit
2. Wipe clean, isopropyl alcohol wipe
3. Light primer coat (grey sandable primer)
4. Cure 30 minutes
5. Matte black spray coat (Rust-Oleum 2X matte or equivalent)
6. Cure 1 hour
7. Optional: second coat for even coverage
8. Final cure 24 hours before assembly

### Edge profile — Obsidian
- All edges: **sharp angular, no rounding**
- Single light deburr pass to remove laser slag only
- Target: industrial, crisp, precise look

---

## LED diffuser mounting

- Frosted acrylic: 130 × 10 × 3 mm
- Friction-fit into riser front face slot
- LED strip sits behind diffuser on rear face of slot, adhesive-backed
- Diffuser face flush with riser front face

---

## Rear spine

- Material: laser-cut ABS, 165 × 35 × 3 mm
- Covers rear face of riser from Z = 3 to Z = 38
- Three cutouts: barrel jack (X = 35–45), USB-C A (X = 116–126), USB-C B (X = 136–146)
- Friction-fit + 2× M3 screws

---

## Assembly order

1. Install heat-set inserts (M3) in riser side walls — soldering iron at 200°C
2. Flat-mount all electronics boards in riser cavity, cable-tie bundles
3. Snap LED strip into diffuser slot, connect JST to ATtiny85
4. Press-fit rear spine, route cables through cutouts
5. Attach Step 1 block — lower walnut/ABS face, screw M3, add silicone pad
6. Attach Step 2 — same
7. Attach Step 3 — same, ensure relay JST seated
8. Place Bumpons in base underside recesses
9. Final check: all JST connectors seated, no pinched wires

### Assembly differences per model

| Step | Walnut | Obsidian |
|---|---|---|
| Step faces | Glue pre-oiled walnut panels to ABS block, clamp 30 min | Snap pre-painted ABS panels onto ABS block |
| Edge profile | Confirm radius before gluing | Confirm sharp edges before attaching |
| Button | Not installed | Install rear tactile button PCB in rear spine slot |
| LED strip | WS2811 warm white | WS2812B RGB |

