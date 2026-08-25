# Penta Dock — UVP and Product Positioning

## Slogan
**"One dock. Every device."**

*190W total output — laptop, tablet, phone, watch, buds, all at full speed.*

## The Claim
The only compact desktop dock that charges your laptop, tablet, phone, watch, and earbuds simultaneously — wirelessly where possible, at full speed, from a single wall socket.

## 190W Total Output
| Zone | Device | Power | Method |
|---|---|---|---|
| Zone 1 | Phone | 20W | Qi2 (magnetic alignment) |
| Zone 2 | Buds or second phone | 20W | Qi (120×80mm dish) |
| Zone 3 | Apple Watch | 5W | Apple Watch puck + universal Qi coil |
| Zone 4 | Laptop | 100W | USB-C PD captive braided cable |
| Zone 5 | Tablet | 45W | USB-C PD captive braided cable |
| **Total** | | **190W worst case** | |
| **PSU** | | **201W rated — 11W headroom** | |
| **ATtiny85 soft cap** | | **185W** | |

## What Makes It Different

### 1. Vertical laptop charging — built in
No other multi-device dock stands your laptop on its spine with a built-in captive 100W USB-C cable. Laptop charges vertically, minimal desk footprint, cable never gets lost.

### 2. 45W tablet charging
iPad Pro from dead to full in 90 minutes. Most docks offer 20W tablet charging. Penta Dock delivers 45W — more than double.

### 3. 100W laptop + full wireless simultaneously
100W USB-C and full Qi simultaneously from one IEC cable into one wall socket. No power strip needed.

### 4. Charges two phones at once
Zone 1 (20W Qi2) and Zone 2 (20W Qi, 120×80mm dish) both fit full-size phones. Two people, one dock.

### 5. Staircase platform — everything visible
Three rising steps face the user. Phone on Step 1. Buds or second phone on Step 2. Watch on Step 3 at reading angle. Every device visible and reachable.

### 6. One cable in. Everything out.
One IEC C13 to the wall. Five zones charge. No power strip. No cable management. No five separate chargers.

## Physical Premium Details

### Wattage etched on step faces
```
PHONE    20W  Qi2
BUDS     20W  Qi
WATCH     5W
LAPTOP  100W  USB-C
TABLET   45W  USB-C
```

### Braided captive cables
- Zone 4: 220mm braided nylon, 100W rated, angled dock-end connector
- Zone 5: 200mm braided nylon, 65W rated, angled dock-end connector
- Colour: matte black matching dock finish

### Magnetic phone alignment — Zone 1
Qi2 magnetic ring on Step 1 silicone. Phone snaps to charging position instantly.

### Watch at viewing angle — Zone 3
Cradle pod on Step 3 tilts Apple Watch toward user. Face visible while charging.

### Textured silicone surfaces
Dot-pattern silicone on all charging surfaces.

### Physical power button
Rear rail, next to IEC C13. Cuts all zones. Tactile click. Matte black.

### LED status strip
Frosted acrylic diffuser, front fascia. ESP32-C3-controlled.

Per-zone colours:
- Zone 1 Phone: blue
- Zone 2 Buds or second phone: purple
- Zone 3 Watch: green
- Zone 4 Laptop: orange
- Zone 5 Tablet: blue

Behaviour:
- Charging active: full brightness
- Fully charged: slow pulse every 3 seconds
- No device: off

### Laser-etched product name
"PENTA DOCK" on rear panel above IEC C13 inlet.

### Rubber feet
3M Bumpons SJ5023 ×4.

## Colour Variants
| Variant | Finish | Availability |
|---|---|---|
| Penta Dock Obsidian | Matte black ABS, dark silicone | Batch 1 |
| Penta Dock Arctic | Matte white ABS, light grey silicone | Batch 2 |

## Packaging
- Magnetic closure matte black rigid box
- Foam insert cut to dock shape
- Cables in separate foam cutouts
- Setup card: matte black card stock, zone reference, QR to epitomecharge.com
- Belly band: "Penta Dock — One dock. Every device."

## Pricing
- **$249 USD**
- Free shipping (US)
- Pre-order — ships [date TBD]
- Obsidian only at launch

## Website
epitomecharge.com

## Future Features (shelved — Batch 2 consideration)
Companion app with BLE zone monitoring, theft alert, night mode scheduling, and zone dashboard. Full spec preserved in docs/app-spec.md.
