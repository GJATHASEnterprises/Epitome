# Quad-Dock — Electronics Specification

## Main Electronics

- MCU: ESP32-C3 Mini
- Monitoring: INA3221 (Zones 1–3), INA219 Zone 4 (100W), INA219 Zone 5 (20W)
- Ambient sensor: BH1750
- Power: internal 180W AC/DC PSU + IEC C13 inlet
- Outputs: 2×15W Qi, 1×Watch puck, 2×USB-C PD boards (100W + 20W)

## Exact Placement Coordinates

Exact interior/exterior positions are defined in [component-positions.md](component-positions.md).

Key electronics placements:

- PCB main board center: `X=-35.00, Y=110.00, Z=5.00`
- PCB extents: **X:-95.00..+25.00, Y:70.00..150.00**
- PCB standoff height: **5.00mm**
- PSU module center: `X=0.00, Y=210.00, Z=5.00`
- Qi coils: `(-45.00,60.00,4.00)` and `(-45.00,140.00,4.00)`
- Watch puck module: `(-45.00,225.00,4.00)`
- USB-C PD board Zone 4 center: `(+40.00,150.00,5.00)`
- USB-C PD board Zone 5 center: `(+80.00,150.00,5.00)`
- Zone 5 INA219: `(+75.00,150.00,8.50)`
- Zone 5 USB-C port: `(+80.00,258.00,8.00)`

## Power Path

`IEC C13 -> 180W PSU -> zone branches + regulation -> monitoring + protections`

- Zone 1: Qi 15W + polyfuse + thermistor
- Zone 2: Qi 15W + polyfuse + thermistor
- Zone 3: Watch puck + polyfuse + thermistor
- Zone 4: USB-C PD 100W + INA219 + polyfuse + thermistor
- Zone 5: USB-C PD 20W + INA219 + polyfuse + thermistor

## Power Budget

| Zone | Power |
|---|---:|
| Zone 1 Phone Qi2 | 15W |
| Zone 2 Buds Qi | 5W |
| Zone 3 Watch | 5W |
| Zone 4 Laptop | 100W |
| Zone 5 iPad/Phone | 20W |
| **Total** | **145W** |
| PSU (180W) headroom | **35W spare** |

## PCB Layout Notes

- Board position is fixed at **X:-95..+25, Y:70..150 on 5mm standoffs**.
- Keep Qi power traces wide and short to entry points near `Y≈60` and `Y≈140`.
- Keep INA3221 and both INA219 monitors close to their branch sensing points.
- Route the Zone 5 PD branch to the right-half secondary groove and keep the 20W board close to the `X=+80` slot.
- Keep ESP32-C3 antenna near the board edge with copper keep-out.
- Place BH1750 near edge exposure side for reliable ambient readings.

## Night Mode / Sleep Mode

- **Trigger:** local time 23:00–07:00 (configurable via app, default ON)
- **LED behaviour:** all zone LEDs off unless that zone has active power draw > 0.5W (read via INA3221/INA219)
- **Notification behaviour:** theft alert push notifications silenced overnight (configurable, default ON)
- **Implementation:** ESP32-C3 stores time via SNTP over WiFi; falls back to BLE-synced time from phone if no WiFi
- **Override:** placing a new device on any zone during night mode briefly illuminates that zone's LED for 3 seconds to confirm charging started, then returns to off
