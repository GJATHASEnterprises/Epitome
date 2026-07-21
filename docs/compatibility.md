# Quad-Dock — Compatibility Reference

---

## Laptop Compatibility (Zone 4 — USB-C PD 100W)

Zone 4 uses standard USB-C Power Delivery (PD). It automatically negotiates voltage and wattage with any PD-capable device.

| Brand / Model | USB-C PD? | Max Charge Speed | Notes |
|---------------|-----------|-----------------|-------|
| MacBook Air (M1, M2, M3) | ✅ | 30–67W | Well within 100W limit |
| MacBook Pro 14" (M-series) | ✅ | 67–96W | Well within 100W limit |
| MacBook Pro 16" (M-series) | ✅ | 100W | Charges at 100W; slightly slower under peak CPU+GPU load (needs 140W for max speed — normal for any 100W charger) |
| MacBook (USB-C, 2015–2019) | ✅ | 29–61W | Fully compatible |
| Dell XPS 13 / 15 / 17 | ✅ | 45–130W | Quad-Dock caps at 100W; XPS 15/17 may charge slightly slower under load |
| HP Spectre / Envy | ✅ | 45–100W | Fully compatible |
| HP Elite Dragonfly | ✅ | 65W | Fully compatible |
| Lenovo ThinkPad (USB-C models, 2018+) | ✅ | 45–100W | Fully compatible |
| Lenovo IdeaPad (USB-C models) | ✅ | 45–65W | Fully compatible |
| ASUS ZenBook / VivoBook (USB-C models) | ✅ | 45–100W | Fully compatible |
| Acer Swift / Aspire (USB-C models) | ✅ | 45–65W | Fully compatible |
| Microsoft Surface Pro 9 / 10 | ✅ | 60–65W (USB-C) | Fully compatible |
| Microsoft Surface Laptop 5+ | ✅ | 65W | Fully compatible |
| Samsung Galaxy Book series | ✅ | 65W | Fully compatible |
| LG Gram series | ✅ | 65W | Fully compatible |
| Razer Blade (USB-C charging models) | ✅ | 100W | At limit — charges but slowly under gaming load |
| Google Pixelbook / Go | ✅ | 45–65W | Fully compatible |

### Laptops That Will NOT Work

| Device | Why |
|--------|-----|
| Older MacBook Pro (pre-2016 MagSafe only) | No USB-C port |
| MacBook Air (2017 and earlier, MagSafe) | No USB-C port |
| Dell, HP, Lenovo laptops with barrel connector only (pre-2018) | No USB-C PD |
| Surface Pro 1–7 (Surface Connect only) | No USB-C charging |

**Summary:** Any laptop with USB-C PD charging from approximately 2018 onward works with Quad-Dock.

---

## Phone Compatibility

### Zone 1 — 15W Qi Wireless
| Device | Compatible? | Notes |
|--------|-------------|-------|
| iPhone 8 and later (all models) | ✅ | Qi standard |
| iPhone 12–15 (MagSafe aligned via N52 magnets) | ✅ | Snaps into position |
| Samsung Galaxy S series (S6 and later) | ✅ | Qi standard |
| Google Pixel (Pixel 3 and later) | ✅ | Qi standard |
| OnePlus / Xiaomi / OPPO (Qi models) | ✅ | Qi standard |
| Any phone with Qi wireless charging | ✅ | Universal |

### Zone 2 — 15W Qi Wireless
Same compatibility as Zone 1 — works for a second phone simultaneously.

### Zone 4 — USB-C PD (wired, up to 27W for phones)
| Device | Compatible? |
|--------|-------------|
| Any phone with USB-C (iPhone 15+, Android USB-C) | ✅ |
| iPhone with Lightning connector (via adapter) | ⚠️ Adapter required |

### 3 Phones Simultaneously
Quad-Dock can charge **3 phones at the same time**:
- Zone 1: Phone 1 (15W Qi)
- Zone 2: Phone 2 (15W Qi)
- Zone 4: Phone 3 (up to 27W USB-C)

Total draw: ~60W — well within the 180W PSU budget.

---

## Apple Watch Compatibility (Zone 3)

| Model | Compatible? |
|-------|-------------|
| Apple Watch Series 1 | ✅ |
| Apple Watch Series 2 | ✅ |
| Apple Watch Series 3 | ✅ |
| Apple Watch Series 4 | ✅ |
| Apple Watch Series 5 | ✅ |
| Apple Watch Series 6 | ✅ |
| Apple Watch SE (1st gen) | ✅ |
| Apple Watch Series 7 | ✅ |
| Apple Watch Series 8 | ✅ |
| Apple Watch SE (2nd gen) | ✅ |
| Apple Watch Series 9 | ✅ |
| Apple Watch Ultra | ✅ |
| Apple Watch Ultra 2 | ✅ |

All Apple Watch models that use the standard magnetic charging puck are compatible.

---

## AirPods Compatibility (Zone 2 recommended — also Zone 1)

| Model | Compatible? | Notes |
|-------|-------------|-------|
| AirPods Pro (1st gen) | ✅ | Qi case |
| AirPods Pro (2nd gen) | ✅ | Qi + MagSafe case |
| AirPods (3rd gen) | ✅ | Qi case |
| AirPods 4 (with wireless charging case) | ✅ | Qi case |
| AirPods (1st/2nd gen) | ❌ | Lightning case only — no Qi |
| AirPods Max | ❌ | Lightning / USB-C only — no Qi |

---

## iPad Compatibility (Zone 4 — USB-C PD)

| Model | Compatible? | Notes |
|-------|-------------|-------|
| iPad Pro 11" (2018+) | ✅ | USB-C PD |
| iPad Pro 12.9" (2018+) | ✅ | USB-C PD |
| iPad Air (4th gen+) | ✅ | USB-C PD |
| iPad mini (6th gen+) | ✅ | USB-C PD |
| iPad (10th gen) | ✅ | USB-C PD |
| iPad (9th gen and earlier) | ❌ | Lightning only — no USB-C |
| iPad Air (3rd gen and earlier) | ❌ | Lightning only |
| iPad mini (5th gen and earlier) | ❌ | Lightning only |

---

## 100W Limit Notes

Quad-Dock Zone 4 outputs a maximum of 100W. USB-C PD negotiates automatically:

- Devices that need less than 100W → get exactly what they need, no issue
- Devices rated for more than 100W (e.g. some gaming laptops at 130–200W) → will charge, but slower under heavy load. The laptop draws from its battery for the difference. **This is normal behaviour for any 100W charger.**
- MacBook Pro 16" note specifically: charges at 100W; slightly slower under sustained peak CPU + GPU workloads. Fine for overnight or desk use.
