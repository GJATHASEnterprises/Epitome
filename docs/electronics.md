# Epitome Penta — Electronics Specification

## Main Electronics

- MCU: ESP32-C3 Mini
- Monitoring: INA3221 (Zones 1–3), INA219 Zone 4 (100W), INA219 Zone 5 (20W)
- Ambient sensor: BH1750
- Power: internal 180W AC/DC PSU + IEC C13 inlet
- Outputs: 2×15W Qi, 1×Watch puck, 2×USB-C PD boards (100W + 20W)

## Exact Placement Coordinates

Exact interior/exterior positions are defined in [component-positions.md](component-positions.md).

Key electronics placements:

- PCB main board center: `X=-35.00, Y=110.00, Z=5.00`
- PCB extents: **X:-95.00..+25.00, Y:70.00..150.00**
- PCB standoff height: **5.00mm**
- PSU module center: `X=0.00, Y=210.00, Z=5.00`
- Qi coils: `(-45.00,60.00,4.00)` and `(-45.00,140.00,4.00)`
- Watch puck module: `(-45.00,225.00,4.00)`
- USB-C PD board Zone 4 center: `(+40.00,150.00,5.00)`
- USB-C PD board Zone 5 center: `(+80.00,150.00,5.00)`
- Zone 5 INA219: `(+75.00,150.00,8.50)`
- Zone 5 USB-C port: `(+80.00,258.00,8.00)`

## Power Path

`IEC C13 -> 180W PSU -> zone branches + regulation -> monitoring + protections`

- Zone 1: Qi 15W + polyfuse + thermistor
- Zone 2: Qi 15W + polyfuse + thermistor
- Zone 3: Watch puck + polyfuse + thermistor
- Zone 4: USB-C PD 100W + INA219 + polyfuse + thermistor
- Zone 5: USB-C PD 20W + INA219 + polyfuse + thermistor

## Power Budget

| Zone | Power |
|---|---:|
| Zone 1 Phone Qi2 | 15W |
| Zone 2 Buds Qi | 5W |
| Zone 3 Watch | 5W |
| Zone 4 Laptop | 100W |
| Zone 5 iPad/Phone | 20W |
| **Total** | **145W** |
| PSU (180W) headroom | **35W spare** |

## PCB Layout Notes

- Board position is fixed at **X:-95..+25, Y:70..150 on 5mm standoffs**.
- Keep Qi power traces wide and short to entry points near `Y≈60` and `Y≈140`.
- Keep INA3221 and both INA219 monitors close to their branch sensing points.
- Route the Zone 5 PD branch to the right-half secondary groove and keep the 20W board close to the `X=+80` slot.
- Keep ESP32-C3 antenna near the board edge with copper keep-out.
- Place BH1750 near edge exposure side for reliable ambient readings.

## Night Mode / Sleep Mode

- **Trigger:** local time 23:00–07:00 (configurable via app, default ON)
- **LED behaviour:** all zone LEDs off unless that zone has active power draw > 0.5W (read via INA3221/INA219)
- **Notification behaviour:** theft alert push notifications silenced overnight (configurable, default ON)
- **Implementation:** ESP32-C3 stores time via SNTP over WiFi; falls back to BLE-synced time from phone if no WiFi
- **Override:** placing a new device on any zone during night mode briefly illuminates that zone's LED for 3 seconds to confirm charging started, then returns to off

---

## Comprehensive Electronics Engineering Expansion (Revision A)

This section is a full electrical reference intended for design review, prototype bring-up, and PCB implementation.

### Cross-Reference Documents

- Mechanical positions: [component-positions.md](component-positions.md)
- Wiring implementation: [wiring.md](wiring.md)
- Firmware night mode and timing: [firmware-notes.md](firmware-notes.md)
- Procurement and target parts: [bom.md](bom.md)

## 1) Full System Architecture Narrative

