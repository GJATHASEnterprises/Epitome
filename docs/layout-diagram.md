# Quad-Dock — Layout Diagram

> **Note:** Full enclosure specification is in [enclosure.md](enclosure.md). This file shows the physical layout diagrams for reference.

---

## Top View (Surface Layout)

```
                    ← 300mm long →
+============================================================+  ← rear edge (140mm wide, 22mm high)
|                                                            |
|   [⌚ ZONE 3 — Watch]        [💻 ZONE 4 — Laptop]          |
|   Teardrop pod                Vertical spine groove        |
|   30° tilt, rear-left         22mm × 12mm, rear-right      |
|                                                            |
+------------------------------------------------------------+  ← arc taper (R20mm all edges)
|                                                            |
|   [📱 ZONE 1 — Phone]        [🎧 ZONE 2 — Buds]            |
|   15W Qi + N52 magnets         15W Qi                      |
|   Silicone dish pocket          Silicone dish pocket        |
|                                                            |
+---[■■ PHONE ■■|■■ BUDS ■■|■■ WATCH ■■|■■ LAPTOP ■■]-------+
← front edge (110mm wide, 12mm high) ←  IEC C13 inlet (rear)
```

Zone icons laser-etched on aluminum top plate above each LED section:
- Zone 1: 📱 + "PHONE"
- Zone 2: 🎧 + "BUDS"
- Zone 3: ⌚ + "WATCH"
- Zone 4: 💻 + "LAPTOP"

---

## Side Profile View (Arc Taper)

```
Rear (22mm high)                            Front (12mm high)
     |                                            |
     |  [Watch Zone 3]   [Laptop Zone 4]          |
     |  teardrop pod     spine groove             |
     |                                            |
+====+============================================+====+
|    Internal PSU | PCB | Qi coil 1 | Qi coil 2       |
|    INA3221/INA219      ESP32-C3 Mini  BH1750         |
+=========================================================+
       |                                          |
  IEC C13 inlet (rear)       [WS2812B LED — front lip, indirect]
```

---

## Internal Component Layout (Top-Down)

```
+========================================================================+
| [IEC C13 Inlet] → [180W AC/DC PSU Module] → [Main 20V Rail]           |
|                                       |                                |
|    +----------------------------------+                                |
|    |            |            |             |                           |
| [Qi TX 1]   [Qi TX 2]   [Watch Puck]   [USB-C PD Board]               |
| (15W, Z1)   (15W, Z2)   (5W, Z3)       (100W, Z4)                     |
|    |            |            |             |                           |
| [INA3221 ch1] [INA3221 ch2] [INA3221 ch3] [INA219]                    |
|    |            |            |             |                           |
|    +------+-----+------------+-------------+                           |
|           |                                                            |
|        [I2C Bus: GPIO 8/9]                                             |
|           |                                                            |
|      [ESP32-C3 Mini]                                                   |
|           |               |               |                            |
|    [BLE / WiFi]  [GPIO 4 → WS2812B]   [I2C: GPIO 8/9 (BH1750)]        |
|                                                                        |
| [WS2812B LED strip — 16 LEDs — under front lip overhang]               |
| [Zone 1: LEDs 0–3] [Zone 2: LEDs 4–7] [Zone 3: LEDs 8–11] [Z4: 12–15] |
| [Frosted diffuser strip over LED bar]                                  |
+========================================================================+
```

---

## Enclosure Dimensions

```
             ← 300mm →
+------------------------+
|                        |  Rear: 22mm high, 140mm wide
|     [Z3]     [Z4]      |
+------arc taper---------+
|  [Z1]   [Z2]           |  Front: 12mm high, 110mm wide
|  [LED BAR — front lip] |
+------------------------+
  R20mm radius all corners
```

---

## Zone Pocket Dimensions

| Zone | Type | Depth | Silicone | Special |
|------|------|-------|----------|---------|
| Zone 1 — Phone | Recessed dish | 2–3mm | Yes | N52 ring magnets beneath |
| Zone 2 — Buds | Recessed dish | 2–3mm | Yes | — |
| Zone 3 — Watch | Teardrop pod | Elevated | Yes | 30° tilt, rear-left |
| Zone 4 — Laptop | Groove slot | 12mm deep | Yes (lining) | 22mm wide, rear-right |

---

## LED Strip Key

| State | LED Color | Meaning |
|-------|-----------|---------|
| Charging | Red | Device actively charging |
| Full | Green | Device fully charged |
| Empty | Off | No device detected |

---

## Notes
- Arc enclosure: smooth curved wedge, zero sharp corners, R20mm all edges
- No guide rails — zone pockets are silicone-lined recessed dishes
- Laptop groove is in rear-right; laptop stands vertically on its spine
- Watch cradle teardrop pod is in rear-left at 30° tilt toward user
- WS2812B LED strip is hidden under front lip with frosted diffuser (indirect glow)
- LED bar divided into 4 sections by recessed divider lines
- Zone icons laser-etched directly on aluminum top plate above each LED section
- Quad-Dock wordmark laser-etched on rear of aluminum top plate
- Rubber feet ×4 on underside with Quad-Dock logo embossed
- Aluminum top plate is removable (snap-fit + 2× M3 screws)
- IEC C13 inlet is on the rear centre
- No USB-A port
