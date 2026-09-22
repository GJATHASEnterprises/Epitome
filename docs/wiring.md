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
        ├──→ USB-C PD 15W output trigger board            [screw terminal feed]
        ├──→ 12V screw-terminal buck converter input
        │       └──→ 12V distribution terminals ──→ Zone 1 Qi2 TX   [J1]
        │                                          └──→ Zone 2 Qi TX [J2]
        └──→ 5V screw-terminal buck converter input
                └──→ 5V distribution terminals ──→ Zone 3 watch TX   [J3]
                                                   ├──→ Digispark ATtiny85 [J4]
                                                   └──→ Lighting      [J5/J6]
```

All power branches terminate in screw terminals or pre-crimped JST-XH pigtails.

---

## Zone 1 — Phone (Qi2 20W)

| Wire | From | To |
|---|---|---|
| 12V power | 12V distribution terminals via J1 | Qi2 TX VIN |
| GND | 12V distribution terminals via J1 | Qi2 TX GND |
| Detect | Qi2 TX STAT via J7 (orange) | Digispark ATtiny85 PB1 |

- Polyfuse remains in-line on the 12V feed.

---

## Zone 2 — Buds or second phone (up to 15W)

| Wire | From | To |
|---|---|---|
| 12V power | 12V distribution terminals via J2 | Qi TX VIN |
| GND | 12V distribution terminals via J2 | Qi TX GND |
| Detect | Qi TX STAT via J8 (orange) | Digispark ATtiny85 PB2 |

- Polyfuse remains in-line on the 12V feed.

---

## Zone 3 — Watch (5W)

| Wire | From | To |
|---|---|---|
| 5V power | 5V distribution terminals via J3 | Watch TX VIN |
| GND | 5V distribution terminals via J3 | Watch TX GND |
| Detect | Watch TX STAT via J9 (orange) | Digispark ATtiny85 PB3 |

- Generic watch coil is not Apple Watch-compatible unless MFi hardware is selected.

---

## USB-C ports

| Port / stage | Protection / board | From | To |
|---|---|---|---|
| USB-C PD input stage | Panel-mount USB-C receptacle + PD input trigger board | 65W GaN brick | 20V distribution rail |
| USB-C output (15W) | ~1A hold polyfuse + TVS + 15W trigger board | 20V distribution block | Rear output receptacle |

Rear panel uses **2× panel-mount USB-C**: **IN at X=40**, **OUT at X=130**.

---

## Digispark ATtiny85 connections summary

| Pin | Net | Notes |
|---|---|---|
| PB0 | LED DATA out | Both models |
| PB1 | Zone 1 detect in | HIGH = phone present |
| PB2 | Zone 2 detect in | HIGH = zone active |
| PB3 | Zone 3 detect in | HIGH = watch zone active |
| PB4 | **Obsidian only:** mode button in | Active LOW, internal pull-up enabled |

---

## JST assignments

| Connector | Colour | Signal |
|---|---|---|
| J1 | Red/Black | 12V to Zone 1 Qi2 TX |
| J2 | Red/Black | 12V to Zone 2 Qi TX |
| J3 | Red/Black | 5V to Zone 3 watch TX |
| J4 | Red/Black | 5V to Digispark ATtiny85 |
| J5 | Red/Black | 5V to lighting |
| J6 | White | LED DATA line |
| J7 | Orange/Black | Zone 1 detect to PB1 |
| J8 | Orange/Black | Zone 2 detect to PB2 |
| J9 | Orange/Black | Zone 3 detect to PB3 |
| J10 | Grey | **Obsidian only:** mode button to PB4 |
