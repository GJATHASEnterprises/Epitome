# Epitome Penta — Design Specification

> **Note:** This file provides a summary of the product spec. For detailed specifications see:
> - [Enclosure Specification](enclosure.md)
> - [Electronics Specification](electronics.md)
> - [Definitive Component Positions](component-positions.md)
> - [Packaging Specification](packaging.md)
> - [Firmware Notes](firmware-notes.md)

---

## Product Name
Epitome Penta

## Brand
Epitome

## Color Variants
- **Black** — Gunmetal brushed aluminum top, matte black soft-touch ABS base
- **White** — Silver brushed aluminum top, matte white soft-touch ABS base

---

## Physical Dimensions

| Dimension | Value |
|-----------|-------|
| Overall width | ~700mm |
| Overall depth | ~300mm |
| Left slot depth | 25mm (laptop, open front) |
| Right slot depth | 25mm (iPad, open front) |
| Step 1 height | base level (0mm) |
| Step 2 height | +40mm |
| Corner radius | R20mm (all edges) |
| Top plate thickness | 1.5mm brushed aluminum |

---

## Enclosure Design — Stepped Centre Platform

The Epitome Penta uses a **stepped centre platform** flanked by two open-front device slots.

- **Left slot** — Laptop slides in horizontally on its side, open front entry. USB-C charging port in rear wall of slot. Sized for up to 17" laptop (395mm wide × 18mm thick).
- **Right slot** — iPad slides in horizontally on its side, open front entry. USB-C charging port in rear wall of slot. Sized for iPad Pro 13" (281mm tall × 5.1mm thick).
- **Centre Step 1** (lower, base level) — Phone Qi wireless pad (15W MagSafe-compatible). Large enough that a phone can also be placed here as an alternative.
- **Centre Step 2** (upper, +40mm) — Apple Watch cradle + AirPods Pro Qi pad side by side. Wide enough that a phone can be placed on the buds pad if needed.
- **Base:** Matte ABS, Black or White.
- **Top surfaces:** 1.5mm brushed aluminium, Gunmetal or Silver.
- **Silicone lining** in all slots and pads.
- **LED system:** WS2812B strip on front face, 5 sections.
- **Single IEC C13 power inlet** at rear.
- **Internal 180W PSU** — no external brick.

---

## Device Sizing Reference

| Device | Model sized for | Key dimension |
|---|---|---|
| Phone | iPhone 16 Pro Max | 163mm tall × 77mm wide × 8.25mm thick |
| iPad | iPad Pro 13" | 281mm tall × 215mm wide × 5.1mm thick |
| Laptop | 17" generic | 395mm wide × 270mm deep × 18mm thick |
| Watch | Apple Watch Ultra 2 | 49mm case, 51mm wide with lugs |
| Buds | AirPods Pro | 65mm × 45mm × 21mm case |

---

## Zone Layout

```
[TOP VIEW — 700mm wide × 300mm deep]

+------------------+--------------------+------------------+
|                  |   STEP 2 (+40mm)   |                  |
|   LAPTOP SLOT    |--------------------|   iPAD SLOT      |
|   (open front)   |  WATCH  |  BUDS   |   (open front)   |
|   USB-C 100W     |  cradle |  pad    |   USB-C 20W      |
|   in rear wall   |--------------------|   in rear wall   |
|                  |   STEP 1 (base)    |                  |
|                  |--------------------|                  |
|                  |      PHONE         |                  |
|                  |      pad 15W       |                  |
+------------------+--------------------+------------------+
[FRONT — user faces this edge]
```

---

## Zone Specifications

### Zone 1 — Phone (Qi 15W)
- 50mm Qi TX coil, 15W
- N52 ring magnets for MagSafe-style alignment
- Silicone-lined recessed dish on Step 1
- Centre platform, lower step

### Zone 2 — AirPods Pro (Qi 5W)
- Qi wireless TX, 5W
- Silicone-lined pad on Step 2, beside watch cradle
- Large enough to also place a phone if needed

### Zone 3 — Apple Watch
- Apple Watch magnetic puck (wired internally)
- 5W output
- Cradle on Step 2, beside buds pad
- Compatible: Apple Watch Series 1–9, SE, Ultra 2

### Zone 4 — Laptop (USB-C PD 100W)
- USB-C PD, up to 100W
- Left slot, open front, laptop slides in on its side
- Slot sized: 400mm wide × 25mm deep × 20mm tall
- USB-C female port in rear wall of slot
- Compatible: any USB-C laptop up to 17"

### Zone 5 — iPad (USB-C PD 20W)
- USB-C PD 2.0, up to 20W
- Right slot, open front, iPad slides in on its side
- Slot sized: 290mm wide × 25mm deep × 8mm tall
- USB-C female port in rear wall of slot
- Compatible: iPad Pro 13", any USB-C tablet

---

## LED Status System

| State | Color | Meaning |
|-------|-------|--------|
| Charging | Red | Device charging |
| Full | Green | Device fully charged |
| Empty | Off | No device detected |

Night mode: all LEDs off 23:00–07:00 unless zone draws >0.5W.

---

## Electronics Summary

See [electronics.md](electronics.md) for full spec.

- **MCU:** ESP32-C3 Mini (WiFi + BLE)
- **Power monitors:** INA3221 (Zones 1–3), INA219 (Zone 4), INA219 (Zone 5)
- **Ambient light:** BH1750 (I2C)
- **LED:** WS2812B strip (20 LEDs, 4 per zone)
- **PSU:** Internal 180W AC/DC (IEC C13 inlet)
- **No USB-A port**
- **No physical buttons**

---

## Packaging

- Rigid kraft or matte-black retail box
- Die-cut foam insert
- Black tissue paper wrap
- Epitome Penta logo sticker
- Quick-start guide
- Warranty card
- 1.5m braided IEC C13 cable in-box

---

## Price

**$249** — Black or White
Early bird: **$199** (first 20 pre-orders)
Retail post-launch: **$279**
