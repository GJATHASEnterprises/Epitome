# Epitome Step — Physical Design Specification (Sept 2026)

## Envelope targets

- Footprint and tier envelope are finalized from measured modules and CAD lock review.
- Use the measurement-order workflow and dimensional lock process defined in project planning docs before freezing STL/STEP outputs.
- Corner radii target: 6–8 mm external.

## Material split

| Part | Walnut | Obsidian |
|---|---|---|
| Base shell | Black PETG | CF-PETG |
| Top shell | Wood-PLA (oiled) | CF-PETG |
| Lighting | White light pipe status LED | Recessed WS2812B side glow lines |
| MCU | ATtiny85 | ESP32-C3 |

## Hard constraints

- Coil window ≤1.5 mm above each TX coil.
- M3 insert bosses and wiring channels integrated into shell geometry.
- Rear USB-C input recess and strain-relief path required.

For dimensions and measurements to lock before final CAD, use `docs/design-brief-step.md`.
