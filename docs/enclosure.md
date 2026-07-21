# Quad-Dock — Enclosure Specification

---

## Design Name

**Arc** — smooth curved wedge, wide at rear, slightly narrower at front. Zero sharp corners. R20mm radius on all edges.

---

## Dimensions

| Dimension | Value |
|-----------|-------|
| Length | 300mm |
| Width (front edge) | 110mm |
| Width (rear edge) | 140mm |
| Height (front edge) | 12mm |
| Height (rear edge) | 22mm |
| Corner radius | R20mm (all edges) |

The tapered wedge profile means the dock naturally angles devices slightly toward the user. The rear height of 22mm is set specifically to accommodate the laptop groove (22mm wide × 12mm deep) without the groove cutting through the base.

---

## Materials

### Top Plate
- **Material:** Brushed aluminum (1.5mm sheet)
- **Finish (Black model):** Gunmetal anodized
- **Finish (White model):** Silver brushed natural
- **Manufacturing:** Laser cut to Arc profile, local laser cutter at 50+ units
- **Features:** Laser-etched zone icons + labels, Quad-Dock wordmark on rear edge
- **Fastening:** Snap-fit + 2× M3 screws (removable for service)

### Base
- **Material:** Soft-touch matte ABS
- **Finish (Black model):** Matte black
- **Finish (White model):** Matte white
- **Manufacturing:** Laser cut + bent for Batch 1; injection mold from Batch 2 (see [production-roadmap.md](production-roadmap.md))
- **Features:** Cooling vents, rubber feet with embossed Quad-Dock logo

---

## Zone Layout

```
         ← 300mm long →
+----------------------------------------------+  ← rear edge (140mm wide, 22mm high)
|                                              |
|  [⌚ ZONE 3]              [💻 ZONE 4]         |
|  Watch cradle               Laptop groove    |
|  Teardrop pod               22×12mm slot     |
|  30° tilt, rear-left        rear-right       |
|                                              |
+----------------------------------------------+  ← taper / curve
|                                              |
|  [📱 ZONE 1]    [🎧 ZONE 2]                  |
|  Phone Qi       Phone/Buds Qi                |
|  15W + magnets  15W                          |
|                                              |
+---[■ PHONE ■|■ BUDS ■|■ WATCH ■|■ LAPTOP ■]--+  ← LED bar under front lip
← front edge (110mm wide, 12mm high) →
                     IEC C13 inlet (rear centre)
```

---

## Zone Pocket Specification

Each zone has a **silicone-lined recessed dish** (replacing guide rails from earlier designs):

| Zone | Shape | Depth | Silicone | Notes |
|------|-------|-------|----------|-------|
| Zone 1 — Phone | Rounded rectangle | 2–3mm | Yes | N52 ring magnets beneath for phone alignment |
| Zone 2 — Buds | Rounded rectangle | 2–3mm | Yes | Works for AirPods case or phone |
| Zone 3 — Watch | Teardrop pod | Elevated | Yes | See Watch Cradle spec below |
| Zone 4 — Laptop | Groove slot | 12mm deep | Yes, lining | See Laptop Groove spec below |

---

## Watch Cradle Specification

- **Shape:** Teardrop-shaped elevated pod
- **Position:** Rear-left
- **Tilt:** 30° toward user (faces user when sitting at desk)
- **Purpose:** Apple Watch rests on puck face-up, band drapes naturally
- **Material:** Same ABS as base, silicone contact surface
- **Puck:** Apple Watch magnetic charging module mounted internally

---

## Laptop Groove Specification

- **Position:** Rear-right
- **Orientation:** Laptop stands **vertically on its spine** (bottom edge down)
- **Groove dimensions:** 22mm wide × 12mm deep
- **Lining:** Silicone-lined on all three groove surfaces (prevents scratching)
- **Why 22mm wide:** Accommodates most laptop base widths (MacBook Pro 16" base is ~18mm; 22mm gives 2mm clearance each side)
- **Why 12mm deep:** Provides stable grip without needing to force the laptop in
- **Rear height:** 22mm total — groove occupies 12mm of the 22mm rear height, leaving 10mm of solid base material below

---

## LED System

### Hardware
- **Strip type:** WS2812B addressable RGB LED strip
- **Position:** Hidden under front lip overhang (indirect glow, not direct-view)
- **Diffuser:** Frosted acrylic diffuser strip over LED bar for smooth, even glow
- **Sections:** 4 clearly separated sections divided by recessed lines in the diffuser housing

### Zone Icon Labels (Laser-Etched on Aluminum Top Plate)
Etched directly above each LED section:

| Zone | Icon | Label |
|------|------|-------|
| Zone 1 | 📱 | PHONE |
| Zone 2 | 🎧 | BUDS |
| Zone 3 | ⌚ | WATCH |
| Zone 4 | 💻 | LAPTOP |

### LED States

| State | Color | Meaning |
|-------|-------|---------|
| Charging | Red | Device actively charging on that zone |
| Full | Green | Device fully charged on that zone |
| Empty | Off | No device on that zone |

---

## Branding

- **Top plate rear edge:** Quad-Dock wordmark laser-etched into aluminum
- **Rubber feet:** Quad-Dock logo embossed into each foot
- **No other external branding** — clean, minimal aesthetic

---

## Assembly

- **Fastening:** Snap-fit base + 2× M3 screws only (no full screw assembly)
- **Top plate:** Removable — snap + 2 screws, accessible for DIY repair
- **Rubber feet:** ×4 on underside

---

## Finish Options

| Feature | Black Model | White Model |
|---------|-------------|-------------|
| Aluminum top | Gunmetal anodized brushed | Silver natural brushed |
| ABS base | Matte black soft-touch | Matte white soft-touch |
| LED glow | Warm, subtle | Bright, clean |

---

## Manufacturing by Batch

### Batch 1 — Laser Cut + Bent (No Mold)
- Enclosure formed from laser-cut and hand-bent ABS sheet
- Top plate: aluminum sheet laser-cut to Arc profile
- No injection mold tooling cost — ~$0 setup
- Per-unit enclosure cost: ~$12–$18
- Target: 17–19 units at $1,500 total investment
- Appearance: Still looks clean and sharp; slightly more handmade character

### Batch 2 — Injection Mold
- ABS base injection mold ordered after break-even (~13 units sold)
- Mold cost: $800–$1,500 one-time
- Per-unit cost drops to ~$6–$10 for the base
- Consistent production quality, exact Arc geometry every unit
- See [production-roadmap.md](production-roadmap.md)

---

## Cooling

- Passive airflow via vents slotted into the base underside
- Aluminum top plate acts as a passive heat spreader for Qi coils
- No fan required at 180W PSU / normal operating draw
