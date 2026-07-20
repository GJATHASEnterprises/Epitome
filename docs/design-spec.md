# Quad Device Dock — Design Specification

---

## Product Name
Quad Device Dock

## Version
1.1 (render + LED update)

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
- **LED indicators:** Per-zone red/green LEDs mounted behind a frosted front diffuser strip
- **Branding:** Laser-etched or pad-printed "Quad Device Dock" mark on the base
- **Dark mode control:** Physical front button disables all LEDs regardless of charge state

---

## Product Visualization

See the rendered concept image in the repository root at `images/quad-dock-render.png`.

---

## Guide Rail Specification

### Zones 1 and 2 — Phone / AirPods Rails
- **Material:** Clear acrylic
- **Thickness:** 3mm
- **Height:** 8mm for phone placement support
- **Width:** 5mm
- **Shape:** Gently angled inward so the device self-centers on the Qi coil

### Zone 3 — Watch Rails
- **Material:** Clear acrylic
- **Thickness:** 3mm
- **Height:** 6mm to avoid interfering with the watch band while still guiding placement
- **Width:** 5mm
- **Shape:** Gently angled inward toward the magnetic cradle

### Zone 4 — Laptop Upright Rails
- **Material:** Clear acrylic
- **Thickness:** 4mm
- **Height:** 40–50mm
- **Support surface:** Soft rubber or silicone insert on the inner face of both rails
- **Laptop position:** Device rests between rails at a 70–80° angle from horizontal for stable upright charging

---

## Zone Layout

```
+----------------------------------------------------------------+
|                        QUAD DEVICE DOCK                        |
|                                                                |
|  [ ZONE 1 ]   [ ZONE 2 ]   [ ZONE 3 ]      [ ZONE 4 ]          |
|   Phone Qi     Phone/Buds   Watch Cradle    USB-C Laptop       |
|  /  rails  \  /  rails  \  /  rails  \    / upright rails \   |
|                                                                |
| [LED 1]      [LED 2]      [LED 3]          [LED 4] [Dark Btn]  |
+---------------------------[ USB-C IN ]-------------------------+
```

---

## Zone Specifications

### Zone 1 — Phone (Qi Wireless)
- Coil diameter: 50mm
- Output power: 5W–15W (auto-negotiated)
- Compatible: iPhone (MagSafe-adjacent), Android Qi devices
- Alignment guide: subtle raised ring on surface with clear 3mm acrylic side rails

### Zone 2 — Phone / AirPods (Qi Wireless)
- Coil diameter: 50mm
- Output power: 5W–15W (auto-negotiated)
- Compatible: iPhone, AirPods Pro/3rd gen (Qi case), Android
- Alignment guide: subtle raised ring on surface with clear 3mm acrylic side rails

### Zone 3 — Apple Watch (Built-in Puck)
- Module: Apple Watch magnetic charging module (wired internally)
- Output: 5W (standard watch charge)
- Mount: Recessed cradle holds watch face-up
- Compatible: Apple Watch Series 1–9, Ultra
- Alignment guide: 6mm tall clear acrylic rails on either side of the cradle

### Zone 4 — Laptop / Tablet (USB-C PD)
- Output: Up to 100W USB-C PD
- Cable: Built-in short USB-C cable (coiled/retractable preferred) OR flush USB-C port
- Compatible: MacBook Air/Pro, iPad Pro, any USB-C PD device
- E-marker cable required for 100W delivery
- Support: 40–50mm upright guide rails with soft inner pads to protect laptop edges

---

## LED Status System

### LED Behavior
- **Green solid:** Device fully charged
- **Red solid:** Device actively charging
- **Off:** No device detected
- **Dark mode button:** Press once to force every LED off, press again to restore normal status display

### LED Hardware
- RGB LEDs or paired red/green LEDs mounted underneath a frosted diffuser strip at the front edge of each zone
- LEDs driven directly from ESP32 GPIO pins through current-limiting resistors
- Dark mode button wired to a dedicated GPIO input with debounce handled in firmware

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
- Dual-color status LEDs per zone (GPIO-controlled)
- Dark mode pushbutton on front edge

---

## Safety Requirements
- Overheat shutoff (thermistor per coil zone)
- Overcurrent protection per zone
- Short circuit protection on USB-C output
- Foreign object detection (via power monitoring anomaly)
- UL/CE certification target for commercial production
