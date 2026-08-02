# Quad-Dock — Layout Diagram

Coordinate reference: [component-positions.md](component-positions.md)

## Top View (X/Y)

```text
Y=300 (rear)
X=-70                                                                  X=+70
+--------------------------------------------------------------------------------+
|      WATCH cradle base (-45,225)       LAPTOP groove (+40,15..285)  iPAD groove |
|      Ø50 pod, 30° tilt                 22mm wide, silicone-lined     (+80,15..285)* |
|                                                                                |
|  PHONE dish center (-45,60)            BUDS dish center (-45,140)             |
|  80×55 R10                              65×55 R10                               |
+--------------------------------------------------------------------------------+
Y=0 (front)

LED strip centerline: Y=-2.00, Z=1.50 (5× 56mm sections)
*Zone 5 groove is located on the right half beside Zone 4 in the widened top-view illustration.
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
| Zone 1 dish center | -45.00 | 60.00 | 14.50 |
| Zone 2 dish center | -45.00 | 140.00 | 17.17 |
| Zone 3 cradle base | -45.00 | 225.00 | 21.00 |
| Zone 4 groove center | +40.00 | 150.00 | right-half centered |
| Zone 5 groove center | +80.00 | 150.00 | right-half centered |
| Zone 4 USB-C port | +40.00 | 258.00 | 8.00 |
| Zone 5 USB-C port | +80.00 | 258.00 | 8.00 |
| IEC C13 inlet | 0.00 | 298.50 | 6.00 |
| M3 hole left | -60.00 | 150.00 | top plate |
| M3 hole right | +60.00 | 150.00 | top plate |
| Foot FL | -39.17 | 15.00 | -1.50 |
| Foot FR | +39.17 | 15.00 | -1.50 |
| Foot RL | -53.50 | 285.00 | -1.50 |
| Foot RR | +53.50 | 285.00 | -1.50 |

For the full exterior + interior list, use [component-positions.md](component-positions.md).
