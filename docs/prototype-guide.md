# Epitome Step — Prototype Guide (Batch 1, Sept 2026)

## Batch target

- Build: **3 Step Walnut + 3 Step Obsidian**.

## Before printing

1. Place Week 1 measurement order (~$35, one of each module).
2. Record caliper dimensions in `docs/design-brief-step.md` §5.
3. Finalize CAD production files (friend sketches or CAD freelancer output).

## Print/material baseline

| Model | Base | Top | Notes |
|---|---|---|---|
| Walnut | Black PETG | Wood-PLA | Sand + Danish oil on top shell |
| Obsidian | CF-PETG | CF-PETG | Hardened steel nozzle required |

## Electronics/FW split

- Walnut controller: ATtiny85, white status LED only.
- Obsidian controller: ESP32-C3 + WS2812B RGB (8–12 LEDs per side).

## Validation gates

- Charge compatibility and thermal soak
- Thermal cutoff/recovery
- Obsidian RGB modes + OFF persistence
- Full-load dual-coil test with Obsidian brightness cap behavior

Detailed per-model QC: `docs/technical-readouts/`.
