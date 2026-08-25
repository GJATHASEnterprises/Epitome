# Penta Dock — Electronics Specification

## Main Electronics

- LED logic controller: **ATtiny85** (programmed at assembly — zone LED logic + global 185W soft cap)
- Power: internal **201W** AC/DC PSU (**Mean Well LRS-200-24, 201W, 24V output trim-adjusted to ~20V. Physical size: 199×98×30mm. Located under centre platform.**) + **right-angle IEC C13 inlet**
- Outputs: 20W Qi2 (Zone 1), 20W Qi (Zone 2, 120×80mm dish), Zone 3 dual charger (Apple puck + Qi coil sharing 5W, hardware relay for mutual exclusion), 2×USB-C PD branches (100W + 45W)
- Lighting: WS2811 addressable LED strip (~15 LED, 250mm)
- **NO ESP32, NO INA3221, NO BLE, NO WiFi, NO app hardware in Batch 1**

## Exact Placement Coordinates

Exact interior/exterior positions are defined in [component-positions.md](component-positions.md).

Key placement updates:
- PSU now sits under the **centre platform cavity**
- Zone 3 includes both Apple puck module and Qi watch coil in same cradle region
- Zone 4 and Zone 5 terminate to captive cable harnesses
- Centre platform uses three 15mm steps above a 20mm riser cavity

## Power Path

`Right-angle IEC C13 -> 201W PSU (Mean Well LRS-200-24, under centre platform cavity) -> zone branches + regulation -> protections`

- Zone 1: Qi2 20W TX module (Qi2 certified, magnetic alignment N52 ring, recessed 1mm dish) + polyfuse + thermistor
- Zone 2: Qi 20W (120×80mm dish) + polyfuse + thermistor
- Zone 3: Apple puck + Qi watch coil, shared 5W policy (hardware relay enforces single active target)
- Zone 4: USB-C PD 100W + captive 220mm cable harness (100W braided, 90° angled dock-end) + silicone strain relief boot at exit
- Zone 5: USB-C PD 45W + captive 200mm cable harness (65W rated braided, 90° angled dock-end) + silicone strain relief boot at exit

## Power Budget

| Zone | Device | Power | Method |
|---|---|---|---|
| Zone 1 | Phone | 20W | Qi2 (magnetic alignment, N52 ring, recessed 1mm dish) |
| Zone 2 | Buds or second phone | 20W | Qi (120×80mm dish) |
| Zone 3 | Watch | 5W | Apple Watch puck + Qi coil, hardware relay |
| Zone 4 | Laptop | 100W | USB-C PD (captive 220mm braided cable) |
| Zone 5 | Tablet | 45W | USB-C PD (captive 200mm braided cable, 65W rated) |
| **Total worst case** | | **190W** | |
| **PSU rated** | | **201W (Mean Well LRS-200-24)** | |
| **Headroom** | | **11W** | |
| **ATtiny85 soft cap** | | **185W** | |

## ATtiny85 LED Logic

- ATtiny85 is the sole MCU — no ESP32, no wireless, no app
- Programmed at assembly with zone LED logic
- Controls WS2811 strip via single data line
- Enforces global 185W soft power cap
- Per-zone LED colours:
  - Zone 1 Phone: blue
  - Zone 2 Buds or second phone: purple
  - Zone 3 Watch: green
  - Zone 4 Laptop: orange
  - Zone 5 Tablet: blue
- LED behaviour: charging active = full brightness; fully charged = slow pulse; no device = off

## Zone 3 — Watch Hardware Relay

- Hardware relay provides mutual exclusion between Apple Watch puck and Qi watch coil
- Only one watch charging path active at any time
- Relay state is set on device detection; no firmware needed

## Wattage Etch Labels

```
PHONE    20W  Qi2
BUDS     20W  Qi
WATCH     5W
LAPTOP  100W  USB-C
TABLET   45W  USB-C
```

---

## Comprehensive Electronics Reference (Revision A)

This section is a full electrical reference intended for design review, prototype bring-up, and assembly.

### Cross-Reference Documents

- Mechanical positions: [component-positions.md](component-positions.md)
- Wiring implementation: [wiring.md](wiring.md)
- Procurement and target parts: [bom.md](bom.md)

## 1) Full System Architecture

Penta Dock uses a centralised internal AC/DC supply to generate a 20V primary DC rail. That rail is split into five protected zone branches plus a low-voltage logic branch.

Architecture:
- PSU is Mean Well LRS-200-24 (201W nominal) with a 185W ATtiny85 soft cap.
- Zone 1: Qi2 certified, magnetic alignment N52 ring, recessed 1mm dish.
- Zone 2: 20W Qi, 120×80mm dish.
- Zone 3 supports Apple Watch magnetic protocol plus generic Qi-watch charging in one cradle footprint; hardware relay enforces one active path.
- Zone 4 and Zone 5 use captive braided cables with 90° angled dock-end connectors and silicone strain relief boots at exit points.
- Microfibre lining applied to inner walls of Zone 4 (laptop slot) and Zone 5 (tablet slot).

