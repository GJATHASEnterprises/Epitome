# Penta Dock — Electronics Specification

## Main Electronics

- MCU: ESP32-C3 Mini
- Power safety controller: ATtiny85 (enforces global 185W soft cap)
- Monitoring: **INA3221 #1 (Zones 1–3) + INA3221 #2 (Zones 4–5 + spare/system)**
- Ambient sensor: **Removed (BH1750 dropped for cost reduction)**
- Power: internal **201W** AC/DC PSU (**Mean Well LRS-200-24, 201W, 24V output trim-adjusted to ~20V. Physical size: 199×98×30mm. Located under centre platform.**) + **right-angle IEC C13 inlet**
- Outputs: 20W Qi2 (Zone 1), 20W Qi (Zone 2), Zone 3 dual charger (Apple puck + Qi coil sharing 5W), 2×USB-C PD branches (100W + 45W)
- Lighting: WS2811 addressable strip

## Exact Placement Coordinates

Exact interior/exterior positions are defined in [component-positions.md](component-positions.md).

Key placement updates:
- PSU now sits under the **centre platform cavity**
- Zone 3 includes both Apple puck module and Qi watch coil in same cradle region
- Zone 4 and Zone 5 terminate to captive cable harnesses
- Centre platform uses three 15mm steps above a 20mm riser cavity

## Power Path

`Right-angle IEC C13 -> 201W PSU (Mean Well LRS-200-24, under centre platform cavity) -> zone branches + regulation -> monitoring + protections`

- Zone 1: Qi2 20W TX module (Qi2 certified, magnetic alignment ring compatible) + polyfuse + thermistor
- Zone 2: Qi 20W + polyfuse + thermistor
- Zone 3: Apple puck + Qi watch coil, shared 5W policy (single active target)
- Zone 4: USB-C PD 100W + INA3221 #2 + captive 220mm cable harness
- Zone 5: USB-C PD 45W + INA3221 #2 + captive 200mm cable harness (65W rated cable)

## Power Budget

| Zone | Device | Power | Method |
|---|---|---|---|
| Zone 1 | Phone | 20W | Qi2 (magnetic alignment) |
| Zone 2 | Buds or second phone | 20W | Qi |
| Zone 3 | Watch | 5W | Apple Watch puck + Qi coil |
| Zone 4 | Laptop | 100W | USB-C PD (captive braided cable) |
| Zone 5 | Tablet | 45W | USB-C PD (captive braided cable) |
| **Total worst case** | | **190W** | |
| **PSU rated** | | **201W (Mean Well LRS-200-24)** | |
| **Headroom** | | **11W** | |
| **ATtiny85 soft cap** | | **185W** | |

## PCB Layout Notes

- Board position remains fixed reference for Rev A.
- Keep Zone 4 and Zone 5 output pads aligned to captive cable strain-relief anchors.
- Add zone-3 mux/switching logic footprint for puck-vs-Qi exclusivity (single-device mode).
- Keep ESP32-C3 antenna near board edge with copper keep-out.
- Add PCB **PTC resettable fuse** stage on main branch protection path (replaces inlet fuse holder).
- **Logic board (ESP32-C3 + INA3221 ×2) mounts in the 20mm riser cavity between PSU top (Z=33mm) and Step 1 base (Z=50mm).**

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

Penta Dock uses a centralized internal AC/DC supply to generate a 20V primary DC rail. That rail is split into five protected zone branches plus a low-voltage logic branch.

Architecture update highlights:
- PSU is Mean Well LRS-200-24 (201W nominal) with a 185W ATtiny85 soft cap.
- Zone 3 supports Apple Watch magnetic protocol plus generic Qi-watch charging in one cradle footprint.
- Zone 4 and Zone 5 use captive braided cables.
- Ambient auto-dim sensor removed; brightness is app-controlled.
- PSU sits under the centre platform so the step bodies can carry the embedded coils directly above the wiring cavity.

## 2) Core Controller — ESP32-C3 Mini

| Parameter | Specification |
|---|---|
| MCU core | 32-bit RISC-V single core |
| Wireless | WiFi 802.11 b/g/n (2.4 GHz), BLE 5.0 |
| Flash | 4 MB onboard |
| Supply | 3.3V from local LDO |

## 3) Power Monitoring ICs

### INA3221 #1 (Zones 1–3)

| Parameter | Specification |
|---|---|
| Type | 3-channel high-side current/voltage monitor |
| Channel mapping | CH1=Zone 1, CH2=Zone 2, CH3=Zone 3 |
| Address | 0x40 |

### INA3221 #2 (Zones 4–5 + spare/system)

| Parameter | Specification |
|---|---|
| Type | 3-channel high-side current/voltage monitor |
| Channel mapping | CH1=Zone 4, CH2=Zone 5, CH3=spare/system |
| Address | 0x41 (A0 pin high) |

## 4) LED Engine — WS2811

- 20 LEDs total (4/zone)
- Data protocol differs from WS2812B timing implementation; firmware driver selection must match WS2811 signal model.

