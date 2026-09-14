# Epitome Step — Electronics Reference

Both models share the same beginner-friendly easy-connect electronics architecture. The only model differences are the lighting hardware and the Obsidian rear mode button.

---

## Shared schematic overview

```
65W GaN brick + barrel cable
        │
        ▼
DC barrel jack with screw terminals
        │
        ▼
Raw DC distribution PCB / block
        ├──→ 12V screw-terminal buck converter ──→ Qi2 20W TX (Zone 1)
        ├──→ 5V screw-terminal buck converter ──→ Qi 5W TX (Zone 2)
        │                                      ├──→ Apple Watch PCBA / Qi watch coil (Zone 3, via relay)
        │                                      ├──→ Digispark-style ATtiny85 USB board
        │                                      └──→ Lighting harness
        ├──→ USB-C PD 60W trigger board (Port A, rear X=120)
        └──→ USB-C PD 30W trigger board (Port B, rear X=140)
```

---

## Zone-by-zone power paths

### Zone 1 — Phone (Qi2 20W)
- Feed: 12V from the 12V screw-terminal buck converter via the 12V distribution terminals
- TX module: Qi2 20W (magnetic alignment, iPhone 13+ snaps on, all Qi devices work)
- Protection: polyfuse (1.5A) + pre-crimped NTC thermistor on TX coil + hardwired thermal cutoff
- Thermistor role: the NTC feeds the Qi TX module's own thermal protection / cutoff path, not the ATtiny85
- Silicone dish: 75 × 90 mm portrait, 1 mm recess

### Zone 2 — Buds / small phone (Qi 5W)
- Feed: 5V from the 5V screw-terminal buck converter
- TX module: standard Qi 5W
- Protection: polyfuse (1A)
- Pad: 65 × 50 mm flat silicone

### Zone 3 — Watch (Apple Watch + Qi 5W)
- Feed: 5V from the 5V screw-terminal buck converter
- TX: Apple Watch magnetic puck PCBA (all models) + universal Qi watch coil 5W
- Mutual exclusion: hardware relay ensures only one coil active at a time
- Cradle: 55 × 55 mm with raised lip

### USB-C Port A (rear X = 120)
- Trigger board: USB-C PD 60W
- Panel-mount USB-C receptacle
- Protection: polyfuse (3A) + TVS diode
- Feed: raw DC distribution block

### USB-C Port B (rear X = 140)
- Trigger board: USB-C PD 30W
- Panel-mount USB-C receptacle
- Protection: polyfuse (2A) + TVS diode
- Feed: raw DC distribution block

---

## Digispark-style ATtiny85 USB board — role and pin assignments

The Digispark-style ATtiny85 board handles LED control, the 60W soft power cap, and night mode. It flashes directly over USB before installation; no USBasp and no soldered programming header are required.

| Pin | Assignment |
|---|---|
| PB0 | Lighting data out |
| PB1 | Zone 1 detect (Qi2 TX STAT — HIGH when phone present) |
| PB2 | Zone 2 detect |
| PB3 | Zone 3 detect |
| PB4 | Obsidian only: RGB mode button input (active LOW, internal pull-up) |
| 5V | 5V from 5V buck |
| GND | Common ground |

Current firmware reads zone-detect inputs only; no ATtiny85 ADC channel is used for the Zone 1 thermistor.

---

## Lighting differences per model

| Parameter | Walnut | Obsidian |
|---|---|---|
| Lighting hardware | Single white status LED + 3 mm light pipe | Dual WS2812B side strips |
| LED count | 1 | 16 total (8 per side) |
| Wiring style | Pre-wired 2-wire/3-wire pigtail | Pre-wired strips with factory JST-SM leads |
| Colour | Warm white only (#FFD6A0, fixed) | Full RGB — 8 modes |
| Mode cycling | N/A | Rear tactile button (PB4) cycles through 8 modes |
| RGB modes | — | Blue → Purple → Green → Red → Cyan → Yellow → White → Off |
| Colour codes | — | #3399FF → #9966FF → #33CC66 → #FF3333 → #00FFFF → #FFFF00 → #FFFFFF → off |
| Data pin | PB0 | PB0 |

---

## Power budget

Both models have identical power-consumption limits except for the lighting hardware.

| Load | Voltage | Max current | Max power |
|---|---:|---:|---:|
| Zone 1 Qi2 TX | 12V | 1.67A | 20W |
| Zone 2 Qi TX | 5V | 1.0A | 5W |
| Zone 3 Watch TX | 5V | 1.0A | 5W |
| USB-C Port A | PD | — | 60W |
| USB-C Port B | PD | — | 30W |
| ATtiny85 + lighting | 5V | 0.3A | 1.5W |
| **Theoretical max** | | | **121.5W** |
| **ATtiny85 soft cap** | | | **60W** |
| **Included brick** | | | **65W** |

The included 65W GaN brick comfortably covers all three wireless zones plus only a **partial** USB-C load. It does **not** support full simultaneous 60W Port A + 30W Port B output, and it should not be documented as doing so. If a user expects the full 60W USB-C path while all wireless zones are active, they should supply a higher-watt external brick.

---

## Safety systems

| System | Purpose |
|---|---|
| Polyfuse Zone 1 | Overcurrent protection on Qi2 TX |
| NTC thermistor Zone 1 | Feeds the Qi2 TX module's own thermal protection / cutoff path |
| Thermal cutoff Zone 1 | Hard cutoff if coil exceeds 70°C |
| Polyfuse Zone 2 | Overcurrent on Qi 5W TX |
| Polyfuse Zone 3 | Overcurrent on watch coil |
| Hardware relay Zone 3 | Prevents both watch coils being active simultaneously |
| Polyfuse + TVS Port A | Overcurrent + ESD on USB-C Port A |
| Polyfuse + TVS Port B | Overcurrent + ESD on USB-C Port B |
| ATtiny85 soft cap | Dims LEDs if estimated load approaches 60W |

---

## Soft cap explanation

The ATtiny85 tracks which zones are active via the three detect pins and estimates total draw. If estimated draw approaches the 60W soft cap, it reduces lighting brightness to pull back roughly 1–1.5W from the LED budget. This is a soft protection measure only — the polyfuses, TVS parts, and the Zone 1 hard thermal cutoff handle actual hardware faults.

---

## Night mode

Lights automatically turn off between 23:00 and 07:00 using a simple time counter derived from power-on time. The ATtiny85 has no RTC. The user sets night mode by pressing and holding the Obsidian mode button for 3 seconds at 23:00 (Walnut: factory-set, no external button). First power-on at any time assumes 12:00 noon and counts from there.