## 2) ATtiny85 Controller

| Parameter | Specification |
|---|---|
| MCU | ATtiny85 8-bit AVR |
| Role | Zone LED logic, WS2811 data output, global 185W soft cap |
| Programming | Programmed at assembly (no field updates) |
| Power | 5V from 5V buck converter |

## 3) Main Power Supply Unit

| Parameter | Specification |
|---|---|
| Model | Mean Well LRS-200-24 |
| Physical size | 199×98×30mm |
| Input | 100–240VAC |
| Inlet | **Rear right-angle IEC C13** |
| Nominal available output | **201W** |
| Output voltage | 24V, trim-adjusted to ~20V |
| System full-load design | **190W total branch budget** |
| Headroom | **11W** |
| ATtiny85 global cap | **185W** |

PSU location: **under centre platform cavity**.

## 4) Power Architecture and Distribution

### Primary Distribution
1. AC enters through right-angle IEC C13 inlet.
2. PSU converts AC to regulated ~20V DC.
3. 20V rail feeds bulk capacitor and main distribution bus.
4. Bus branches split into 5 independent zone paths plus logic regulation branch.
5. Per-zone polyfuses provide overcurrent protection.

### Zone 1 — Qi2 20W Path
`20V rail -> 12V buck -> Qi2 TX module (20W, magnetic alignment N52 ring, recessed 1mm dish)`

### Zone 2 — Qi 20W Path
`20V rail -> 12V buck -> Qi TX module (20W, 120×80mm dish)`

### Zone 3 — Watch Universal 5W Path
`20V rail -> 5V buck -> hardware relay -> (Apple puck OR Qi watch coil) [one active at a time]`

### Zone 4 — USB-C PD 100W Path
`20V rail -> USB-C PD 100W board -> polyfuse -> TVS -> captive 220mm braided cable (90° dock-end, silicone strain relief boot at exit)`

### Zone 5 — USB-C PD 45W Path
`20V rail -> USB-C PD 45W board -> polyfuse -> TVS -> captive 200mm braided cable (65W rated, 90° dock-end, silicone strain relief boot at exit)`

## 5) Logic Rail

`20V rail -> 5V buck -> ATtiny85 + WS2811 strip VCC`

## 6) WS2811 LED Strip

- ~15 LEDs, 250mm length
- ATtiny85 data line -> 300–470Ω -> WS2811 DIN
- 5V rail -> LED strip VCC
- Common GND
- 100µF capacitor at strip entry

## 7) Safety Systems

- Polyfuse per zone output
- TVS on PD outputs (Zones 4 and 5)
- NTC thermistor feedback in heat-prone zones
- Thermal cutoff on PSU branch
- PTC fuse on main protection path

## 8) Thermal Management

- PSU under centre platform, physically separated from slot zones
- 20mm riser cavity for wiring clearance above PSU
- 11W power headroom (190W load, 201W PSU), backed by 185W ATtiny85 soft cap

## 9) Mechanical Notes

- Add silicone strain relief boots at captive cable exit points (Zone 4 and Zone 5 top of slot)
- Apply microfibre lining to inner walls of Zone 4 (laptop slot) and Zone 5 (tablet slot)
- Zone 1 silicone surface: 1mm recessed dish for Qi2 magnetic alignment
- Captive cable strain relief anchors: mechanical anchoring at top of each slot

## 10) Power Budget Table (Final Reference)

| Zone | Device | Power | Method |
|---|---|---|---|
| Zone 1 | Phone | 20W | Qi2 (magnetic alignment, N52 ring, recessed 1mm dish) |
| Zone 2 | Buds or second phone | 20W | Qi (120×80mm dish) |
| Zone 3 | Watch | 5W | Apple Watch puck + Qi coil, hardware relay |
| Zone 4 | Laptop | 100W | USB-C PD (captive 220mm braided cable) |
| Zone 5 | Tablet | 45W | USB-C PD (captive 200mm braided cable, 65W rated) |
| **Total worst case** | | **190W** | |
| **PSU rated** | | **201W (Mean Well LRS-200-24)** | |
| **Headroom** | | **11W** | |
| **ATtiny85 soft cap** | | **185W** | |

## 11) Future Batch 2 Considerations (Shelved)

App hardware (ESP32-C3, INA3221 power monitoring, BLE, WiFi) is preserved for potential Batch 2 revisitation. See [app-spec.md](app-spec.md) and [firmware-notes.md](firmware-notes.md). Not part of the current build.
