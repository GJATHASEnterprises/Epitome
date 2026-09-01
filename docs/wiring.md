# Epitome Step — Wiring Guide

---

## Power path

```
DC barrel jack (rear X=40, Z=15)
        │
        ├── 12V rail ──→ 12V buck ──→ Zone 1 Qi2 TX    [JST-2 red/black]
        │
        ├── 5V rail ──→ 5V buck ──→ ATtiny85 VCC       [JST-2 red/black]
        │                       ──→ Zone 2 Qi TX        [JST-2 red/black]
        │                       ──→ Zone 3 relay board  [JST-2 red/black]
        │
        ├── Port A: USB-C PD 60W trigger board          [direct barrel tap]
        │
        └── Port B: USB-C PD 30W trigger board          [direct barrel tap]
```

All barrel tap connections use JST-XH 2.54mm connectors. Hot (positive) wire: red. Ground: black. Heat-shrink all solder joints.

---

## Zone 1 — Phone (Qi2 20W)

| Wire | From | To |
|---|---|---|
| 12V power | 12V buck output | Qi2 TX VIN |
| GND | Common bus | Qi2 TX GND |
| Detect | Qi2 TX STAT pin | ATtiny85 PB1 |
| NTC | Qi2 coil thermistor | ATtiny85 ADC2 (PB4 on Walnut) |

- Polyfuse in-line on 12V feed between buck and TX module
- NTC thermistor glued to coil underside with thermal epoxy

---

## Zone 2 — Buds (Qi 5W)

| Wire | From | To |
|---|---|---|
| 5V power | 5V buck output | Qi 5W TX VIN |
| GND | Common bus | Qi 5W TX GND |
| Detect | Qi 5W TX STAT | ATtiny85 PB2 |

- Polyfuse in-line on 5V feed

---

## Zone 3 — Watch (relay mutual exclusion)

| Wire | From | To |
|---|---|---|
| 5V power | 5V buck output | Relay board VIN |
| GND | Common bus | Relay board GND |
| Coil A data | Relay output A | Apple Watch PCBA |
| Coil B data | Relay output B | Qi watch coil |
| Detect | Relay STAT | ATtiny85 PB3 |

- Relay board receives 5V, switches between Apple Watch PCBA and Qi watch coil
- Polyfuse on 5V feed to relay board

---

## USB-C ports

| Port | Polyfuse | TVS | From | To |
|---|---|---|---|---|
| Port A (60W) | 3A | TVS3V3 | Barrel rail | 60W PD trigger board |
| Port B (30W) | 2A | TVS3V3 | Barrel rail | 30W PD trigger board |

Route USB-C lines through rear spine cutouts. Both ports panel-mount with M2 screws.

---

## LED strip

| Wire | From | To |
|---|---|---|
| VCC 5V | 5V buck | LED strip +5V pad |
| GND | Common bus | LED strip GND pad |
| DATA | ATtiny85 PB0 | LED strip DIN pad |

- Strip: 130 mm, 8 LEDs, 3-wire (VCC / DATA / GND)
- **Walnut:** WS2811 strip — warm white only
- **Obsidian:** WS2812B strip — full RGB
- DATA line: single wire, no resistor needed at 130 mm (short run)

---

## ATtiny85 connections summary

| Pin | Net | Notes |
|---|---|---|
| PB0 | LED DATA out | Both models |
| PB1 | Zone 1 detect in | HIGH = phone present |
| PB2 | Zone 2 detect in | HIGH = buds present |
| PB3 | Zone 3 detect in | HIGH = watch present |
| PB4 | **Obsidian only:** mode button in | Active LOW, internal pull-up enabled |
| VCC | 5V | From 5V buck |
| GND | GND | Common bus |

---

## JST assignments

| Connector | Colour | Signal |
|---|---|---|
| J1 | Red/Black | 12V to Zone 1 Qi2 TX |
| J2 | Red/Black | 5V to Zone 2 Qi TX |
| J3 | Red/Black | 5V to Zone 3 relay |
| J4 | Red/Black | 5V to ATtiny85 |
| J5 | Red/Black | 5V to LED strip |
| J6 | White | LED DATA line |
| J7 | Orange/Black | Zone 1 detect + NTC to ATtiny85 |
| J8 | Orange/Black | Zone 2 detect to ATtiny85 |
| J9 | Orange/Black | Zone 3 detect to ATtiny85 |
| J10 | Grey | **Obsidian only:** mode button to PB4 |

All JST-XH 2.54 mm throughout. Label each connector with a paint pen before final assembly.

---

## Wire routing

- All power wiring: 22 AWG silicone wire
- Signal wiring (detect, DATA): 26 AWG
- Bundle with cable ties at 40 mm intervals
- Route power wires along riser perimeter
- Route signal wires down centre
- Leave ~20 mm service loop at each connector

