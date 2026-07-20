# Quad Device Dock

![Quad Device Dock Render](images/quad-dock-render.png)

**A smart, app-controlled 4-zone charging dock for Apple devices and laptops.**

---

## Overview

The Quad Device Dock is a self-built, smart charging station designed to charge up to 4 devices simultaneously from a single wall connection. It features wireless Qi charging zones, a built-in Apple Watch puck, a high-power USB-C laptop output, a USB-A side port for accessories, a continuous WS2812B LED status bar, and a companion mobile app for full customization.

The dock plugs directly into a standard wall outlet via a built-in IEC C13 inlet and an internal 180W AC/DC power supply — no external power brick required.

Available in **Black** and **White** colorways.

---

## Zones

| Zone | Device | Method |
|------|--------|--------|
| Zone 1 | Phone | Qi Wireless (15W), MagSafe-style alignment magnets |
| Zone 2 | Phone / AirPods | Qi Wireless (15W) |
| Zone 3 | Apple Watch | Built-in Watch Puck (wired internally) |
| Zone 4 | MacBook / Laptop | USB-C PD (up to 100W) |
| Side port | Accessories / older devices | USB-A 12W (5V/2.4A) |

---

## Key Features
- Plugs directly into the wall — internal 180W AC/DC PSU, IEC C13 inlet (standard PC/kettle cable)
- Continuous WS2812B addressable LED bar across the full front edge — color per zone
- Ambient light sensor (TEMT6000) auto-dims LEDs in dark rooms, brightens in light
- Smart per-zone power monitoring
- ESP32-powered intelligence (WiFi + Bluetooth)
- Companion iOS/Android app (Flutter)
- Auto device detection — app displays device type icon per zone
- Theft alert — push notification if device is removed unexpectedly
- OTA firmware updates via app
- Weekly charge report in app
- Voice assistant shortcuts (Siri / Google Assistant)
- Battery health scheduling (stop at 80%)
- Priority charging mode
- Real-time charge % display per device
- Overcharge and overheat protection

---

## Physical Features
- **Tiered/stepped enclosure** — front tier is 15mm tall, rear tier rises to 40mm for an architectural, premium look
- **Aluminum top plate** — passively cools Qi coils; sourced cut-to-size from SendCutSend
- **ABS base** — raw matte finish, no paint or coating needed
- **Integrated molded ABS rails** — part of the base; small rails on Zones 1–3, tall 40–50mm rails on Zone 4 for laptop support
- **Silicone pads** on all charging zones to prevent scratching and improve device grip
- **Cooling vents** slotted into the base for passive airflow
- **Removable aluminum top plate** — unscrews with M3 fasteners for DIY repair access
- **Cable clips** integrated on the rear to route the laptop USB-C cable neatly
- **IEC C13 power inlet** on rear — uses any standard PC power cable
- **USB-A port** on the right side for 12W accessory charging
- **M3 screws** standardized throughout for easy assembly and repair
- Available in **Black** and **White** colorways

---

## LED Status System

| LED State | Meaning |
|-----------|---------|
| Red segment | Device actively charging on that zone |
| Green segment | Device fully charged on that zone |
| Off segment | No device detected on that zone |
| Full bar pulses green | All four zones simultaneously at 100% |
| LEDs off | Dark mode active (set via app or ambient sensor) |

---

## Target Pricing

| Version | Price |
|---------|-------|
| Standard (Black or White) | $249–$279 |
| Premium (bundled accessories) | $299–$349 |

---

## Documentation

- [Design Spec](docs/design-spec.md)
- [Bill of Materials](docs/bom.md)
- [Wiring & Schematic Notes](docs/wiring.md)
- [App Feature Spec](docs/app-spec.md)
- [Layout Diagram](docs/layout-diagram.md)

---

## Target Build Cost
- **Per unit (self-built, 20–50 qty):** ~$74–$104
- **Per unit (self-built, 50+ qty):** ~$62–$90

---

*Built by GJATHASEnterprises*
