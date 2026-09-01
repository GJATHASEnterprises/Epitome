# Epitome Step — Electronics Reference

Both models share identical electronics except for the LED strip type and the Obsidian rear mode button.

---

## Shared schematic overview

```
DC barrel jack inlet (rear)
        │
        ├──→ 12V buck converter ──→ Qi2 20W TX (Zone 1)
        │
        ├──→ 5V buck converter ──→ Qi 5W TX (Zone 2)
        │                     ──→ Apple Watch PCBA / Qi watch coil (Zone 3, via relay)
        │                     ──→ ATtiny85
        │
        ├──→ USB-C PD 60W trigger board (Port A, rear X=120)
        │
        └──→ USB-C PD 30W trigger board (Port B, rear X=140)
```

---

## Zone-by-zone power paths

### Zone 1 — Phone (Qi2 20W)
- Feed: 12V from DC rail via 12V buck converter
- TX module: Qi2 20W (magnetic alignment, iPhone 13+ snaps on, all Qi devices work)
- Protection: polyfuse (1.5A) + NTC thermistor on TX coil + thermal cutoff
- Silicone dish: 75 × 90 mm portrait, 1 mm recess

### Zone 2 — Buds / small phone (Qi 5W)
- Feed: 5V from 5V buck converter
- TX module: standard Qi 5W
- Protection: polyfuse (1A)
- Pad: 65 × 50 mm flat silicone

### Zone 3 — Watch (Apple Watch + Qi 5W)
- Feed: 5V from 5V buck converter
- TX: Apple Watch magnetic puck PCBA (all models) + universal Qi watch coil 5W
- Mutual exclusion: hardware relay ensures only one coil active at a time
- Cradle: 55 × 55 mm with raised lip

### USB-C Port A (rear X = 120)
- Trigger board: USB-C PD 60W
- Panel-mount USB-C receptacle
- Protection: polyfuse (3A) + TVS diode
- Feed: DC barrel rail

### USB-C Port B (rear X = 140)
- Trigger board: USB-C PD 30W
- Panel-mount USB-C receptacle
- Protection: polyfuse (2A) + TVS diode
- Feed: DC barrel rail

---

## ATtiny85 — role and pin assignments

The ATtiny85 handles LED control, soft power cap, and night mode. It does **not** communicate externally (no BLE, no Wi-Fi, no app).

| Pin | Assignment |
|---|---|
| PB0 | WS2811 / WS2812B data out |
| PB1 | Zone 1 detect (NTC threshold — HIGH when phone present) |
| PB2 | Zone 2 detect |
| PB3 | Zone 3 detect |
| PB4 | Obsidian only: RGB mode button input (active LOW, internal pull-up) |
| VCC | 5V from 5V buck |
| GND | Common ground |

---

## LED differences per model

| Parameter | Walnut | Obsidian |
|---|---|---|
| Strip type | WS2811 | WS2812B |
| LED count | 8 | 8 |
| Strip length | 130 mm | 130 mm |
| Colour | Warm white only (#FFD6A0, fixed) | Full RGB — 8 modes |
| Mode cycling | N/A | Rear tactile button (PB4) cycles through 8 modes |
| RGB modes | — | Blue → Purple → Green → Red → Cyan → Yellow → White → Off |
| Colour codes | — | #3399FF → #9966FF → #33CC66 → #FF3333 → #00FFFF → #FFFF00 → #FFFFFF → off |
| Data pin | PB0 | PB0 |

---

## Power budget

Both models have identical power consumption profiles.

| Load | Voltage | Max current | Max power |
|---|---:|---:|---:|
| Zone 1 Qi2 TX | 12V | 1.67A | 20W |
| Zone 2 Qi TX | 5V | 1.0A | 5W |
| Zone 3 Watch TX | 5V | 1.0A | 5W |
| USB-C Port A | PD | — | 60W |
| USB-C Port B | PD | — | 30W |
| ATtiny85 + LEDs | 5V | 0.3A | 1.5W |
| **Theoretical max** | | | **121.5W** |
| **ATtiny85 soft cap** | | | **60W** |
| **Included brick** | | | **100W** |

The included 100W brick safely covers simultaneous wireless charging across all three zones plus both USB-C ports at partial load. For simultaneous 60W + 30W USB-C at full PD negotiation, a 100W brick is recommended (included).

---

## Safety systems

| System | Purpose |
|---|---|
| Polyfuse Zone 1 | Overcurrent protection on Qi2 TX |
| NTC thermistor Zone 1 | Temperature monitoring on Qi2 coil |
| Thermal cutoff Zone 1 | Hard cutoff if coil exceeds 70°C |
| Polyfuse Zone 2 | Overcurrent on Qi 5W TX |
| Polyfuse Zone 3 | Overcurrent on watch coil |
| Hardware relay Zone 3 | Prevents both watch coils being active simultaneously |
| Polyfuse + TVS Port A | Overcurrent + ESD on USB-C Port A |
| Polyfuse + TVS Port B | Overcurrent + ESD on USB-C Port B |
| ATtiny85 soft cap | Dims LEDs if estimated load approaches 60W |

---

## Soft cap explanation

The ATtiny85 tracks which zones are active (via detect pins) and estimates total draw. If estimated draw exceeds 60W, it reduces LED brightness to pull back ~1.5W from the LED strip. This is a soft protection measure — the polyfuses and TVS handle hard faults.

---

## Night mode

LEDs automatically turn off between 23:00 and 07:00 using a simple time counter derived from power-on time. The ATtiny85 has no RTC. The user sets night mode by pressing and holding the power button for 3 seconds at 23:00 (Obsidian: the mode button; Walnut: no external button, factory-set). First power-on at any time assumes 12:00 noon and counts from there.

