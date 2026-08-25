# Penta Dock — Parts, Tools & Direct Buy Links

Everything needed to build Penta Dock Batch 1.

---

## SECTION 1 — TOOLS

Keep existing core tool set: soldering iron, solder, flux, multimeter, wire strippers, hot glue gun, cutters, helping hands, safety glasses.

---

## Verified US Suppliers — Batch 1 (August 2026)

### AliExpress (single combined order — apply 25% Section 301 tariff)
- Qi2 20W TX module (~$5.00 before tariff → ~$6.25)
- Qi 20W TX module (120×80mm dish compatible) (~$4.40 before tariff → ~$5.50)
- Apple Watch magnetic puck PCBA (~$1.60 before tariff → ~$2.00)
- Qi watch coil 5W module (~$5.00 before tariff → ~$6.25)
- USB-C PD 100W trigger board (~$1.50 before tariff → ~$1.88)
- USB-C PD 45W trigger board (~$1.60 before tariff → ~$2.00)
- WS2811 LED strip ~15 LED 250mm section (~$1.75 before tariff → ~$2.19)
- IEC C13 right-angle inlet (~$3.00 before tariff → ~$3.75)
- 12V buck converter ×2 (for Qi zones) (~$1.00 each before tariff → ~$1.25 each)
- 5V buck converter ×1 (watch zone + ATtiny85) (~$1.00 before tariff → ~$1.25)

### LCSC (combine if possible — same tariff rules)
- Mean Well LRS-200-24 PSU ×10 (~$17.60 each before tariff → ~$22.00)

### Amazon US (domestic, no tariff, Prime shipping)
- ATtiny85 microcontroller (~$1.50 each)
- Captive USB-C cable 220mm 100W braided 90° angled (~$4.00 each) — Zone 4
- Captive USB-C cable 200mm 65W braided 90° angled (~$3.00 each) — Zone 5
- Hardware relay module (~$1.50 each) — Zone 3 mutual exclusion
- PTC fuse + polyfuses ×5 + TVS ×2 (~$2.50 lot)
- NTC thermistors ×2 + thermal cutoff (~$1.50 lot)
- Wiring / JST connectors / heat shrink bulk ÷10 (~$2.60)
- 3M Bumpons SJ5023 100-pack (~$7)
- M3 screw + heat-set insert + grommet assortment (~$9)
- Silicone sheet 500×500mm textured dot (~$13)
- Weld-On #3 ABS cement (~$8)
- Physical power button rear rail type (~$1.50 each)
- Strain relief silicone boots ×2 (sized for USB-C captive cable) (~$0.60)
- Self-adhesive microfibre sheet dark grey, 400×300mm (~$5 for 10 units = $0.50/unit) → cut to $1.30/unit allocated
- Velcro cable ties matte black (~$5 for 50)
- Magnetic closure rigid boxes ~300×160×130mm matte black (~$5.50 each)
- Black foam sheets for inserts (~$1.50 + $0.80 per unit)
- Braided fabric IEC C13 cable 1.5m matte black (~$5.50 each)

### Inventables (Chicago, fast to Downers Grove IL)
- ABS sheet 3mm black (enough for all 10 units)
- Frosted acrylic 3mm strip material
- ABS sheet sized per enclosure.md: base and top panels 250×100mm; slot wall sizes per spec

### Pumping Station One (Chicago makerspace)
- Address: 3519 N. Elston Ave, Chicago IL
- Membership: ~$50/month
- Use: laser cutting all ABS panels and acrylic diffuser strips for all 10 units
- Bring: DXF files of all panels (from generate_3d_model.py), own ABS sheet from Inventables

### School makerspace
- Use: 3D printing centre platform ×10
- Bring: own ABS filament spool ($20, Bambu or Hatchbox ABS)
- Print settings: 2.5mm walls, 20% infill, 0.2mm layer height
- Print time: ~6–8 hours per part

### Home Depot / Walmart (Downers Grove)
- Acetone 1 litre
- Rust-Oleum Filler Primer
- Rust-Oleum 2X Matte Black
- Rust-Oleum Matte Clear Coat
- Sandpaper assortment
- Spray adhesive (3M Super 77 or equivalent)

### Microcenter (Westmont IL — 7 min from Downers Grove)
- Backup source for electronics (ATtiny85 programmer, soldering supplies)
- Do not pay Microcenter prices for parts cheaper on Amazon/AliExpress

### Moo.com
- Setup cards 85×55mm matte black — Penta Dock, zone reference, QR to epitomecharge.com
- Order minimum 50 cards for cost efficiency

### Payment / shipping
- Wise.com: international bank transfer to AliExpress/LCSC (0.45% fee, much cheaper than PayPal)
- Stripe: payment processing for customer orders (2.9% + $0.30 per transaction)
- Shopify: storefront + Stripe integration + real-time shipping calculation (Pirateship integration)
- Pirateship: discounted USPS/UPS Ground labels for customer shipping

---

## Parts NOT in This Build (Batch 2+ / Shelved)

These parts are explicitly excluded from Batch 1:
- ~~ESP32-C3 SuperMini~~ — no wireless, no app in Batch 1
- ~~INA3221 power monitor~~ — no per-zone power monitoring in Batch 1
- ~~JLCPCB PCBs~~ — no custom PCBs in Batch 1

See [app-spec.md](app-spec.md) for future app hardware spec.