Epitome Penta uses a centralized internal AC/DC supply to generate a robust 20V primary DC rail. That rail is split into five protected zone branches plus a low-voltage logic branch. High-power and low-power branches are electrically isolated at distribution points with per-zone fusing and monitoring so the firmware can provide per-zone telemetry and safety behaviors.

- **Control/Connectivity Core:** ESP32-C3 Mini (WiFi + BLE) orchestrates telemetry, user control, and LED behavior.
- **Zone Power Telemetry:** INA3221 measures Zones 1–3; separate INA219 devices independently measure Zones 4 and 5.
- **Ambient Feedback:** BH1750 provides lux measurement for dynamic LED dim control and environmental context for night mode UX.
- **User Feedback Plane:** WS2812B strip is segmented logically into five sections (4 LEDs per zone).
- **Energy Source:** Internal 180W PSU (Mean Well LRS-200-24 adjusted to ~20V) receives 100–240VAC via rear IEC C13 inlet.

Architecture objective: maintain reliable multi-zone charging while exposing measurable, firmware-usable, per-zone power state with sufficient electrical headroom.

## 2) Core Controller — ESP32-C3 Mini

| Parameter | Specification |
|---|---|
| MCU core | 32-bit RISC-V single core |
| Wireless | WiFi 802.11 b/g/n (2.4 GHz), BLE 5.0 |
| Flash | 4 MB onboard |
| GPIO capacity | ESP32-C3 SoC supports up to 22 GPIO functions (module/board breakout exposes a subset); used pins listed in GPIO table |
| Supply | 3.3V from local LDO |
| Programming | Onboard USB flashing path |
| GPIO use model | I2C, ADC thermistors, WS2812 data, optional zone enable lines |

Design rationale:
- Chosen for integrated WiFi + BLE at low cost and compact footprint.
- 3.3V logic domain aligns with BH1750 and monitor IC logic interfaces.
- USB-flash convenience reduces prototype bring-up friction and fixture complexity.

## 3) Power Monitoring ICs

### INA3221 (Zones 1–3)

| Parameter | Specification |
|---|---|
| Type | 3-channel high-side current/voltage monitor |
| Bus interface | I2C |
| Typical shunt | 0.1Ω per channel |
| Address control | A0 pin configurable |
| Channel mapping | CH1=Zone 1, CH2=Zone 2, CH3=Zone 3 |

Address options (A0 strap):
- GND: 0x40
- VCC: 0x41
- SDA: 0x42
- SCL: 0x43

### INA219 (Zone 4)

| Parameter | Specification |
|---|---|
| Type | Single-channel high-side current/voltage monitor |
| Bus interface | I2C |
| Typical shunt | 0.1Ω |
| Address control | A0/A1 pin strap combinations |
| Monitored branch | Zone 4 USB-C PD (100W branch) |

### INA219 (Zone 5)

| Parameter | Specification |
|---|---|
| Type | Same IC family as Zone 4 monitor |
| Bus interface | I2C |
| Typical shunt | 0.1Ω |
| Address control | Different A0/A1 strap from Zone 4 |
| Monitored branch | Zone 5 USB-C PD (20W branch) |

## 4) Ambient Sensor — BH1750

| Parameter | Specification |
|---|---|
| Interface | I2C |
| Address options | 0x23 (ADDR low), 0x5C (ADDR high) |
| Measurement range | 1 to 65535 lux |
| Role in system | Ambient-dim control + contextual night-mode behavior |

Configured default: ADDR low (0x23) unless bus conflict requires remap.

## 5) LED Engine — WS2812B

| Parameter | Specification |
|---|---|
| LED type | Addressable RGB |
| Supply voltage | 5V |
| Data input conditioning | 300–470Ω series resistor on MCU data line |
| Strip entry decoupling | 100µF electrolytic cap across 5V/GND |
| Physical quantity | 20 LEDs total (4/zone) |
| Source format | Cut from 60 LEDs/m reel |

Electrical integrity notes:
- Keep common ground between ESP32 and LED supply.
- Place series data resistor close to MCU output pin.
- Place 100µF capacitor physically at strip power entry pads.