## 5) Main Power Supply Unit

| Parameter | Specification |
|---|---|
| Model baseline | Mean Well LRS-200-24 or equivalent (trim-adjusted to ~20V output target) |
| Physical size | 199×98×30mm |
| Input | 100–240VAC |
| Inlet | **Rear right-angle IEC C13** |
| Nominal available output | **201W (Mean Well LRS-200-24)** |
| System full-load design | **190W total branch budget** |
| Headroom | **11W** |
| Firmware global cap | **185W** |

PSU location: **under centre platform cavity**.

## 6) Power Architecture and Distribution Narrative

### Primary Distribution
1. AC enters through right-angle IEC C13 inlet.
2. PSU converts AC to regulated ~20V DC.
3. 20V rail feeds bulk capacitor and main distribution bus.
4. Bus branches split into 5 independent zone paths plus logic regulation branch.
5. PCB PTC resettable fuse provides overcurrent protection in place of separate inlet fuse holder.

### Zone 1 — Qi 20W Path
`20V rail -> 12V buck -> Qi TX module (20W)`

### Zone 2 — Qi 20W Path
`20V rail -> 12V buck -> Qi TX module (20W)`

### Zone 3 — Watch Universal 5W Path
`20V rail -> 5V buck -> dual-output watch branch (Apple puck + Qi watch coil) with firmware/hardware mutual-exclusion`

### Zone 4 — USB-C PD 100W Path
`20V rail -> USB-C PD 100W board -> INA3221 #2 CH1 -> captive 220mm cable (USB-C male free end)`

### Zone 5 — USB-C PD 45W Path
`20V rail -> USB-C PD 45W board -> INA3221 #2 CH2 -> captive 200mm cable (USB-C male free end, 65W rated)`

## 7) Logic Rail and 3.3V LDO

`5V intermediary -> 3.3V LDO -> ESP32-C3 + INA3221 x2`

## 8) I2C Bus Definition

- **SDA:** GPIO 8
- **SCL:** GPIO 9
- **Pull-ups:** 4.7kΩ to 3.3V

### I2C Bus Node and Address Table

| Device | Function | Address |
|---|---|---|
| INA3221 #1 | Zones 1–3 monitor | 0x40 |
| INA3221 #2 | Zones 4–5 + spare/system monitor | 0x41 |

## 9) Full GPIO Assignment Table

| GPIO | Function |
|---|---|
| GPIO 8 | I2C SDA |
| GPIO 9 | I2C SCL |
| GPIO 4 | WS2811 data |
| GPIO 2/3/10/1 | NTC ADC inputs |

## 10) Safety Systems

- PCB PTC resettable fuse on main protection path
- Polyfuse per zone output
- TVS on PD outputs
- NTC thermistor feedback in heat-prone zones

## 11) Night Mode Firmware Behavior

| Parameter | Behavior |
|---|---|
| Schedule | 23:00–07:00 |
| LED gating threshold | 0.5W zone draw |
| Zone 3 mode | detect puck-vs-Qi watch path, allow one active charging path at a time |

## 12) Thermal Management Strategy

- PSU now positioned under centre platform.
- Centre platform perimeter wall creates an enclosed PSU cavity with 20mm riser space above for wiring.
- Thermal isolation from slot zones is maintained by physical separation.
- 11W power headroom (190W load, 201W PSU), backed by 185W ATtiny85 soft cap to avoid sustained edge load.

## 13) PCB Layout Notes (Manufacturing-Facing)

- 2-layer PCB
- Add mechanical anchoring for captive cable strain relief on Zones 4 and 5
- Keep watch dual-mode branch routing short and isolated
- Keep dual INA3221 traces short and symmetric for measurement consistency
- Mount ESP32-C3 + INA3221 ×2 assembly in the 20mm riser cavity for short, flat I2C routing

## 14) Power Budget Table (Final Reference)

| Zone | Device | Power | Method |
|---|---|---|---|
| Zone 1 | Phone | 20W | Qi2 (magnetic alignment) |
| Zone 2 | Buds or second phone | 20W | Qi |
| Zone 3 | Watch | 5W | Apple Watch puck + Qi coil |
| Zone 4 | Laptop | 100W | USB-C PD (captive braided cable) |
| Zone 5 | Tablet | 45W | USB-C PD (captive braided cable) |
| **Total worst case** | | **190W** | |
| **PSU rated** | | **201W (Mean Well LRS-200-24)** | |
| **Headroom** | | **11W** | |
| **ATtiny85 soft cap** | | **185W** | |

## 15) Design Intent Summary

The electronics architecture remains modular and monitorable, while now adding universal watch support, safer captive cable UX for both slots, dual INA3221 monitoring, and a tightly packaged 201W PSU envelope under the centre platform with a dedicated riser cavity for logic and coil routing.

## Wattage Etch Labels

```
PHONE    20W  Qi2
BUDS     20W  Qi
WATCH     5W
LAPTOP  100W  USB-C
TABLET   45W  USB-C
```
