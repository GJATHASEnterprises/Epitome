# Step Go — Travel Charging Dock (FOR LATER — do not start until Batch 1 sells)

**Status:** Concept only. $500 reserved. Go/no-go criteria at bottom.

**One-liner:** Your nightstand, anywhere. A compact two-step wireless dock powered by a removable, certified USB-C power bank — charge phone + watch/buds off-grid, ~3 full phone charges per bank.

---

## Why this architecture: docked bank, not embedded cells

We do NOT build a battery. We build a dock that a certified off-the-shelf power bank slides into.

| | Embedded lithium cells | Docked certified power bank (CHOSEN) |
|---|---|---|
| UN38.3 testing | Required, $3–8K | Covered by bank manufacturer |
| Hazmat shipping | Yes | No — bank ships in its own retail cert |
| Fire liability | Ours entirely | Shared with certified manufacturer (BMS, cutoffs already built in) |
| Dead battery after 500 cycles | Product is e-waste | User buys a new bank — product lives on |
| Airline carry-on | Must stay under 100Wh | 20,000mAh (74Wh) banks are pre-approved size |
| Added BOM cost | ~$30 + certification | ~$25 retail bank (or BYOB — bring your own bank) |

This is the same "pre-certified module" strategy that avoided $30K+ of Qi2/MFi certification on the Step.

## Safety requirements (non-negotiable if built)

1. Only spec name-brand banks with UL 2056 / UN38.3 certification (Anker, INIU, etc.). Publish a compatibility list; never bundle no-name cells.
2. Wireless coils generate heat — enclosure must have passive vent channels above the bank bay and an NTC thermistor cutoff on the phone coil (same part as Step: already in BOM).
3. Coil TX modules must be pre-certified Qi modules (same sourcing rule as Step).
4. No charging while enclosed in a bag: lid/open-frame design so the bank is never sealed in a heated cavity.
5. Firmware: cut wireless TX below 10% bank charge to prevent deep-discharge brownout loops.

With these, risk profile ≈ any commercial power bank + any commercial Qi pad. High degree of safety: **yes**.

## The charge math (honest numbers)

- iPhone battery: ~13.5Wh. End-to-end wireless efficiency from battery: ~65%.
- 20,000mAh bank = 74Wh → ~48Wh delivered wirelessly → **~3.5 full phone charges**, or ~2.5 charges plus watch + buds top-ups.
- "About 3 full charges" is a defensible marketing claim.

## Draft BOM (bundled-bank version)

| Part | Cost |
|---|---:|
| Certified 20,000mAh 45W PD power bank (wholesale) | $22.00 |
| Qi2-class 15–20W TX module (pre-certified) | $6.25 |
| Qi 5W TX module (buds/watch shelf) | $2.50 |
| USB-C trigger/boost board | $2.00 |
| NTC thermistor + polyfuse + wiring/JST | $2.00 |
| ATtiny85 + LED (single warm white, battery gauge blink) | $2.50 |
| 3D printed enclosure (2-step, bank bay, PETG/ABS) | $4.00 |
| Silicone pads + feet + fasteners | $2.00 |
| Packaging (smaller box, card, band — no brick needed!) | $6.00 |
| **Build cost** | **~$49.25** |

BYOB variant (no bank included): build cost ~$27, sell $69–79.

## Unit economics @ $120 (bundled bank)

| Item | Amount |
|---|---:|
| Build cost | $49.25 |
| Stripe fee (2.9% + $0.30) | $3.78 |
| Defect buffer 10% | $4.93 |
| **Full cost** | **$57.96** |
| **Sell price** | **$120.00** |
| **Profit per unit** | **$62.04** |
| **Margin** | **52%** |

**Verdict: profitable at $120 — better margin than either Step model.** Break-even on a 5-unit test batch: 3 sales.

## Positioning

- Target: campers, van-lifers, frequent travelers who already own AirPods + Watch; overlaps with the Walnut buyer's "considered gear" mindset.
- Channels: same Etsy/Shopify + r/vandwellers, r/CampingGear, r/onebag.
- Hero photo: dock on a wooden camp table at dusk, phone + watch charging, lantern glow, tent in background.
- Claims language: "compatible with Qi-enabled devices" — same certification-safe wording rules as Step.

## Go / No-Go criteria (all must be true before spending the $500)

- [ ] Batch 1 (Step) sold through — at least 3 paid units shipped
- [ ] Zero safety/thermal incidents from Batch 1 field use
- [ ] LLC formed + product liability insurance active
- [ ] Confirmed wholesale source for a UL 2056-certified bank at ≤$25
- [ ] One prototype torture-tested: full 74Wh discharge cycle × 3, thermal logged, no cutoff events above spec
