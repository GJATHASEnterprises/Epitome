# Quad Device Dock — Bill of Materials (BOM)

**Target per-unit cost:** ~$74–$104 (self-built, 20–50 unit quantities)

All components sourced from **LCSC** where possible. PCB assembled via **JLCPCB PCBA service** — JLCPCB sources and machine-solders all components, reducing hand-assembly cost and improving consistency.

---

## Parts List

| # | Part | Spec | Qty | Unit Cost | Total Est. | Source |
|---|------|------|-----|-----------|------------|--------|
| 1 | Qi Wireless TX Module | 15W capable, 50mm coil | 2 | $7–$10 | $14–$20 | LCSC |
| 2 | Apple Watch Charging Module | Magnetic puck, 5W | 1 | $8–$15 | $8–$15 | LCSC / DigiKey |
| 3 | USB-C PD Routing Board | 100W capable | 1 | $8–$14 | $8–$14 | LCSC / DigiKey |
| 4 | ESP32 Module | ESP32-WROOM-32, 4MB flash | 1 | $3–$6 | $3–$6 | LCSC |
| 5 | INA3221 Power Monitor | 3-channel I2C, Zones 1–3 | 1 | $2–$4 | $2–$4 | LCSC |
| 6 | INA219 Power Monitor | 1-channel I2C, Zone 4 | 1 | $1–$2 | $1–$2 | LCSC |
| 7 | WS2812B LED Strip | 16 LEDs cut from 60 LED/m reel | 1 | $2–$4 | $2–$4 | LCSC |
| 8 | TEMT6000 Ambient Light Sensor | Analog output, SOT-23 | 1 | $0.50–$1 | $0.50–$1 | LCSC |
| 9 | 3.3V LDO Regulator | Shared for ESP32 + sensors | 1 | $0.50–$1 | $0.50–$1 | LCSC (JLCPCB basic) |
| 10 | USB-A Charging IC | SY6280 or equiv., 5V/2.4A (12W) | 1 | $0.50–$1 | $0.50–$1 | LCSC |
| 11 | USB-A Connector | Type-A, through-hole or SMD | 1 | $0.30–$0.60 | $0.30–$0.60 | LCSC |
| 12 | N52 Neodymium Ring Magnet | Ring, fits 50mm Qi coil, Zone 1 | 1 | $1–$2 | $1–$2 | LCSC / Vetted Alibaba |
| 13 | Internal AC/DC PSU Module | 180W, 100–240V AC in, 20V DC out | 1 | $18–$28 | $18–$28 | LCSC / Mouser (e.g., Mean Well RS-150-20 equiv.) |
| 14 | IEC C13 Power Inlet | Panel mount, with fuse holder | 1 | $2–$4 | $2–$4 | LCSC |
| 15 | E-marker USB-C Cable | 100W, 1m | 1 | $4–$8 | $4–$8 | LCSC / Vetted Alibaba |
| 16 | Thermistors | NTC 10K, per coil zone | 3 | $0.20–$0.40 | $0.60–$1.20 | LCSC (JLCPCB basic) |
| 17 | Overcurrent Protection ICs | Per zone polyfuse/IC | 4 | $0.50–$1 | $2–$4 | LCSC |
| 18 | Silicone Pads | Thin pad per zone (custom cut or sheet) | 1 pack | $2–$4 | $2–$4 | LCSC / Local |
| 19 | Wiring / Connectors | JST, Dupont, misc | 1 lot | $3–$6 | $3–$6 | LCSC |
| 20 | Aluminum Top Plate | 1.5mm sheet, cut to spec | 1 | $6–$10 | $6–$10 | SendCutSend |
| 21 | ABS Base (Molded) | Tiered/stepped, with integrated rails | 1 | $8–$14 | $8–$14 | Self-built / Injection molder |
| 22 | Custom PCB | 2-layer, panelized, JLCPCB PCBA | 1 | $8–$14 | $8–$14 | JLCPCB |
| 23 | M3 Fasteners | Screws + standoffs, bulk pack | 1 lot | $1–$2 | $1–$2 | LCSC / Local |
| 24 | Capacitors / Resistors / Passives | Assorted SMD (JLCPCB basic library) | 1 lot | $1–$3 | $1–$3 | JLCPCB basic |
| 25 | Kraft Box + Foam Insert | Packaging, first 50 units | 1 | $3–$6 | $3–$6 | Local / Alibaba |

---

## Cost Summary

| Quantity Built | Est. Per Unit Cost |
|----------------|--------------------|
| 20–50 units | $74–$104 |
| 50+ units | $62–$90 |

---

## Approved Suppliers

| Supplier | Use For | Notes |
|----------|---------|-------|
| LCSC (lcsc.com) | ICs, passives, modules, connectors, sensors | Primary source for all components |
| JLCPCB (jlcpcb.com) | Custom PCB manufacturing + PCBA assembly | Machine soldering = better quality than hand-assembly |
| SendCutSend | Aluminum top plate (sheet metal laser cut) | Cheaper than CNC for flat plates |
| DigiKey (digikey.com) | Safety-critical ICs, Apple Watch module | Authorized, slightly higher cost |
| Mouser (mouser.com) | Internal PSU module, power components | Authorized distributor |
| Arrow / Newark | Backup authorized source | Use if LCSC/DigiKey are out of stock |
| Vetted Alibaba suppliers | Qi coil modules, cables, ring magnets | Only suppliers with 2+ year trade history and reviews |

---

## What NOT to buy from
- Amazon (high counterfeit risk for power/PD parts)
- eBay (unverifiable sourcing)
- Unknown AliExpress stores with no trade history

---

## Notes
- **No external power brick** — the dock has an internal 180W AC/DC PSU and plugs directly into the wall via an IEC C13 power cable (user supplied — any standard PC power cable works)
- Order 25% extra passives/connectors as spares for the first prototype batch
- All passives (resistors, caps, LDO) should be placed in JLCPCB basic parts library to avoid surcharges
- Qi TX modules must be rated for 15W to support fast charge on Zones 1 and 2
