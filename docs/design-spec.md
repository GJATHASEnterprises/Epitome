# Quad Device Dock — Design Specification

---

## Product Name
Quad Device Dock

## Version
2.0 (tiered enclosure, internal PSU, WS2812B LED bar, USB-A port, MagSafe magnets)

## Color Variants
- **Black** — matte black raw ABS base, black anodized aluminum top plate
- **White** — matte white raw ABS base, natural brushed aluminum top plate

---

## Physical Dimensions (Target)

| Dimension | Target |
|-----------|--------|
| Length | 280–320mm |
| Width | 120–140mm |
| Height (front tier) | 15mm |
| Height (rear tier) | 40mm |
| Weight | ~400–600g (assembled) |

---

## Enclosure Design

The dock uses a **tiered/stepped two-piece enclosure**: a front tier at 15mm height and a rear tier that rises to 40mm. The Watch zone (Zone 3) sits elevated on the back tier. The Laptop zone (Zone 4) is at the far right with a tall rear wall for upright laptop support.

- **Top plate:** 1.5mm brushed aluminum (Black anodized or natural finish depending on color variant) — sourced cut-to-size from **SendCutSend**. The aluminum top plate sits directly against the Qi coil housings and acts as a passive heat spreader, conducting heat away from the coils without the need for additional thermal pads. The plate is fastened with M3 screws and is fully **removable** for DIY repair access.
- **Base:** Molded ABS in a **2-piece enclosure** (top plate + base). Raw matte finish — no paint or coating needed. Available in black or white.
- **Rails:** Integrated molded-in ABS rails (same piece as the base — no separate acrylic parts):
  - Zones 1–3: small low-profile rails to guide devices onto charging zones
  - Zone 4: tall rails (40–50mm) with integrated silicone inner pads for laptop support
- **Silicone pads:** Thin silicone pad on each charging zone surface to prevent device scratching and improve grip
- **Cooling vents:** Slotted openings in the base for passive airflow under the Qi coils
- **Cable management:** Integrated cable clips on the rear edge to route the laptop USB-C cable neatly
- **Power inlet:** IEC C13 inlet (standard PC/kettle cable) on the rear left
- **USB-A port:** On the right side panel for 12W accessory charging
- **Fasteners:** M3 screws standardized throughout
- **Branding:** Laser-etched or pad-printed "Quad Device Dock" mark on the base

---

## Product Visualization

See the rendered concept image in the repository root at `images/quad-dock-render.png`.

---

## Zone Layout

```
+------------------------------------------------------------------+  ← Rear tier (40mm high)
|   [Watch - elevated Zone 3]            [Laptop Zone 4]           |
|   /+--------+\                         /+--------------+\        |
|   || ZONE 3 ||                         ||   ZONE 4     ||        |
|   || Watch  ||                         || USB-C Laptop ||        |
|   \+--------+/                         \+--------------+/        |
+------------------------------------------------------------------+  ← Front-rear step
|  /+----------+\  /+----------+\                                  |  ← Front tier (15mm high)
|  || ZONE 1   ||  || ZONE 2   ||                                  |
|  || Phone Qi ||  || Phone /  ||                                  |
|  ||  (coil)  ||  || AirPods  ||                                  |
|  \+----------+/  \+----------+/                                  |
|                                                                  |
| [====== WS2812B LED BAR — full front edge =====================] |
+==================[ IEC C13 IN (rear) ] [ USB-A side ]===========+
```

---

## Zone Specifications

### Zone 1 — Phone (Qi Wireless)
- Coil diameter: 50mm
- Output power: 15W (fast charge capable)
- Compatible: iPhone, Android Qi devices
- **MagSafe-style alignment:** N52 neodymium ring magnet under the Qi coil for phone snap-alignment
- Alignment guide: small integrated ABS rails on both sides; silicone surface pad

### Zone 2 — Phone / AirPods (Qi Wireless)
- Coil diameter: 50mm
- Output power: 15W (fast charge capable)
- Compatible: iPhone, AirPods Pro/3rd gen (Qi case), Android
- Alignment guide: small integrated ABS rails; silicone surface pad

