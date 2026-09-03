# Epitome Step — Design Brief for CAD / Sketch Artist

**For:** the friend turning our vision into accurate drawings/CAD.
**Products:** Step Walnut ($99, minimalist) and Step Obsidian ($109, gamer RGB). Same body, different materials/lighting.

---

## 1. The vision in one paragraph

A two-tier "stepped" desktop wireless charging stand. Big flat pad on the upper tier for the phone (lying flat, slight tilt OK up to 15°), smaller pad on the lower tier for earbuds. One USB-C input at the rear. Walnut version looks like warm sculpted wood with a single soft white status LED dot. Obsidian version is continuous matte carbon-fiber weave with recessed RGB glow *lines* along both sides (glow, never visible LED dots).

## 2. Overall envelope (target dimensions — adjust ±10% for proportions)

| Dimension | Target |
|---|---|
| Footprint (W × D) | 190 × 100 mm |
| Upper tier height | 22 mm |
| Lower tier height | 12 mm |
| Upper tier (phone) surface | ≥ 95 × 75 mm flat |
| Lower tier (buds) surface | ≥ 55 × 55 mm flat |
| Corner radii | 6–8 mm (soft, premium) |
| Split line | Horizontal, 8 mm above desk — base shell + top shell |

## 3. Hard engineering constraints (non-negotiable)

1. **Wall thickness 2.4 mm** everywhere, EXCEPT directly above each charging coil: **1.2–1.5 mm max** (thicker kills charging).
2. **Coil pockets:** cylindrical recesses under each pad surface, sized from the measured coil module + **0.3 mm clearance** all around. Coil must sit flush against the top surface's underside.
3. **4× M3 heat-set insert bosses** in the base shell (Ø7.2 mm hole for M3 insert, boss Ø10 mm, near corners); matching screw counterbores through the top shell from below — **no visible screws from top or sides**.
4. **Rear USB-C recess:** pocket for the port board so the connector face sits 1 mm recessed from the rear wall; cable strain channel below it.
5. **Thermistor channel:** 3 mm wide groove from the phone coil pocket to the main board bay.
6. **Board standoffs:** 2 mm tall pins/clips for the trigger board and MCU board (dimensions after we measure — see §5).
7. **Walnut only:** Ø3.2 mm light-pipe hole on front face, centered, 8 mm above desk.
8. **Obsidian only:** recessed groove on each side face, 5 mm tall × 3 mm deep × ~140 mm long, positioned 6 mm above desk, to hold an LED strip behind a press-fit diffuser bar (diffuser sits flush or 0.5 mm proud). Wire pass-through from each groove into the base cavity.
9. **4× feet recesses** on the bottom: Ø10 mm × 1 mm deep (for silicone bumpers).
10. Design for FDM printing: no overhangs >50° without a chamfer, flat surfaces face up on the print bed, both shells printable without supports if possible.

## 4. Deliverables we need from you

- Dimensioned drawings (top, front, side, section through both coil pockets) — hand-drawn with real numbers is fine
- If doing CAD: STEP + STL of both shells, per model variant
- Exploded view sketch showing stack order: base → boards → coils → top shell

## 5. Component measurement checklist (WE fill this in before you finalize)

Measure with calipers — do not trust seller datasheets. All in mm.

| Component | Measure | Value |
|---|---|---|
| Phone Qi TX coil | Coil outer Ø, thickness, PCB L×W×H if attached, cable exit position | ___ |
| Buds TX coil | Same | ___ |
| Trigger/boost board | L × W × H, tallest component height, USB-C port overhang, mounting hole positions/Ø | ___ |
| MCU board (ATtiny85 carrier / ESP32-C3) | L × W × H, mounting holes | ___ |
| LED strip (Obsidian) | Width, thickness, LED pitch, cut lengths | ___ |
| Light pipe (Walnut) | Ø, length | ___ |
| Thermistor | Bead Ø, lead length | ___ |
| M3 heat-set insert | OD, length | ___ |
| USB-C cable plug | Overmold W × H (for the rear recess clearance) | ___ |

**Rule: no coil pocket, boss, or standoff gets final dimensions until this table is filled with caliper measurements from the actual parts on our bench.**

## 6. Look & feel references

- Walnut: warm, soft-edged, like a sculpted wooden pebble with steps. Think high-end desk accessory, not gadget.
- Obsidian: sharp but not aggressive; continuous CF weave; when RGB is on, two clean underglow-style light lines; when off, it should look completely minimal.
- Nothing on the top surfaces except the device pads (subtle 0.4 mm raised locating ring around each pad zone is welcome).