## 6) Main Power Supply Unit

| Parameter | Specification |
|---|---|
| Model baseline | Mean Well LRS-200-24 (trim-adjusted to ~20V output target) |
| Input | 100–240VAC |
| Inlet | Rear IEC C13 panel inlet |
| Nominal available output | 180W usable target for this product spec |
| System full-load design | 145W total branch budget |
| Headroom | 35W |
| Protection expectation | AC line fuse + branch protection + output fusing strategy |

PSU is positioned rearward in enclosure to support thermal behavior and mechanical center-of-gravity targets (see [component-positions.md](component-positions.md)).

## 7) Power Architecture and Distribution Narrative

### Primary Distribution

1. AC enters through IEC C13 inlet and safety fuse.
2. PSU converts AC to regulated ~20V DC.
3. 20V rail feeds bulk capacitor and main distribution bus.
4. Bus branches split into 5 independent zone paths plus logic regulation branch.

### Zone 1 — Qi 15W Path

`20V rail → 12V buck converter → 50mm Qi TX module (15W) → polyfuse → NTC thermistor supervision`

Notes:
- N52 ring magnet mechanical stack-up assists alignment but does not participate electrically.
- Polyfuse is sized for zone overcurrent protection with resettable behavior.

### Zone 2 — Qi 5W Path

`20V rail → 12V buck converter → Qi TX module (5W budget) → polyfuse → NTC thermistor supervision`

Notes:
- Uses same architecture class as Zone 1 but lower negotiated/allocated power budget.
- Thermal and EMI coupling are improved by lower steady-state current.

### Zone 3 — Apple Watch Path

`20V rail → 5V buck converter → Apple Watch puck module (5W) → polyfuse → NTC thermistor supervision`

### Zone 4 — USB-C PD 100W Path

`20V rail → USB-C PD 100W board → INA219 Zone 4 current/voltage monitor → polyfuse → TVS diode at output`

Notes:
- High-current branch, shortest practical routing and heavier copper/wire recommendation.
- TVS clamps transients on user-facing USB-C output.

### Zone 5 — USB-C PD 20W Path

`20V rail → 9V–12V step-down → USB-C PD 20W board → INA219 Zone 5 monitor → polyfuse → TVS diode at output`

## 8) Logic Rail and 3.3V LDO

`5V intermediary rail (or validated direct source path) → 3.3V LDO → ESP32-C3 + INA3221 + INA219x2 + BH1750`

The 3.3V domain is intentionally shared for all control and sensor ICs to simplify level compatibility and reduce conversion complexity.

## 9) I2C Bus Definition

- **SDA:** GPIO 8
- **SCL:** GPIO 9
- **Pull-ups:** 4.7kΩ to 3.3V (shared bus)

### I2C Bus Node and Address Table

| Device | Function | Address | Address Strap/Setting |
|---|---|---|---|
| ESP32-C3 (I2C master) | Bus controller | N/A (master) | Fixed firmware role, no slave address used |
| INA3221 | Zones 1–3 monitor | 0x40 (default) | A0→GND |
| INA219 Z4 | Zone 4 monitor | 0x41 (example) | A0/A1 strap per module |
| INA219 Z5 | Zone 5 monitor | 0x44 (example) | A0/A1 strap distinct from Z4 |
| BH1750 | Ambient lux sensor | 0x23 (default) | ADDR→GND |

If module strap maps differ by vendor breakout, keep uniqueness as the primary requirement and update firmware constants accordingly.

## 10) Full GPIO Assignment Table

