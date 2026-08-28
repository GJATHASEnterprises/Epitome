# Penta Dock — Wiring & Schematic Notes

---

## System Overview

```text
[Wall Outlet]
     |
[Right-Angle IEC C13 Inlet]
     |
[Internal 201W AC/DC PSU (Mean Well LRS-200-24) under centre platform cavity] --> [Main DC Rail: 20V]
                                               |
       +----------------+----------------+----------------+----------------+----------------+
       |                |                |                |                |                |
   [Qi2 TX]        [Qi TX]        [Watch Branch]     [PD 100W]        [PD 45W]
   Zone 1 20W       Zone 2 20W     Zone 3 5W shared   Zone 4           Zone 5
                                    (Puck + Qi)        captive 220mm    captive 200mm
                                    hardware relay     strain relief    strain relief
```

---

## Power Rail Design

| Rail | Voltage | Used For |
|------|---------|----------|
| AC input | 100–240V AC | Right-angle IEC C13 inlet to internal PSU |
| Main DC rail | 20V | Source for all zones and step-downs |
| Qi coil supply | 12V | Zones 1 & 2 wireless TX modules (via 12V buck ×2) |
| Watch branch | 5V | Zone 3 Apple puck + Qi watch coil (one active via hardware relay) |
| USB-C PD out (Zone 4) | 5V–20V negotiated | Laptop via captive 220mm USB-C cable (100W rated, 90° dock-end) |
| USB-C PD out (Zone 5) | 5V–12V negotiated | Tablet via captive 200mm USB-C cable (65W rated, 90° dock-end) |
| ATtiny85 + logic | 5V | LED controller (ATtiny85), WS2811 strip |

---

## ATtiny85 Pin Assignments

| Pin | Function |
|-----|----------|
| PB4 (physical pin 3) | WS2811 LED strip data |
| PB3 (physical pin 2) | Zone indicator input A |
| PB2 (physical pin 7) | Zone indicator input B |

*Pin assignments are provisional and subject to layout constraints. ATtiny85 programmed at assembly.*

---

## WS2811 LED Strip Wiring

- ATtiny85 data pin -> 300–470Ω -> DIN
- 5V rail -> LED strip VCC
- Common GND
- 100µF capacitor at strip entry

---

## Hardware Relay — Zone 3 Mutual Exclusion

- Hardware relay selects between Apple Watch puck output and Qi watch coil output
- Only one watch charging path is active at any time
- Relay state determined by device detection on Zone 3
- No firmware required for relay switching

```text
5V buck -> relay -> [Apple Watch puck]
                 -> [Qi watch coil 5W]
```

---

## Safety Wiring Notes

- Polyfuse on each zone output
- TVS on both USB-C PD outputs (Zones 4 and 5)
- NTC thermistors on heat-prone branches
- Thermal cutoff on PSU branch
- PTC fuse on main protection path
- Bulk capacitor (470–1000µF) on 20V rail
- **Silicone strain relief boots** at captive cable exit points (top of Zone 4 and Zone 5 slots)

---

## Comprehensive Wiring Implementation Guide (Revision B)

This section defines practical wiring execution from wall inlet to every electrical load branch.

### Reference Documents

- Electrical architecture: [electronics.md](electronics.md)
- Coordinates and placement: [component-positions.md](component-positions.md)
- Parts and recommended modules: [bom.md](bom.md)

## 1) Full System Wiring Narrative (End-to-End)

1. Bring AC mains into rear right-angle IEC C13 inlet.
2. Route neutral/earth to PSU per safety standards.
3. Convert AC to regulated ~20V DC.
4. Split 20V bus into five protected zone branches + logic branch.
5. Zone 1: 20V → 12V buck → Qi2 TX module (20W, magnetic alignment).
6. Zone 2: 20V → 12V buck → Qi TX module (20W, 90×70mm dish).
7. Zone 3: 20V → 5V buck → hardware relay → Apple puck or Qi watch coil (one active).
8. Zone 4: 20V → PD 100W board → polyfuse → TVS → captive 220mm cable (100W rated, 90° dock-end) → silicone strain relief boot at slot exit.
9. Zone 5: 20V → PD 45W board → polyfuse → TVS → captive 200mm cable (65W rated, 90° dock-end) → silicone strain relief boot at slot exit.
10. ATtiny85: 5V from 5V buck → controls WS2811 strip via data line.
11. Route all PSU-to-zone wiring through the **17mm riser cavity (Z=33mm to Z=50mm)** under centre platform Step 1.