### Zone 3 — Apple Watch (Built-in Puck)
- Module: Apple Watch magnetic charging module (wired internally)
- Output: 5W (standard watch charge)
- Mount: Recessed cradle on elevated rear tier, watch face-up
- Compatible: Apple Watch Series 1–9, Ultra
- Alignment guide: small integrated ABS rails on either side of the cradle; silicone pad

### Zone 4 — Laptop / Tablet (USB-C PD)
- Output: Up to 100W USB-C PD
- Cable: Built-in short USB-C cable (coiled/retractable preferred) OR flush USB-C port
- Compatible: MacBook Air/Pro, iPad Pro, any USB-C PD device
- E-marker cable required for 100W delivery
- Support: Tall integrated ABS rear rails (40–50mm) with integrated silicone inner pads to protect laptop edges
- Laptop leans at 75° from horizontal

### Side Port — USB-A (12W)
- Output: 5V/2.4A (12W)
- Charging IC: SY6280 or equivalent (LCSC sourced)
- Compatible: Any USB-A device (cables, older phones, accessories)

---

## LED Status System

### LED Hardware
- **WS2812B addressable RGB LED strip** running the full width of the front edge
- 16 LEDs total (4 per zone)
- Driven by a single data wire from ESP32 GPIO 12 (FastLED library)
- **TEMT6000 analog ambient light sensor** on GPIO 36 (ADC) — auto-dims LEDs in dark rooms, auto-brightens in light

### LED Behavior
- **Red segment:** Device actively charging on that zone
- **Green segment:** Device fully charged on that zone
- **Off segment:** No device detected on that zone
- **Full bar pulses green:** All four zones simultaneously at 100% — breathing animation
- **Dark mode (app override):** User can force all LEDs off from the app regardless of sensor reading

---

## Power System

- **Input:** Standard wall outlet via IEC C13 inlet (rear of dock)
- **Internal PSU:** 180W AC/DC switching power supply module built inside the dock — no external power brick required
- **Main DC rail:** 20V
- **Input cable:** Standard IEC C13 to IEC C14 PC power cable (user supplied or bundled)
- **Overvoltage/overcurrent protection:** Required on the 20V output of the internal PSU and on each zone output

---

## Internal Components Overview

- ESP32-WROOM-32 microcontroller (WiFi + BT)
- Internal 180W AC/DC PSU module (e.g., Mean Well RS-150-20 or equivalent)
- IEC C13 power inlet with fuse
- INA3221 (3-channel) power monitor for Zones 1–3 (LCSC sourced)
- INA219 (1-channel) power monitor for Zone 4 (LCSC sourced)
- WS2812B LED strip (16 LEDs, front edge)
- TEMT6000 ambient light sensor (ADC, auto-brightness)
- USB-A charging IC (SY6280, 5V/2.4A, LCSC sourced)
- N52 neodymium ring magnet under Zone 1 Qi coil (MagSafe alignment)
- USB-C PD routing board (100W capable, LCSC sourced)
- Thermistors (NTC 10K) per coil zone
- Overcurrent protection per zone output
- Single shared 3.3V LDO for ESP32 and all logic/sensors
- Custom 2-layer PCB (JLCPCB PCBA service, panelized)

---

## PCB & Manufacturing

- **PCB:** 2-layer (sufficient for this design); panelized for cost efficiency
- **Assembly:** JLCPCB PCBA service — components sourced and machine-soldered by JLCPCB
- **Passives:** All resistors, capacitors, and small passives from JLCPCB basic parts library
- **Components:** Sourced from LCSC wherever possible

---

## Packaging (First 50 Units)

- **Box:** Kraft cardboard box with custom foam insert
- **Manual:** Digital only — QR code inside box links to GitHub documentation. No printed booklet.

---

## Safety Requirements
- Overheat shutoff (thermistor per coil zone)
- Overcurrent protection per zone
- Short circuit protection on USB-C output
- Foreign object detection (via power monitoring anomaly)
- Fuse on IEC C13 input line
- UL/CE certification target for commercial production
