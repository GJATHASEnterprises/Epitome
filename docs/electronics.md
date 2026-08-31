# Step — Electronics Reference

---

## Power Input

- **Connector:** DC barrel jack, rear centre-left (X=40, Y=100, Z=15)
- **Included:** 65W USB-C power brick + USB-C to barrel adapter cable (1m)
- **Soft cap:** 60W enforced by ATtiny85 — protects included brick
- **High-power note:** For simultaneous high-power USB-C use (Port A + Port B both loaded), replace included brick with a 100W+ USB-C charger

---

## Zone-by-Zone Power Paths

### Zone 1 — Phone (Qi2 20W)

```
DC jack → 12V buck converter → Qi2 20W TX module → N52 ring magnet array → phone coil
                             → Polyfuse → NTC thermistor → overcurrent + thermal protection
```

- Input: 12V from 12V buck converter
- Max output: 20W to phone
- Safety: polyfuse + NTC thermistor + thermal cutoff

### Zone 2 — Buds / Small Phone (Qi 5W)

```
DC jack → 5V buck converter → Qi 5W TX module → buds pad
                            → Polyfuse → overcurrent protection
```

- Input: 5V from 5V buck converter
- Max output: 5W
- Safety: polyfuse

### Zone 3 — Watch (Apple Watch puck + Qi 5W)

```
DC jack → 5V buck converter → Hardware relay (mutual exclusion)
                                ├─ Apple Watch magnetic puck PCBA (when relay = Apple)
                                └─ Universal Qi 5W watch coil (when relay = Qi)
```

- **Mutual exclusion:** Hardware relay ensures only one coil is active at a time
- Input: 5V from 5V buck converter
- Max output: 5W
- Safety: polyfuse on 5V line

---

## USB-C Ports

### Port A — 60W (X=120, Y=100, Z=15)

```
DC jack → USB-C PD 60W trigger board → panel mount USB-C receptacle
        → Polyfuse + TVS diode → ESD + overcurrent protection
```

- Max output: 60W PD
- Protection: polyfuse + TVS

### Port B — 30W (X=140, Y=100, Z=15)

```
DC jack → USB-C PD 30W trigger board → panel mount USB-C receptacle
        → Polyfuse + TVS diode → ESD + overcurrent protection
```

- Max output: 30W PD
- Protection: polyfuse + TVS

**BYOC:** Users bring their own USB-C cables. No cables included for these ports.

---

## ATtiny85 — Zone LED Logic + Soft Power Cap

### Role
- Monitors power draw estimates from zone enable signals
- Drives WS2811 LED strip (8 LEDs, 130mm, front fascia)
- Enforces 60W soft power cap: if estimated load approaches 60W, disables lowest-priority active zone
- Priority order: Port A > Port B > Zone 1 > Zone 2 > Zone 3

### Connections
| Pin | Function |
|---|---|
| PB0 | WS2811 data out |
| PB1 | Zone 1 sense / enable |
| PB2 | Zone 2 sense / enable |
| PB3 | Zone 3 relay control |
| PB4 | USB-C Port A sense |
| PB5 (RESET) | USB-C Port B sense |
| VCC | 5V from 5V buck |
| GND | Common ground |

### LED Strip — WS2811 8 LEDs 130mm

| Segment | Zone | Colour |
|---|---|---|
| LEDs 1–2 | Zone 1 phone | Blue (#0044FF) |
| LEDs 3–4 | Zone 2 buds | Purple (#8800FF) |
| LEDs 5–6 | Zone 3 watch | Green (#00CC44) |
| LED 7 | Port A USB-C | Orange (#FF6600) |
| LED 8 | Port B USB-C | Teal (#00BBAA) |

LEDs illuminate when the corresponding zone/port has a device present and is actively charging.

---

## Power Budget

| Zone | Max draw |
|---|---:|
| Phone Qi2 (Zone 1) | 20W |
| Buds Qi (Zone 2) | 5W |
| Watch (Zone 3) | 5W |
| USB-C Port A | 60W |
| USB-C Port B | 30W |
| Logic + LEDs | 2W |
| **Worst case total** | **122W** |
| **Typical real load** | ~50–65W |
| **Included brick** | 65W |
| **Soft cap** | 60W |

---

## Safety Systems

| System | Location | Purpose |
|---|---|---|
| Polyfuse | Zone 1, Zone 2, Zone 3, Port A, Port B | Overcurrent protection per zone |
| TVS diode | Port A, Port B | ESD / voltage spike protection |
| NTC thermistor | Zone 1 (Qi2 module) | Thermal monitoring |
| Thermal cutoff | Zone 1 | Hard thermal shutoff |
| ATtiny85 soft cap | System-level | 60W aggregate cap — protects brick |
| Hardware relay | Zone 3 | Mutual exclusion — prevents dual-coil conflict |

---

## Buck Converters

| Converter | Output voltage | Feeds |
|---|---|---|
| 12V buck | 12V | Zone 1 Qi2 module |
| 5V buck | 5V | Zone 2 Qi module, Zone 3 relay + coils, ATtiny85, LED strip |

Both converters fed from DC barrel jack rail.
