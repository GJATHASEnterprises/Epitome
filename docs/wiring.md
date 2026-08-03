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

---

## Comprehensive Wiring Implementation Guide (Revision A)

This section defines practical wiring execution from wall inlet to every electrical load branch.

### Reference Documents

- Electrical architecture: [electronics.md](electronics.md)
- Coordinates and placement: [component-positions.md](component-positions.md)
- Parts and recommended modules: [bom.md](bom.md)
- Firmware safety/night behavior: [firmware-notes.md](firmware-notes.md)

## 1) Full System Wiring Narrative (End-to-End)

1. Bring AC mains into the rear IEC C13 inlet.
2. Route line through 3A slow-blow fuse before PSU AC input terminal.
3. Route neutral and earth to PSU per PSU terminal labeling and enclosure grounding practice.
4. Convert AC to regulated ~20V DC inside PSU.
5. Route PSU DC+ through bulk capacitor staging into the main 20V distribution bus.
6. Split the 20V bus into five protected zone branches and one logic-regulation branch.
7. For each branch, apply required conversion (buck/PD board), monitoring element, and protection chain.
8. Distribute 3.3V logic power to ESP32-C3 and all I2C sensors/monitors.
9. Wire control/sense network: I2C, thermistors, and WS2812 data path.
10. Verify grounds are commoned correctly with star-ground topology and single-point analog tie.

## 2) AC Wiring Section

### Path

`IEC C13 inlet (rear panel) → 3A slow-blow fuse → PSU AC-L/AC-N terminals`

### AC Wiring Requirements

| Item | Requirement |
|---|---|
| Minimum AC conductor gauge | 18 AWG |
| Inlet type | Panel-mount IEC C13 |
| Fuse type | 3A slow-blow (time-delay) |
| PSU input | 100–240VAC compatible terminals |
| Terminal style | Screw terminals with secure strain relief |

### AC Assembly Notes

- Keep AC harness physically isolated from low-voltage I2C/sensor wiring.
- Use insulated crimp terminals or ferrules for terminal-block reliability.
- Maintain clear polarity and earth continuity marking.

## 3) DC Main Rail Section (20V Backbone)

### Path

`PSU DC+ output → bulk capacitor (470–1000µF) → main 20V distribution bus`

### Main Rail Requirements

| Item | Requirement |
|---|---|
| Main rail gauge | 16 AWG recommended |
| Bulk capacitor value | 470–1000µF electrolytic |
| Rail topology | Short trunk + branch fan-out |
| Grounding | Star return to PSU GND |

## 4) Per-Zone DC Wiring Detail

### Zone 1 (Qi 15W)

`20V rail → 16V/12V buck converter → Qi TX module VCC/GND (18 AWG) → polyfuse 2A inline → NTC divider output to GPIO 2`

| Zone 1 Element | Spec |
|---|---|
| Branch wire gauge | 18 AWG |
| Converter | 20V to ~12V class buck for Qi TX input |
| Protection | 2A resettable polyfuse |
| Thermal sensing | NTC + 10k divider to ADC GPIO 2 |

### Zone 2 (Qi 5W)

`20V rail → 16V/12V buck converter → Qi TX module VCC/GND (18 AWG) → polyfuse 2A inline → NTC divider output to GPIO 3`

| Zone 2 Element | Spec |
|---|---|
| Branch wire gauge | 18 AWG |
| Converter | Same architecture as Zone 1 with lower power budget |
| Protection | 2A resettable polyfuse |
| Thermal sensing | NTC + 10k divider to ADC GPIO 3 |

### Zone 3 (Watch 5W)

`20V rail → 5V buck converter → Apple Watch puck VCC/GND (22 AWG) → polyfuse 1A inline → NTC divider output to GPIO 10`

| Zone 3 Element | Spec |
|---|---|
| Branch wire gauge | 22 AWG |
| Converter | 20V to 5V buck |
| Protection | 1A resettable polyfuse |
| Thermal sensing | NTC + 10k divider to ADC GPIO 10 |

### Zone 4 (USB-C PD 100W)

`20V rail → USB-C PD 100W board VIN/GND (14 AWG) → INA219 Z4 shunt inline → polyfuse 6A → TVS diode on USB-C output pins`

| Zone 4 Element | Spec |
|---|---|
| Branch wire gauge | 14 AWG (high current) |
| Conversion/control | USB-C PD 100W controller board |
| Monitoring | INA219 Zone 4 inline current/voltage sense |
| Protection | 6A resettable polyfuse + TVS at output |

### Zone 5 (USB-C PD 20W)

`20V rail → 9V–12V buck → USB-C PD 20W board VIN/GND (18 AWG) → INA219 Z5 shunt inline → polyfuse 2A → TVS diode on USB-C output pins`

