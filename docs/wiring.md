# Epitome Penta — Wiring & Schematic Notes

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
       |                |                |                |                |
   [Qi TX 1]        [Qi TX 2]      [Watch Branch]   [PD 100W]        [PD 20W]
   Zone 1 20W       Zone 2 20W     Zone 3 5W shared  Zone 4          Zone 5
                                     (Puck + Qi)      captive 220mm    captive 200mm
```

---

## Power Rail Design

| Rail | Voltage | Used For |
|------|---------|----------|
| AC input | 100–240V AC | Right-angle IEC C13 inlet to internal PSU |
| Main DC rail | 20V | Source for all zones and step-downs |
| Qi coil supply | 12V | Zones 1 & 2 wireless TX modules |
| Watch branch | 5V | Zone 3 Apple puck + Qi watch coil (single active output) |
| USB-C PD out (Zone 4) | 5V–20V negotiated | Laptop via captive 220mm USB-C cable |
| USB-C PD out (Zone 5) | 5V–12V negotiated | Tablet/phone via captive 200mm USB-C cable |
| ESP32-C3 + logic | 3.3V | MCU, monitors, LEDs |

---

## ESP32-C3 Mini Pin Assignments

| Pin | Function |
|-----|----------|
| GPIO 8 | I2C SDA |
| GPIO 9 | I2C SCL |
| GPIO 4 | WS2811 LED strip data |
| GPIO 2 / 3 / 10 / 1 | Thermistor ADC channels |

*Pin assignments are provisional and subject to PCB routing constraints.*

---

## WS2811 LED Strip Wiring

- GPIO 4 -> 300–470Ω -> DIN
- 5V rail -> LED strip VCC
- Common GND
- 100µF capacitor at strip entry

---

## INA3221 #1 — 3-Channel Power Monitor (Zones 1–3)

- CH1 Zone 1 (20W)
- CH2 Zone 2 (20W)
- CH3 Zone 3 (5W shared puck/Qi)

---

## INA3221 #2 — 3-Channel Power Monitor (Zones 4–5 + spare/system)

- CH1 Zone 4 (USB-C PD up to 100W)
- CH2 Zone 5 (USB-C PD up to 45W)
- CH3 spare/system branch
- Address: **0x41** (A0 high)

---

## ESP32-C3 Mini

- Main MCU
- WiFi + BLE
- Flashed via onboard USB

---

## LED Behavior Logic

- **Red:** charging
- **Green:** full
- **Off:** no device detected
- **Night mode:** 23:00–07:00 LEDs off unless zone draw >0.5W

---

## Safety Wiring Notes

- PCB PTC resettable fuse on main protection path (replaces inlet fuse holder)
- Polyfuse on each zone output
- TVS on both USB-C PD outputs
- Thermistors on heat-prone branches
- Bulk capacitor (470–1000µF) on 20V rail

---

## PCB Notes

- 2-layer PCB
- Add pads/anchors for captive cable strain relief (Zone 4 + Zone 5)
- Keep watch dual-mode switching path short
- Route logic board and monitor interconnects flat through the riser cavity

---

## Comprehensive Wiring Implementation Guide (Revision A)

This section defines practical wiring execution from wall inlet to every electrical load branch.

### Reference Documents

- Electrical architecture: [electronics.md](electronics.md)
- Coordinates and placement: [component-positions.md](component-positions.md)
- Parts and recommended modules: [bom.md](bom.md)
- Firmware safety/night behavior: [firmware-notes.md](firmware-notes.md)

## 1) Full System Wiring Narrative (End-to-End)

1. Bring AC mains into rear right-angle IEC C13 inlet.
2. Route neutral/earth to PSU per safety standards.
3. Convert AC to regulated ~20V DC.
4. Split 20V bus into five protected zone branches + logic branch.
5. Route Zone 4 to captive 220mm cable harness (100W rated).
6. Route Zone 5 to captive 200mm cable harness (65W rated).
7. Route Zone 3 to both Apple puck and Qi watch coil through one-at-a-time control.
8. Route branch protection through PCB PTC resettable fuse stage.
9. Route all PSU-to-zone wiring through the **20mm riser cavity (Z=33mm to Z=50mm)** under centre platform Step 1.

## 2) AC Wiring Section

### Path

`Right-angle IEC C13 inlet -> PSU AC terminals`

### AC Wiring Requirements

| Item | Requirement |
|---|---|
| Minimum AC conductor gauge | 18 AWG |
| Inlet type | Panel-mount right-angle IEC C13 |
| Overcurrent strategy | PCB PTC resettable fuse on downstream protection branch |

### AC Assembly Notes

- Keep AC harness isolated from I2C wiring.
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

### Zone 1 (Qi 20W)
`20V -> buck -> Qi TX 20W -> polyfuse -> NTC`

### Zone 2 (Qi 20W)
`20V -> buck -> Qi TX 20W -> polyfuse -> NTC`

### Zone 3 (Watch 5W shared)
`20V -> 5V buck -> (Apple puck OR Qi watch coil) -> polyfuse -> NTC`

### Zone 4 (USB-C PD 100W)
`20V -> PD 100W board -> INA3221 #2 CH1 -> polyfuse -> TVS -> captive USB-C cable (220mm)`

