# Epitome Penta — Companion App Specification

---

## App Name
Epitome Penta

## Platform
- **iOS (iPhone)** — primary platform
- Built with **Swift / SwiftUI**
- Hardware remains fully functional without the app for iOS and Android users
- Android companion app is optional future scope; charging compatibility is already universal at hardware level

## Communication
- **Bluetooth Low Energy (BLE)** — primary, local connection
- **Firebase** — push notifications (FCM)
- ESP32-C3 acts as BLE peripheral

---

## Features

### Dashboard
- Real-time charge status per zone
- Zone icons: 📱 PHONE, 🎧 BUDS/PHONE, ⌚ WATCH, 💻 LAPTOP, 📲 TABLET
- Per-zone status: charging / full / empty
- Zone compatibility labels: Qi universal / USB-C universal / watch dual-mode

### Device Detection
- Zone state inferred by per-zone power draw thresholds
- Zone 3 reports **dual-mode source** (`puck` or `qi_watch`)
- A dedicated **Zone 3 mode** field is surfaced in UI and telemetry exports

### LED Control
- LED enable/disable
- Ambient light auto-dim toggle
- Manual brightness override

### Theft Alert
Three alert modes: Away / Night / Passive.

### BLE Proximity Detection
- Distance threshold settings

### Notifications (Firebase FCM)
- Theft alert
- Charge complete
- Weekly report

### Alert History Log
- Timestamped events per zone

### Weekly Charge Reports
- Total charge time + energy summary

### Voice Assistant Shortcuts
- Siri shortcuts for status and LED controls

### Ambient Light Auto-Dim
- BH1750-driven LED dimming

### Onboarding Animation
- Introduces updated zone map including captive cables and watch dual-mode charging

### iPhone Home Screen Widget
- Live per-zone state

### Dark Mode UI
- Full iOS dark mode support

### Haptic Feedback
- Zone complete / connect feedback

---

## App Architecture

```
Epitome Penta iOS App (SwiftUI)
    |
    +-- BLE Service
    |    +-- Zone telemetry read (Z1..Z5)
    |    +-- Zone 3 source-mode read (puck / qi_watch)
    |    +-- LED control + alert mode writes
    |
    +-- Firebase Service
    +-- UI Screens
    +-- Widget Extension
    +-- Local Storage
```

---

## ESP32-C3 BLE Interface

| GATT Characteristic | Direction | Data |
|---------------------|-----------|------|
| Zone 1 Power | Read/Notify | Voltage/current/watts |
| Zone 2 Power | Read/Notify | Voltage/current/watts (**15W max**) |
| Zone 3 Power | Read/Notify | Voltage/current/watts (**5W max**) |
| Zone 3 Mode | Read/Notify | `puck` or `qi_watch` |
| Zone 4 Power | Read/Notify | Voltage/current/watts |
| Zone 5 Power | Read/Notify | Voltage/current/watts |
| LED Strip Status | Read/Notify | Per-zone color + brightness |
| LED Control | Write | LED config |
| Device Presence | Read/Notify | Per-zone booleans |
| Theft Alert | Notify | Zone index |
| System Status | Read/Notify | Firmware version + thermal flags |