| Zone 5 Element | Spec |
|---|---|
| Branch wire gauge | 18 AWG |
| Converter | 20V to 9V–12V pre-regulation for 20W branch |
| Monitoring | INA219 Zone 5 inline current/voltage sense |
| Protection | 2A resettable polyfuse + TVS at output |

## 5) I2C Bus Wiring

### Physical Bus

`ESP32 GPIO8 (SDA) + GPIO9 (SCL) → 4.7k pull-ups to 3.3V → INA3221 + INA219 Z4 + INA219 Z5 + BH1750`

| Item | Requirement |
|---|---|
| Pull-ups | 4.7kΩ to 3.3V on SDA and SCL |
| Signal wire gauge | 22–24 AWG |
| Preferred wire type | Twisted pair or short ribbon for SDA/SCL + local ground |
| Max practical bus length inside dock | Keep under ~300 mm total routed length |

I2C is low-speed and local in this enclosure; keep routing compact and away from AC wiring and high di/dt PD paths.

## 6) WS2812B LED Strip Wiring

### Path

`ESP32 GPIO4 → 300–470Ω series resistor → LED strip DIN`

`5V rail → strip VCC`

`GND common → strip GND`

`100µF electrolytic between strip VCC/GND at strip entry`

| Item | Requirement |
|---|---|
| Data resistor | 300–470Ω, place near GPIO output |
| Decoupling | 100µF electrolytic at strip input |
| Ground | Must be common with ESP32 ground |
| LED count | 20 total (4 per zone) |

## 7) BH1750 Wiring

| BH1750 Pin | Connection |
|---|---|
| VCC | 3.3V logic rail |
| GND | Logic/sensor ground |
| SDA | GPIO 8 |
| SCL | GPIO 9 |
| ADDR | GND for 0x23 default |

## 8) NTC Thermistor Wiring

Each NTC uses a voltage divider with 10k fixed resistor:

`3.3V → 10k fixed resistor → ADC sense node → NTC 10k → GND`

| Zone | ADC GPIO |
|---|---|
| Zone 1 | GPIO 2 |
| Zone 2 | GPIO 3 |
| Zone 3 | GPIO 10 |
| Zone 5 | GPIO 1 |

Use matched tolerance resistors where possible to simplify calibration curves.

## 9) 3.3V LDO Wiring

### Path

`5V source (or validated direct 3.3V source path) → 3.3V LDO IN`

`3.3V LDO OUT → ESP32-C3 VCC + INA3221 VCC + INA219 Z4 VCC + INA219 Z5 VCC + BH1750 VCC`

| Item | Requirement |
|---|---|
| LDO input source | 5V preferred local logic supply |
| LDO output | 3.3V regulated logic rail |
| Decoupling | Follow LDO datasheet input/output capacitor requirements |
| Load class | MCU + I2C monitor/sensor fleet |

## 10) Full ESP32-C3 Pin Assignment + Wire Color Guidance

| GPIO/Pin | Function | Recommended Wire Color |
|---|---|---|
| GPIO 8 | I2C SDA | Blue |
| GPIO 9 | I2C SCL | Yellow |
| GPIO 4 | WS2812 DIN | Green |
| GPIO 5 | Zone 1 enable (optional) | Orange |
| GPIO 6 | Zone 2 enable (optional) | Purple |
| GPIO 7 | PD enable (optional) | Grey |
| GPIO 2 | NTC Zone 1 ADC | White/Blue stripe |
| GPIO 3 | NTC Zone 2 ADC | White/Yellow stripe |
| GPIO 10 | NTC Zone 3 ADC | White/Green stripe |
| GPIO 1 | NTC Zone 5 ADC | White/Grey stripe |
| 3.3V | Logic rail distribution | Red |
| GND | Common logic ground | Black |

## 11) I2C Address Table and Conflict Avoidance

| Device | Role | Address | Address Setting Method |
|---|---|---|---|
| INA3221 | Zones 1–3 monitor | 0x40 default | A0 strapped to GND |
| INA219 Z4 | Zone 4 monitor | 0x41 example | A0/A1 strap per board |
| INA219 Z5 | Zone 5 monitor | 0x44 example | A0/A1 strap distinct from Z4 |
| BH1750 | Ambient lux sensor | 0x23 default | ADDR to GND (0x5C if ADDR high) |

Conflict avoidance rule: unique address per installed I2C peripheral. If a breakout’s hardwired default collides, adjust strap pins and firmware constants before power-load testing.

## 12) Grounding Strategy

- Implement **star-ground topology** from PSU GND as central return point.
- Keep high-current branch returns (especially Zone 4) physically separated from sensor/ADC returns until star junction.
- Use a dedicated analog/sensor ground region for ADC and low-level sensing, joined at a **single-point tie** to main ground.
- Avoid daisy-chained long ground loops between branches.

