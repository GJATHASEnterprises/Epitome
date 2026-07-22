# Quad-Dock — Prototype Guide

---

## Goal of the Prototype

Not a sellable unit — a functional proof of concept to verify:

- ✅ All 4 zones charge correctly
- ✅ ESP32-C3 connects, reads sensors, controls LEDs
- ✅ iOS app connects via BLE
- ✅ Theft alert triggers and sends notification
- ✅ Arc shape feels right in hand and on desk
- ✅ Laptop groove holds laptop securely

Definitive placement coordinates for prototyping and fixtures are in
[component-positions.md](component-positions.md).

---

## Budget: $500

| Category | Low | High |
|----------|-----|------|
| Electronics (breakout boards) | $68 | $111 |
| Enclosure (3D print from JLCPCB) | $40 | $70 |
| Shipping (JLCPCB 3D print) | $15 | $25 |
| Tools (if you need them) | $51 | $84 |
| Buffer for mistakes + spares | $50 | $80 |
| Second 3D print iteration | $0 | $70 |
| **Total** | **~$224** | **~$440** |

You will have ~$60–$150 remaining for unexpected costs.

---

## Tools Needed

| Tool | Why | Cost If Buying |
|------|-----|---------------|
| **Soldering iron** | Solder wires to coils, connectors, PSU leads | $20–$35 |
| **Multimeter** | Check voltages, continuity, debug faults | $15–$25 |
| **Wire strippers** | Strip PSU wires and hookup wire | $8–$12 |
| **Hot glue gun** | Prototype assembly — holds components in 3D print shell | $8–$12 |
| Flush cutters | Trim wire ends and component leads | $5–$10 |
| **Total if buying all tools** | | **$56–$94** |

*If you already have a soldering iron and multimeter, tool cost is near zero.*

---

## Prototype BOM (AliExpress + LCSC)

| # | Part | Qty | Est. Cost | Source |
|---|------|-----|-----------|--------|
| 1 | ESP32-C3 Mini dev board | 2 (1 spare) | $6–$10 | LCSC / AliExpress |
| 2 | Qi 15W TX coil module (50mm) | 2 | $10–$16 | AliExpress |
| 3 | Apple Watch charger module (puck) | 1 | $8–$12 | AliExpress |
| 4 | USB-C PD 100W controller board | 1 | $8–$14 | AliExpress |
| 5 | INA3221 breakout board | 1 | $2–$4 | LCSC / AliExpress |
| 6 | INA219 breakout board | 1 | $1–$3 | LCSC / AliExpress |
| 7 | BH1750 ambient light sensor breakout | 1 | $1–$2 | AliExpress |
| 8 | WS2812B LED strip (1m reel) | 1 | $3–$5 | AliExpress |
| 9 | N52 ring magnets (×5) | 1 pack | $3–$5 | AliExpress |
| 10 | 180W AC/DC PSU module (20V out) | 1 | $15–$22 | AliExpress / LCSC |
| 11 | IEC C13 inlet socket (panel mount) | 1 | $2–$3 | AliExpress |
| 12 | Full-size breadboard (830 tie-points) | 2 | $6–$10 | Local / AliExpress |
| 13 | Jumper wires (male-male + male-female) | 2 packs | $4–$8 | Local / AliExpress |
| 14 | USB-C connector breakout boards | 2 | $2–$4 | AliExpress |
| 15 | Assorted resistors (300Ω, 10K) + 100µF capacitors | 1 lot | $3–$5 | LCSC |
| 16 | Frosted acrylic strip (LED diffuser test) | 1 | $5–$10 | Local hardware / AliExpress |
| **Electronics total** | | | **$79–$133** | |

*Order at least 25% extra passives and jumper wires as spares.*

---

## 4-Week Build Plan

### Week 1 — Order Everything

**Day 1–2: Place Orders**
1. Order all electronics from AliExpress (7–14 day shipping — order first)
2. Order 3D print from JLCPCB (5–7 business days):
   - Upload Arc profile at actual dimensions: 300mm × 140mm (rear) × 110mm (front), 22mm rear height, 12mm front height
   - Request SLA or FDM print (FDM is cheaper; SLA is smoother)
   - Include laptop groove (22mm × 12mm) and watch cradle teardrop pod in the model
3. Order any missing tools if needed

**Day 3–7: Prep**
- Cut cardboard to Arc dimensions (see Week 2)
- Review ESP32-C3 datasheet and pin assignments
- Set up Arduino IDE with ESP32-C3 board support
- Install FastLED or NeoPixel library

---

### Week 2 — Cardboard Mock

**Goal:** Verify physical layout and feel before the 3D print arrives. Costs $0.

**Steps:**
1. Cut cardboard to Arc profile — 300mm long, taper from 140mm (rear) to 110mm (front)
2. Build up rear height to 22mm and front to 12mm using stacked cardboard layers
3. Cut a 22mm × 12mm slot in the rear-right for the laptop groove
4. Cut a rough teardrop shape in the rear-left for the watch cradle
5. Place all 4 devices on the cardboard mock:
   - Phone on Zone 1 at `(-20,70)`
   - AirPods/phone on Zone 2 at `(+20,70)`
   - Apple Watch cradle zone at `(-22,225)`
   - Laptop groove zone at `(+29,294)` / `X:+18..+40, Y:288..300`
