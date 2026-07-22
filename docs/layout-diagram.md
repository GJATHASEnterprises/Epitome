# Quad-Dock — Layout Diagram

Coordinate reference: [component-positions.md](component-positions.md)

## Top View (X/Y)

```text
Y=300 (rear)
X=-70                                                 X=+70
+----------------------------------------------------------------+
|      WATCH cradle base (-22,225)       LAPTOP groove (+29,294) |
|      Ø50 pod, 30° tilt                 X:+18..+40 Y:288..300   |
|                                                                |
|  PHONE dish center (-20,70)         BUDS dish center (+20,70)  |
|  80x55 R10                           65x55 R10                 |
+----------------------------------------------------------------+
Y=0 (front)

LED strip centerline: Y=-2.00, Z=1.50 (4x 71mm sections)
```

## Side View (Y/Z)

```text
Z
^                  top profile H(Y)=12+10*(Y/300)
|                /
|              /
|            /
|___________/__________________________________________> Y
0          0(front)                                300(rear)
```

## Exact Coordinates Quick Reference

| Feature | X (mm) | Y (mm) | Z (mm) |
|---|---:|---:|---:|
| Zone 1 dish center | -20.00 | 70.00 | 14.83 |
| Zone 2 dish center | +20.00 | 70.00 | 14.83 |
| Zone 3 cradle base | -22.00 | 225.00 | 21.00 |
| Zone 4 groove center | +29.00 | 294.00 | rear-wall centered |
| USB-C port | +29.00 | 297.00 | 8.00 |
| IEC C13 inlet | 0.00 | 298.50 | 6.00 |
| M3 hole left | -35.00 | 150.00 | top plate |
| M3 hole right | +30.00 | 150.00 | top plate |
| Foot FL | -39.17 | 15.00 | -1.50 |
| Foot FR | +39.17 | 15.00 | -1.50 |
| Foot RL | -53.50 | 285.00 | -1.50 |
| Foot RR | +53.50 | 285.00 | -1.50 |

For the full exterior + interior list, use [component-positions.md](component-positions.md).
