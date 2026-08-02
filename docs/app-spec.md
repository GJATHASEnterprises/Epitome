# Quad-Dock — Companion App Specification

---

## App Name
Quad-Dock

## Platform
- **iOS (iPhone)** — primary platform
- Built with **Swift / SwiftUI**

## Communication
- **Bluetooth Low Energy (BLE)** — primary, local connection
- **Firebase** — push notifications (FCM), remote alert delivery
- ESP32-C3 acts as BLE peripheral

---

## Features

### Dashboard
- Real-time charge status per zone (from INA3221/INA219 via ESP32-C3)
- Zone icons: 📱 PHONE, 🎧 BUDS, ⌚ WATCH, 💻 LAPTOP
- Per-zone status: charging / full / empty
- Per-zone LED color bar mirroring physical WS2812B strip state

### Device Detection
- ESP32-C3 detects device presence per zone by monitoring power draw threshold
- App displays zone as active when power draw rises above idle threshold
- Zone icons update automatically

### LED Control
- Enable/disable LED bar from app
- Ambient light auto-dim toggle (BH1750 sensor — on by default)
- Manual brightness override (0–100%)

### Theft Alert
Three alert modes:

| Mode | Behaviour |
|------|-----------|
| **Away** | Full theft alert — any unexpected removal triggers immediate push notification |
| **Night** | Alert only if dock is in a dark room (BH1750 reads below threshold) |
| **Passive** | Logs removal events but does not push a notification |

- Alerts delivered via **Firebase Cloud Messaging (FCM)** push notifications
- Alert history log in app (timestamped removal events per zone)

### BLE Proximity Detection
- App detects when phone moves away from dock (BLE RSSI drop below threshold)
- Triggers theft alert if a device is detected as removed while phone is far away
- Configurable distance threshold in app settings

### Notifications (Firebase FCM)
- Theft alert (device removed unexpectedly)
- Device reached 100% charge (haptic + FCM)
- Weekly charge report (delivered Sunday morning)

### Alert History Log
- Full log of all theft alert events
- Timestamped per zone
- Clearable by user

### Weekly Charge Reports
- Auto-generated every Sunday
- Summary: total charge time, energy used (kWh), charge sessions per zone
- Delivered as FCM push notification + in-app view

### Voice Assistant Shortcuts
- **Siri Shortcuts (iOS):** "Hey Siri, check my dock", "Hey Siri, turn off dock LEDs"
- Configured in app Settings screen

### Ambient Light Auto-Dim
- BH1750 sensor data used to auto-dim LEDs in dark rooms
- Toggle in app to override with fixed brightness

### Onboarding Animation
- Plays on first connection to a new Quad-Dock
- Animated zone introduction showing each zone icon and name
- Skip button available

### iPhone Home Screen Widget
- Shows live dock status per zone (charging / full / empty)
- Tap widget → opens app dashboard
- Small and medium widget sizes

### Dark Mode UI
- Full iOS dark mode support
- App UI adapts to system appearance setting

### Haptic Feedback
- Haptic tap when any device reaches 100% charge
- Haptic on BLE connection established

---

## App Architecture

```
Quad-Dock iOS App (SwiftUI)
    |
    +-- BLE Service
    |       |
    |       +-- Connect to ESP32-C3
    |       +-- Read zone power data (GATT characteristics)
    |       +-- Read LED strip state
    |       +-- Send LED control + theft alert mode commands
    |       +-- RSSI proximity monitoring
    |
    +-- Firebase Service
    |       |
    |       +-- FCM push notification registration
    |       +-- Receive theft alert notifications
    |       +-- Receive weekly report notifications
    |       +-- Receive charge complete notifications
    |
    +-- UI Screens
    |       |
    |       +-- Dashboard Screen
    |       +-- Theft Alert Screen
    |       +-- Alert History Log
    |       +-- Settings Screen (LED, proximity, alert mode, brightness)
    |       +-- Weekly Report Screen
    |       +-- Onboarding Screen (first launch)
    |
    +-- Widget Extension
    |       |
    |       +-- Small / Medium home screen widget
    |       +-- Live dock zone status display
    |
    +-- Local Storage (Core Data / UserDefaults)
            |
            +-- Alert history log
            +-- User preferences
            +-- Onboarding completion flag
```

---

## ESP32-C3 BLE Interface

| GATT Characteristic | Direction | Data |
|---------------------|-----------|------|
| Zone 1 Power | Read/Notify | Voltage, current, watts (JSON) |
| Zone 2 Power | Read/Notify | Voltage, current, watts (JSON) |
| Zone 3 Power | Read/Notify | Voltage, current, watts (JSON) |
| Zone 4 Power | Read/Notify | Voltage, current, watts (JSON) |
| Zone 5 Power | Read/Notify | Voltage, current, watts (JSON) |
| LED Strip Status | Read/Notify | Per-zone color state + brightness (JSON) |
| LED Control | Write | Set brightness override, auto-dim / night mode on/off |
| Device Presence | Read/Notify | Per-zone device detected flag (boolean array) |
| Theft Alert | Notify | Zone index of unexpected removal event |
| Theft Alert Mode | Write | Away / Night / Passive (enum) |
| System Status | Read/Notify | Overall dock status, firmware version |
