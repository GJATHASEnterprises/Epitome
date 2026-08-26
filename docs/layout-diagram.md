# Penta Dock — Layout Diagram

## Top View (Penta Standard ~250mm wide × ~100mm deep × ~100mm tall)

```text
+----------+--------------------------------------------------+----------+
| Z4       |           3-STEP CENTRE PLATFORM                | Z5       |
| LAPTOP   | Step 1 (180mm wide) — Phone 20W Qi2             | TABLET   |
| SLOT     | Step 2 (140mm wide) — Buds/Phone 20W Qi         | SLOT     |
| 35mm     | Step 3 (100mm wide, rear 20mm setback) — Watch 5W | 20mm   |
| 400mm L  | All step faces point TOWARD USER (front-facing) | 290mm L  |
| 90mm D   | Steps rise front→back between the two slots    | 70mm D   |
| 35mm W   | Riser cavity 17mm over PSU beneath             | 20mm W   |
| 95mm H   |                                               | 75mm H   |
+----------+--------------------------------------------------+----------+
REAR SPINE: full width, IEC C13 rear-left ~X=45mm
FRONT FASCIA: full width, LED diffuser strip 250×15mm
```

## Front View

```text
Standard width ~250mm

+----------+   +------+   +-----------+   +------+   +----------+
| LAPTOP   |   |      |   | Step 3    |   |      |   | TABLET   |
| SLOT     |   |      |   | 100mm     |   |      |   | SLOT     |
| 35mm     |   | Step |   +-----------+   | Step |   | 20mm     |
| 95mm     |   |  2   |   Step 2          |  2   |   | 75mm     |
| tall     |   | 140mm|   140mm wide      | 140mm|   | tall     |
|          |   |      +-------------------+      |   |          |
|          |   Step 1 — 180mm wide               |   |          |
+----------+---+-------------------------------------+-+----------+
[============= 250mm FRONT FASCIA + LED DIFFUSER =============]
```

## Side View (centre platform)

```text
Z
^
98mm  |
95mm  |            +------------------+  Step 3 top (watch)
80mm  |       +-----------------------+  Step 2 top
65mm  |  +----------------------------+  Step 1 top
50mm  |  +============================+  Step 1 base / riser cavity top
33mm  |  |     PSU 199×98×30mm       |  PSU top
 3mm  |  +============================+  PSU base / base plate top
 0mm  |__|____________________________|____> depth (~100mm)
       rear spine                front fascia
```

Side-view note: **17mm riser cavity (Z=33–50)**.

## Zone Quick Reference

| Zone | Location | Device | Power | Notes |
|---|---|---|---|---|
| Zone 1 | Centre Step 1 (base) | Phone | Qi2 20W | coil embedded in Step 1 body |
| Zone 2 | Centre Step 2 (middle) | Buds or second phone | Qi 20W | coil embedded in Step 2 body |
| Zone 3 | Centre Step 3 rear (top) | Watch (Apple puck + Qi) | 5W shared | puck + Qi coil embedded in Step 3 body |
| Zone 4 | Left slot | Laptop | USB-C PD 100W via captive 220mm cable | 35mm wide, 90mm deep, cable from top |
| Zone 5 | Right slot | Tablet/Phone | USB-C PD 45W via captive 200mm cable | 20mm wide, 70mm deep, cable from top |
| IEC inlet | Rear spine | AC input | IEC C13 | rear-left ~X=45mm |
