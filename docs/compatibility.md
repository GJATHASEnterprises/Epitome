# Step — Device Compatibility

---

## Zone 1 — Phone (Qi2 20W)

| Device | Compatible | Notes |
|---|---|---|
| iPhone 13 | ✓ | Qi2 20W |
| iPhone 14 / 14 Pro | ✓ | Qi2 20W |
| iPhone 15 / 15 Pro | ✓ | Qi2 20W |
| iPhone 16 / 16 Pro | ✓ | Qi2 20W |
| Any Qi2-certified phone | ✓ | 20W |
| Samsung Galaxy (any) | ✓ | 15W Qi |
| Google Pixel (any) | ✓ | 15W Qi |
| Any Qi-compatible phone | ✓ | Standard Qi (5–15W depending on phone) |

Zone 1 uses a Qi2 20W TX module with N52 magnetic alignment ring. Qi2 phones charge at up to 20W. Standard Qi phones charge at their maximum Qi rate.

---

## Zone 2 — Buds / Small Phone (Qi 5W)

| Device | Compatible | Notes |
|---|---|---|
| AirPods (2nd gen, Pro, 3rd gen, 4th gen) | ✓ | Requires Qi charging case |
| AirPods Max | ✗ | Not Qi compatible |
| Samsung Galaxy Buds | ✓ | Qi 5W |
| Google Pixel Buds | ✓ | Qi 5W |
| Any earbuds case with Qi | ✓ | 5W |
| Small Qi phone | ✓ | 5W max on this zone |

Zone 2 is a standard Qi 5W pad. Works with any device that supports Qi charging and physically fits the 65×50mm pad.

---

## Zone 3 — Watch

### Apple Watch (magnetic puck)

| Device | Compatible | Notes |
|---|---|---|
| Apple Watch Series 1–9 | ✓ | Via magnetic puck PCBA |
| Apple Watch Ultra / Ultra 2 | ✓ | Via magnetic puck PCBA |
| Apple Watch SE | ✓ | Via magnetic puck PCBA |

Step's Zone 3 includes Apple's magnetic charging puck PCBA. All Apple Watch models that use the standard magnetic charger are compatible.

### Other Watches (Qi universal coil)

| Device | Compatible | Notes |
|---|---|---|
| Garmin (Qi-compatible models) | ✓ | Via Qi coil |
| Samsung Galaxy Watch (Qi) | ✓ | Via Qi coil |
| Fitbit (Qi-compatible models) | ✓ | Via Qi coil |
| Any Qi-compatible watch | ✓ | Via Qi coil, 5W |

**Relay mutual exclusion:** Only one of the Apple Watch puck or Qi coil is active at a time. The ATtiny85 controls the relay. When an Apple Watch is detected, the puck activates. Otherwise the Qi coil is active. There is no conflict between the two.

---

## USB-C Ports (Rear)

| Device | Port A (60W) | Port B (30W) | Notes |
|---|---|---|---|
| MacBook Air M-series | ✓ | ✓ | 60W for Air, 30W for slower charge |
| MacBook Pro 14" | ✓ | — | Needs 60W+ for full speed |
| iPad Pro (USB-C) | ✓ | ✓ | Either port works |
| Any USB-C laptop | ✓ | Depends | 60W for most laptops |
| Any USB-C phone | ✓ | ✓ | Both ports more than sufficient |
| Any USB-C device | ✓ | ✓ | Universal USB-C PD |

**BYOC — Bring Your Own Cables:** Step does not include USB-C cables for the rear ports. The user provides their own USB-C cables. Cable standard: USB-C to USB-C, any length, rated for PD charging.

---

## Power Note

For simultaneous high-power use of both USB-C ports (60W + 30W), the included 65W brick is not sufficient. Replace the included brick with a 100W+ USB-C charger. The ATtiny85 soft cap will limit total draw to 60W with the included brick, which means heavy USB-C use may throttle wireless zones.
