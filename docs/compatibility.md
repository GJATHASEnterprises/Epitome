# Epitome Penta — Compatibility Reference

---

## Laptop Compatibility (Zone 4 — USB-C PD 100W)

Zone 4 uses USB-C PD up to 100W through a **captured 220mm braided USB-C cable**. Any USB-C charging laptop is compatible.

| Device Category | Compatible? | Notes |
|---|---|---|
| MacBook Air/Pro USB-C models | ✅ | Up to 100W negotiated |
| Dell/HP/Lenovo/ASUS/Acer USB-C PD laptops | ✅ | Up to 100W negotiated |
| Surface USB-C charging models | ✅ | USB-C PD only |
| Gaming laptops requiring >100W | ⚠️ | Charges at up to 100W, may drain under full peak load |

### Laptops That Will NOT Work

| Device | Why |
|--------|-----|
| Non-USB-C legacy laptops | No USB-C PD charge path |
| Barrel-only charge designs | No USB-C input |

**Slot fit update:** 35mm slot width, device on thin edge (like a book on a shelf), cable from top — fits any laptop up to ~28mm thick including case.

---

## Phone Compatibility

### Zone 1 — 20W Qi Wireless
All Qi-compatible phones are supported.

### Zone 2 — 15W Qi Wireless
All Qi-compatible phones and earbuds are supported. 90×65mm pad includes a subtle 68×48mm inner ridge for buds alignment.

### Zone 5 — USB-C PD (wired, up to 20W)
Any USB-C phone is supported via captive cable.

### 3 Phones + 1 Laptop Simultaneously
Supported configuration:
- Zone 1: Phone (20W Qi)
- Zone 2: Phone/earbuds (15W Qi)
- Zone 4: Laptop (100W)
- Zone 5: Phone/tablet (20W)

---

## Apple Watch Compatibility (Zone 3)

Zone 3 supports both:
1. **Apple Watch magnetic puck charging**, and
2. **Qi watch charging** for compatible non-Apple watches.

| Watch Type | Compatible? | Method |
|---|---|---|
| Apple Watch Series/SE/Ultra | ✅ | Magnetic puck |
| Galaxy Watch (Qi models) | ✅ | Qi coil |
| Pixel Watch (Qi models) | ✅ | Qi coil |
| Garmin watches with Qi support | ✅ | Qi coil |
| Non-wireless-charge watches | ❌ | No wireless charging protocol |

Power policy: Zone 3 remains **5W total**, one watch active at a time.

---

## AirPods Compatibility (Zone 2 recommended — also Zone 1)

Any Qi-capable earbuds case is supported on Zones 1 or 2.

---

## iPad Compatibility (Zone 5 — USB-C PD 20W)

Zone 5 supports USB-C tablets through the captive 200mm braided cable.

- iPad Pro/Air/mini USB-C generations: ✅
- Galaxy Tab / Pixel Tablet / Surface Go USB-C models: ✅
- Lightning-only legacy tablets: ❌ (adapter-dependent)

Slot fit update: **20mm slot width**, device on thin edge (like a book on a shelf), cable from top — fits any tablet up to ~16mm thick including case.

---

## Power Limit Notes

- Zone 4 max: 100W
- Zone 5 max: 20W
- Zone 1: 20W
- Zone 2: 15W
- Zone 3: 5W shared
- System total: **155W** (156W PSU Mean Well LRS-150-24, 1W headroom, firmware cap 150W)
