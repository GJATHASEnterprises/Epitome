# Quad-Dock — Electronics Specification

---

## Microcontroller: ESP32-C3 Mini

| Feature | Detail |
|---------|--------|
| **Module** | ESP32-C3 Mini (RISC-V core) |
| **Why chosen** | Same WiFi + BLE capability as ESP32-WROOM but cheaper (~$2–$3 vs ~$4–$6) |
| **WiFi** | 802.11 b/g/n 2.4GHz |
| **Bluetooth** | BLE 5.0 |
| **Flash** | 4MB onboard |
| **Flashing** | Via ESP32-C3 onboard USB — no separate UART IC required |
| **GPIO count** | Sufficient for this design (I2C, LED data, ambient sensor) |
| **Physical buttons** | None — all control via iOS app + ambient light sensor |

---

## Component List

| # | Component | Part / Spec | Qty | Zone / Use |
|---|-----------|-------------|-----|------------|
| 1 | MCU | ESP32-C3 Mini | 1 | Main controller |
| 2 | Qi 15W TX Coil | 50mm Qi TX module, 15W | 2 | Zone 1 + Zone 2 |
| 3 | Apple Watch Puck | Magnetic charging module | 1 | Zone 3 |
| 4 | USB-C PD Controller | 100W capable routing board | 1 | Zone 4 |
| 5 | Power Monitor (3-ch) | INA3221, I2C | 1 | Zones 1–3 |
| 6 | Power Monitor (1-ch) | INA219, I2C | 1 | Zone 4 |
| 7 | Ambient Light Sensor | BH1750, I2C | 1 | Auto LED dimming |
| 8 | LED Strip | WS2812B, 16 LEDs cut from 60/m reel | 1 | Front lip glow bar |
| 9 | N52 Ring Magnets | Ring, fits 50mm Qi coil | 1 set | Zone 1 phone alignment |
| 10 | Internal AC/DC PSU | 180W, 100–240V AC in, 20V DC out | 1 | Main power |
| 11 | IEC C13 Inlet | Panel mount, with fuse holder | 1 | Wall inlet |
| 12 | 3.3V LDO Regulator | Shared for ESP32-C3 + sensors | 1 | Logic rail |
| 13 | Thermistors | NTC 10K, per coil zone | 3 | Overheat protection |
| 14 | Overcurrent Protection | Polyfuse/IC per zone | 4 | Per-zone safety |
| 15 | Custom PCB | 2-layer, JLCPCB PCBA, panelized 4/panel | 1 | Main board |
| 16 | Capacitors / Resistors | Assorted SMD (JLCPCB basic library) | lot | Passives |
| 17 | Wiring / Connectors | JST, Dupont, misc | lot | Interconnects |
| 18 | Frosted Diffuser Strip | Frosted acrylic, LED bar width | 1 | LED diffusion |

---

## No USB-A Port

USB-A has been removed from the design to reduce cost and simplify the PCB. All wired charging is handled by Zone 4 USB-C PD. Any device needing USB-A can use a USB-A to USB-C adapter.

---

## No Physical Buttons

There are no physical buttons on Quad-Dock. All control is handled via:
- iOS companion app (BLE)
- Ambient light sensor (BH1750) for automatic LED dimming

---

## Power Architecture

```
[Wall Outlet]
     |
[IEC C13 Inlet + Fuse]
     |
[Internal 180W AC/DC PSU — 100–240V AC in → 20V DC out]
     |
     +----[Zone 1: Qi 15W TX]—[INA3221 ch1]
     |
     +----[Zone 2: Qi 15W TX]—[INA3221 ch2]
     |
     +----[Zone 3: Watch Puck 5W]—[INA3221 ch3]
     |
     +----[Zone 4: USB-C PD 100W]—[INA219]
     |
     +----[3.3V LDO]—[ESP32-C3 Mini]—[BH1750]—[WS2812B]
```

### Power Rail Summary

| Rail | Voltage | Used For |
|------|---------|----------|
| AC input | 100–240V AC | IEC C13 wall inlet → PSU |
| Main DC rail | 20V | Source for all zones |
| Qi coil supply | 12V (stepped down) | Wireless TX modules |
| Watch puck | 5V | Apple Watch module |
| USB-C PD out | 5V–20V (negotiated) | Laptop / phone / iPad |
| ESP32-C3 + logic | 3.3V | MCU, sensors, LEDs |

### 180W PSU Note
The 180W internal PSU provides significant headroom. Typical draw:
- 3 phones charging simultaneously: ~60W total
- MacBook Pro 16" at 100W: 100W
- All zones simultaneously (worst case): ~130W
- PSU never exceeds 75% of rated capacity under normal use

### Single 5V Rail Consideration
A single shared 5V rail for the ESP32-C3, BH1750, WS2812B, and Watch puck (all stepped down from 20V via a 5V buck converter) is feasible and reduces BOM complexity. Confirm current budget allows for Watch puck + WS2812B + ESP32-C3 simultaneously on one rail.

