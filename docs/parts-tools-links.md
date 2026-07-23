# Quad-Dock — Parts, Tools & Direct Buy Links

Everything you need to order to build the prototype. All links are verified manufacturer
or authorised distributor sources only — no random AliExpress stores.

---

## SECTION 1 — TOOLS

Buy these first. You need them before any parts arrive.

| Tool | Why You Need It | Buy Link | Cost |
|------|----------------|----------|------|
| **Soldering iron** (temperature-controlled) | Soldering wires to coils, PSU leads, connectors | [Amazon — Hakko FX-888D](https://www.amazon.com/dp/B00ANZRT4M) | ~$50 (worth it — cheap irons ruin joints) |
| **Solder** (60/40 rosin core, 0.8mm) | The actual joining material | [Amazon — Kester 44](https://www.amazon.com/dp/B00068IJWC) | ~$10 |
| **Flux pen** | Helps solder flow cleanly, prevents cold joints | [Amazon — MG Chemicals 835](https://www.amazon.com/dp/B005DNR01Q) | ~$8 |
| **Multimeter** | Measure voltage, check continuity, debug faults | [Amazon — AstroAI DT132A](https://www.amazon.com/dp/B01ISAMUA6) | ~$15 |
| **Wire strippers** | Strip PSU wires and hookup wire | [Amazon — Irwin Self-Adjusting](https://www.amazon.com/dp/B000OQ21CA) | ~$12 |
| **Flush cutters** | Trim component leads and wire ends | [Amazon — Hakko CHP-170](https://www.amazon.com/dp/B00FZPDG1K) | ~$8 |
| **Hot glue gun** | Prototype assembly — holds parts in the 3D printed shell | Any hardware store | ~$8 |
| **Helping hands / PCB vice** | Holds boards still while you solder | [Amazon — Kaisi 899-II](https://www.amazon.com/dp/B07MDKXNPC) | ~$12 |
| **Solder wick** (desoldering braid) | Remove bad solder joints | [Amazon — Chemtronics CSW2-25](https://www.amazon.com/dp/B00B89ARC8) | ~$6 |
| **Safety glasses** | Flux splatter and wire ends can fly | Any hardware store | ~$5 |

**Total tools if buying everything: ~$134**
*If you already have a multimeter and soldering iron, cut that to ~$60.*

---

## SECTION 2 — ELECTRONICS PARTS (Direct Buy Links)

### ✅ Safe to order from LCSC — guaranteed genuine manufacturer parts

| # | Part | LCSC Part # | Direct Link | Unit Cost | Qty to Order |
|---|------|-------------|-------------|-----------|--------------|
| 1 | ESP32-C3-MINI-1-N4 (MCU) | C2838502 | [lcsc.com/product-detail/C2838502](https://www.lcsc.com/product-detail/C2838502.html) | ~$2.50 | 2 (1 spare) |
| 2 | INA3221AIRGVR (power monitor, Zones 1–3) | C207114 | [lcsc.com/product-detail/C207114](https://www.lcsc.com/product-detail/C207114.html) | ~$2.00 | 2 (1 spare) |
| 3 | INA219BIDCNT (power monitor, Zone 4) | C214795 | [lcsc.com/product-detail/C214795](https://www.lcsc.com/product-detail/C214795.html) | ~$1.00 | 2 (1 spare) |
| 4 | BH1750FVI-TR (ambient light sensor) | C97234 | [lcsc.com/product-detail/C97234](https://www.lcsc.com/product-detail/C97234.html) | ~$0.60 | 2 (1 spare) |
| 5 | WS2812B-B/W (addressable LEDs) | C114586 | [lcsc.com/product-detail/C114586](https://www.lcsc.com/product-detail/C114586.html) | ~$0.15 | 30 (need 16, order extra) |
| 6 | FUSB302MPX (USB-C PD controller chip) | C442699 | [lcsc.com/product-detail/C442699](https://www.lcsc.com/product-detail/C442699.html) | ~$1.50 | 2 (1 spare) |
| 7 | Mean Well LRS-200-24 PSU (adjust to ~20V) | C2857547 | [lcsc.com/product-detail/C2857547](https://www.lcsc.com/product-detail/C2857547.html) | ~$18 | 1 |
| 8 | IEC C13 inlet socket (panel mount) | Search "IEC C13" on LCSC | [lcsc.com/search?q=IEC+C13](https://www.lcsc.com/search?q=IEC+C13) | ~$2 | 1 |
| 9 | NTC thermistor 10K (per coil zone) | Search "NTC 10K" on LCSC | [lcsc.com/search?q=NTC+10K](https://www.lcsc.com/search?q=NTC+10K) | ~$0.20 | 5 |
| 10 | Polyfuse (resettable fuse, per zone) | Search "polyfuse 2A" on LCSC | [lcsc.com/search?q=polyfuse](https://www.lcsc.com/search?q=polyfuse) | ~$0.40 | 6 |
| 11 | 300Ω resistor (LED data line protection) | Search "300R 0805" on LCSC | [lcsc.com/search?q=300R+0805](https://www.lcsc.com/search?q=300R+0805) | ~$0.02 | 10 |
| 12 | 100µF 25V capacitor | Search "100uF 25V" on LCSC | [lcsc.com/search?q=100uF+25V](https://www.lcsc.com/search?q=100uF+25V) | ~$0.10 | 5 |
| 13 | Full-size breadboard (830 tie-points) | Any | [Amazon](https://www.amazon.com/dp/B07LFD4LT6) | ~$5 | 2 |
| 14 | Jumper wires (M-M and M-F packs) | Any | [Amazon](https://www.amazon.com/dp/B01EV70C78) | ~$6 | 1 pack each |

### ✅ Order from Adafruit — for Qi coils and Apple Watch puck (verified, safe, returnable)

| # | Part | Direct Link | Cost |
|---|------|-------------|------|
| 15 | Qi wireless charging transmitter coil (15W capable) | [adafruit.com/product/4526](https://www.adafruit.com/product/4526) | ~$10 |
| 16 | Apple Watch magnetic charging puck (USB-A) | [adafruit.com/product/4459](https://www.adafruit.com/product/4459) | ~$15 |

> **Why Adafruit instead of AliExpress for these?**
> Qi coil quality directly affects phone charging safety. Adafruit tests their modules.
> AliExpress is fine for passive components — not for power-delivery coils.

---

## SECTION 3 — ENCLOSURE / 3D PRINT

| Item | Service | What to Upload | Cost |
|------|---------|----------------|------|
| Arc enclosure shell (prototype) | [JLCPCB 3D printing](https://jlcpcb.com/3d-printing) | `.STL` or `.STEP` file of the dock body | ~$40–70 |
| Frosted acrylic LED diffuser strip | Local hardware / plastics shop | 290mm × 8mm × 3mm frosted acrylic | ~$5–10 |
| Aluminium top plate | Local laser cutter (search "laser cutting near me") | `.DXF` file of the Arc profile | ~$15–25 |

**For the 3D model file:** Use Fusion 360 (free) to model the enclosure.
All dimensions are in `docs/enclosure.md` and `docs/component-positions.md` in this repo.

---

## SECTION 4 — SOLDERING TUTORIAL

### Before you touch anything

- Work on a non-conductive surface (wooden desk or silicone mat)
- Wear safety glasses — flux can spit
- Never touch the iron tip — it reaches 350°C
- Keep a damp sponge or brass wool tip cleaner next to you at all times

### Tools check before starting

- [ ] Soldering iron set to **350°C** (lead solder) or **370°C** (lead-free)
- [ ] Solder: 60/40 rosin core, 0.8mm
- [ ] Flux pen ready
- [ ] Multimeter set to continuity mode (beeps when two points are connected)
- [ ] Helping hands clamping your board or wire

---

### Step-by-step: How to solder a wire to a pad

**Step 1 — Tin the iron**
Touch a small amount of solder to the hot iron tip until it coats it with a shiny silver layer.
Wipe on brass wool. The tip should look shiny, not black. Do this every 2–3 joints.

**Step 2 — Tin the wire**
Strip 5mm of insulation. Twist the strands. Touch the iron to the wire, then feed a tiny
amount of solder into the wire until it soaks in. The wire should look silver and stiff.

**Step 3 — Tin the pad**
Touch the iron to the pad on the board for 2 seconds. Feed a tiny amount of solder onto
the pad (not onto the iron). It should form a small shiny mound.

**Step 4 — Join them**
Hold the tinned wire against the tinned pad. Touch the iron to both at the same time for
1–2 seconds. The solder on both should melt and merge. Remove the iron. **Do not move
the wire for 5 seconds** while it cools.

**Step 5 — Inspect**
A good joint is: **shiny, smooth, volcano-shaped**.
A bad joint is: **dull, grey, blobby, or cracked**. If bad, reheat and add a tiny bit of fresh
solder. If still bad, use solder wick to remove it and start again.

---

### Common mistakes and how to fix them

| Mistake | What it looks like | Fix |
|---------|-------------------|-----|
| Cold joint | Dull grey, crumbly | Reheat for 2s, add tiny solder |
| Too much solder | Big blob, may bridge to nearby pad | Use solder wick to remove excess |
| Solder bridge | Two pads connected when they shouldn't be | Drag solder wick across both pads with iron |
| Burnt pad | Pad turns black, lifts off board | Overheated — use flux, lower temp, work faster |
| Wire won't tin | Solder beads off | Clean with flux pen first, then try again |

---

### Video tutorials (watch these before you start)

- **Absolute beginner:** [youtube.com/watch?v=-XSrkcRxKw8](https://www.youtube.com/watch?v=-XSrkcRxKw8)
- **Step-by-step written guide:** [engineerfix.com/how-to-solder](https://engineerfix.com/how-to-solder-a-step-by-step-guide-for-beginners/)
- **Common mistakes:** [electronicsandyou.com/blog/soldering-in-electronics](https://www.electronicsandyou.com/blog/soldering-in-electronics.html)

---

## SECTION 5 — 3D DESIGN TOOLS

| Tool | Cost | What it's for | Link |
|------|------|---------------|------|
| **Fusion 360** | Free (personal use) | Model the dock enclosure to exact spec | [autodesk.com/fusion360](https://www.autodesk.com/products/fusion360/free-trial) |
| **Blender** | Free | Photorealistic renders for Kickstarter / marketing | [blender.org/download](https://www.blender.org/download/) |
| **Canva** | Free tier | Kickstarter page, social posts, 2D marketing | [canva.com](https://www.canva.com) |
| **JLCPCB** | Pay per order | 3D print your enclosure shell | [jlcpcb.com/3d-printing](https://jlcpcb.com/3d-printing) |

> **If you're not confident with 3D design:** Post on Fiverr searching
> "Fusion 360 product render" or "3D product visualization" — budget $30–80
> and send them this repo's docs. A good Fiverr render will look better than
> most first attempts in Blender and takes 1–3 days.

---

## SECTION 6 — SELLING PLATFORM LINKS

| Platform | Use | Link |
|----------|-----|------|
| **Kickstarter** | Launch campaign, get funded before building | [kickstarter.com/learn](https://www.kickstarter.com/learn) |
| **Shopify** | Your own store, full margin | [shopify.com](https://www.shopify.com) |
| **Etsy** | Handmade/small batch appeal for batch 1 | [etsy.com/sell](https://www.etsy.com/sell) |
| **Fiverr** (hire a designer) | 3D renders, logo, Kickstarter page design | [fiverr.com](https://www.fiverr.com) |

---

*Last updated: 2025 — verify prices and stock before ordering.*
