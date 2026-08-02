# Quad-Dock — Wiring & Schematic Notes

---

## System Overview

```
[Wall Outlet]
     |
[IEC C13 Power Inlet + Fuse]
     |
[Internal 180W AC/DC PSU Module] ──→ [Main DC Rail: 20V]
                                            |
          +---------------------------------+------------------+------------------+----------+
          |              |              |              |                  |                  |
   [Qi TX 1]      [Qi TX 2]     [Watch Puck]  [USB-C PD 100W]   [USB-C PD 20W]      [3.3V LDO]
   Zone 1 (15W)  Zone 2 (5W)   Zone 3 (5W)   Zone 4 (100W)      Zone 5 (20W)            |
      |               |              |              |                  |              [ESP32-C3 Mini]
  [INA3221 ch1]  [INA3221 ch2]  [INA3221 ch3]  [INA219 Z4]        [INA219 Z5]             |
      |               |              |              |                  |       [BH1750][WS2812B][NTC]
      +---------------+--------------+--------------+------------------+
                              |
                        [ESP32-C3 I2C Bus (GPIO 8/9)]
```

---

## Power Rail Design

| Rail | Voltage | Used For |
|------|---------|----------|
| AC input | 100–240V AC | IEC C13 wall inlet to internal PSU |
| Main DC rail | 20V | Source for all zones and step-downs |
| Qi coil supply | 12V (stepped down from 20V) | Wireless TX modules |
| Watch puck | 5V | Apple Watch module |
| USB-C PD out (Zone 4) | 5V–20V (negotiated) | Laptop / high-power USB-C device |
| USB-C PD out (Zone 5) | 9V–12V (from 20V rail step-down) | iPad / phone / secondary USB-C device |
| ESP32-C3 + logic | 3.3V | MCU, sensors, LEDs (shared LDO) |

---

## ESP32-C3 Mini Pin Assignments

| Pin | Function |
|-----|----------|
| GPIO 8 | I2C SDA (INA3221 + INA219 Z4 + INA219 Z5 + BH1750) |
| GPIO 9 | I2C SCL (INA3221 + INA219 Z4 + INA219 Z5 + BH1750) |
| GPIO 4 | WS2812B LED strip data |
| GPIO 5 | Zone 1 Qi coil enable (optional) |
| GPIO 6 | Zone 2 Qi coil enable (optional) |
| GPIO 7 | USB-C PD enable (optional) |
| GPIO 2 | Thermistor Zone 1 (ADC) |
| GPIO 3 | Thermistor Zone 2 (ADC) |
| GPIO 10 | Thermistor Zone 3 (ADC) |
| GPIO 1 | Thermistor Zone 5 (ADC) |
| USB | Onboard USB — for flashing (no separate UART IC required) |

*Pin assignments are provisional and subject to change during PCB layout.*

---

## WS2812B LED Strip Wiring

- **Data wire:** GPIO 4 → 300–470Ω series resistor → DIN of LED strip
- **Power:** 5V from internal rail → VCC of LED strip
- **Ground:** Common GND
- **Decoupling:** 100µF electrolytic capacitor across 5V/GND at strip power entry
- Total LEDs: 20 (4 per zone); cut from a 60 LED/m reel

---

## Ambient Light Sensor: BH1750

- **Interface:** I2C (same bus as INA3221 + both INA219 monitors: GPIO 8/9)
- **I2C address:** 0x23 (ADDR pin low) or 0x5C (ADDR pin high) — ensure no conflict with INA3221/INA219
- **Range:** 1–65535 lux
- **Use:** Auto-dims LED bar in dark rooms, night mode verifies when LEDs should remain off

---

## INA3221 — 3-Channel Power Monitor (Zones 1–3)

- I2C address: set via A0 pin (GND = 0x40, VCC = 0x41, SDA = 0x42, SCL = 0x43)
- Channels: CH1 = Zone 1 (Qi 15W), CH2 = Zone 2 (Qi 5W), CH3 = Zone 3 (Watch 5W)
- Typical shunt resistor: 0.1Ω per channel
- Datasheet: LCSC part search "INA3221"

---

## INA219 — Single-Channel Power Monitor (Zone 4)

- I2C interface to ESP32-C3
- Monitors Zone 4 (USB-C PD up to 100W)
- Address set via A0/A1 pins — ensure no conflict with INA3221, Zone 5 INA219, or BH1750
- Typical shunt resistor: 0.1Ω

---

## INA219 — Single-Channel Power Monitor (Zone 5)

- I2C interface to ESP32-C3
- Monitors Zone 5 (USB-C PD up to 20W)
- Address set via A0/A1 pins — ensure no conflict with INA3221, Zone 4 INA219, or BH1750
- Typical shunt resistor: 0.1Ω

---

## ESP32-C3 Mini

- Main MCU
- WiFi 802.11 b/g/n 2.4GHz + BLE 5.0
- Flash: 4MB onboard
- Flashed via onboard USB — no separate UART IC (no CP2102, CH340, or similar required)
- Power via shared 3.3V LDO

---

## LED Behavior Logic

- **Red:** Device is charging on that zone
- **Green:** Device is fully charged on that zone
- **Off:** No device detected on that zone
- **Night mode:** Between 23:00–07:00, LEDs stay off unless that zone is actively drawing >0.5W
- **App override:** User forces brightness / LED off from the iOS app via BLE command

The firmware implementation lives in:
- `firmware/led_controller.h`
- `firmware/led_controller.cpp`

The controller exposes:
- `setZoneStatus(int zone, ZoneStatus status)` — called by the charging monitor task
- `setDarkMode(bool enable)` — called by the BLE command handler
- `isDarkMode()` — read by the BLE status notifier
- `update()` — called from the main loop every iteration

---

## Safety Wiring Notes

- Add **polyfuse or resettable fuse** on each zone output
- Add **TVS diode** on USB-C outputs for surge protection
- Thermistors (NTC 10K) connected to ESP32-C3 ADC pins with voltage divider (10K + NTC 10K)
- ESP32-C3 triggers zone shutoff via I2C command if temp exceeds threshold (~45°C)
- Fuse on IEC C13 inlet line (3A slow-blow recommended)
- Bulk capacitor (470–1000µF) on 20V main rail for stability

---

## PCB Notes

- **2-layer PCB** — sufficient for this circuit
- **Panelized** — 4 boards per panel at JLCPCB to reduce per-unit cost
- **JLCPCB PCBA** — all components sourced and assembled by JLCPCB; use basic parts library for all passives
- Keep Qi coil traces wide (2mm minimum for coil supply)
- Separate analog ground (sensors, ADC) from power ground with a single-point star connection
- Use JLCPCB standard 2-layer stackup
- Place INA3221 and both INA219 monitors close to their respective load zones
- ESP32-C3 antenna must be near board edge with no copper pour underneath
- WS2812B data line: add 300–470Ω resistor at GPIO output, place close to MCU
