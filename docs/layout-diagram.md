# Quad Device Dock — Layout Diagram

---

## Top View (Surface Layout)

```
+================================================================+
|                                                                |
|   QUAD DEVICE DOCK                              [LOGO]         |
|                                                                |
|  +------------+  +------------+  +--------+  +------------+  |
|  |            |  |            |  |  (  )  |  |            |  |
|  |  ZONE 1    |  |  ZONE 2    |  | ZONE 3 |  |  ZONE 4    |  |
|  |            |  |            |  |        |  |            |  |
|  | [Qi Phone] |  |[Qi Phone / |  | [Watch |  | [USB-C PD] |  |
|  |            |  |  AirPods]  |  |  Puck] |  |  [Cable]   |  |
|  |            |  |            |  |        |  |            |  |
|  +------------+  +------------+  +--------+  +------------+  |
|                                                                |
|  [LED 1]         [LED 2]         [LED 3]     [LED 4]         |
|                                                                |
+============================[ USB-C IN (rear) ]================+
```

---

## Side Profile View

```
              Zone 1     Zone 2    Zone 3    Zone 4
               Phone      Phone    Watch    Laptop
                 |          |        |         |
+----------------+----------+--------+---------+----+
|  === Qi Coil ==|== Qi Coil|=Watch  |  USB-C  |    |
|                                    |  Port   |    |
|  [PCB] [ESP32] [INA219x4] [PD IC]  [Fuses]       |
+----------------------------------------------------+
              |______ USB-C Power In (rear) __________|
```

---

## Internal Component Layout (Top-Down PCB View)

```
+================================================================+
|  [USB-C IN] --> [CH224K PD IC] --> [Main Power Rail]           |
|                                          |                     |
|     +------------------------------------+                     |
|     |           |           |            |                     |
|  [Qi TX 1]  [Qi TX 2]  [Watch Mod]  [USB-C PD Out]           |
|     |           |           |            |                     |
|  [INA219]  [INA219]   [INA219]      [INA219]                  |
|     |           |           |            |                     |
|     +-----+-----+-----------+------------+                     |
|           |                                                    |
|        [I2C Bus]                                               |
|           |                                                    |
|       [ESP32-WROOM-32]                                         |
|           |           |                                        |
|       [BLE/WiFi]   [GPIO: LEDs x4, Thermistors x3,            |
|                          Zone enable/disable x4]               |
|                                                                |
|  [Thermistor 1] [Thermistor 2] [Thermistor 3]                 |
|  (under Qi 1)   (under Qi 2)   (under Watch)                  |
+================================================================+
```

---

## Enclosure Dimensions (Target)

```
         320mm
+------------------------+
|                        |  
|  [Z1] [Z2] [Z3] [Z4]  |  130mm
|                        |
+------------------------+
      (rear: USB-C in)

Height: 28mm base + device clearance
```

---

## Zone Spacing (Center-to-Center)

| Zones | Center-to-Center Distance |
|-------|---------------------------|
| Z1 to Z2 | 70mm |
| Z2 to Z3 | 65mm |
| Z3 to Z4 | 70mm |

---

## LED Indicator Key

| Color | Meaning |
|-------|---------|
| Blue pulse | Device detected, charging |
| Green solid | Device fully charged |
| Yellow pulse | Charging paused (scheduled or 80% limit) |
| Red flash | Error / overheat |
| Off | No device detected |

---

## Notes
- Zone 3 watch cradle is recessed 8mm to hold watch securely
- Zone 4 USB-C cable exits from front-right edge of enclosure
- All LEDs are front-facing, low brightness (non-distracting at night)
- Rubber feet (x4) on underside for grip and airflow
- Rear cable exit is recessed to keep cable flat against desk
