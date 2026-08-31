# Step — Wiring Guide

---

## Overview

All wiring is routed through the riser cavity (Z=3 to Z=25). All components must be flat-mounted — no upright components over 22mm tall. Use JST connectors for all zone connections to allow disassembly.

---

## Power Path

```
Wall → 65W USB-C brick → USB-C to barrel cable → DC barrel jack (X=40, Y=100, Z=15)
     → DC rail (internal)
          ├─ 12V buck converter → Zone 1 Qi2 20W module
          ├─ 5V buck converter  → Zone 2 Qi 5W module
          │                    → Zone 3 relay + coils
          │                    → ATtiny85 (VCC)
          │                    → WS2811 LED strip
          ├─ USB-C PD 60W board → Port A panel mount receptacle
          └─ USB-C PD 30W board → Port B panel mount receptacle
```

---

## Zone-by-Zone Wiring

### Zone 1 — Phone Qi2 20W

```
DC rail → 12V buck converter → [JST-2] → polyfuse → NTC thermistor → Qi2 20W TX board
                                                                    → Qi2 coil (Zone 1 top, Z=40)
```

- Wire gauge: 22 AWG
- JST connector: JST-PH 2-pin at buck output
- Polyfuse rating: 2A
- NTC thermistor: on TX board, monitors coil temperature
- Thermal cutoff: in series with TX board power; opens at 85°C

### Zone 2 — Buds Qi 5W

```
DC rail → 5V buck converter → [JST-2] → polyfuse → Qi 5W TX board → coil (Zone 2 top, Z=55)
```

- Wire gauge: 24 AWG
- JST connector: JST-PH 2-pin at buck output
- Polyfuse rating: 1.5A

### Zone 3 — Watch

```
DC rail → 5V buck converter → polyfuse → hardware relay
                                          ├─ [JST-2] → Apple Watch puck PCBA → puck (Zone 3 top)
                                          └─ [JST-2] → Qi 5W watch coil (Zone 3 top)
Relay control: ATtiny85 PB3
```

- Wire gauge: 24 AWG
- JST connectors: JST-PH 2-pin for each coil
- Relay: SPDT, 5V coil
- Only one output active at a time (mutual exclusion)

---

## USB-C Port Wiring

### Port A — 60W (X=120, Y=100, Z=15)

```
DC rail → [JST-2] → USB-C PD 60W trigger board → polyfuse → TVS diode → panel mount USB-C receptacle (Port A)
```

- Wire gauge: 20 AWG (for 60W)
- JST connector: JST-VH 2-pin at trigger board input
- Polyfuse rating: 4A
- TVS diode: 20V rated

### Port B — 30W (X=140, Y=100, Z=15)

```
DC rail → [JST-2] → USB-C PD 30W trigger board → polyfuse → TVS diode → panel mount USB-C receptacle (Port B)
```

- Wire gauge: 22 AWG
- JST connector: JST-VH 2-pin at trigger board input
- Polyfuse rating: 2.5A
- TVS diode: 20V rated

---

## ATtiny85 Connections

| ATtiny85 Pin | Connection | Description |
|---|---|---|
| PB0 (pin 5) | WS2811 data line | LED strip data out |
| PB1 (pin 6) | Zone 1 Qi2 enable | Zone 1 presence sense |
| PB2 (pin 7) | Zone 2 Qi enable | Zone 2 presence sense |
| PB3 (pin 2) | Zone 3 relay IN | Watch zone relay control |
| PB4 (pin 3) | Port A sense | Port A current sense |
| PB5 / RESET (pin 1) | Port B sense | Port B current sense |
| VCC (pin 8) | 5V from 5V buck | Power |
| GND (pin 4) | Common ground | Ground |

---

## LED Strip Wiring

```
ATtiny85 PB0 → 470Ω resistor → WS2811 DIN
5V buck → WS2811 VCC
GND → WS2811 GND
```

- LED strip: WS2811, 8 LEDs, 130mm, positioned behind frosted acrylic diffuser
- Resistor: 470Ω on data line (prevents ringing)
- Decoupling cap: 100µF across VCC/GND near strip

---

## JST Connector Assignments

| Connector | Type | Circuit |
|---|---|---|
| J1 | JST-PH 2-pin | 12V buck → Zone 1 Qi2 board |
| J2 | JST-PH 2-pin | 5V buck → Zone 2 Qi board |
| J3 | JST-PH 2-pin | Relay NO → Apple Watch puck |
| J4 | JST-PH 2-pin | Relay NC → Qi watch coil |
| J5 | JST-VH 2-pin | DC rail → Port A PD board |
| J6 | JST-VH 2-pin | DC rail → Port B PD board |
| J7 | JST-PH 3-pin | ATtiny85 → LED strip (VCC, GND, DATA) |

---

## Flat-Mount Rule

All boards and components in the riser cavity must be flat-mounted. Maximum height above board floor: 22mm. Any component taller than 22mm must be repositioned or substituted with a lower-profile alternative.

---

## Cable Routing Notes

- Route 12V and 5V power lines along rear wall of cavity (Y=80–100)
- Route zone coil wires through dedicated vertical channels in ABS structure
- All wires on Zone 3 (watch) must pass through the Step 2 structure before reaching Step 3 level
- Secure all wiring with cable ties or hot glue to prevent rattling
- Leave 30mm service loop on all JST connections for reassembly access
