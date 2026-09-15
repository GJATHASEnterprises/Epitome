# Epitome Step — Firmware Notes (Digispark ATtiny85)

No ESP32. No BLE. No app. The Digispark-style ATtiny85 board handles LED control, the 60W soft power cap, and night mode only.

See `firmware/led_controller.h` and `firmware/led_controller.cpp` for full implementation.

---

## Compile-time model selection

```cpp
// Select model at compile time — uncomment one line only
#define MODEL_WALNUT
// #define MODEL_OBSIDIAN
```

Flash two separate binaries: one for Walnut units, one for Obsidian units.

---

## Walnut model behaviour

- **LED type:** single white status LED via light pipe
- **Colour:** Warm white only — #FFD6A0 (R=255, G=214, B=160), fixed, cannot be changed
- **Brightness:** Full brightness during daytime; off during night mode
- **Zone indicators:** When a device is detected on any zone, LEDs pulse once (brief 200 ms brightening) then return to steady on
- **Night mode:** factory-set approximate overnight blackout using the timer-based logic described below
- **No button** on Walnut model

---

## Obsidian model behaviour

- **LED type:** WS2812B, **16 total LEDs (8 per side)**
- **Colour modes:** 8 modes, cycled by single rear button press
  1. Blue (#3399FF)
  2. Purple (#9966FF)
  3. Green (#33CC66)
  4. Red (#FF3333)
  5. Cyan (#00FFFF)
  6. Yellow (#FFFF00)
  7. White (#FFFFFF)
  8. Off (LEDs disabled — night mode equivalent)
- **Button:** PB4, active LOW, internal pull-up, interrupt-driven
- **Zone indicators:** Same pulse behaviour as Walnut but uses current colour mode
- **Night mode:** same timer-based blackout logic; users can re-align it relative to their desired evening start time

---

## Night mode

The ATtiny85 has no real-time clock. Night mode uses a software timer:
1. On first power-on, internal time counter initialises to 12:00 (noon)
2. Timer increments using the ATtiny85 watchdog timer (1 Hz tick)
3. At simulated 23:00, LEDs go off; at 07:00, LEDs resume
4. **To set the clock:** Hold mode button (Obsidian) for 3 seconds at a known time — this does not adjust the clock but resets the counter to 12:00. Hold at actual 23:00 to align night mode to real time.

This is intentionally simple. Night mode will drift over time. For most users, "LEDs off for roughly 8 hours per day" is sufficient.

---

## Soft cap logic

The ATtiny85 estimates the **wireless/lighting** portion of the load from zone detect pins:
- Zone 1 active: +20W estimate
- Zone 2 active: +5W estimate
- Zone 3 active: +5W estimate
- Lighting budget: up to ~1.5W

That estimate tops out around **31.5W**. The owner-confirmed **60W soft cap** should therefore be read as a **documentation/planning target** for the overall product budget, with the balance left for possible concurrent USB-C use from the included 65W brick. The firmware does **not** directly measure USB-C current and does **not** enforce a true combined system cap; it only dims lighting when the wireless stack is fully active. This is cosmetic headroom, not a hard safety limit.

---

## Pin assignments

| ATtiny85 Pin | Direction | Function |
|---|---|---|
| PB0 (pin 5) | Output | Lighting DATA |
| PB1 (pin 6) | Input | Zone 1 detect (HIGH = phone present) |
| PB2 (pin 7) | Input | Zone 2 detect (HIGH = buds present) |
| PB3 (pin 2) | Input | Zone 3 detect (HIGH = watch present) |
| PB4 (pin 3) | Input | **Obsidian only** — mode button (active LOW) |
| 5V | Power | 5V from 5V buck |
| GND | Power | Common ground |

Zone 1 thermals are handled by the Qi TX module's own NTC + hard-cutoff path, so the firmware currently reads no ADC input for coil temperature.

---

## Programming the ATtiny85

- Board: Digispark-style ATtiny85 USB dev board
- Programming path: USB direct from Arduino IDE (no USBasp required)
- Arduino IDE: install **Digistump AVR Boards** using the Boards Manager URL `http://digistump.com/package_digistump_index.json`
- Clock: use the board profile that matches the purchased Digispark-style board
- Library: FastLED

Flash Walnut first, then Obsidian. Label each board before installing.
