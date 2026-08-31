# Step — Component Positions

All coordinates use the Step coordinate system:
- X=0 left edge, X=165 right edge, centred at X=82.5
- Y=0 front, Y=100 rear
- Z=0 base floor, up = +Z

---

## Charging Zones

| Component | X | Y | Z | Notes |
|---|---|---|---|---|
| Zone 1 phone pad centre | 82.5 | 50 | 40 | 75×90mm portrait, Step 1 top |
| Zone 2 buds pad centre | 82.5 | 50 | 55 | 65×50mm, Step 2 top |
| Zone 3 watch cradle centre | 82.5 | 60 | 70 | 55×55mm, Step 3 top (set back) |

---

## Rear Face Connectors

| Component | X | Y | Z | Notes |
|---|---|---|---|---|
| DC barrel jack inlet | 40 | 100 | 15 | Rear centre-left |
| USB-C Port A (60W) | 120 | 100 | 15 | Rear right |
| USB-C Port B (30W) | 140 | 100 | 15 | Rear right, outboard of Port A |

---

## Front Fascia

| Component | X | Y | Z | Notes |
|---|---|---|---|---|
| LED diffuser strip | 17.5–147.5 | 0 | ~32 | 130mm wide × 8mm tall, front face of Step 1 riser |

---

## Internal (Riser Cavity, Z=3 to Z=25)

All internal components are flat-mounted in the riser cavity. Clearance: 22mm maximum height.

| Component | X (approx) | Y (approx) | Z | Notes |
|---|---|---|---|---|
| 12V buck converter | 20 | 20 | 3 | Flat mount |
| 5V buck converter | 20 | 50 | 3 | Flat mount |
| ATtiny85 | 82.5 | 30 | 3 | Flat mount, centred |
| Qi2 20W TX board | 82.5 | 50 | 25 | Under Step 1 top surface |
| Qi 5W TX board | 82.5 | 50 | 40 | Under Step 2 top surface |
| Apple Watch puck PCBA | 82.5 | 60 | 55 | Under Step 3 surface |
| Qi watch coil | 82.5 | 60 | 55 | Under Step 3, relay-switched |
| Hardware relay | 82.5 | 60 | 3 | Riser cavity, flat mount |
| USB-C PD 60W board | 110 | 90 | 3 | Riser cavity, near rear spine |
| USB-C PD 30W board | 130 | 90 | 3 | Riser cavity, near rear spine |
| WS2811 LED strip | 17.5–147.5 | 2 | 27 | Behind LED diffuser |

---

## Step Geometry Reference

| Feature | X range | Y range | Z range |
|---|---|---|---|
| Base plate | 0–165 | 0–100 | 0–3 |
| Riser cavity | 0–165 | 0–100 | 3–25 |
| Step 1 block | 0–165 | 0–100 | 25–40 |
| Step 2 block | 17.5–147.5 | 0–100 | 40–55 |
| Step 3 block | 35–130 | 20–100 | 55–70 |
