# Quad Device Dock — Bill of Materials (BOM)

**Target per-unit cost:** ~$95–$110 (self-built, 20–50 unit quantities)

---

## Parts List

| # | Part | Spec | Qty | Unit Cost | Total Est. | Source |
|---|------|------|-----|-----------|------------|--------|
| 1 | Qi Wireless TX Module | 5–15W, 50mm coil | 2 | $7–$10 | $14–$20 | LCSC / Vetted Alibaba |
| 2 | Apple Watch Charging Module | Magnetic puck, 5W | 1 | $8–$15 | $8–$15 | LCSC / DigiKey |
| 3 | USB-C PD Trigger IC | CH224K or IP2716 | 1 | $1–$2 | $1–$2 | LCSC |
| 4 | USB-C PD Routing Board | 100W capable | 1 | $8–$14 | $8–$14 | LCSC / DigiKey |
| 5 | ESP32 Module | ESP32-WROOM-32 | 1 | $3–$6 | $3–$6 | LCSC / DigiKey |
| 6 | Power Monitoring IC | INA3221 (3-ch) or 2x INA219 | 1–2 | $3–$6 | $3–$8 | LCSC / Mouser |
| 7 | Custom PCB | All zones unified, JLCPCB | 1 | $8–$14 | $8–$14 | JLCPCB |
| 8 | E-marker USB-C Cable | 100W, 1m | 1 | $4–$8 | $4–$8 | LCSC / Vetted Alibaba |
| 9 | Status LEDs | RGB or single color, SMD | 4 | $0.10–$0.20 | $0.40–$0.80 | LCSC |
| 10 | Thermistors | NTC 10K | 3 | $0.20–$0.40 | $0.60–$1.20 | LCSC |
| 11 | Overcurrent Protection ICs | Per zone fuse/IC | 4 | $0.50–$1 | $2–$4 | LCSC / Mouser |
| 12 | Thermal Pads | Under coils | 1 pack | $2–$4 | $2–$4 | LCSC / Mouser |
| 13 | Wiring / Connectors | JST, Dupont, misc | 1 lot | $4–$8 | $4–$8 | LCSC / Mouser |
| 14 | Enclosure | Self-manufactured ABS/acrylic | 1 | $10–$18 | $10–$18 | Self-built |
| 15 | Fasteners / Misc Hardware | Screws, standoffs, feet | 1 lot | $2–$4 | $2–$4 | Local / LCSC |
| 16 | Capacitors / Resistors / Passives | Assorted SMD | 1 lot | $2–$4 | $2–$4 | LCSC |

---

## Cost Summary

| Quantity Built | Est. Per Unit Cost |
|----------------|--------------------|
| 5 units | $115–$145 |
| 20 units | $95–$115 |
| 50 units | $80–$100 |
| 100+ units | $65–$85 |

---

## Approved Suppliers

| Supplier | Use For | Notes |
|----------|---------|-------|
| LCSC (lcsc.com) | ICs, passives, modules, connectors | Best price/quality for components |
| DigiKey (digikey.com) | Safety-critical ICs, ESP32, sensors | Authorized, reliable, slightly higher cost |
| Mouser (mouser.com) | ICs, power components | Authorized distributor |
| JLCPCB (jlcpcb.com) | Custom PCB manufacturing + assembly | Low cost, good quality for prototypes |
| Arrow / Newark | Backup authorized source | Use if LCSC/DigiKey are out of stock |
| Vetted Alibaba suppliers | Enclosure parts, coil modules, cables | Only suppliers with 2+ year trade history and reviews |

---

## What NOT to buy from
- Amazon (high counterfeit risk for power/PD parts)
- eBay (unverifiable sourcing)
- Unknown AliExpress stores with no trade history

---

## Notes
- Power brick (140W GaN) is **not included** in Standard BOM (user supplied)
- Power brick adds ~$60–$120 per unit for Premium tier
- Order 25% extra passives/connectors as spares for first prototype batch
