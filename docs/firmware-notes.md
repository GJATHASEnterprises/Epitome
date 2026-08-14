# Epitome Penta — Firmware Notes

## Night Mode / Sleep Mode

- **Trigger:** local time 23:00–07:00 (configurable via app, default ON)
- **LED behaviour:** all zone LEDs off unless that zone has active power draw > 0.5W
- **Notification behaviour:** theft alert push notifications silenced overnight (configurable, default ON)
- **Implementation:** ESP32-C3 uses SNTP with BLE fallback
- **Override:** new charging event flashes zone LED for 3 seconds, then returns to off

## Power Budget Thresholds (Updated)

- Zone 1 max: 15W
- Zone 2 max: **15W**
- Zone 3 max: **5W total shared budget**
- Zone 4 max: 100W
- Zone 5 max: 20W
- System max budget: **155W**
- PSU headroom target: **25W**

## Zone 3 Dual-Mode Detection

- Firmware reports Zone 3 mode as `puck` or `qi_watch`.
- Only one Zone 3 charging source should be active at a time.
- If both detect load, firmware prioritizes currently active path and rejects concurrent activation.
