# Quad Device Dock — Wiring & Schematic Notes

---

## System Overview

```
[Wall Outlet]
     |
[IEC C13 Power Inlet + Fuse]
     |
[Internal 180W AC/DC PSU Module] ──→ [Main DC Rail: 20V]
                                            |
          +---------------------------------+------------------+
          |              |              |              |       |
   [Qi TX 1]      [Qi TX 2]     [Watch Puck]  [USB-C PD Out]  [USB-A Out]
   Zone 1 (15W)  Zone 2 (15W)  Zone 3 (5W)   Zone 4 (100W)   Side (12W)
      |               |              |              |              |
  [INA3221 ch1]  [INA3221 ch2]  [INA3221 ch3]  [INA219]      [SY6280]
      |               |              |              |              |
      +---------------+--------------+--------------+              |
                              |                                    |
                        [ESP32 I2C Bus]                            |
                              |                                    |
                  [ESP32-WROOM-32 Microcontroller] ←──────────────+
                       |              |             |
               [WiFi / BT]  [WS2812B LED Strip]  [ADC: Ambient + Thermistors]
                       |              |
                 [Mobile App]    [GPIO 12, single data wire]
```

---

## Power Rail Design

| Rail | Voltage | Used For |
|------|---------|----------|
| AC input | 100–240V AC | IEC C13 wall inlet to internal PSU |
| Main DC rail | 20V | Stepped down as needed by each zone |
| Qi coil supply | 12V | Wireless TX modules (stepped down from 20V) |
| Watch puck | 5V | Apple Watch module |
| USB-C PD out | 5V–20V (negotiated) | Laptop/tablet |
| USB-A out | 5V | SY6280 IC → USB-A port |
| ESP32 + logic | 3.3V | MCU, sensors, LEDs (single shared LDO from 5V rail) |

---

## ESP32 Pin Assignments

| GPIO Pin | Function |
|----------|----------|
| GPIO 21 | I2C SDA (INA3221 + INA219) |
| GPIO 22 | I2C SCL (INA3221 + INA219) |
| GPIO 12 | WS2812B LED strip data (FastLED) |
| GPIO 36 | TEMT6000 ambient light sensor (ADC1_CH0, input only) |
| GPIO 34 | Thermistor Zone 1 (ADC1_CH6, input only) |
| GPIO 35 | Thermistor Zone 2 (ADC1_CH7, input only) |
| GPIO 32 | Thermistor Zone 3 (ADC1_CH4) |
| GPIO 33 | Thermistor Zone 4 (ADC1_CH5) |

GPIO 36 is used for the ambient light sensor because it is an ADC1 input-only pin with no conflicts and does not require internal pull-up/pull-down. GPIO 12 is used for the WS2812B data line because it is a stable GPIO that does not affect the ESP32 boot strapping sequence when held low at reset.

---

## WS2812B LED Strip Wiring

- **Data wire:** GPIO 12 → 300–470 ohm series resistor → DIN of LED strip
- **Power:** 5V from internal rail → VCC of LED strip
- **Ground:** Common GND
- **Decoupling:** 100µF electrolytic capacitor across 5V/GND at strip power entry
- Total LEDs: 16 (4 per zone); order from a 60 LED/m reel and cut to length

---

## Ambient Light Sensor Wiring (TEMT6000)

- **TEMT6000** SOT-23 package: Emitter → GND, Collector → 10kΩ resistor → 3.3V; collector junction → GPIO 36 (ADC)
- In darkness the collector voltage is near 3.3V (high ADC value); in bright light it is near GND (low ADC value) — firmware inverts this to map to brightness appropriately
- No I2C address required; purely analog

**Alternative: BH1750 (I2C)**
If digital precision is preferred, the BH1750 can be placed on the same I2C bus (SDA/SCL on GPIO 21/22). Use ADDR pin to set address (0x23 or 0x5C). This requires an additional I2C driver in firmware.

---

## INA3221 — 3-Channel Power Monitor (Zones 1–3)

- I2C address: set via A0 pin (GND = 0x40, VCC = 0x41, SDA = 0x42, SCL = 0x43)
- Channels: CH1 = Zone 1 (Qi 15W), CH2 = Zone 2 (Qi 15W), CH3 = Zone 3 (Watch 5W)
- Typical shunt resistor: 0.1 ohm per channel
- Datasheet: LCSC part search "INA3221"

---

## INA219 — Single-Channel Power Monitor (Zone 4)

- I2C interface to ESP32
- Monitors Zone 4 (USB-C PD up to 100W)
- Address set via A0/A1 pins; ensure no conflict with INA3221 address
- Typical shunt resistor: 0.1 ohm

---

## USB-A Charging IC (SY6280 or Equivalent)

- Handles 5V/2.4A (12W) USB-A output on the side port
- Input: 5V rail from internal PSU step-down
- D+/D– resistor divider sets charging profile (Apple/Android detection)
- LCSC sourced; JLCPCB PCBA compatible

---

## ESP32-WROOM-32

- Main MCU
- WiFi 802.11 b/g/n + Bluetooth 4.2/BLE
- Flash: 4MB minimum
- Power via shared 3.3V LDO from 5V rail
- OTA firmware updates supported over WiFi

---

## LED Behavior Logic

- **Red:** Device is charging on that zone.
- **Green:** Device is fully charged on that zone.
- **Off:** No device detected on that zone.
- **Full bar pulses green:** All four zones are simultaneously full — breathing animation.
- **Dark mode (app):** User forces all LEDs off from the app; sensor auto-brightness is suspended.

The firmware implementation lives in:
- `firmware/led_controller.h`
- `firmware/led_controller.cpp`

The controller exposes:
- `setZoneStatus(int zone, ZoneStatus status)` — called by the charging monitor task
- `setDarkMode(bool enable)` — called by the BLE/WiFi command handler
- `isDarkMode()` — read by the BLE status notifier
- `update()` — called from the main loop every iteration (handles pulsing and auto-brightness)

---

## Safety Wiring Notes
- Add **polyfuse or resettable fuse** on each zone output
- Add **TVS diode** on USB-C output for surge protection
- Thermistors connected to ESP32 ADC pins with voltage divider (10K + NTC 10K)
- ESP32 triggers zone shutoff via I2C command if temp exceeds threshold (~45°C)
- Fuse on IEC C13 inlet line (3A slow-blow recommended)
- Add **bulk capacitor** (470–1000µF) on 20V main rail for stability

---

## PCB Notes
- **2-layer PCB** — sufficient for this circuit; significantly cheaper than 4-layer
- **Panelized** — fit multiple boards per panel at JLCPCB to reduce per-unit cost
- **JLCPCB PCBA** — all components sourced and assembled by JLCPCB; use basic parts library for all passives
- Keep Qi coil traces wide (2mm minimum for coil supply)
- Separate analog ground (sensors, ADC) from power ground with a single-point star connection
- Use JLCPCB standard 2-layer stackup
- Place INA3221 and INA219 close to their respective load zones
- ESP32 antenna must be near board edge with no copper pour underneath
- WS2812B data line: add 300–470 ohm resistor at GPIO 12 output, place close to MCU
