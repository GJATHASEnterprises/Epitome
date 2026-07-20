# Quad Device Dock — Design Specification

---

## Product Name
Quad Device Dock

## Version
1.0 (MVP)

---

## Physical Dimensions (Target)

| Dimension | Target |
|-----------|--------|
| Length | 280–320mm |
| Width | 120–140mm |
| Height | 20–35mm (base) + device slots |
| Weight | ~400–600g (assembled) |

---

## Enclosure Design

- **Material:** Matte ABS plastic or CNC-cut acrylic (self-manufactured)
- **Finish:** Matte black or dark grey (premium feel)
- **Surface:** Soft-touch or rubberized top surface to grip devices
- **Cable management:** Single recessed cable exit at rear
- **LED indicators:** Per-zone status LEDs (subtle, low-brightness)
- **Branding:** Laser-etched or pad-printed logo on front face

---

## Zone Layout

```
+----------------------------------------------------------+
|                  QUAD DEVICE DOCK                        |
|                                                          |
|  [ ZONE 1 ]    [ ZONE 2 ]    [ ZONE 3 ]   [ ZONE 4 ]   |
|   Phone Qi      Phone/Buds    Watch Puck   USB-C PD     |
|   Wireless      Wireless      Built-in     Cable Out    |
|                                                          |
|  [LED]          [LED]         [LED]        [LED]        |
+---------------------------[ USB-C IN ]-------------------+
```

---

## Zone Specifications

### Zone 1 — Phone (Qi Wireless)
- Coil diameter: 50mm
- Output power: 5W–15W (auto-negotiated)
- Compatible: iPhone (MagSafe-adjacent), Android Qi devices
- Alignment guide: subtle raised ring on surface

### Zone 2 — Phone / AirPods (Qi Wireless)
- Coil diameter: 50mm
- Output power: 5W–15W (auto-negotiated)
- Compatible: iPhone, AirPods Pro/3rd gen (Qi case), Android
- Alignment guide: subtle raised ring on surface

### Zone 3 — Apple Watch (Built-in Puck)
- Module: Apple Watch magnetic charging module (wired internally)
- Output: 5W (standard watch charge)
- Mount: Recessed cradle holds watch face-up
- Compatible: Apple Watch Series 1–9, Ultra

### Zone 4 — Laptop / Tablet (USB-C PD)
- Output: Up to 100W USB-C PD
- Cable: Built-in short USB-C cable (coiled/retractable preferred) OR flush USB-C port
- Compatible: MacBook Air/Pro, iPad Pro, any USB-C PD device
- E-marker cable required for 100W delivery

---

## Power Input
- **Input:** USB-C PD or barrel jack (140W–200W)
- **Recommended adapter:** 140W GaN USB-C PD (user supplied or bundled in Premium tier)
- **Overvoltage/overcurrent protection:** Required on input stage

---

## Internal Components Overview
- ESP32 microcontroller (brains)
- Per-zone INA219 or INA3221 current/voltage sensors
- USB-C PD trigger IC (CH224K or similar)
- Power distribution PCB (custom, JLCPCB manufactured)
- Thermal pads + passive cooling under coils
- Status LEDs per zone (GPIO-controlled)

---

## Safety Requirements
- Overheat shutoff (thermistor per coil zone)
- Overcurrent protection per zone
- Short circuit protection on USB-C output
- Foreign object detection (via power monitoring anomaly)
- UL/CE certification target for commercial production
