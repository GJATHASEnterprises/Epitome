# Epitome Step — Electronics Reference

Both models share the same beginner-friendly easy-connect electronics architecture. The only model differences are lighting hardware and the Obsidian rear mode button.

---

## Shared schematic overview

```
65W GaN brick
        │
        ▼
USB-C PD input receptacle (rear X=40)
        │
        ▼
PD input trigger board (20V negotiated input)
        │
        ▼
20V distribution PCB / block
        ├──→ 12V screw-terminal buck converter ──→ Qi2 20W TX (Zone 1)
        │                                      └──→ Qi TX up-to-15W (Zone 2)
        ├──→ 5V screw-terminal buck converter ──→ Watch TX coil (Zone 3)
        │                                      ├──→ Digispark-style ATtiny85 USB board
        │                                      └──→ Lighting harness
        └──→ USB-C PD 15W trigger board (rear output)
```

---

## Zone-by-zone power paths

### Zone 1 — Phone (Qi2 20W)
- Feed: 12V branch
- TX module: Qi2 20W magnetic module
- Protection: polyfuse (1.5A) + NTC + hardwired thermal cutoff
- Marketing language: "Qi2 magnetic charging — compatible with MagSafe-case iPhones and Qi2 Android phones"

### Zone 2 — Buds or second phone (up to 15W)
- Feed: **12V branch** (moved from 5V path)
- TX module: same $5.63 class TX as Zone 1 (non-magnetic placement)
- Protection: polyfuse (1.5A)
- Positioning language: "buds or a second phone — up to 15W"

### Zone 3 — Watch zone (5W)
- Feed: 5V branch
- TX: generic watch coil by default
- Important truth: generic watch coil does not charge Apple Watch without MFi-certified hardware

### USB-C output (rear)
- Trigger board: 15W-class output board
- Protection: polyfuse (~1A hold) + TVS diode
- Fuse basis: 15W at 20V is ~0.75A nominal

---

## Power budget (Sept-2026 planning)

| Load | Max power |
|---|---:|
| Zone 1 Qi2 TX | 20W |
| Zone 2 Qi TX | 15W |
| Zone 3 watch | 5W |
| USB-C output | 15W |
| ATtiny85 + lighting | ~1.5W |
| **Theoretical max** | **~56.5W** |
| **Marketing claim cap** | **Up to 60W total** |
| **Included brick** | **65W** |

The firmware soft cap is a detect-based heuristic only. When all zones are active, Zone 2 drops to a low-power profile. USB-C branch current is not directly measured by firmware.

---

## Safety systems

| System | Purpose |
|---|---|
| Polyfuse Zone 1 | Overcurrent protection on Zone 1 TX |
| NTC thermistor Zone 1 | Feeds TX thermal protection path |
| Thermal cutoff Zone 1 | Hard cutoff above thermal threshold |
| Polyfuse Zone 2 | Overcurrent on Zone 2 TX |
| Polyfuse Zone 3 | Overcurrent on watch coil |
| 1A hold polyfuse + TVS on USB-C output | Overcurrent + ESD on output branch |

---

## Hard sourcing and compliance rules

- All TX modules must have verifiable module-level FCC IDs.
- Battery module rules (UN38.3 + UL docs) apply to Outdoor Block gating before sourcing.
