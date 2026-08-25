# Penta Dock — Layout Diagram

## Top View (Penta Standard ~250mm wide × ~100mm deep × ~100mm tall)

```text
Rear spine plate at full width (~250mm) closes the back edge.
Front fascia strip at full width (~250mm) carries the LED diffuser along the front base.

+------------------+-------------------------------+------------------+
|  Z4 LAPTOP SLOT  |      3-STEP CENTRE STACK      |  Z5 TABLET SLOT  |
| 400mm long       | Step 3 (100×80): WATCH 5W     | 290mm long       |
| 90mm deep        | Step 2 (140×100): BUDS 20W    | 70mm deep        |
| 35mm wide        | Step 1 (180×110): PHONE 20W   | 20mm wide        |
| 95mm wall height | raised over PSU cavity        | 75mm wall height |
| Captive USB-C    | coils embedded in step bodies | Captive USB-C    |
| 220mm, 100W      | 20mm riser cavity below       | 200mm, 45W       |
| cable from top   |                               | cable from top   |
+------------------+-------------------------------+------------------+
        FRONT (fascia + diffuser)            REAR (spine + centred C13)
```

## Front View

```text
Standard width ~250mm

+-----------+   +---------------------------------+   +-----------+
|  LAPTOP   |   | Step 3: 100mm (Watch)           |   |  TABLET   |
|   SLOT    |   | Step 2: 140mm (Buds or second phone)      |   |   SLOT    |
| 35mm wide |   | Step 1: 180mm (Phone 20W)       |   | 20mm wide |
| 95mm tall |   | top reaches Z=95mm              |   | 75mm tall |
+-----------+   +---------------------------------+   +-----------+
[==== 20mm FRONT FASCIA STRIP WITH 250×15 LED DIFFUSER CHANNEL ====]
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

## Zone Quick Reference

| Zone | Location | Device | Power | Notes |
|---|---|---|---|---|
| Zone 1 | Centre Step 1 (base) | Phone | Qi2 20W | coil embedded in Step 1 body |
| Zone 2 | Centre Step 2 (middle) | Buds or second phone | Qi 20W | coil embedded in Step 2 body |
| Zone 3 | Centre Step 3 rear (top) | Watch (Apple puck + Qi) | 5W shared | puck + Qi coil embedded in Step 3 body |
| Zone 4 | Left slot | Laptop | USB-C PD 100W via captive 220mm cable | 35mm wide, 90mm deep, cable from top |
| Zone 5 | Right slot | Tablet/Phone | USB-C PD 45W via captive 200mm cable | 20mm wide, 70mm deep, cable from top |
