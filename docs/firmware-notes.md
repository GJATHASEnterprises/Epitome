# Epitome Step — Firmware Notes (ATtiny85)

No ESP32. No BLE. No app. The ATtiny85 handles LED control, soft power cap, and night mode only.

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

- **LED type:** WS2811
- **Colour:** Warm white only — #FFD6A0 (R=255, G=214, B=160), fixed, cannot be changed
- **Brightness:** Full brightness during daytime; off during night mode
- **Zone indicators:** When a device is detected on any zone, LEDs pulse once (brief 200 ms brightening) then return to steady on
- **Night mode:** LEDs off from 23:00 to 07:00 (timer-based — see Night Mode section)
- **No button** on Walnut model

---

## Obsidian model behaviour

- **LED type:** WS2812B
- **Colour modes:** 8 modes, cycled by single rear button press
  1. Blue (#3399FF)
  2. Purple (#9966FF)
  3. Green (#33CC66)
  4. Red (#FF3333)
  5. Cyan (#00FFFF)
  6. Yellow (#FFFF00)
  7. White (#FFFFFF)
  8. Off (LEDs disabled — night mode equivalent)
- **Button:** PB4, active LOW, internal pull-up, interrupt-driven (INT0)
- **Zone indicators:** Same pulse behaviour as Walnut but uses current colour mode
- **Night mode:** Same timer-based logic; forces mode to "Off" state during 23:00–07:00

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

The ATtiny85 estimates total power draw from zone detect pins:
- Zone 1 active: +20W estimate
- Zone 2 active: +5W estimate
- Zone 3 active: +5W estimate
- USB-C ports: assumed at max (90W total) — always included

If estimated wireless draw > 30W (i.e., Zones 1 + 2 + 3 all active simultaneously), LED brightness is reduced to 40% to shed ~0.9W. This is cosmetic headroom, not a hard safety limit.

---

## Pin assignments

| ATtiny85 Pin | Direction | Function |
|---|---|---|
| PB0 (pin 5) | Output | WS2811/WS2812B DATA |
| PB1 (pin 6) | Input | Zone 1 detect (HIGH = phone present) |
| PB2 (pin 7) | Input | Zone 2 detect (HIGH = buds present) |
| PB3 (pin 2) | Input | Zone 3 detect (HIGH = watch present) |
| PB4 (pin 3) | Input | **Obsidian only** — mode button (active LOW) |
| VCC (pin 8) | Power | 5V from 5V buck |
| GND (pin 4) | Power | Common ground |

---

## Programming the ATtiny85

- Programmer: USBasp or Arduino as ISP
- Arduino IDE: install ATtiny85 board package (David Mellis or SpenceKonde)
- Clock: 8 MHz internal (no crystal needed)
- Fuses: Low = 0xE2, High = 0xDF, Extended = 0xFF
- Library: FastLED (WS2811 / WS2812B both supported)

Flash Walnut binary first. Program Obsidian binary separately. Label each chip with a marker before installing.

