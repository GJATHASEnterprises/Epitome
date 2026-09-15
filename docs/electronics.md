# Epitome Step — Electronics Reference

Both models share the same beginner-friendly easy-connect electronics architecture. The only model differences are the lighting hardware and the Obsidian rear mode button.

---

## Shared schematic overview

```
65W GaN brick
        │
        ▼
USB-C PD input receptacle (rear X=40)
        │
        ▼
PD input trigger board (20V negotiated input, ≥3.25A at 20V)
        │
        ▼
20V distribution PCB / block
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

### USB-C PD input (rear X = 40)
- Receptacle: panel-mount USB-C input port
- Trigger board: USB-C PD input trigger board negotiating 20V from the included 65W GaN brick
- Minimum rating: **≥3.25A at 20V**
- Feed: raw 20V rail into the distribution block, which then feeds the 12V buck, 5V buck, and both output trigger boards
- Human-factors note: the input port must be visually differentiated (deeper recess or engraved **IN** label) so customers do not mistake it for an output port

### USB-C Port A (rear X = 120)
- Trigger board: USB-C PD 60W
- Panel-mount USB-C receptacle
- Protection: polyfuse (3.5A hold) + TVS diode
- Feed: 20V distribution block
- Rating note: 60W is the **peak branch label** for Port A, not a guarantee of simultaneous 60W + 30W rear-port output from the included 65W brick
- Fuse basis: 60W on a 20V branch implies about **3.0A nominal input current**, so the **3.5A hold** fuse leaves modest tolerance / inrush headroom without opening under normal full-port use

### USB-C Port B (rear X = 140)
- Trigger board: USB-C PD 30W
- Panel-mount USB-C receptacle
- Protection: polyfuse (2A hold) + TVS diode
- Feed: 20V distribution block
- Rating note: 30W is the **peak branch label** for Port B, not a guarantee of simultaneous 60W + 30W rear-port output from the included 65W brick
- Fuse basis: 30W on a 20V branch implies about **1.5A nominal input current**, so the **2A hold** fuse intentionally keeps tighter overcurrent protection while still leaving limited tolerance headroom

### Bench-verification note
- Current canonical architecture keeps the **20V input rail + dedicated 12V buck** for Zone 1.
- Possible simplification to test on bench: if the chosen PD input trigger can negotiate **12V directly** with enough current for the intended load, the 12V buck may become optional.
- Do **not** remove the 12V buck from the design docs, wiring guide, or CAD assumptions until that direct-12V path is verified on hardware.

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
| **Documentation planning figure** | | | **60W** |
| **Included brick** | | | **65W** |

The included 65W GaN brick comfortably covers all three wireless zones plus only a **partial** USB-C load. The practical in-box expectation should be read as **full wireless use plus low-power USB-C accessory charging only**; sustained laptop-class USB-C output should assume fewer active wireless loads or a higher-watt external brick. It does **not** support full simultaneous 60W Port A + 30W Port B output, and it should not be documented as doing so. If a user expects the full 60W USB-C path while all wireless zones are active, they should supply a higher-watt external brick.

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
| 3.5A hold polyfuse + TVS Port A | Overcurrent + ESD on USB-C Port A |
| 2A hold polyfuse + TVS Port B | Overcurrent + ESD on USB-C Port B |
| Lighting trim against 60W target | Dims lights under full wireless load as a planning-margin measure |

---

## Soft cap explanation

The documented 60W soft cap is a planning target for the overall product budget, not a measured whole-system enforcement loop. The ATtiny85 only tracks which wireless zones are active via the three detect pins, and when the wireless stack is fully active it trims roughly 1–1.5W from the lighting budget. USB-C current is not measured by the firmware, so any remaining headroom for concurrent USB-C use is a design-budget assumption tied to the included 65W brick. This is a soft planning measure only — the polyfuses, TVS parts, and the Zone 1 hard thermal cutoff handle actual hardware faults.

---

## Night mode

Lights automatically turn off overnight using a simple time counter derived from power-on time. The ATtiny85 has no RTC. Obsidian users can re-align the timer by pressing and holding the mode button for 3 seconds at the desired evening start time. Walnut has no external button, so its night mode should be treated as a factory-set approximate overnight blackout rather than a user-calibrated local-time schedule.
