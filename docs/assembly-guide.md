# Epitome Step — Beginner Assembly Guide (No-Solder)

This scaffold is for a first-time builder. The target build method is plug-in JST and screw-terminal only.

## Tools

- Small screwdriver
- Wire stripper
- Multimeter
- Heat gun *(for solder-seal fallback + heat-set insert work)*
- Thermal epoxy

## Before you start

- **Unit #1 is a learning unit.** Photograph every step, every wire label, and every finished subassembly.
- Fold those photos back into this guide after the first build so Units #2–#6 become paint-by-numbers.
- Read `docs/wiring.md` first and keep it open next to the bench.

## Ordered build steps

1. **Print the shells**
   - Print the current Step base and top shells for the target model.
   - Dry-fit the shells and confirm the cable exits and insert bosses are clean before electronics go in.

2. **Install heat-set inserts**
   - Practice on scrap first.
   - Install the M3 inserts square to the bosses and let the plastic cool fully before test-threading screws.

3. **Mount the power hardware**
   - Install the panel-mount USB-C input receptacle and the PD input trigger board.
   - Install the screw-terminal 20V distribution block / PCB.
   - Install both screw-terminal buck converters.
   - Leave the module outputs disconnected from the loads for now.

4. **HARD GATE — set and verify buck outputs before connecting any module**
   - Power only the USB-C input receptacle + PD input trigger board + distribution block + buck converters.
   - Confirm the PD input trigger is negotiating the intended input rail before landing any load wiring.
   - Use the multimeter to set the 12V buck to **12.0V ±0.1V**.
   - Use the multimeter to set the 5V buck to **5.0V ±0.1V**.
   - **Do not connect the Qi boards, the Digispark, or the LEDs until both outputs are verified.**

5. **Connect modules via JST per `docs/wiring.md` J1–J10**
   - Plug in the pre-crimped JST-XH pigtails for J1–J10.
   - Keep the polyfuses in-line exactly as shown in the wiring guide.
   - Use the factory JST-SM LED leads; do not solder LED pads.

6. **Polarity checklist for every screw terminal**
   - Red = **+**
   - Black = **GND**
   - Label each terminal pair with a paint pen before landing the wire.
   - Tug-test every wire after tightening.

7. **Install the Digispark-style ATtiny85 board**
   - Flash over USB in the Arduino IDE.
   - Build the correct firmware target before install:
     - `MODEL_WALNUT`
     - `MODEL_OBSIDIAN`
   - After flashing, mount the board and connect J4/J6/J7/J8/J9/J10 as applicable.

8. **Smoke test with no devices on the charger**
   - Power the unit.
   - Confirm there is no unexpected heat, smell, or flicker.
   - Confirm the expected idle light behavior for the model.

9. **Zone-by-zone charge test**
   - Test Zone 1 alone.
   - Test Zone 2 alone.
   - Test Zone 3 alone.
   - Then test combined wireless use before trying any USB-C output load.

10. **Thermal check**
    - Run a 15-minute phone charge on Zone 1 and confirm charging stays stable for the full test (no repeated dropouts).
    - Remove the phone, then **disconnect input power** before setting up the cutoff test.
    - Identify the chosen Qi TX board family's observable thermal-cutoff indicator for Batch 1 documentation: onboard status/fault LED, documented fault pin, or the exposed Zone 1 status lead if that board family uses it for cutoff state.
    - Re-apply input power with **no device charging**, set the heat gun to low, hold it roughly **15–20 cm (6–8 in)** away, and warm the NTC bead in **2–3 second sweeps** until the documented indicator flips to the thermal-cutoff state. Stop heating immediately, allow cooldown, and confirm the same indicator returns to its normal ready state.
    - Acceptance rule: **the 15-minute charging run must stay stable, and the documented board-family cutoff indicator must show both cutoff and recovery during the warm-up test.** Record which indicator was used for the unit log.

11. **Final assembly**
    - Dress the service loops.
    - Close the shell.
    - Install feet / bumpons.
    - Re-run a short final power-on check after the enclosure is closed.

## Fallback note

If a wire join is unavoidable, use a **solder-seal wire connector** and a heat gun rather than freehand soldering.

## Per-unit QA sign-off

| Unit | Model | 12V buck verified | 5V buck verified | J1–J10 polarity checked | USB flash OK | Smoke test OK | Zone 1 | Zone 2 | Zone 3 | Thermal check OK | Final closeout |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |  |  |  |  |  |
| 3 |  |  |  |  |  |  |  |  |  |  |  |
| 4 |  |  |  |  |  |  |  |  |  |  |  |
| 5 |  |  |  |  |  |  |  |  |  |  |  |
| 6 |  |  |  |  |  |  |  |  |  |  |  |