| GPIO | Direction | Function | Voltage Domain |
|---|---|---|---|
| GPIO 8 | Bi-dir | I2C SDA (INA3221, INA219 Z4, INA219 Z5, BH1750) | 3.3V |
| GPIO 9 | Output/Input | I2C SCL (shared bus clock) | 3.3V |
| GPIO 4 | Output | WS2812B data stream | 3.3V logic to LED DIN |
| GPIO 5 | Output (optional) | Zone 1 enable/control line | 3.3V |
| GPIO 6 | Output (optional) | Zone 2 enable/control line | 3.3V |
| GPIO 7 | Output (optional) | USB-C PD enable/control line | 3.3V |
| GPIO 2 | ADC input | NTC Zone 1 divider readback | 3.3V ref |
| GPIO 3 | ADC input | NTC Zone 2 divider readback | 3.3V ref |
| GPIO 10 | ADC input | NTC Zone 3 divider readback | 3.3V ref |
| GPIO 1 | ADC input | NTC Zone 5 divider readback | 3.3V ref |
| USB | USB | Firmware flashing + maintenance | N/A |

## 11) Safety Systems

| Safety Element | Location | Purpose |
|---|---|---|
| AC slow-blow fuse | IEC inlet line side | Protects against input faults/inrush anomalies |
| Polyfuse per zone | All 5 zone branches | Local overcurrent isolation |
| TVS diode | USB-C zone outputs | Surge/transient suppression |
| NTC thermistor feedback | Heat-critical zones | Firmware thermal detection and mitigation |
| Bulk capacitor (470–1000µF) | 20V rail entry | Load-step buffering and ripple damping |
| Output branch fusing strategy | DC branches | Limits fault propagation |

## 12) Night Mode Firmware Behavior

| Parameter | Behavior |
|---|---|
| Schedule | 23:00–07:00 local time |
| Time source | SNTP first, BLE time fallback |
| LED gating threshold | 0.5W zone power draw |
| Indicator override | 3-second flash on new night-time charge event |
| User control | App-configurable enable/disable and related preferences |

See [firmware-notes.md](firmware-notes.md) for the concise baseline definition.

## 13) Thermal Management Strategy

- PSU is rear-positioned to separate concentrated AC/DC heat from front-touch user areas.
- Wireless zones are physically separated from high-current USB-C branch regions.
- Eight underside vents establish passive convection path through base cavity.
- NTC thermistors provide direct firmware observability of heat-prone subassemblies.
- Power budget maintains 35W margin below PSU nominal output to reduce sustained thermal stress.

## 14) PCB Layout Notes (Manufacturing-Facing)

| Item | Requirement |
|---|---|
| Layer stack | 2-layer PCB |
| Panelization | 4 boards/panel at JLCPCB |
| High-current traces | Size to branch current demand; prioritize wide, short runs |
| Qi branch routing | Short, low-impedance feed from buck to TX module |
| Grounding | Solid ground plane strategy with controlled analog tie-in |
| Antenna keepout | ESP32-C3 antenna edge placement; no copper under keepout |
| Sensor placement | Place INA/BH1750 physically near function domains |
| Protection placement | Keep polyfuses/TVS close to branch/output interfaces |

Recommended trace width guidance (starting points; finalize by copper thickness and temp rise target):
- 20V main rail and Zone 4 high-current branch: wide copper pours/traces, target 2.0–3.0 mm or equivalent copper area.
- Zone 1/2/3 moderate-current branches: target ~1.0–1.5 mm.
- Logic and I2C traces: 0.20–0.30 mm typical.

## 15) Power Budget Table (Final Reference)

| Zone | Function | Max Power |
|---|---|---:|
| Zone 1 | Qi phone charging | 15W |
| Zone 2 | Qi buds/secondary charging | 5W |
| Zone 3 | Apple Watch puck | 5W |
| Zone 4 | USB-C PD laptop branch | 100W |
| Zone 5 | USB-C PD tablet/phone branch | 20W |
| **Total load** |  | **145W** |
| **PSU nominal output budget** |  | **180W** |
| **Headroom** |  | **35W** |

## 16) Design Intent Summary

The electronics architecture intentionally combines modular charging hardware with explicit per-zone instrumentation. This enables robust UX (clear zone state feedback and app intelligence), practical safety (fuse + TVS + thermal sensing), and manufacturable implementation (2-layer board, standard modules, clear branch separation) while staying inside a controlled 145W system envelope.
