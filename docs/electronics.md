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

- PCB main board center: `X=-35.00, Y=110.00, Z=5.00`
- PCB extents: **X:-95.00..+25.00, Y:70.00..150.00**
- PCB standoff height: **5.00mm**
- PSU module center: `X=0.00, Y=210.00, Z=5.00`
- Qi coils: `(-45.00,60.00,4.00)` and `(-45.00,140.00,4.00)`
- Watch puck module: `(-45.00,225.00,4.00)`
- USB-C PD board center: `(+50.00,150.00,5.00)`

## Power Path

`IEC C13 -> 180W PSU -> zone branches + regulation -> monitoring + protections`

- Zone 1: Qi 15W + polyfuse + thermistor
- Zone 2: Qi 15W + polyfuse + thermistor
- Zone 3: Watch puck + polyfuse + thermistor
- Zone 4: USB-C PD + INA219 + polyfuse

## PCB Layout Notes

- Board position is fixed at **X:-95..+25, Y:70..150 on 5mm standoffs**.
- Keep Qi power traces wide and short to entry points near `Y≈60` and `Y≈140`.
- Keep INA3221/INA219 close to their branch sensing points.
- Keep ESP32-C3 antenna near the board edge with copper keep-out.
- Place BH1750 near edge exposure side for reliable ambient readings.
