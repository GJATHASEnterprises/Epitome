# Epitome Penta — Parts, Tools & Direct Buy Links

Everything needed to build the updated prototype revision.

---

## SECTION 1 — TOOLS

Keep existing core tool set: soldering iron, solder, flux, multimeter, wire tools, helping hands, safety glasses.

---

## SECTION 2 — ELECTRONICS PARTS (Direct Buy Links)

### ✅ Safe to order from LCSC — core electronics

Keep current LCSC core parts list for ESP32/INA3221/passives/PSU.

### ✅ Add/replace key revision parts

| Part | What changed | Source guidance |
|---|---|---|
| Captive USB-C cable (220mm, braided, 100W) | Zone 4 cable shortened from 300mm to 220mm | LCSC/AliExpress verified |
| Captive USB-C cable (200mm, braided, 20W) | Zone 5 cable retained | LCSC/AliExpress verified |
| Qi 20W TX module | Upgrades Zone 1 from 15W to 20W | Verified Qi vendor, sample test first |
| Qi watch coil 5W module | Zone 3 universal watch support | AliExpress verified |
| Apple Watch puck module | MOQ 50 direct sourcing target | Verified Shenzhen supplier, target $4–6 |
| INA3221 (second unit) | Replaces both INA219 monitors | LCSC preferred |
| Right-angle IEC C13 inlet | Replaces straight-through C13 inlet | LCSC preferred |
| PCB PTC resettable fuse | Replaces separate inlet fuse holder function | LCSC preferred |
| Step-riser reinforcement insert/rib material | Added to prevent riser cracking (3-step stack) | Local/LCSC |
| WS2811 LED strip | Replaces WS2812B line item | LCSC/AliExpress verified |

### ❌ Removed from current revision

- BH1750 ambient light sensor
- INA219 monitor modules (Zone 4/Zone 5)
- Separate rear inlet fuse holder
- Fixed USB-C panel-mount rear slot ports (Zone 4 / Zone 5 user interface now captive cables)

---

## SECTION 3 — ENCLOSURE SOURCING

- **Centre platform (3-step):** 3D print ABS only for centre geometry
- **Slot walls:** laser cut + bent ABS
- **Base:** vacuum-formed ABS
- **Top plates + riser faces:** laser cut + bent 1.5mm aluminium

Batch 1 target (15 units): ~**$40–62** enclosure cost per unit.

---

## SECTION 4 — SOLDERING TUTORIAL

No process change; existing soldering guidance remains valid.

---

## SECTION 5 — CAD / RENDER TOOLS

Use existing Blender + Fusion 360 workflow and update geometry to 3-step tapered centre + hybrid enclosure parts.

---

## SECTION 6 — SELLING PLATFORM LINKS

Use Kickstarter/Indiegogo or lawyer-reviewed direct-site terms for pre-order legal coverage.

---

## SECTION 7 — PACKAGING & IN-BOX ITEMS

| Item | Source | Cost |
|---|---|---|
| 1.5m braided IEC C13 power cable | AliExpress / local bulk | ~$3 |
| Moulded pulp tray (Apple-style cardboard) | Local packaging vendor | ~$1.50–$2.50 |
| Warranty / setup docs | QR code on box base + dock base (`epitome.io/warranty`, `epitome.io/setup`) | Print removed |
