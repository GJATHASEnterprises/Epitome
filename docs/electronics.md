# Epitome Penta — Electronics Specification

## Main Electronics

- MCU: ESP32-C3 Mini
- Monitoring: INA3221 (Zones 1–3), INA219 Zone 4 (100W), INA219 Zone 5 (20W)
- Ambient sensor: BH1750
- Power: internal 180W AC/DC PSU + **right-angle IEC C13 inlet**
- Outputs: 2×15W Qi, **Zone 3 dual charger (Apple puck + Qi coil sharing 5W)**, 2×USB-C PD branches (100W + 20W)

## Exact Placement Coordinates

Exact interior/exterior positions are defined in [component-positions.md](component-positions.md).

Key placement updates:
- PSU moved under laptop slot cavity
- Zone 3 includes both Apple puck module and Qi watch coil in same cradle region
- Zone 4 and Zone 5 no longer expose fixed rear-wall user ports; each branch now terminates to captive cable harnesses

## Power Path

`Right-angle IEC C13 -> 180W PSU (under laptop slot) -> zone branches + regulation -> monitoring + protections`

- Zone 1: Qi 15W + polyfuse + thermistor
- Zone 2: Qi 15W + polyfuse + thermistor
- Zone 3: Apple puck + Qi watch coil, shared 5W policy (single active target)
- Zone 4: USB-C PD 100W + INA219 + captive cable harness
- Zone 5: USB-C PD 20W + INA219 + captive cable harness

## Power Budget

| Zone | Power |
|---|---:|
| Zone 1 Phone Qi2 | 15W |
| Zone 2 Buds/Phone Qi | 15W |
| Zone 3 Watch (puck or Qi) | 5W |
| Zone 4 Laptop | 100W |
| Zone 5 Tablet/Phone | 20W |
| **Total** | **155W** |
| PSU (180W) headroom | **25W spare** |

## PCB Layout Notes

- Board position remains fixed reference for Rev A.
- Keep Zone 4 and Zone 5 output pads aligned to captive cable strain-relief anchors.
- Add zone-3 mux/switching logic footprint for puck-vs-Qi exclusivity (single-device mode).
- Keep ESP32-C3 antenna near board edge with copper keep-out.

## Night Mode / Sleep Mode

- **Trigger:** local time 23:00–07:00 (configurable via app, default ON)
- **LED behaviour:** all zone LEDs off unless that zone has active power draw > 0.5W
- **Notification behaviour:** theft alert push notifications silenced overnight (configurable, default ON)
- **Override:** placing a new device on any zone during night mode briefly illuminates that zone's LED for 3 seconds

---

## Comprehensive Electronics Engineering Expansion (Revision A)

This section is a full electrical reference intended for design review, prototype bring-up, and PCB implementation.

### Cross-Reference Documents

- Mechanical positions: [component-positions.md](component-positions.md)
- Wiring implementation: [wiring.md](wiring.md)
- Firmware thresholds and dual-mode behavior: [firmware-notes.md](firmware-notes.md)
- Procurement and target parts: [bom.md](bom.md)

## 1) Full System Architecture Narrative

Epitome Penta uses a centralized internal AC/DC supply to generate a 20V primary DC rail. That rail is split into five protected zone branches plus a low-voltage logic branch.

Architecture update highlights:
- PSU heat source moved under Zone 4 cavity to reduce thermal coupling to Qi surfaces.
- Zone 3 supports Apple Watch magnetic protocol plus generic Qi-watch charging in one cradle footprint.
- Zone 4 and Zone 5 user-side cable interface changed from fixed panel ports to captive braided cables for safer insertion UX.

## 2) Core Controller — ESP32-C3 Mini

| Parameter | Specification |
|---|---|
| MCU core | 32-bit RISC-V single core |
| Wireless | WiFi 802.11 b/g/n (2.4 GHz), BLE 5.0 |
| Flash | 4 MB onboard |
| Supply | 3.3V from local LDO |

## 3) Power Monitoring ICs

### INA3221 (Zones 1–3)

| Parameter | Specification |
|---|---|
| Type | 3-channel high-side current/voltage monitor |
| Channel mapping | CH1=Zone 1, CH2=Zone 2, CH3=Zone 3 |

### INA219 (Zone 4)
- Monitored branch: Zone 4 USB-C PD (100W branch)