---

## USB-C PD Zone 4 (100W)

- **Controller:** 100W-capable USB-C PD routing board (LCSC sourced)
- **Max output:** 100W (20V × 5A)
- **PD negotiation:** Automatic — negotiates voltage and current with connected device
- **Compatible devices:** Any USB-C PD device — laptops, phones, iPads, Nintendo Switch
- **MacBook Pro 16" note:** Charges fine at 100W; slightly slower under maximum CPU + GPU load (which needs 140W for full speed). This is normal behaviour for any 100W charger — the laptop just draws from its battery for the difference.
- **Power monitoring:** INA219 on Zone 4 output

---

## Qi Charging Zones 1 + 2 (15W)

- **Coil spec:** 50mm Qi TX coil modules, 15W capable
- **Source:** LCSC — order in sets of 10 for bulk pricing
- **Standard:** Qi universal (compatible with iPhone, Android, AirPods Qi case)
- **Zone 1 extras:** N52 neodymium ring magnets beneath coil for phone snap-alignment (MagSafe-style)
- **Power monitoring:** INA3221 channels 1 and 2

---

## Apple Watch Zone 3

- **Module:** Apple Watch magnetic charging module (standard watch puck)
- **Output:** 5W
- **Source:** Bulk order (×10 minimum) for better pricing
- **Mount:** Wired internally to PCB; pod mounted in teardrop cradle on enclosure
- **Power monitoring:** INA3221 channel 3

---

## Power Monitoring

### INA3221 (Zones 1–3)
- 3-channel I2C power monitor
- CH1 = Zone 1 (Qi 15W), CH2 = Zone 2 (Qi 15W), CH3 = Zone 3 (Watch 5W)
- I2C address configurable via A0 pin
- Shunt resistor: 0.1Ω per channel
- LCSC sourced

### INA219 (Zone 4)
- 1-channel I2C power monitor
- Monitors Zone 4 USB-C PD output (up to 100W)
- Address set via A0/A1 pins — ensure no conflict with INA3221
- Shunt resistor: 0.1Ω
- LCSC sourced

---

## Ambient Light Sensor: BH1750

- **Interface:** I2C (shares bus with INA3221 + INA219)
- **Range:** 1–65535 lux
- **Use:** Auto-dims LED bar in dark rooms, auto-brightens in light
- **ADDR pin:** Sets I2C address (0x23 or 0x5C)
- **Why BH1750 over TEMT6000:** Digital I2C output is cleaner and more precise; no ADC channel required; same I2C bus as power monitors

---

## LED System: WS2812B

- **Type:** WS2812B addressable RGB LED strip
- **LED count:** 16 total (4 per zone)
- **Data pin:** GPIO from ESP32-C3 (single data wire)
- **Series resistor:** 300–470Ω on data line
- **Power:** 5V rail
- **Decoupling:** 100µF electrolytic cap across 5V/GND at strip entry
- **Firmware library:** FastLED or NeoPixel

---

## ESP32-C3 Pin Assignments

| Pin | Function |
|-----|----------|
| GPIO 8 | I2C SDA (INA3221, INA219, BH1750) |
| GPIO 9 | I2C SCL (INA3221, INA219, BH1750) |
| GPIO 4 | WS2812B LED strip data |
| GPIO 5 | Zone 1 Qi coil enable (optional) |
| GPIO 6 | Zone 2 Qi coil enable (optional) |
| GPIO 7 | USB-C PD enable (optional) |
| USB | Onboard USB for flashing (no separate UART IC) |

*Pin assignments are provisional and may be adjusted during PCB layout.*

---

## Flashing

ESP32-C3 Mini has a built-in USB interface for flashing. No separate USB-to-UART IC (e.g., CP2102, CH340) is required. Connect the dock's USB-C service port (or a direct micro-USB/USB-C connection to the ESP32-C3) to a computer and flash using the ESP-IDF or Arduino IDE.

---

## PCB Specification

| Spec | Value |
|------|-------|
| Layers | 2 |
| Manufacturer | JLCPCB |
| Assembly | JLCPCB PCBA (machine soldered) |
| Panelization | 4 boards per panel (reduces per-unit cost) |
| Parts library | JLCPCB basic parts for all passives |
| Component sourcing | LCSC wherever possible |

### PCB Layout Notes
- Keep Qi coil traces wide (2mm minimum)
- Separate analog ground (sensors) from power ground with star connection
- ESP32-C3 antenna must be near board edge — no copper pour underneath
- WS2812B data resistor placed close to MCU output
- INA3221 and INA219 placed close to their respective load zones

---

## Safety Features

- Polyfuse or resettable fuse on each zone output
- TVS diode on USB-C output for surge protection
- Thermistors (NTC 10K) per coil zone — ESP32-C3 triggers shutoff if >45°C
- Fuse on IEC C13 inlet line (3A slow-blow)
- Overcurrent protection per zone
- Bulk capacitor (470–1000µF) on 20V main rail for stability
