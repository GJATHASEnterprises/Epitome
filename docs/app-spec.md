# Epitome Step — Future Features (Batch 2+)

**No app in Batch 1.** The ATtiny85 in Batch 1 handles everything locally. No BLE, no Wi-Fi, no app.

This document captures ideas for future batches. Nothing here is on the roadmap yet.

---

## Why no app in Batch 1

1. **Complexity kills Batch 1.** Adding app connectivity (ESP32, BLE pairing, iOS app) would double the electronics cost and triple the firmware work. Not justified for 10 units.
2. **Most users don't want an app for a charger.** Plug in and charge. The simpler it is, the better the product.
3. **The ATtiny85 is sufficient.** LED control, night mode, soft cap — all done without any wireless.

---

## Future ideas — Obsidian RGB app control

If there's demand for it, the Obsidian model could add a BLE module (ESP32-C3 or nRF52840) to allow app-based colour control:

- Choose any colour, not just the 8 presets
- Schedule night mode to actual clock time
- Per-zone LED brightness (e.g. dim Zone 2 if no buds detected)
- RGB mode sync with music (requires phone microphone access — complicated)

This would require replacing the ATtiny85 with a more capable MCU and adding a BLE antenna. Estimated additional cost: $4–6 per unit.

---

## Future ideas — zone scheduling

- Set specific zones to turn on/off at set times (e.g., disable Zone 1 phone charging after midnight)
- Use BLE-synced real-time clock instead of ATtiny85 timer

---

## Future ideas — zone toggles

- Physical or app-controlled toggle to disable a zone
- Useful for power management if user only has phone + watch (disable Zone 2)

---

## What to do before building any of this

1. Finish Batch 1 and ship it
2. Ask customers if they want an app
3. If > 50% say yes, prototype a BLE version for Batch 3
4. Keep Walnut as app-free — the Walnut buyer does not want an app for their charger

---

## What is explicitly NOT planned

- Voice control (Alexa/Google — unnecessary complexity)
- USB data transfer (charging only — USB-C ports are power-only PD)
- Display / screen on dock (adds cost, adds failure mode)
- Battery / UPS mode (too complex, too expensive)
- Laptop Qi charging (not in Qi/Qi2 spec at useful wattage)