## 13) Wire Gauge Summary Table

| Branch | Recommended AWG | Approx. Max Current Class | Rationale |
|---|---:|---:|---|
| AC input harness | 18 AWG min | Mains side | Safety and mechanical robustness |
| 20V main rail trunk | 16 AWG | Multi-branch aggregate current | Lower voltage drop and heating |
| Zone 1 Qi branch | 18 AWG | Moderate | Stable Qi feed with manageable flexibility |
| Zone 2 Qi branch | 18 AWG | Low-moderate | Shared architecture and consistency |
| Zone 3 watch branch | 22 AWG | Low | 5W load, easier routing in pod area |
| Zone 4 PD 100W branch | 14 AWG | High | Highest current branch in system |
| Zone 5 PD 20W branch | 18 AWG | Moderate | Lower than Zone 4 but above logic class |
| I2C + sensor signals | 22–24 AWG | Signal only | Low current and flexible harnessing |

## 14) Connector Recommendations

| Connection Type | Recommended Connector |
|---|---|
| DC branch power interconnects | JST-XH 2.54 mm |
| Signal / I2C / thermistor leads | Dupont 2.54 mm |
| PSU AC input terminals | Screw terminals (with ferrules/crimps) |
| Service-disconnect points | JST-XH where branch modularity is desired |

## 15) Safety Checklist Before First Power-On

- [ ] IEC C13 inlet is mechanically secure and insulated from low-voltage wiring.
- [ ] 3A slow-blow AC fuse is fitted and correctly rated.
- [ ] PSU AC polarity and earth wiring verified against terminal labels.
- [ ] PSU output measured unloaded and confirmed near target ~20V before branch connection.
- [ ] All five branch polyfuses installed and value-checked.
- [ ] TVS diodes fitted on both USB-C output branches (Zones 4 and 5).
- [ ] No continuity short between 20V rail and GND (multimeter check).
- [ ] No continuity short between 3.3V rail and GND.
- [ ] Thermistor divider readings are plausible at room temperature.
- [ ] I2C scan passes with expected unique addresses before high-power load tests.
- [ ] LED strip polarity and data direction (DIN) verified.
- [ ] Common ground continuity confirmed across PSU, MCU, sensors, and LED branch.

## 16) Full-System ASCII Schematic

```text
                    AC MAINS
                       |
              [ IEC C13 INLET ]
                       |
                 [ 3A SLOW FUSE ]
                       |
             +---------------------+
             | 180W AC/DC PSU      |
             | (100-240VAC -> 20V) |
             +---------------------+
                  |            |
                +20V          GND
                  |            |
                  +----[470-1000uF]----+
                  |                     |
                  |               STAR GND NODE
                  |
      ================== 20V DISTRIBUTION BUS ==================
         |            |             |              |          |
         |            |             |              |          |
      [Z1 BR]      [Z2 BR]       [Z3 BR]        [Z4 BR]    [Z5 BR]
         |            |             |              |          |
   [12V BUCK]   [12V BUCK]      [5V BUCK]   [PD 100W BD] [9-12V BUCK]
         |            |             |              |          |
      [QI TX]      [QI TX]    [WATCH PUCK]     [INA219]  [PD 20W BD]
         |            |             |              |          |
     [2A PFUSE]   [2A PFUSE]    [1A PFUSE]     [6A PFUSE]  [INA219]
         |            |             |              |          |
      [NTC->ADC2] [NTC->ADC3]  [NTC->ADC10]   [TVS OUT]  [2A PFUSE]
                                                       |       |
                                                [USB-C Z4]  [TVS OUT]
                                                             |
                                                         [USB-C Z5]


                 LOGIC/SENSING POWER + CONTROL

                     [5V LOGIC SOURCE]
                            |
                         [3.3V LDO]
                            |
        +-------------------+-------------------------------+
        |                   |               |               |
     [ESP32-C3]         [INA3221]      [INA219 Z4]     [INA219 Z5]
        |                   |               |               |
        +-------------------+---------------+---------------+
                            |
                          I2C BUS
                     SDA=GPIO8 SCL=GPIO9
                        (4.7k pull-ups)
                            |
                         [BH1750]

 ESP32 GPIO4 --[300-470R]--> WS2812 DIN
 5V ------------------------> WS2812 VCC
 GND -----------------------> WS2812 GND
 (100uF across VCC/GND at strip entry)
```

## 17) Practical Integration Notes

- Keep Zone 4 harness mechanically restrained to avoid repeated flex stress at the PD board.
- Route thermistor leads away from high-current conductors to reduce ADC noise.
- Validate each branch standalone first, then progressively combine into full system test.
- Keep final harness map aligned to coordinates in [component-positions.md](component-positions.md) for repeatable builds.
