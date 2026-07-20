# Quad Device Dock — Companion App Specification

---

## App Name
Quad Dock

## Platform
- iOS (iPhone)
- Android
- Built with **Flutter** (single codebase, both platforms)

## Communication
- **Bluetooth** (primary, local connection)
- **WiFi** (optional, for remote monitoring)
- ESP32 acts as BLE peripheral + WiFi server

---

## MVP Features (Version 1.0)

### Dashboard
- Real-time charge % per zone (pulled from INA219 data via ESP32)
- Device icons per zone (auto-detect or user-assigned)
- Per-zone status indicator (charging / full / idle / error)
- Per-zone LED color display that mirrors the physical red/green/off hardware state
- Total power draw display (watts)

### Zone Controls
- Enable / disable charging per zone
- Set max charge % per zone (e.g. stop at 80% for battery health)
- Priority mode — boost one zone to max wattage
- Rename each zone (e.g. "My iPhone", "Kids Watch")
- Dark mode LED toggle so the user can disable all dock LEDs from the app

### Scheduling
- Set charging schedule per zone (e.g. only charge 11pm–7am)
- "Smart charge" mode — charge to 80%, pause, top up before wake time

### Notifications
- Alert when device reaches full charge
- Alert when device removed from zone
- Overheat warning alert

### History & Stats
- Daily/weekly charge session log
- Estimated battery health impact tracker
- Total energy used (kWh) display

---

## Future Features (Version 2.0+)
- Multi-dock support (manage multiple Quad Docks)
- Home automation integration (Apple Home / Google Home)
- Widget for iPhone/Android home screen
- Siri / Google Assistant shortcuts
- Firmware OTA updates via app
- Usage export (CSV)

---

## App Architecture

```
Flutter App
    |
    +-- BLE Service (flutter_blue_plus package)
    |       |
    |       +-- Connect to ESP32
    |       +-- Read zone power data (GATT characteristics)
    |       +-- Read LED state + dark mode state
    |       +-- Send zone control and LED control commands
    |
    +-- UI Screens
    |       |
    |       +-- Dashboard Screen
    |       +-- Zone Detail Screen
    |       +-- Schedule Screen
    |       +-- Settings Screen
    |       +-- History Screen
    |
    +-- Local Storage (Hive or sqflite)
            |
            +-- Zone names/settings
            +-- Charge history log
            +-- User preferences
```

---

## ESP32 Firmware BLE Interface

| GATT Characteristic | Direction | Data |
|---------------------|-----------|------|
| Zone 1 Power | Read/Notify | Voltage, current, watts (JSON) |
| Zone 2 Power | Read/Notify | Voltage, current, watts (JSON) |
| Zone 3 Power | Read/Notify | Voltage, current, watts (JSON) |
| Zone 4 Power | Read/Notify | Voltage, current, watts (JSON) |
| Zone Control | Write | Enable/disable, max %, priority (JSON) |
| Device Temp | Read/Notify | Per-zone temp in °C |
| LED Status | Read/Notify | Per-zone red/green/off state + dark mode flag |
| LED Control | Write | Toggle dark mode, restore normal LED behavior |
| System Status | Read/Notify | Overall dock status |

---

## Recommended Flutter Packages

| Package | Use |
|---------|-----|
| flutter_blue_plus | BLE communication with ESP32 |
| provider or riverpod | State management |
| hive | Local storage |
| fl_chart | Charge history graphs |
| flutter_local_notifications | Push alerts |

---

## Development Phases

| Phase | Target | Description |
|-------|--------|-------------|
| Phase 1 | Week 1–2 | ESP32 BLE server + basic Flutter BLE connection |
| Phase 2 | Week 3–4 | Dashboard with live power + LED status data |
| Phase 3 | Week 5–6 | Zone controls, dark mode toggle, and scheduling |
| Phase 4 | Week 7–8 | Notifications + history |
| Phase 5 | Week 9–10 | Polish, testing, app store prep |
