# Epitome Step — Prototype Guide (Batch 1)

Build plan: 10 units total. Suggested split: 5 Walnut + 5 Obsidian.

---

## Before you start

- Order all parts at least 2 weeks before build sessions
- Confirm school makerspace bookings: 3D printers, laser cutter, spray booth
- Program all 10 ATtiny85 chips before the build weekend (5 Walnut, 5 Obsidian)
- Pre-cut all silicone pads

---

## 3D print settings

| Parameter | Value |
|---|---|
| Material | ABS (preferred) or PETG (acceptable) |
| Layer height | 0.2 mm |
| Infill | 40% cubic |
| Perimeters | 3 (min 1.2 mm wall) |
| Supports | None needed (design is support-free) |
| Bed adhesion | ABS: brim + ABS slurry or enclosure; PETG: brim only |
| Print temperature | ABS: 240°C nozzle / 100°C bed; PETG: 230°C / 80°C |
| Print time | ~4 h per unit (base + riser as one print) |
| Quantity | Print 10 × base+riser sets |

**Tip:** Print two sets at a time on a Bambu P1P or similar. Don't overcrowd — 2 per plate max for ABS warping prevention.

### Post-processing of 3D prints
1. Remove brim with flush cutters
2. Light sand exterior (220 grit) to remove layer lines on visible faces
3. Install M3 heat-set inserts (×4 per unit, side walls) using soldering iron at 200°C
4. Test fit rear spine and step face panels before electronics assembly

---

## Laser cut settings

### Walnut (4 mm)
- Power: 75%, Speed: 15 mm/s, Passes: 2
- Test cut first on scrap — walnut density varies
- Cut grain horizontal on step faces

### ABS (4 mm, black)
- Power: 65%, Speed: 20 mm/s, Passes: 2
- Ventilate the laser room — ABS fumes are acrid
- ABS rear spines: Power 60%, Speed: 25 mm/s

### Cut quantity per 10-unit batch
| Part | Qty |
|---|---|
| Walnut step face sets (3 faces each) | 5 sets = 15 pieces |
| Walnut top surface sets (3 each) | 5 sets = 15 pieces |
| ABS step face sets (Obsidian) | 5 sets = 15 pieces |
| ABS top surface sets (Obsidian) | 5 sets = 15 pieces |
| ABS rear spine 165×35 mm | 10 pieces |

---

## Walnut vs ABS cut differences

| Parameter | Walnut | ABS |
|---|---|---|
| Edge burn | Some charring — sand away | Slight melt — clean with IPA |
| Kerf | ~0.2 mm wider than ABS | ~0.1 mm |
| Smell | Woody, pleasant | Chemical — ventilate well |
| Warp | Minimal | Can warp if overheated — reduce power |
| Edge quality | Fibrous — sand smooth | Slightly glossy — lightly abrade |

---

## Electronics assembly order

Do one complete unit before doing all 10. Verify the first unit fully before batch.

**Per unit:**
1. Mount 12V buck and 5V buck flat in riser cavity — adhesive foam tape
2. Mount USB-C PD boards (Port A, Port B) — align to rear cutouts
3. Mount Zone 3 relay board
4. Install ATtiny85 in DIP socket (Walnut binary or Obsidian binary — confirm before inserting)
5. Solder polyfuses in-line on each zone feed (pre-solder, then install with JST)
6. Thread wiring through riser — power first (22 AWG), then signal (26 AWG)
7. Connect barrel jack to power rail
8. Install LED strip in diffuser slot — LED strip adhesive + diffuser friction-fit
9. Connect JST J5 (LED strip power) and J6 (DATA line) to ATtiny85
10. **Obsidian only:** install rear button PCB in rear spine slot, connect J10

---

## Per-zone testing checklist

Test each zone individually before full assembly. Use a benchtop PSU at 12V, 3A.

### Zone 1 — Phone
- [ ] Qi2 TX powers on (LED on module, if present)
- [ ] Phone snaps to pad magnetically
- [ ] Phone shows charging icon
- [ ] NTC thermistor measures room temp (~25°C) on ATtiny84 ADC (or multimeter)

### Zone 2 — Buds
- [ ] Qi 5W TX powers on
- [ ] Buds case charges when placed on pad
- [ ] ATtiny85 PB2 goes HIGH when buds detected

### Zone 3 — Watch
- [ ] Relay board switches correctly (test with continuity meter)
- [ ] Apple Watch charges via PCBA
- [ ] Qi watch coil charges a Qi watch (if available for testing)

### USB-C Ports
- [ ] Port A negotiates 60W with a compatible device (phone or laptop)
- [ ] Port B negotiates 30W
- [ ] TVS diodes not shorted (continuity — should not conduct in either direction at low voltage)

### LED strip
- [ ] All 8 LEDs light on first power-on
- [ ] Walnut: warm white colour correct (#FFD6A0)
- [ ] Obsidian: button cycles through all 8 modes
- [ ] Night mode activates after simulated 11-hour timer (test by advancing counter in firmware)

---

## Common mistakes

| Mistake | Symptom | Fix |
|---|---|---|
| Wrong ATtiny85 binary | Walnut unit has RGB modes / Obsidian is stuck warm white | Re-flash correct binary |
| JST connector reversed | Zone doesn't charge, or ATtiny85 detects wrong state | Check polarity — red = positive |
| LED strip orientation wrong | First LED is at wrong end of strip | Flip strip (DATA must flow from DIN end) |
| NTC not secured to coil | Thermal cutoff triggers falsely at room temp | Re-glue with thermal epoxy |
| ABS warp in 3D print | Step face gap, misalignment | Reprint with enclosure or increased bed temp |
| Rubio Monocoat pooling | Sticky walnut face, dark patches | Wipe more aggressively during application; re-oil if severe |
| Relay not switching | Watch charges from wrong coil | Check relay control wire from ATtiny85 PB3 |
| Heat-set insert crooked | M3 screw won't thread | Re-heat with iron and straighten before fully cool |

---

## Build timeline (Batch 1, single weekend)

| Session | Duration | Tasks |
|---|---|---|
| Friday evening | 2 h | Set up tools, label all parts, pre-tin ATtiny85 JST wires |
| Saturday morning | 4 h | 3D print runs (set and monitor), laser cut all panels |
| Saturday afternoon | 4 h | Electronics assembly for all 10 units |
| Saturday evening | 2 h | Per-zone testing, fix issues |
| Sunday morning | 3 h | Walnut finishing (oil, cure) / Obsidian spray finishing |
| Sunday afternoon | 2 h | Final assembly, Bumpons, rear spine, final QC |
| Sunday evening | 1 h | Photography, pack into boxes, label |

Total: ~18 h across a weekend, 2 people.

