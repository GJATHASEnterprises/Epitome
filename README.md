# Quad Device Dock

![Quad Device Dock Render](images/quad-dock-render.png)

**A smart, app-controlled 4-zone charging dock for Apple devices and laptops.**

---

## Overview

The Quad Device Dock is a self-built, smart charging station designed to charge up to 4 devices simultaneously from a single wall connection. It features wireless Qi charging zones, a built-in Apple Watch puck, a high-power USB-C laptop output, upright support rails, and a companion mobile app for full customization.

---

## Zones

| Zone | Device | Method |
|------|--------|--------|
| Zone 1 | Phone | Qi Wireless (up to 15W) |
| Zone 2 | Phone / AirPods | Qi Wireless (up to 15W) |
| Zone 3 | Apple Watch | Built-in Watch Puck (wired internally) |
| Zone 4 | MacBook / Laptop | USB-C PD (up to 100W) |

---

## Key Features
- Single wall cable input
- Smart per-zone power monitoring
- ESP32-powered intelligence (WiFi + Bluetooth)
- Companion iOS/Android app (Flutter)
- Battery health scheduling (stop at 80%)
- Priority charging mode
- Real-time charge % display per device
- Overcharge and overheat protection
- Front dark mode button to disable all zone LEDs instantly

---

## Physical Features
- Clear acrylic guide rails on Zones 1 and 2 to guide phones or AirPods onto the Qi coils
- Compact clear acrylic rails around the watch cradle in Zone 3 to keep the watch centered
- Tall clear acrylic laptop rails in Zone 4 with soft inner rubber inserts to hold a USB-C laptop upright at a 70–80° angle
- Frosted diffuser strip along the front edge with one red/green LED status indicator per zone
- Matte dark enclosure with top-side product branding and a single rear power input

---

## LED Status System

| LED State | Meaning |
|-----------|---------|
| Red solid | Device actively charging |
| Green solid | Device fully charged |
| Off | No device detected |
| Dark mode enabled | All LEDs forced off regardless of charging state |

---

## Target Pricing

| Version | Price |
|---------|-------|
| Starter (no app) | $149–$179 |
| Standard (full smart + app) | $199–$249 |
| Premium (bundled power brick) | $279–$329 |

---

## Documentation

- [Design Spec](docs/design-spec.md)
- [Bill of Materials](docs/bom.md)
- [Wiring & Schematic Notes](docs/wiring.md)
- [App Feature Spec](docs/app-spec.md)
- [Layout Diagram](docs/layout-diagram.md)

---

## Target Build Cost
- **Per unit (self-built, 20–50 qty):** ~$95–$110
- **Per unit (self-built, 50+ qty):** ~$80–$95

---

*Built by GJATHASEnterprises*