### INA219 (Zone 5)
- Monitored branch: Zone 5 USB-C PD (20W branch)

## 4) Ambient Sensor — BH1750

- Interface: I2C
- Role: ambient dim + night mode context

## 5) LED Engine — WS2812B

- 20 LEDs total (4/zone)

## 6) Main Power Supply Unit

| Parameter | Specification |
|---|---|
| Model baseline | Mean Well LRS-200-24 (trim-adjusted to ~20V output target) |
| Input | 100–240VAC |
| Inlet | **Rear right-angle IEC C13** |
| Nominal available output | 180W usable target |
| System full-load design | **155W total branch budget** |
| Headroom | **25W** |

PSU location: **under laptop slot cavity**.

## 7) Power Architecture and Distribution Narrative

### Primary Distribution
1. AC enters through right-angle IEC C13 inlet and safety fuse.
2. PSU converts AC to regulated ~20V DC.
3. 20V rail feeds bulk capacitor and main distribution bus.
4. Bus branches split into 5 independent zone paths plus logic regulation branch.

### Zone 1 — Qi 15W Path
`20V rail -> 12V buck -> Qi TX module (15W)`

### Zone 2 — Qi 15W Path
`20V rail -> 12V buck -> Qi TX module (15W)`

### Zone 3 — Watch Universal 5W Path
`20V rail -> 5V buck -> dual-output watch branch (Apple puck + Qi watch coil) with firmware/hardware mutual-exclusion`

### Zone 4 — USB-C PD 100W Path
`20V rail -> USB-C PD 100W board -> INA219 -> captive 300mm cable (USB-C male free end)`

### Zone 5 — USB-C PD 20W Path
`20V rail -> USB-C PD 20W board -> INA219 -> captive 200mm cable (USB-C male free end)`

## 8) Logic Rail and 3.3V LDO

`5V intermediary -> 3.3V LDO -> ESP32-C3 + INA3221 + INA219x2 + BH1750`

## 9) I2C Bus Definition

- **SDA:** GPIO 8
- **SCL:** GPIO 9
- **Pull-ups:** 4.7kΩ to 3.3V

### I2C Bus Node and Address Table

| Device | Function | Address |
|---|---|---|
| INA3221 | Zones 1–3 monitor | 0x40 default |
| INA219 Z4 | Zone 4 monitor | 0x41 example |
| INA219 Z5 | Zone 5 monitor | 0x44 example |
| BH1750 | Ambient lux sensor | 0x23 default |

## 10) Full GPIO Assignment Table

| GPIO | Function |
|---|---|
| GPIO 8 | I2C SDA |
| GPIO 9 | I2C SCL |
| GPIO 4 | WS2812B data |
| GPIO 2/3/10/1 | NTC ADC inputs |

## 11) Safety Systems

- AC fuse at inlet
- Polyfuse per zone
- TVS on PD outputs
- NTC thermistor feedback in heat-prone zones

## 12) Night Mode Firmware Behavior

| Parameter | Behavior |
|---|---|
| Schedule | 23:00–07:00 |
| LED gating threshold | 0.5W zone draw |
| Zone 3 mode | detect puck-vs-Qi watch path, allow one active charging path at a time |

## 13) Thermal Management Strategy

- PSU repositioned under Zone 4 cavity, away from centre wireless zones
- Wireless zones physically separated from highest-current branch
- 25W power headroom retained for safe thermal margin

## 14) PCB Layout Notes (Manufacturing-Facing)

- 2-layer PCB
- Add mechanical anchoring for captive cable strain relief on Zones 4 and 5
- Keep watch dual-mode branch routing short and isolated

## 15) Power Budget Table (Final Reference)

| Zone | Function | Max Power |
|---|---|---:|
| Zone 1 | Qi phone charging | 15W |
| Zone 2 | Qi buds/secondary phone | 15W |
| Zone 3 | Apple puck or Qi watch | 5W |
| Zone 4 | USB-C PD laptop branch | 100W |
| Zone 5 | USB-C PD tablet/phone branch | 20W |
| **Total load** |  | **155W** |
| **PSU nominal output budget** |  | **180W** |
| **Headroom** |  | **25W** |

## 16) Design Intent Summary

The electronics architecture remains modular and monitorable, while now adding universal watch support, safer captive cable UX for both slots, and improved thermal placement of the PSU.
