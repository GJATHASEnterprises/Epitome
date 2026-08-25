> ⚠️ SHELVED — FUTURE REFERENCE ONLY
> Firmware/MCU is not part of the current build (ATtiny85 only, no wireless). Preserved for future app integration reference.

# Penta Dock — Firmware Notes

## Night Mode / Sleep Mode

- **Trigger:** local time 23:00–07:00 (configurable via app, default ON)
- **LED behaviour:** all zone LEDs off unless that zone has active power draw > 0.5W
- **Notification behaviour:** theft alert push notifications silenced overnight (configurable, default ON)
- **Implementation:** ESP32-C3 uses SNTP with BLE fallback
- **Override:** new charging event flashes zone LED for 3 seconds, then returns to off
- **Brightness control:** manual brightness slider in app (ambient BH1750 auto-dim removed)

## Power Budget Thresholds (Updated)

- Zone 1 max: **20W**
- Zone 2 max: **20W**
- Zone 3 max: **5W total shared budget**
- Zone 4 max: **100W**
- Zone 5 max: **45W**
- System max budget: **190W**
- PSU capacity: **201W** (Mean Well LRS-200-24)
- Headroom target: **11W** (190W load, 201W PSU)
- ATtiny85 soft cap: **185W total draw**

## Zone 3 Dual-Mode Detection

- Firmware reports Zone 3 mode as `puck` or `qi_watch`.
- Only one Zone 3 charging source should be active at a time.
- If both detect load, firmware prioritizes currently active path and rejects concurrent activation.

## Monitoring IC Map

- **INA3221 #1 @ 0x40**: CH1=Zone 1, CH2=Zone 2, CH3=Zone 3
- **INA3221 #2 @ 0x41 (A0 high)**: CH1=Zone 4, CH2=Zone 5, CH3=spare/system

## LED Protocol Note

- Lighting controller changed from WS2812B references to **WS2811**.
- For this build use-case they are functionally equivalent from a zone UX perspective, but firmware timing/driver configuration must explicitly target the WS2811 3-wire protocol behavior.
