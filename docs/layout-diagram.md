# Quad Device Dock — Layout Diagram

![Quad Device Dock Render](images/quad-dock-render.png)

---

## Top View (Surface Layout)

```
+============================================================================+
|                                                                            |
|   QUAD DEVICE DOCK                                            [LOGO]       |
|                                                                            |
|  /+----------+\  /+----------+\  /+--------+\  /+--------------+\          |
|  || ZONE 1   ||  || ZONE 2   ||  || ZONE 3 ||  ||   ZONE 4     ||          |
|  || Phone Qi ||  || Phone /  ||  || Watch  ||  || USB-C Laptop ||          |
|  ||  (coil)  ||  || AirPods  ||  || cradle ||  || upright slot ||          |
|  \+----------+/  \+----------+/  \+--------+/  \+--------------+/          |
|                                                                            |
| [LED 1]         [LED 2]         [LED 3]        [LED 4]  [Dark Mode Btn]    |
|==================== frosted front diffuser strip ========================== |
+==============================[ USB-C IN (rear) ]===========================+
```

---

## Side Profile View

```
                Zone 1      Zone 2      Zone 3         Zone 4
                 Phone   Phone/Buds     Watch      Upright Laptop
                   |          |           |               /
         acrylic rails   acrylic rails  small rails   tall rails
+------------------+----------+-----------+------------/---------+
|   Qi coil        |  Qi coil | Watch puck| USB-C port / cable   |
|   8mm rails      |  8mm rails| 6mm rails| 40-50mm rails + pads |
|                                                                  |
| [PCB] [ESP32] [INA219x4] [LED driver resistors] [button input]   |
+------------------------------------------------------------------+
               |___________ USB-C Power In (rear) _____________|
```

---

## Internal Component Layout (Top-Down PCB View)

```
+========================================================================+
| [USB-C IN] --> [CH224K PD IC] --> [Main Power Rail]                    |
|                                       |                                |
|    +----------------------------------+                                |
|    |            |            |             |                           |
| [Qi TX 1]   [Qi TX 2]   [Watch Mod]   [USB-C PD Out]                  |
|    |            |            |             |                           |
| [INA219]    [INA219]     [INA219]      [INA219]                       |
|    |            |            |             |                           |
|    +------+-----+------------+-------------+                           |
|           |                                                         |
|        [I2C Bus]                                                    |
|           |                                                         |
|      [ESP32-WROOM-32]                                               |
|           |             |                |                            |
|    [BLE / WiFi]   [GPIO LEDs x8]   [GPIO button + thermistors]       |
|                                                                        |
| [Front diffuser strip] [Z1 LED] [Z2 LED] [Z3 LED] [Z4 LED] [Button]   |
+========================================================================+
```

---

## Guide Rail Dimensions

| Zone | Rail Material | Thickness | Height | Width | Notes |
|------|---------------|-----------|--------|-------|-------|
| Zone 1 | Clear acrylic | 3mm | 8mm | 5mm | Inward angle centers phone on Qi coil |
| Zone 2 | Clear acrylic | 3mm | 8mm | 5mm | Inward angle works for phone or AirPods case |
| Zone 3 | Clear acrylic | 3mm | 6mm | 5mm | Lower profile to avoid interfering with watch band |
| Zone 4 | Clear acrylic + rubber insert | 4mm | 40–50mm | 5mm+ | Supports laptop upright at 70–80° from horizontal |

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

| State | LED Color | Meaning |
|-------|-----------|---------|
| Charging | Red solid | Device is actively charging |
| Full | Green solid | Device is fully charged |
| No device | Off | No device detected on that zone |
| Dark mode | All off | Physical button or app disables every LED regardless of status |

---

## Notes
- Guide rails on Zones 1–3 are clear and low-profile so the dock still looks minimal from the front.
- Zone 3 watch cradle is recessed 8mm to hold the watch securely between the side rails.
- Zone 4 USB-C cable exits from the front-right edge or can terminate in a flush USB-C port depending on enclosure revision.
- Each LED sits behind a frosted diffuser strip at the front edge of its zone for a soft, premium glow.
- The dark mode button is front-facing for quick nighttime use, with matching app control available remotely.
- Rubber feet (x4) on underside provide grip and airflow.
