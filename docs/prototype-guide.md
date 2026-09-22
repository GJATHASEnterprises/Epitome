# Epitome Step — Prototype Guide (Sept 2026 planning estimates)

## Prototype target

- Build: **2 total prototypes** (1 Step Walnut + 1 Step Obsidian).
- Purpose: geometry, thermal behavior, firmware behavior, and demand-content capture.

## Before printing

1. Place measurement order (~$35, one of each module).
2. Record caliper dimensions in `docs/design-brief-step.md`.
3. Finalize CAD production files.
4. Validate Zone 2 second-device landing geometry before STL freeze.

## Print/material baseline

| Model | Base | Top | Notes |
|---|---|---|---|
| Walnut | Black PETG | Wood-PLA | Sand + Danish oil on top shell |
| Obsidian | CF-PETG | CF-PETG | Hardened steel nozzle required |

## Electronics/FW split

- Walnut: Digispark-style ATtiny85, white status LED.
- Obsidian: Digispark-style ATtiny85 + WS2812B RGB (8 LEDs per side).
- Shared charging config: 20W phone + up-to-15W Zone 2 + 5W watch + 15W USB-C output.

## Validation gates

- Charge compatibility and thermal soak (single-zone and dual-zone)
- Thermal cutoff/recovery
- Obsidian RGB modes + OFF persistence
- Full-load behavior with firmware low-power profile on Zone 2 when all zones are active
- USB-C 15W output stability

Detailed per-model QC: `docs/technical-readouts/`.
