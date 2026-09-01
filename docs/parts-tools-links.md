# Epitome Step — Parts, Tools, and Supplier Links

---

## Key electronics suppliers

| Part | Supplier | Search / notes |
|---|---|---|
| Qi2 20W TX module | AliExpress / LCSC | Search "Qi2 transmitter module 20W" — verify MPP spec |
| Qi 5W TX module | AliExpress | Search "5W Qi wireless charging module PCBA" |
| Apple Watch PCBA | AliExpress | Search "Apple Watch wireless charger PCBA module" |
| Qi watch coil 5W | AliExpress | Search "universal Qi watch coil 5W" |
| Hardware relay SPDT | LCSC / Digi-Key | IM03TS or equivalent, 5V coil |
| 12V buck converter | AliExpress / LCSC | MP1584 or LM2596 module, compact |
| 5V buck converter | AliExpress / LCSC | MP2307 or similar, <10 mm tall |
| ATtiny85 DIP-8 | Digi-Key / Mouser | ATtiny85-20PU |
| WS2811 LED strip | AliExpress | "WS2811 warm white 30LED/m" — cut to 8 LEDs, 130 mm |
| WS2812B LED strip | AliExpress | "WS2812B 60LED/m black PCB" — cut to 8 LEDs, 130 mm |
| DC barrel jack 5.5/2.5 mm | Amazon / AliExpress | Panel-mount female, straight |
| USB-C PD 60W trigger board | AliExpress | Search "USB-C PD 60W trigger module" |
| USB-C PD 30W trigger board | AliExpress | Search "USB-C PD 30W trigger module" |
| USB-C panel-mount receptacle | AliExpress | USB-C female panel mount, solder type |
| Polyfuses ×5 | Digi-Key | Littelfuse 0ZCJ0110AF2E or 1A/1.5A/2A/3A variants |
| TVS diodes ×2 | Digi-Key | SMAJ5.0A or 3.3V bidirectional |
| NTC thermistor 10kΩ | Digi-Key | 10kΩ NTC, 0603 or through-hole |
| Thermal cutoff | AliExpress | 70°C thermal fuse, axial |
| JST-XH 2.54 mm kit | Amazon | Assorted connectors and housings |
| 22 AWG silicone wire | Amazon | Red/black, 25 ft each |
| 26 AWG stranded wire | Amazon | Signal wire, assorted colours |

---

## Enclosure materials

| Part | Supplier | Notes |
|---|---|---|
| Walnut sheet 4 mm | Woodcraft / local hardwood | 300 × 300 mm minimum per step set |
| ABS sheet 4 mm black | TAP Plastics / Amazon | "ABS plastic sheet 4mm black" |
| ABS filament (matte black) | Printed Solid / Amazon | For 3D printing base and riser |
| Frosted acrylic 3 mm | TAP Plastics / Amazon | "Frosted white acrylic sheet" — cut to 130 × 10 mm |
| Silicone sheet 1.5 mm | Amazon | "Black silicone sheet 1.5mm food grade" |
| Rubio Monocoat Pure | Woodcraft / Amazon | 100 mL tin, enough for ~20 step sets |
| M3 heat-set inserts | Amazon | "M3 × 4 mm brass heat-set inserts" |
| M3 button head screws | Amazon | M3 × 8 mm, M3 × 12 mm mix |
| 3M Bumpons SJ5012 | Amazon | Clear or black, 4 per unit |
| Matte black spray paint | Hardware store | Rust-Oleum 2X Matte Black #249127 |
| Grey sandable primer | Hardware store | Rust-Oleum Sandable Primer Grey |
| Thermal epoxy | Amazon | "thermal epoxy adhesive" for NTC |
| Cable ties 3 mm | Amazon | Small, black |
| Adhesive foam tape 1 mm | Amazon | For mounting PCBs flat |

---

## Packaging suppliers

| Part | Supplier | Notes |
|---|---|---|
| Rigid matte black box | Papermart / Uline | ~200 × 130 × 90 mm two-piece |
| EVA foam insert | Amazon / eFoam | Black EVA 20 mm, cut to size |
| 100W USB-C GaN brick | Amazon | Anker 100W GaN, 45W Ugreen, or equivalent |
| USB-C to barrel cable 1 m | AliExpress / Amazon | 5.5/2.5 mm DC output, USB-C input |
| USB-C cables 1 m ×3 | Amazon | USB-C to USB-C, braided |
| Setup cards | Vistaprint / Printify | 85 × 55 mm, matte black, white print |
| Belly bands | Printify / local print shop | 620 × 80 mm, 300 gsm |

---

## Tools required

### School makerspace
- FDM 3D printer (Bambu P1P / Prusa MK4 / similar) — ABS capable
- CO₂ laser cutter (40W+ for walnut; 30W for ABS) — with ventilation
- Soldering iron with fine tip + heat-set tip (or brass barrel)
- Multimeter
- Flush cutters, needle-nose pliers
- USB programmer (USBasp) for ATtiny85
- Laptop with Arduino IDE

### Hand tools
- 220, 320, 400-grit sandpaper
- Lint-free cloths ×10
- Latex gloves
- Spray booth or outdoor area
- Cable tie gun (optional, speeds assembly)
- M3 hex key
- Tweezers

### Pumping Station One (Chicago makerspace) — specific tools
- Epilog Fusion Pro laser cutter (walnut: 65% power, 15 mm/s)
- Ultimaker S5 for ABS (enclosed printer with heated chamber)
- Hakko FX-888D soldering station
- Rigol DP832 bench PSU for zone testing

---

## Test equipment

| Tool | Purpose |
|---|---|
| Benchtop PSU (12V 3A) | Zone testing before final assembly |
| USB-C power meter (FNIRSI or similar) | Verify PD negotiation on both ports |
| Qi charging tester | Verify zone 1 and 2 output |
| Multimeter | Continuity, fuse check, thermistor reading |
| USBasp programmer | Flash ATtiny85 |