6. Sit at your desk — does it feel right? Is the watch angle comfortable? Does the laptop feel stable?
7. **Adjust dimensions in your 3D model** before the print arrives if anything feels off

---

### Week 3 — Electronics Bench Test

**Goal:** Confirm all 4 zones charge and the ESP32-C3 talks to everything.

**Checklist:**
- [ ] Wire PSU: IEC C13 inlet → 180W PSU → main 20V rail. Measure with multimeter — confirm 20V output
- [ ] Wire Qi coil 1 (Zone 1): 12V (via step-down from 20V) → coil module. Place phone on coil — confirm wireless charging LED or phone charging indicator
- [ ] Wire Qi coil 2 (Zone 2): Same as Zone 1. Test with second phone or AirPods
- [ ] Wire Watch puck (Zone 3): 5V → puck. Place Apple Watch — confirm charging
- [ ] Wire USB-C PD board (Zone 4): 20V in → PD board → USB-C out. Connect laptop — confirm charging
- [ ] Flash ESP32-C3 via onboard USB — confirm "Hello World" over serial
- [ ] Wire INA3221 (SDA/SCL to ESP32-C3 GPIO 8/9) — read power data from Zones 1–3
- [ ] Wire INA219 (same I2C bus) — read power data from Zone 4
- [ ] Wire BH1750 (same I2C bus) — read lux value in serial monitor
- [ ] Wire WS2812B LED strip (GPIO 4 → 300Ω resistor → DIN) — confirm all 16 LEDs light up
- [ ] Run LED test: Red → Zone 1, Green → Zone 2, Off → Zones 3+4 — confirm correct zone mapping
- [ ] Connect app via BLE — confirm connection and live zone data reading
- [ ] Test theft alert: remove phone from Zone 1 while app is connected — confirm push notification fires

---

### Week 4 — Full Assembly

**Goal:** Fit everything into the 3D printed Arc shell and test as a unit.

**Checklist:**
- [ ] 3D print has arrived — inspect fit: laptop groove width (22mm), watch cradle shape, overall dimensions
- [ ] Hot glue Qi coil 1 into Zone 1 pocket position
- [ ] Hot glue Qi coil 2 into Zone 2 pocket position
- [ ] Mount Watch puck into teardrop cradle pod
- [ ] Mount USB-C PD board in Zone 4 area — confirm USB-C port aligns with groove
- [ ] Hot glue PSU module into base — ensure cooling vents are not blocked
- [ ] Route IEC C13 inlet to rear panel cutout
- [ ] Mount ESP32-C3 board in accessible position (for re-flashing)
- [ ] Fit WS2812B strip under front lip — add frosted acrylic diffuser strip over it
- [ ] Fit INA3221 + INA219 boards on breadboard or hot glue to base
- [ ] Fit BH1750 sensor facing upward (reads ambient light through diffuser or front gap)
- [ ] Route all wires neatly — use cable ties or hot glue to secure runs
- [ ] Attach rubber feet to base (×4)
- [ ] Place aluminum top plate (or cardboard substitute for prototype) on top
- [ ] Power on — confirm all 4 zones charge simultaneously
- [ ] Confirm app connection and live data
- [ ] Confirm theft alert end-to-end (remove device → push notification)
- [ ] Confirm LED states per zone (Red/Green/Off)
- [ ] Confirm ambient light dim: cover BH1750 — confirm LEDs dim; uncover — confirm brighten

---

## Full Assembly Checklist (Quick Reference)

- [ ] PSU wired and outputting 20V
- [ ] Zone 1 Qi coil charging a phone
- [ ] Zone 2 Qi coil charging a phone or AirPods
- [ ] Zone 3 Watch puck charging Apple Watch
- [ ] Zone 4 USB-C PD charging laptop
- [ ] ESP32-C3 running firmware
- [ ] INA3221 reading Zones 1–3 power
- [ ] INA219 reading Zone 4 power
- [ ] BH1750 reading ambient lux
- [ ] WS2812B LED strip responding to zone states
- [ ] App connected via BLE
- [ ] Theft alert firing correctly
- [ ] Ambient auto-dim working
- [ ] All components fit in 3D print shell

---

## Budget Breakdown

| Category | Low | High |
|----------|-----|------|
| Electronics components | $79 | $133 |
| 3D print (JLCPCB) | $40 | $70 |
| 3D print shipping | $15 | $25 |
| Tools (if purchasing) | $51 | $84 |
| Buffer / spares | $50 | $80 |
| Second 3D print (if shape adjustment needed) | $0 | $70 |
| **Total** | **~$235** | **~$462** |
| **Budget** | | **$500** |
| **Remaining** | | **~$38–$265** |
