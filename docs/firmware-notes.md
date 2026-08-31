# Step — Firmware Notes (ATtiny85)

---

## Overview

Step uses an ATtiny85 for all onboard logic. There is no ESP32, no Bluetooth, no WiFi, and no app in Batch 1.

The ATtiny85 performs two jobs:
1. Drive the WS2811 LED strip (5-zone colour indicator)
2. Enforce the 60W soft power cap (protect the included 65W brick)

---

## Microcontroller

| Attribute | Value |
|---|---|
| MCU | ATtiny85 (DIP-8) |
| Clock | 8MHz internal |
| Flash | 8KB |
| RAM | 512 bytes |
| Programming | ISP via 6-pin header or Arduino as ISP |
| Voltage | 5V from 5V buck converter |

---

## Pin Assignments

| Pin | ATtiny85 | Function |
|---|---|---|
| 1 | PB5 / RESET | Port B current sense (soft) |
| 2 | PB3 | Zone 3 relay control (HIGH = Apple Watch puck) |
| 3 | PB4 | Port A current sense (soft) |
| 4 | GND | Ground |
| 5 | PB0 | WS2811 LED strip data out |
| 6 | PB1 | Zone 1 Qi2 sense / enable |
| 7 | PB2 | Zone 2 Qi sense / enable |
| 8 | VCC | 5V supply |

---

## LED Logic

The WS2811 LED strip has 8 addressable LEDs. The ATtiny85 drives them directly via a single data line.

### LED Assignments

| LED | Zone | Colour | Hex |
|---|---|---|---|
| 1–2 | Zone 1 phone | Blue | #0044FF |
| 3–4 | Zone 2 buds | Purple | #8800FF |
| 5–6 | Zone 3 watch | Green | #00CC44 |
| 7 | Port A USB-C | Orange | #FF6600 |
| 8 | Port B USB-C | Teal | #00BBAA |

LEDs illuminate at full brightness when the zone is actively charging. LEDs pulse slowly (breathe effect) when a device is present but charge is complete. LEDs are off when no device is present.

### LED Library

Use `tinyNeoPixel` (ATtiny-compatible WS2811 driver) or `Adafruit NeoPixel` compiled for ATtiny85 target.

---

## Soft Power Cap (60W)

The ATtiny85 tracks an estimated power draw per zone based on zone enable signals and known maximum zone wattages:

| Zone | Estimated max wattage used in cap logic |
|---|---:|
| Zone 1 Qi2 | 20W |
| Zone 2 Qi | 5W |
| Zone 3 watch | 5W |
| Port A | 60W |
| Port B | 30W |
| Logic + LEDs | 2W |

When the estimated total approaches 60W, the ATtiny85 disables the lowest-priority active zone. Priority order (highest to lowest): Port A → Port B → Zone 1 → Zone 2 → Zone 3.

**This is a soft cap, not a measured cap.** The ATtiny85 does not have current sensing; it uses zone presence signals as proxies for load. A proper current-sense implementation (INA219) is a Batch 2 consideration.

---

## Zone 3 Relay Control

The ATtiny85 controls the hardware relay on PB3:
- `PB3 HIGH` → relay activates Apple Watch puck PCBA
- `PB3 LOW` → relay activates universal Qi watch coil

Detection logic: The ATtiny85 attempts to infer watch type from Zone 3 Qi coil handshake timing. If an Apple Watch-compatible handshake is detected, relay switches to puck mode. Otherwise defaults to Qi coil mode.

In Batch 1 this logic is simplified: the relay defaults to Apple Watch puck mode. Users with non-Apple Qi watches can hold the RESET pin low for 3 seconds at power-on to toggle relay to Qi coil mode.

---

## Programming the ATtiny85

### Toolchain
- Arduino IDE with ATtiny85 board support (SpenceKonde/ATTinyCore)
- Or: avr-gcc + avrdude directly

### Board settings (Arduino IDE)
- Board: ATtiny25/45/85
- Chip: ATtiny85
- Clock: 8MHz (internal)
- Programmer: Arduino as ISP

### ISP Header (on PCB)
6-pin 2.54mm header: MISO, SCK, RESET, GND, MOSI, VCC

### Burn bootloader / fuses
```
Tools > Burn Bootloader
```
Sets fuses for 8MHz internal clock.

### Upload sketch
Connect Arduino as ISP. Select "Sketch > Upload Using Programmer."

---

## Firmware File Location

`firmware/step_attiny85.ino`

---

## Not Implemented in Batch 1

- BLE / WiFi (no ESP32)
- Over-the-air updates
- Real current sensing (no INA219)
- USB serial debug output
- App connectivity
