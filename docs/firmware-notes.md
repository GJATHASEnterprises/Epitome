# Epitome Step — Firmware Notes (Digispark ATtiny85)

No ESP32. No BLE. No app. The Digispark-style ATtiny85 board handles LED control, heuristic load behavior, and night mode.

---

## Soft-cap context

The documented product-level claim is **"up to 60W total"**.

Current firmware is still detect-based:
- Zone 1 active estimate: +20W
- Zone 2 active estimate: up to +15W
- Zone 3 active estimate: +5W
- Lighting budget: up to ~1.5W
- USB-C output path is 15W-class, but firmware does not directly measure branch current.

When all zones are active, firmware shifts Zone 2 to a low-power profile. This is a heuristic behavior, not a measured closed-loop power controller.

---

## Watch-zone note

Default generic watch-coil path is not Apple Watch-compatible. Do not claim Apple Watch support in firmware-linked product docs unless MFi hardware is selected.
