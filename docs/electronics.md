# Quad-Dock — Electronics Specification

## Main Electronics

- MCU: ESP32-C3 Mini
- Monitoring: INA3221 (Zones 1–3), INA219 (Zone 4)
- Ambient sensor: BH1750
- Power: internal 180W AC/DC PSU + IEC C13 inlet
- Outputs: 2×15W Qi, 1×Watch puck, 1×USB-C PD board

## Exact Placement Coordinates

Exact interior/exterior positions are defined in [component-positions.md](component-positions.md).

Key electronics placements:

- PCB main board center: `X=-5.00, Y=110.00, Z=5.00`
- PCB extents: **X:-65.00..+55.00, Y:70.00..150.00**
- PCB standoff height: **5.00mm**
- PSU module center: `X=0.00, Y=210.00, Z=5.00`
- Qi coils: `(-20.00,70.00,4.00)` and `(+20.00,70.00,4.00)`
- Watch puck module: `(-22.00,225.00,4.00)`
- USB-C PD board center: `(+32.00,155.00,5.00)`

## Power Path

`IEC C13 -> 180W PSU -> zone branches + regulation -> monitoring + protections`

- Zone 1: Qi 15W + polyfuse + thermistor
- Zone 2: Qi 15W + polyfuse + thermistor
- Zone 3: Watch puck + polyfuse + thermistor
- Zone 4: USB-C PD + INA219 + polyfuse

## PCB Layout Notes

- Board position is fixed at **X:-65..+55, Y:70..150 on 5mm standoffs**.
- Keep Qi power traces wide and short to entry points near `Y≈75`.
- Keep INA3221/INA219 close to their branch sensing points.
- Keep ESP32-C3 antenna near the board edge with copper keep-out.
- Place BH1750 near edge exposure side for reliable ambient readings.
