# Epitome Step — Physical Design Specification

Both models (Walnut and Obsidian) share identical geometry. This document covers all shared dimensions, zone positions, and material differences.

---

## Coordinate system

- X: left → right (0 at left edge)
- Y: front → rear (0 at front face)
- Z: bottom → top (0 at base underside)

---

## Overall dimensions

| Parameter | Value |
|---|---|
| Width (X) | 165 mm |
| Depth (Y) | 100 mm |
| Height (Z) | 70 mm |
| Footprint area | 165 cm² |

---

## Step geometry table

| Component | X start | X end | Width | Y start | Y end | Depth | Z start | Z end | Height |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Base plate | 0 | 165 | 165 mm | 0 | 100 | 100 mm | 0 | 3 | 3 mm |
| Riser / wiring cavity | 0 | 165 | 165 mm | 0 | 100 | 100 mm | 3 | 25 | 22 mm |
| Step 1 (phone) | 0 | 165 | 165 mm | 0 | 100 | 100 mm | 25 | 40 | 15 mm |
| Step 2 (buds) | 17.5 | 147.5 | 130 mm | 0 | 100 | 100 mm | 40 | 55 | 15 mm |
| Step 3 (watch) | 35 | 130 | 95 mm | 20 | 100 | 80 mm | 55 | 70 | 15 mm |

Step 3 is set back 20 mm from the front face (Y starts at 20 mm, not 0). This provides lateral support and hides the watch cradle wiring behind the step face.

---

## Charging zone positions

| Zone | Device | Surface Z | Notes |
|---|---|---:|---|
| Zone 1 | Phone | 40 mm | Centred on Step 1, portrait orientation |
| Zone 2 | Buds / small phone | 55 mm | Centred on Step 2 |
| Zone 3 | Watch | 70 mm | Centred on Step 3, Y = 20 – 100 |

### Silicone pads / cradles

| Zone | Pad size | Notes |
|---|---|---|
| Zone 1 | 75 × 90 mm portrait | 1 mm recess in walnut / ABS surface |
| Zone 2 | 65 × 50 mm | Flat pad, no recess |
| Zone 3 | 55 × 55 mm cradle | Raised lip, watch sits in well |

---

## Rear face port positions (all at Z = 15, Y = 100)

| Port | X position | Description |
|---|---:|---|
| DC barrel jack inlet | X = 40 | Main power in |
| USB-C Port A | X = 120 | 60W PD |
| USB-C Port B | X = 140 | 30W PD |

---

## Riser / wiring cavity — flat-mount rule

The riser cavity (Z = 3 to Z = 25, usable height = 22 mm) contains all active electronics. **Maximum component height is 18 mm** to leave 4 mm clearance below the Step 1 floor.

All boards must be flat-mounted (lying horizontal). No upright PCBs. JST connectors oriented sideways.

---

## Material differences table

| Part | Walnut model | Obsidian model |
|---|---|---|
| Step faces (×3 sides) | 4 mm laser-cut oiled walnut | 4 mm laser-cut matte black ABS |
| Step top surfaces (×3) | 4 mm laser-cut oiled walnut | 4 mm laser-cut matte black ABS |
| Base plate | Matte black ABS (3D printed) | Matte black ABS (3D printed) |
| Riser / wiring cavity | Matte black ABS (3D printed) | Matte black ABS (3D printed) |
| Rear spine | Laser-cut ABS 165 × 35 mm | Laser-cut ABS 165 × 35 mm |
| LED strip | WS2811, warm white (#FFD6A0) | WS2812B, full RGB |
| Step face edge profile | Soft rounded (hand-sanded) | Sharp angular |

---

## ASCII diagrams

### Front view

```
         ┌────────────────────────────┐  ← Step 3 top (Z=70, 95mm wide)
         │       Watch Zone           │
    ┌────┴────────────────────────────┴────┐  ← Step 2 top (Z=55, 130mm wide)
    │           Buds Zone                  │
┌───┴──────────────────────────────────────┴───┐  ← Step 1 top (Z=40, 165mm wide)
│                  Phone Zone                   │
│━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━│  ← LED diffuser strip (Z=25–40)
│              RISER  (Z=3–25)                  │
└───────────────────────────────────────────────┘  ← Base (Z=0–3)
                  165 mm wide
```

### Side view (cross-section at X = 82.5)

```
70mm ┤     ┌──────┐
     │     │Watch │
55mm ┤   ┌─┘      │
     │   │ Buds   │
40mm ┤ ┌─┘        │
     │ │  Phone   │
25mm ┤ │──────────│  ← LED diffuser
 3mm ┤ │  Riser   │
  0  ┤ └──────────┘
     └──────────────→
        0          100mm (Y)
```

### Top view (Z = 40, looking down)

```
←───────────────── 165 mm ──────────────────→
┌───────────────────────────────────────────┐  Y=0
│          [  Phone Qi2 pad 75×90  ]        │
│               Zone 1                      │
│   ┌─────────────────────────────────┐     │
│   │      [  Buds Qi pad 65×50  ]   │     │
│   │           Zone 2                │     │  Y=50
│   │   ┌───────────────────────┐    │     │
│   │   │ [Watch cradle 55×55] │    │     │
│   │   │      Zone 3          │    │     │  Y=60
│   │   └───────────────────────┘    │     │
│   └─────────────────────────────────┘     │
└───────────────────────────────────────────┘  Y=100
```

### Rear view

```
←─────────────── 165 mm ──────────────────→
┌──────────────────────────────────────────┐
│  [DC]        [USB-C A]  [USB-C B]        │
│  X=40         X=120      X=140           │
│            (all Z=15)                    │
└──────────────────────────────────────────┘
```

---

## Step 3 setback — rationale

Step 3 starts at Y = 20 (20 mm from front face). Benefits:
1. Adds structural wall thickness on the front of Step 3 (≥ 3 mm ABS wall above Step 2 level)
2. Conceals watch cradle wiring
3. Visually anchors Step 3 rearward — makes the staircase silhouette more dramatic from the front

