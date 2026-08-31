# Step — Design Specification

**Brand:** Epitome Charge (epitomecharge.com)
**Product name:** Step
**Tagline:** "Charge everything. Touch nothing."
**Price:** $89

---

## Overview

Step is a three-step wireless charging stand made from walnut and matte black ABS. Three wireless charging zones are arranged on a rising staircase platform. Two USB-C PD ports on the rear allow wired charging for any device. An external 65W USB-C power brick is included. Users bring their own USB-C cables for the rear ports.

---

## Physical Dimensions

| Dimension | Value |
|---|---|
| Overall footprint | 165mm × 100mm |
| Overall height | 70mm |
| Base plate | 165 × 100 × 3mm (Z=0 to Z=3) |
| Riser/wiring cavity | 165 × 100 × 22mm (Z=3 to Z=25) |
| Step 1 block | 165 × 100 × 15mm, top surface Z=40 |
| Step 2 block | 130 × 100 × 15mm, top surface Z=55 |
| Step 3 block | 95 × 80 × 15mm, top surface Z=70 |
| Step 3 setback | 20mm from front (Y=20 to Y=100) |

### Coordinate System

- X=0 left edge, X=165 right edge, centred at X=82.5
- Y=0 front, Y=100 rear
- Z=0 base floor, up = +Z

### Step Widths (centred at X=82.5)

| Step | X range | Width | Y range |
|---|---|---|---|
| Step 1 (phone) | X=0 – X=165 | 165mm | Y=0 – Y=100 |
| Step 2 (buds) | X=17.5 – X=147.5 | 130mm | Y=0 – Y=100 |
| Step 3 (watch) | X=35 – X=130 | 95mm | Y=20 – Y=100 (setback) |

Each step narrows 17.5mm per side (165→130→95mm widths).

---

## Zone Specifications

### Zone 1 — Phone (Step 1 top, Z=40)
- **Standard:** Qi2 20W TX (magnetic alignment, N52 ring)
- **Pad size:** 75×90mm portrait, 1mm recessed silicone dish
- **Centre:** X=82.5, Y=50, Z=40

### Zone 2 — Buds / Small Phone (Step 2 top, Z=55)
- **Standard:** Qi 5W TX
- **Pad size:** 65×50mm silicone pad
- **Centre:** X=82.5, Y=50, Z=55

### Zone 3 — Watch (Step 3 top, Z=70)
- **Standard:** Apple Watch magnetic puck PCBA + universal Qi watch coil 5W
- **Mutual exclusion:** Hardware relay (only one active at a time)
- **Pad size:** 55×55mm cradle
- **Centre:** X=82.5, Y=60, Z=70
- **Note:** Step 3 is set back 20mm from front (front face at Y=20)

### USB-C Ports (rear face)
- **Port A:** USB-C PD 60W, rear right (X=120, Y=100, Z=15)
- **Port B:** USB-C PD 30W, rear right (X=140, Y=100, Z=15)
- **BYOC:** User brings own USB-C cables

---

## Electronics Summary

- Qi2 20W TX module (Zone 1)
- Qi 5W TX module (Zone 2)
- Apple Watch puck PCBA + universal Qi 5W coil (Zone 3)
- Hardware relay for Zone 3 mutual exclusion
- 12V buck converter (Qi2 zone)
- 5V buck converter (watch + logic)
- ATtiny85: zone LED logic + soft power cap (60W)
- WS2811 LED strip: 8 LEDs, 130mm, front fascia frosted diffuser
- DC barrel jack rear inlet
- USB-C PD 60W trigger board (Port A)
- USB-C PD 30W trigger board (Port B)
- Polyfuses + TVS diodes on all power outputs

### LED Colours
| Zone | Colour |
|---|---|
| Zone 1 phone | Blue |
| Zone 2 buds | Purple |
| Zone 3 watch | Green |
| Port A USB-C | Orange |
| Port B USB-C | Teal |

---

## Material Specification

| Component | Material |
|---|---|
| Base / riser | 3D printed matte black ABS |
| Step faces (×3) | Laser cut walnut, 4mm, Rubio Monocoat oiled |
| Step top surfaces (×3) | Laser cut walnut, 4mm, Rubio Monocoat oiled |
| Rear spine | Laser cut ABS, 165×35mm |
| Charging pads | 1mm silicone sheet |
| LED diffuser | Frosted acrylic, 130×10mm |
| Feet | 3M Bumpons ×4 |

---

## ASCII Diagrams

### Front View (3-step rising staircase)

```
       +--------+
       | WATCH  |     Z=70 (Step 3)
  +----+--------+----+
  |    BUDS PAD      |  Z=55 (Step 2)
+-+------------------+-+
|      PHONE PAD       |  Z=40 (Step 1)
+--[ LED DIFFUSER ]----+
|   ==================  |  Riser / base
+----------------------+
```

### Top View

```
X=0                    X=165
|<-------- 165mm -------->|
+-------------------------+   Y=0 (front)
|  +-------------------+  |
|  |  Step 1 (phone)   |  |
|  | [  75x90mm pad  ] |  |
|  +-------------------+  |
|    +---------------+    |
|    | Step 2 (buds) |    |
|    | [65x50mm pad] |    |
|    +---------------+    |
|      +-----------+      |
|      | Step 3    |      |
|      | (watch)   |      |
|      |[55x55 pad]|      |
|      +-----------+      |   Y=100 (rear)
+-------------------------+
```

### Side View (cross-section, left edge)

```
Z=70 |        +--------+
     |        | Step 3 |  15mm
Z=55 |   +----+--------+
     |   | Step 2      |  15mm
Z=40 +---+-------------+
     | Step 1           |  15mm
Z=25 +------------------+
     | Riser cavity     |  22mm
Z=3  +==================+
     | Base plate       |  3mm
Z=0  +==================+
```

### Rear View

```
+----------------------------+
|                            |
|  [DC IN]  [USB-A] [USB-B]  |
|  X=40     X=120   X=140    |
|                            |
+----------------------------+
```

---

## Dimensions Table

| Feature | Value |
|---|---|
| Overall width | 165mm |
| Overall depth | 100mm |
| Overall height | 70mm |
| Step 1 top surface Z | 40mm |
| Step 2 top surface Z | 55mm |
| Step 3 top surface Z | 70mm |
| Step 3 front setback | 20mm (Y=20) |
| Riser cavity height | 22mm (Z=3 to Z=25) |
| Base plate thickness | 3mm |
| Zone 1 pad | 75×90mm portrait |
| Zone 2 pad | 65×50mm |
| Zone 3 cradle | 55×55mm |
| LED diffuser | 130×8mm front fascia |