## 2) AC Wiring Section

### Path

`Right-angle IEC C13 inlet -> PSU AC terminals`

### AC Wiring Requirements

| Item | Requirement |
|---|---|
| Minimum AC conductor gauge | 18 AWG |
| Inlet type | Panel-mount right-angle IEC C13 |
| Overcurrent strategy | PTC fuse on main protection path |

### AC Assembly Notes

- Keep AC harness isolated from DC and LED wiring.
- Use insulated crimp terminals/ferrules.

## 3) DC Main Rail Section (20V Backbone)

### Path

`PSU DC+ -> bulk capacitor -> main 20V distribution bus`

### Main Rail Requirements

| Item | Requirement |
|---|---|
| Main rail gauge | 16 AWG recommended |
| Bulk capacitor value | 470–1000µF |
| Grounding | Star return to PSU GND |

## 4) Per-Zone DC Wiring Detail

### Zone 1 (Qi2 20W)
`20V -> 12V buck -> Qi2 TX 20W -> polyfuse -> NTC`

### Zone 2 (Qi 20W)
`20V -> 12V buck -> Qi TX 20W (90×70mm dish) -> polyfuse -> NTC`

### Zone 3 (Watch 5W shared, hardware relay)
`20V -> 5V buck -> hardware relay -> (Apple puck OR Qi watch coil) -> polyfuse`

### Zone 4 (USB-C PD 100W)
`20V -> PD 100W board -> polyfuse -> TVS -> captive USB-C cable (220mm, 100W, 90° dock-end) + strain relief boot at exit`

### Zone 5 (USB-C PD 45W)
`20V -> PD 45W board -> polyfuse -> TVS -> captive USB-C cable (200mm, 65W rated, 90° dock-end) + strain relief boot at exit`

## 5) WS2811 LED Strip Wiring

ATtiny85 data pin + series resistor + 5V/GND + entry capacitor.

## 6) NTC Thermistor Wiring

`5V -> 10k fixed -> ADC node -> NTC 10k -> GND`


## 7) Wire Gauge Summary Table

| Branch | Recommended AWG |
|---|---:|
| AC input harness | 18 AWG min |
| 20V main rail trunk | 16 AWG |
| Zone 1/2 Qi branches (12V) | 18 AWG |
| Zone 3 watch branch (5V) | 22 AWG |
| Zone 4 PD 100W branch (20V) | 14 AWG |
| Zone 5 PD 45W branch (20V) | 18 AWG |
| ATtiny85 + LED (5V logic) | 22 AWG |

## 8) Connector Recommendations

- DC branches: JST-XH
- Sensor leads: Dupont/JST
- Captive cable internal terminations: locking JST-VH or soldered + strain relief

## 9) Safety Checklist Before First Power-On

- [ ] Right-angle IEC C13 inlet secure and insulated
- [ ] PTC fuse populated on main protection path
- [ ] No short on 20V to GND
- [ ] Silicone strain relief boots installed at Zone 4 and Zone 5 cable exits
- [ ] Zone 3 hardware relay mutual exclusion validated (only one path active)
- [ ] All polyfuses populated per zone

## 10) Full-System ASCII Schematic

```text
AC -> C13(RA) -> 201W PSU (Mean Well LRS-200-24, under centre platform cavity) -> 20V Bus
  -> Z1 Qi2 20W (12V buck -> Qi2 TX)
  -> Z2 Qi 20W (12V buck -> Qi TX, 90×70mm dish)
  -> Z3 Watch 5W (5V buck -> relay -> Puck OR Qi coil, one active)
  -> Z4 PD100W -> Captive USB-C 220mm (100W, 90° dock-end, strain relief boot)
  -> Z5 PD45W -> Captive USB-C 200mm (65W rated, 90° dock-end, strain relief boot)

5V buck -> ATtiny85 -> WS2811 strip data
```

## 11) Practical Integration Notes

- Validate natural cable reach from top-of-slot hang point to common laptop/tablet port locations when device is fully inserted on thin edge.
- Silicone strain relief boots prevent cable damage at exit point and maintain cable position at top of slot.
- Microfibre lining on Zone 4 and Zone 5 inner walls applied after slot assembly.
- Buck converters (12V ×2, 5V ×1) must be mounted **flat** in the riser cavity. Standing upright, typical modules are 12–14mm tall which leaves less than 5mm clearance — insufficient for safe installation. Mounted flat, modules are ~8mm tall leaving 9mm clearance ✅