### Zone 5 (USB-C PD 45W)
`20V -> PD 45W board -> INA3221 #2 CH2 -> polyfuse -> TVS -> captive USB-C cable (200mm, 65W rated)`

## 5) I2C Bus Wiring

`GPIO8/9 + 4.7k pull-ups -> INA3221 #1 + INA3221 #2`

## 6) WS2811 LED Strip Wiring

As above: GPIO4 + resistor + 5V/GND + entry capacitor.

## 7) NTC Thermistor Wiring

`3.3V -> 10k fixed -> ADC node -> NTC 10k -> GND`

## 8) 3.3V LDO Wiring

`5V source -> 3.3V LDO -> ESP32 + monitors`

## 9) Full ESP32-C3 Pin Assignment + Wire Color Guidance

| GPIO/Pin | Function | Recommended Wire Color |
|---|---|---|
| GPIO 8 | I2C SDA | Blue |
| GPIO 9 | I2C SCL | Yellow |
| GPIO 4 | WS2811 DIN | Green |
| GPIO 2/3/10/1 | NTC ADC | White stripe variants |

## 10) I2C Address Table and Conflict Avoidance

| Device | Role | Address |
|---|---|---|
| INA3221 #1 | Zones 1–3 monitor | 0x40 |
| INA3221 #2 | Zones 4–5 + spare/system monitor | 0x41 |

## 11) Grounding Strategy

Star ground from PSU GND, with separate high-current returns merged at star point.

## 12) Wire Gauge Summary Table

| Branch | Recommended AWG |
|---|---:|
| AC input harness | 18 AWG min |
| 20V main rail trunk | 16 AWG |
| Zone 1/2 Qi branches | 18 AWG |
| Zone 3 watch branch | 22 AWG |
| Zone 4 PD 100W branch | 14 AWG |
| Zone 5 PD 45W branch | 18 AWG |

## 13) Connector Recommendations

- DC branches: JST-XH
- Sensor leads: Dupont/JST
- Captive cable internal terminations: locking JST-VH or soldered + strain relief

## 14) Safety Checklist Before First Power-On

- [ ] Right-angle IEC C13 inlet secure and insulated
- [ ] PCB PTC resettable fuse populated
- [ ] No short on 20V to GND
- [ ] Captive cable strain relief installed on both slot outputs
- [ ] Zone 3 puck/Qi exclusivity validated

## 15) Full-System ASCII Schematic

```text
AC -> C13(RA) -> 201W PSU (Mean Well LRS-200-24, under centre platform cavity) -> 20V Bus
  -> Z1 Qi 20W
  -> Z2 Qi 20W
  -> Z3 Watch 5W (Puck + Qi, one active)
  -> Z4 PD100W -> Captive USB-C 220mm
  -> Z5 PD45W -> Captive USB-C 200mm (65W rated)
```

## 16) Practical Integration Notes

- Validate natural cable reach from top-of-slot hang point to common laptop/tablet port locations when device is fully inserted on thin edge.
