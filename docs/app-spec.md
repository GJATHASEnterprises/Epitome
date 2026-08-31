# Step — Future Features (Shelved for Batch 1)

This document tracks features that have been considered and deliberately deferred from Batch 1 to keep scope, cost, and complexity manageable.

---

## Shelved Features

### Companion App / BLE Integration
- Real-time power monitoring per zone via BLE
- Zone enable/disable from phone
- Charging history and usage stats
- Firmware OTA updates
- **Reason shelved:** Requires ESP32 or BLE-capable MCU, adds significant cost and firmware complexity. ATtiny85 is sufficient for Batch 1 LED logic and soft cap. Revisit for Batch 2+ if there is buyer demand.

### USB-A Ports
- 1–2 USB-A ports on rear for legacy devices
- **Reason shelved:** Adds BOM cost and rear spine complexity. USB-C PD ports cover the primary use case. BYOC with USB-C to USB-A adapter if needed.

### Laptop / Tablet Dock Slots
- Vertical or angled slot for laptop passthrough charging
- Tablet cradle
- **Reason shelved:** Dramatically increases size, cost, and manufacturing complexity. The 3-zone wireless + 2× USB-C design is the right product for the market.

### Touch or Button Controls
- Physical button to toggle zones or adjust LED brightness
- **Reason shelved:** Adds complexity with marginal benefit. ATtiny85 auto-detects device presence.

### Multiple Finish Options
- Aluminium base option
- Oak or maple instead of walnut
- **Reason shelved:** Batch 1 is walnut + ABS only. Single-finish production keeps tooling simple.

### Custom Engraving
- Laser engraving of customer name or logo on walnut surface
- **Reason shelved:** Requires per-unit laser job customisation. Consider for Batch 3+.

### Wireless Charging for Laptop
- Qi2 100W+ for laptop wireless
- **Reason shelved:** Not a real standard yet. No practical laptop coil at this form factor.

---

## Revisit Criteria

A shelved feature moves to active development when:
1. Batch 1 sells through (10 units) and break-even is achieved
2. Buyers explicitly request the feature in feedback
3. The feature does not increase unit cost above $75 build cost
4. The feature can be added without redesigning the core enclosure

---

## Current Batch 1 Scope

Batch 1 ships with:
- Zone 1: Qi2 20W phone
- Zone 2: Qi 5W buds
- Zone 3: Apple Watch puck + Qi watch coil (relay)
- USB-C Port A: 60W
- USB-C Port B: 30W
- ATtiny85 LED logic + 60W soft cap
- Walnut + ABS enclosure
- 65W brick included
