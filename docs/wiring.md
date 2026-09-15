# Epitome Step — Wiring Guide

---

## Easy-connect power path

```
65W GaN brick
        │
        ▼
USB-C PD input receptacle (rear X=40, Z=15)
        │
        ▼
PD input trigger board (20V negotiated output)
        │
        ▼
20V screw-terminal distribution PCB / block
        ├──→ Port A: USB-C PD 60W trigger board           [screw terminal feed]
        ├──→ Port B: USB-C PD 30W trigger board           [screw terminal feed]
        ├──→ 12V screw-terminal buck converter input
        │       └──→ 12V distribution terminals ──→ Zone 1 Qi2 TX   [J1]
        └──→ 5V screw-terminal buck converter input
                └──→ 5V distribution terminals ──→ Zone 2 Qi TX     [J2]
                                                   ├──→ Zone 3 relay [J3]
                                                   ├──→ Digispark ATtiny85 [J4]
                                                   └──→ Lighting      [J5/J6]
```

All power branches terminate in screw terminals or pre-crimped JST-XH pigtails. The PD input trigger negotiates the 20V input rail before the distribution block fans out power to the rest of the system. Hot (positive) wire: red. Ground: black. Keep the existing polyfuses in-line on each protected branch. If an unavoidable wire join remains, use a heat-gun-activated solder-seal connector instead of hand-soldering.

---

## Zone 1 — Phone (Qi2 20W)

| Wire | From | To |
|---|---|---|
| 12V power | 12V distribution terminals via J1 | Qi2 TX VIN |
| GND | 12V distribution terminals via J1 | Qi2 TX GND |
| Detect | Qi2 TX STAT via J7 (orange) | Digispark ATtiny85 PB1 |
| Signal ground | J7 black lead | Common ground / Digispark GND |
| NTC thermal pair | Pre-crimped thermistor leads | Qi2 TX thermal header / hardwired 70°C cutoff input |

- Polyfuse remains in-line on the 12V feed between the 12V distribution block and the TX module.
- Use a pre-crimped NTC thermistor lead set and bond the bead to the coil underside with thermal epoxy — no soldering at the coil.
- The NTC is part of the Qi TX module's own thermal protection chain; it is **not** routed to an ATtiny85 ADC pin.

---

## Zone 2 — Buds (Qi 5W)

| Wire | From | To |
|---|---|---|
| 5V power | 5V distribution terminals via J2 | Qi 5W TX VIN |
| GND | 5V distribution terminals via J2 | Qi 5W TX GND |
| Detect | Qi 5W TX STAT via J8 (orange) | Digispark ATtiny85 PB2 |
| Signal ground | J8 black lead | Common ground / Digispark GND |

- Polyfuse remains in-line on the 5V feed.

---

## Zone 3 — Watch (relay mutual exclusion)

| Wire | From | To |
|---|---|---|
| 5V power | 5V distribution terminals via J3 | Relay board VIN |
| GND | 5V distribution terminals via J3 | Relay board GND |
| Coil A data | Relay output A | Apple Watch PCBA |
| Coil B data | Relay output B | Qi watch coil |
| Detect | Relay STAT via J9 (orange) | Digispark ATtiny85 PB3 |
| Signal ground | J9 black lead | Common ground / Digispark GND |

- Relay board receives 5V and switches between the Apple Watch PCBA and Qi watch coil.
- Polyfuse stays on the 5V feed to the relay board.

---

## USB-C ports

| Port / stage | Protection / board | From | To |
|---|---|---|---|
| USB-C PD input stage | Panel-mount USB-C receptacle + PD input trigger board rated for 20V at ≥3.25A | 65W GaN brick | 20V distribution rail |
| Port A (60W) | 3.5A hold polyfuse + TVS3V3 | 20V distribution block | 60W PD trigger board |
| Port B (30W) | 2A hold polyfuse + TVS3V3 | 20V distribution block | 30W PD trigger board |

Rear panel uses **3× panel-mount USB-C**: **IN at X=40** (former DC-jack position), **Port A at X=120**, **Port B at X=140**. Route the input through the PD trigger first, then into the screw-terminal distribution block. The IN port should be recessed deeper or engraved **IN** so users do not plug the brick into an output port. Port A and Port B remain the documented **non-simultaneous peak branch ratings** only; the included 65W brick does **not** sustain both rear USB-C outputs at their full 60W + 30W labels at the same time, especially with wireless zones active. Port A uses a **3.5A hold** fuse because 60W on the 20V rail is about **3.0A nominal**; Port B uses a **2A hold** fuse because 30W on the 20V rail is about **1.5A nominal** and the lower-power branch can keep tighter protection.

---

## Lighting harness

| Wire | From | To |
|---|---|---|
| VCC 5V | 5V distribution via J5 | Lighting positive lead |
| GND | Common bus via J5 | Lighting ground lead |
| DATA | Digispark ATtiny85 PB0 via J6 | Lighting data lead |

- **Walnut:** single pre-wired white status LED/light-pipe assembly.
- **Obsidian:** pre-wired WS2812B side strips with factory JST-SM leads, **8 LEDs per side / 16 total**.
- No pad soldering on LEDs: buy the strip pre-wired and adapt to the JST-XH harness with plug-in leads or screw terminals only.

---

## Digispark ATtiny85 connections summary

| Pin | Net | Notes |
|---|---|---|
| PB0 | LED DATA out | Both models |
| PB1 | Zone 1 detect in | HIGH = phone present |
| PB2 | Zone 2 detect in | HIGH = buds present |
| PB3 | Zone 3 detect in | HIGH = watch present |
| PB4 | **Obsidian only:** mode button in | Active LOW, internal pull-up enabled |
| 5V | VCC | From 5V buck via J4 |
| GND | GND | Common bus |

Flash a **preassembled Digispark-style board with the onboard USB bootloader already present** before installation. If a purchased clone lacks the USB bootloader or arrives without the needed headers/connectors installed, replace it with a fully assembled USB-flashable equivalent rather than adding a soldering step.

---

## JST assignments

| Connector | Colour | Signal |
|---|---|---|
| J1 | Red/Black | 12V to Zone 1 Qi2 TX |
| J2 | Red/Black | 5V to Zone 2 Qi TX |
| J3 | Red/Black | 5V to Zone 3 relay |
| J4 | Red/Black | 5V to Digispark ATtiny85 |
| J5 | Red/Black | 5V to lighting |
| J6 | White | LED DATA line |
| J7 | Orange/Black | Zone 1 detect to PB1 + signal ground |
| J8 | Orange/Black | Zone 2 detect to PB2 + signal ground |
| J9 | Orange/Black | Zone 3 detect to PB3 + signal ground |
| J10 | Grey | **Obsidian only:** mode button to PB4 |

All JST-XH 2.54 mm throughout. Use pre-crimped JST-XH pigtails rather than crimping your own on Batch 1. Label each connector with a paint pen before final assembly.

---

## Wire routing

- All power wiring: 22 AWG silicone wire
- Signal wiring (detect, DATA, button): 26 AWG
- Bundle with cable ties at 40 mm intervals
- Route power wires along riser perimeter
- Route signal wires down centre
- Leave ~20 mm service loop at each connector
