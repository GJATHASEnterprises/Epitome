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
- **WiFi** (optional, for remote monitoring and OTA updates)
- ESP32 acts as BLE peripheral + WiFi server

---

## MVP Features (Version 1.0)

### Dashboard
- Real-time charge % per zone (pulled from INA3221/INA219 data via ESP32)
- Device icons per zone (auto-detected or user-assigned — see Auto Device Detection below)
- Per-zone status indicator (charging / full / idle / error)
- Per-zone LED color bar that mirrors the physical WS2812B strip state (red = charging, green = full, off = no device, pulsing green = all full)
- Total power draw display (watts)

### Zone Controls
- Enable / disable charging per zone
- Set max charge % per zone (e.g. stop at 80% for battery health)
- Priority mode — boost one zone to max wattage
- Rename each zone (e.g. "My iPhone", "Kids Watch")
- **Dark mode LED toggle** — user can force all dock LEDs off from the app, regardless of the ambient light sensor reading. Toggle off restores automatic sensor-based brightness.

### Auto Device Detection
- ESP32 detects device presence on each zone by monitoring power draw threshold via INA3221/INA219
- When power draw rises above the idle threshold, the zone is marked as active and the app displays an auto-assigned device type icon (phone, watch, laptop, accessory)
- User can override the auto-detected icon with a manual assignment per zone

### Scheduling
- Set charging schedule per zone (e.g. only charge 11pm–7am)
- "Smart charge" mode — charge to 80%, pause, top up before wake time

### Ambient Light Override
- The dock's TEMT6000 sensor automatically dims LEDs in dark rooms and brightens them in light — this is on by default
- The app provides a toggle to **override the sensor** and set a fixed LED brightness (0–100%)
- This lets users who want full brightness in a dark room, or a dim room, override the auto-dim behavior

### Notifications
- Alert when device reaches full charge
- Alert when device removed from zone (scheduled removal is excluded)
- Overheat warning alert
- **Theft alert** — if a device is removed from a zone unexpectedly while the app is connected (power draw drops to zero on an active zone without a scheduled removal), the app sends a push notification immediately

### History & Stats
- Daily/weekly charge session log
- **Weekly charge report** — automatically generated summary of total charge time, energy used (kWh), and charge cycles per zone, delivered as an in-app notification every Sunday
- Estimated battery health impact tracker
- Total energy used (kWh) display

### Voice Assistant Shortcuts
- **Siri Shortcuts** (iOS): Users can add shortcuts such as "Hey Siri, check my dock" to read charge status aloud, or "Hey Siri, turn off dock LEDs" to trigger dark mode
- **Google Assistant** (Android): App exposes intents for status read and zone control
- Shortcuts are configured in the app's Settings screen

### OTA Firmware Updates
- The app checks for new ESP32 firmware versions from the GitHub releases feed on app launch
- When an update is available the user is prompted in the app
- Update is delivered over WiFi (ESP32 Arduino OTA) — dock must be connected to the same WiFi network as the phone
- Progress bar displayed in app during update; dock LEDs pulse blue during OTA flash (override color injected by firmware before update begins)

---

## App Architecture

```
Flutter App
    |
    +-- BLE Service (flutter_blue_plus package)
    |       |
    |       +-- Connect to ESP32
    |       +-- Read zone power data (GATT characteristics)
    |       +-- Read LED strip state + dark mode state
    |       +-- Send zone control and LED control commands
    |       +-- Receive theft alert and overheat events
    |
    +-- WiFi Service (http package)
    |       |
    |       +-- OTA update download + push to ESP32
    |       +-- Remote status polling (optional)
    |
    +-- Notification Service (flutter_local_notifications)
    |       |
    |       +-- Charge complete alerts
    |       +-- Theft alert push notification
    |       +-- Overheat warning
    |       +-- Weekly charge report notification
    |
    +-- UI Screens
    |       |
    |       +-- Dashboard Screen
    |       +-- Zone Detail Screen
    |       +-- Schedule Screen
    |       +-- Settings Screen (ambient light override, dark mode, voice shortcuts)
    |       +-- History / Weekly Report Screen
    |       +-- OTA Update Screen
    |
    +-- Local Storage (Hive or sqflite)
            |
            +-- Zone names/settings
            +-- Charge history log
            +-- User preferences (dark mode, ambient override, brightness level)
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
| LED Strip Status | Read/Notify | Per-zone color state + dark mode flag + pulse state (JSON) |
| LED Control | Write | Set dark mode on/off; set brightness override (0 = sensor auto, 1–100 = fixed) |
| Device Presence | Read/Notify | Per-zone device detected flag (boolean array) |
| Theft Alert | Notify | Zone index of unexpected removal event |
| System Status | Read/Notify | Overall dock status |

---

## Recommended Flutter Packages

| Package | Use |
|---------|-----|
| flutter_blue_plus | BLE communication with ESP32 |
| provider or riverpod | State management |
| hive | Local storage |
| fl_chart | Charge history graphs |
| flutter_local_notifications | Push alerts (charge complete, theft, overheat, weekly report) |
| http | WiFi OTA update download |
| app_shortcuts / siri_shortcuts | Voice assistant shortcut integration |

---

## Development Phases

| Phase | Target | Description |
|-------|--------|-------------|
| Phase 1 | Week 1–2 | ESP32 BLE server + basic Flutter BLE connection |
| Phase 2 | Week 3–4 | Dashboard with live power + LED strip status data |
| Phase 3 | Week 5–6 | Zone controls, dark mode toggle, ambient light override, scheduling |
| Phase 4 | Week 7–8 | Notifications, theft alert, auto device detection icons |
| Phase 5 | Week 9–10 | OTA update flow, voice shortcuts, weekly report |
| Phase 6 | Week 11–12 | Polish, testing, app store prep |
