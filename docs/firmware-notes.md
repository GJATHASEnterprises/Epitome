# Quad-Dock — Firmware Notes

## Night Mode / Sleep Mode

- **Trigger:** local time 23:00–07:00 (configurable via app, default ON)
- **LED behaviour:** all zone LEDs off unless that zone has active power draw > 0.5W (read via INA3221/INA219)
- **Notification behaviour:** theft alert push notifications silenced overnight (configurable, default ON)
- **Implementation:** ESP32-C3 stores time via SNTP over WiFi; falls back to BLE-synced time from phone if no WiFi
- **Override:** placing a new device on any zone during night mode briefly illuminates that zone's LED for 3 seconds to confirm charging started, then returns to off
