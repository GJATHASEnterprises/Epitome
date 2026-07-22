# Quad-Dock — Design Specification

> **Note:** This file provides a summary of the product spec. For detailed specifications see:
> - [Enclosure Specification](enclosure.md) — Arc design, dimensions, materials, zone layout, LED system
> - [Electronics Specification](electronics.md) — ESP32-C3, all ICs, power architecture, sensors
> - [Definitive Component Positions](component-positions.md) — exact X/Y/Z coordinates for all exterior/interior features

---

## Product Name
Quad-Dock

## Color Variants
- **Black** — Gunmetal brushed aluminum top, matte black soft-touch ABS base
- **White** — Silver brushed aluminum top, matte white soft-touch ABS base

---

## Physical Dimensions

| Dimension | Value |
|-----------|-------|
| Length | 300mm |
| Width (front edge) | 110mm |
| Width (rear edge) | 140mm |
| Height (front edge) | 12mm |
| Height (rear edge) | 22mm |
| Corner radius | R20mm (all edges) |

---

## Enclosure Design ("Arc")

Smooth curved wedge — wide at rear, slightly narrower at front. Zero sharp corners. R20mm radius on all edges.

- **Top plate:** 1.5mm brushed aluminum — Gunmetal (Black model), Silver (White model). Laser-etched zone icons and Quad-Dock wordmark.
- **Base:** Soft-touch matte ABS — Black or White. Laser cut + bent for Batch 1; injection mold from Batch 2.
- **Zone pockets:** Silicone-lined recessed dishes (2–3mm deep), replacing guide rails
- **Watch cradle:** Teardrop-shaped elevated pod, rear-left, 30° tilt toward user
- **Laptop groove:** Rear-right, 22mm wide × 12mm deep, silicone-lined. Laptop stands vertically on its spine.
- **LED system:** WS2812B strip hidden under front lip with frosted diffuser. 4 sections divided by recessed lines. Laser-etched zone icons above each section.
- **Assembly:** Snap-fit base + 2× M3 screws only
- **Cooling:** Vents on base
- **Top plate:** Removable for service access

---

## Zone Layout

Exact zone anchors:
- Zone 1: `X=-20.00, Y=70.00`
- Zone 2: `X=+20.00, Y=70.00`
- Zone 3: `X=-22.00, Y=225.00`
- Zone 4: `X=+29.00, Y=294.00` (`X:+18..+40, Y:288..300`)

```
         ← 300mm →
+----------------------------------------------+  ← rear (140mm wide, 22mm high)
|  [⌚ ZONE 3 — Watch]    [💻 ZONE 4 — Laptop]  |
|  Teardrop pod            Vertical spine       |
|  30° tilt, rear-left     groove, rear-right   |
+----------------------------------------------+  ← arc taper
|  [📱 ZONE 1 — Phone]   [🎧 ZONE 2 — Buds]    |
|  15W Qi + magnets        15W Qi               |
+---[■ PHONE ■|■ BUDS ■|■ WATCH ■|■ LAPTOP ■]--+
← front (110mm wide, 12mm high) →
                   IEC C13 inlet (rear centre)
```

---

## Zone Specifications

### Zone 1 — Phone (Qi 15W)
- 50mm Qi TX coil, 15W
- N52 ring magnets for phone alignment (MagSafe-style)
- Silicone-lined recessed dish

### Zone 2 — Buds / Phone (Qi 15W)
- 50mm Qi TX coil, 15W
- Works for AirPods (Qi case) or a second phone
- Silicone-lined recessed dish

### Zone 3 — Apple Watch
- Apple Watch magnetic puck (wired internally)
- 5W output
- Teardrop cradle, 30° tilt, rear-left position
- Compatible: Apple Watch Series 1–9, SE, Ultra

### Zone 4 — Laptop / USB-C PD (100W)
- USB-C PD, up to 100W
- Laptop groove: 22mm wide × 12mm deep, silicone-lined
- Laptop stands vertically on its spine
- Compatible: any USB-C laptop (2018+)

---

## LED Status System

| State | Color | Meaning |
|-------|-------|---------|
| Charging | Red | Device charging on that zone |
| Full | Green | Device fully charged |
| Empty | Off | No device detected |

---

## Electronics Summary

See [electronics.md](electronics.md) for full spec.

- **MCU:** ESP32-C3 Mini (WiFi + BLE, flashed via onboard USB)
- **Power monitors:** INA3221 (Zones 1–3), INA219 (Zone 4)
- **Ambient light:** BH1750 (I2C)
- **LED:** WS2812B strip (16 LEDs, 4 per zone)
- **Charging:** 2× Qi 15W (Zones 1–2), Watch puck 5W (Zone 3), USB-C PD 100W (Zone 4)
- **PSU:** Internal 180W AC/DC (IEC C13 inlet, no external power brick)
- **No USB-A port**
- **No physical buttons**

---

## Packaging

- Rigid kraft box with structured corners
- Die-cut foam insert
- Black tissue paper wrap
- Quad-Dock logo sticker on tissue
- QR code card (setup + warranty)
- No IEC cable bundled

---

## Price

**$189** — Black or White
