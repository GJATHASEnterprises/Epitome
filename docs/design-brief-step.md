# Epitome Step — Design Brief for CAD / Sketch Artist

**For:** the friend turning our vision into accurate drawings/CAD.
**Products:** Step Walnut ($99, minimalist) and Step Obsidian ($109, gamer RGB). Same body, different materials/lighting.

---

## 1. The vision in one paragraph

A three-tier "stepped" desktop wireless charging stand with dedicated zones for phone, earbuds, and watch. The footprint target is 165 × 100 mm, with the exact exterior shape still TBD by the owner; proportions may adjust within ±10% so long as the structure stays clearly three-tier and the internal engineering rules below are preserved. Walnut should read like a warm sculpted wood desk object with a single soft white status LED through a front light pipe. Obsidian should read as continuous matte carbon-fiber with recessed RGB glow *lines* along both sides (glow only, never visible LED dots).

## 2. Overall envelope (target dimensions — adjust ±10% for proportions; exact exterior shape TBD)

| Dimension | Target |
|---|---|
| Footprint (W × D) | 165 × 100 mm |
| Base shell thickness | 3 mm |
| Riser height above base | 22 mm |
| Step 1 height | 15 mm |
| Step 2 height | 15 mm |
| Step 3 height | 15 mm |
| Total height | 70 mm |
| Step 1 / Zone 1 | Phone, Qi2 20W |
| Step 2 / Zone 2 | Earbuds, Qi 5W |
| Step 3 / Zone 3 | Watch, 5W |
| Step 3 setback | 20 mm in Y from the front edge of Steps 1–2 |
| Corner radii | 6–8 mm (soft, premium) |
| Split line | Horizontal, 8 mm above desk — base shell + top shell |

## 3. Hard engineering constraints (non-negotiable)

1. **Wall thickness 2.4 mm** everywhere, EXCEPT directly above each charging coil: **1.2–1.5 mm max** (thicker kills charging).
2. **Coil pockets:** cylindrical recesses under each pad surface, sized from the measured phone coil, earbuds coil, and watch coil modules + **0.3 mm clearance** all around. Each coil must sit flush against the underside of its charging surface.
3. **4× M3 heat-set insert bosses** in the base shell (Ø7.2 mm hole for M3 insert, boss Ø10 mm, near corners); matching screw counterbores through the top shell from below — **no visible screws from top or sides**.
4. **Rear USB-C recess:** pocket for the port board so the connector face sits 1 mm recessed from the rear wall; cable strain channel below it.
5. **Thermistor channel:** 3 mm wide groove from the phone coil pocket to the main board bay.
6. **Board standoffs:** 2 mm tall pins/clips for the trigger board and MCU board (dimensions after we measure — see §5).
7. **Walnut only:** Ø3.2 mm light-pipe hole on the front face, centered, **12 mm above desk**, fully owned by the **top shell** so it does not sit on the 8 mm split line.
8. **Obsidian only:** recessed groove on each side face, 5 mm tall × 3 mm deep × ~140 mm long, positioned 6 mm above desk, to hold a press-fit diffuser bar over a **60 LED/m WS2812B strip**. Size the groove for **8 LEDs per side (16 total)** with an approximate **133 mm cut length per side** plus wire relief; diffuser sits flush or up to 0.5 mm proud. Wire pass-through from each groove into the base cavity.
9. **Hidden venting:** add concealed vent slots in the base shell for coil thermal relief, but keep them invisible from normal top/side views.
10. **Optional ballast:** include a base-shell cavity / steel plate pocket option for anti-slip heft without changing the exterior silhouette.
11. **4× feet recesses** on the bottom: Ø10 mm × 1 mm deep (for silicone bumpers).
12. **Shared board bay:** Walnut uses an **ATtiny85 carrier board**; Obsidian uses an **ESP32-C3 dev/carrier board**. The shared enclosure geometry must fit the **larger** measured board footprint/height from §5.
13. Design for FDM printing: no overhangs >50° without a chamfer, flat surfaces face up on the print bed, both shells printable without supports if possible.

## 4. Deliverables we need from you

- Dimensioned drawings (top, front, side, section through all three coil pockets) — hand-drawn with real numbers is fine
- If doing CAD: STEP + STL of both shells, per model variant
- Exploded view sketch showing stack order: base → boards → coils → top shell

## 5. Component measurement checklist (WE fill this in before you finalize)

Measure with calipers — do not trust seller datasheets. All in mm.

| Component | Measure | Value |
|---|---|---|
| Phone Qi TX coil | Coil outer Ø, thickness, PCB L×W×H if attached, cable exit position | ___ |
| Buds TX coil | Same | ___ |
| Watch TX coil | Same + cradle / magnet carrier dimensions if separate | ___ |
| Trigger/boost board | L × W × H, tallest component height, USB-C port overhang, mounting hole positions/Ø | ___ |
| ATtiny85 carrier board (Walnut) | L × W × H, mounting holes | ___ |
| ESP32-C3 dev/carrier board (Obsidian) | L × W × H, mounting holes | ___ |
| LED strip (Obsidian) | Width, thickness, LED pitch, cut lengths | ___ |
| Light pipe (Walnut) | Ø, length | ___ |
| Thermistor | Bead Ø, lead length | ___ |
| M3 heat-set insert | OD, length | ___ |
| USB-C cable plug | Overmold W × H + cable exit angle / bend relief (for the rear recess clearance) | ___ |
| 65W GaN brick + attached cable exit | Brick L × W × H, cable-exit face, overmold clearance, bend relief envelope | ___ |

**Rule: no coil pocket, boss, standoff, or shared board-bay dimension gets finalized until this table is filled with caliper measurements from the actual parts on our bench.**

## 6. Look & feel references

- Walnut: warm, soft-edged, like a sculpted wooden pebble with steps. Think high-end desk accessory, not gadget.
- Obsidian: sharp but not aggressive; continuous CF weave; when RGB is on, two clean underglow-style light lines; when off, it should look completely minimal.
- Nothing on the top surfaces except the device pads (subtle 0.4 mm raised locating ring around each pad zone is welcome).
