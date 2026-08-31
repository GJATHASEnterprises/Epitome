# Step — Layout Diagrams

Coordinate system: X=0 left, X=165 right, Y=0 front, Y=100 rear, Z=0 base

---

## Top View

```
X=0                                           X=165
|<------------------ 165mm ------------------>|
+---------------------------------------------+  Y=0 (FRONT)
|                                             |
|  +-----------------------------------------+
|  |           Step 1 top (Z=40)             |
|  |   +-------[  75×90mm phone pad  ]-------+
|  |   |          centred X=82.5, Y=50       |
|  +-----------------------------------------+
|        +-------------------------------+
|        |     Step 2 top (Z=55)        |
|        |  [  65×50mm buds pad  ]      |
|        |   centred X=82.5, Y=50       |
|        +-------------------------------+
|              +------------------+
|              | Step 3 top (Z=70)|  <-- Y=20 setback
|              | [55×55 watch pad]|
|              | centred X=82.5   |
|              +------------------+
|                                             |
+---------------------------------------------+  Y=100 (REAR)
       [DC IN]       [USB-A]  [USB-B]
        X=40          X=120    X=140
```

---

## Front View (staircase rising away from user)

```
                         +----------+
                         |  Step 3  |  Z=55–70, 95mm wide
               +---------+  watch   |
               |  Step 2  +----------+
               |  buds    |            Z=40–55, 130mm wide
+----+---------+----------+
|    |          Step 1 (phone)         Z=25–40, 165mm wide
| B  +--[ === LED DIFFUSER === ]--+
| A  |                             |
| S  |   riser cavity (22mm)       |   Z=3–25
| E  |                             |
+----+-----------------------------+   Z=0
     |  base plate  3mm            |
     +---------------------------------+

     |<-------- 165mm ------------->|
```

---

## Side Cross-Section (left edge view, Y=50)

```
Z=70 |            +--------+
     |            | Step 3 |  15mm walnut top
     |            | (watch)|
Z=55 |      +-----+--------+
     |      |  Step 2       |  15mm
     |      |  (buds)       |
Z=40 +------+---------------+
     |   Step 1              |  15mm
     |   (phone)             |
Z=25 +-----------------------+
     | ~~~~riser cavity~~~~  |  22mm  <-- all PCBs + wiring here
Z=3  +=======================+
     |  base plate           |  3mm
Z=0  +=======================+
     |   bumpons ×4          |
```

---

## Rear View

```
+---------------------------------------------+
|                                             |
|                                             |
|   [DC IN]              [USB-C A] [USB-C B]  |
|   X=40, Z=15           X=120    X=140       |
|   barrel jack           60W PD   30W PD     |
|                         Z=15      Z=15      |
+---------------------------------------------+
|<------------------ 165mm ------------------>|
```

---

## Zone Summary

| Zone | Step | Top Z | Width | Depth | Pad size |
|---|---|---|---|---|---|
| 1 — Phone | Step 1 | Z=40 | 165mm | 100mm | 75×90mm portrait |
| 2 — Buds | Step 2 | Z=55 | 130mm | 100mm | 65×50mm |
| 3 — Watch | Step 3 | Z=70 | 95mm | 80mm | 55×55mm |
