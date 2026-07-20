# Quad Device Dock — Wiring & Schematic Notes

---

## System Overview

```
[Wall Outlet]
     |
[140W–200W GaN Adapter]
     |
[USB-C PD Input] --> [PD Trigger IC (CH224K)] --> [Main Power Rail: 12V or 20V]
                                                        |
               +----------------------------------------+-------------------+
               |              |              |              |               |
        [Qi TX 1]      [Qi TX 2]     [Watch Puck]   [USB-C PD Out]   [LED/Button IO]
        Zone 1          Zone 2        Zone 3          Zone 4          Status + Control
          |               |               |               |               |
       [INA219]        [INA219]       [INA219]        [INA219]      [GPIO Resistors]
          |               |               |               |               |
          +---------------+---------------+---------------+---------------+
                                  |
                            [ESP32 I2C Bus]
                                  |
                    [ESP32-WROOM-32 Microcontroller]
                         |               |              |
                    [WiFi/BT]      [Zone LEDs x8]   [Dark Mode Button]
                         |
                   [Mobile App]
```

---

## Power Rail Design

| Rail | Voltage | Used For |
|------|---------|----------|
| Main input | 20V (from PD) | Stepped down as needed |
| Qi coil supply | 12V | Wireless TX modules |
| Watch puck | 5V | Apple Watch module |
| USB-C PD out | 5V–20V (negotiated) | Laptop/tablet |
| ESP32 + logic | 3.3V | MCU, sensors, LEDs, button input |

---

## ESP32 Pin Assignments (Draft)

| GPIO Pin | Function |
|----------|----------|
| GPIO 21 | I2C SDA (power monitors) |
| GPIO 22 | I2C SCL (power monitors) |
| GPIO 2 | Zone 1 red LED |
| GPIO 4 | Zone 1 green LED |
| GPIO 5 | Zone 2 red LED |
| GPIO 18 | Zone 2 green LED |
| GPIO 19 | Zone 3 red LED |
| GPIO 23 | Zone 3 green LED |
| GPIO 25 | Zone 4 red LED |
| GPIO 26 | Zone 4 green LED |
| GPIO 27 | Dark mode button input |
| GPIO 34 | Thermistor Zone 1 (ADC) |
| GPIO 35 | Thermistor Zone 2 (ADC) |
| GPIO 32 | Thermistor Zone 3 (ADC) |
| GPIO 33 | Thermistor Zone 4 (ADC) |

GPIO 27 is used for the dark mode button because it is a stable digital-capable GPIO that does not conflict with the four LED outputs or the reserved ADC inputs already allocated for per-zone thermistors.

---

## LED Hardware
- Use either compact RGB LEDs configured only for red/green states or paired red/green LEDs per zone.
- Mount each LED pair underneath a **frosted diffuser strip** at the front edge of the corresponding zone.
- Add current-limiting resistors sized for 3.3V GPIO drive and desired brightness.
- Route LED grounds back to the logic ground plane to avoid noise coupling into the INA219 sense paths.
- Dark mode button should pull the GPIO low when pressed, using the ESP32 internal pull-up and firmware debounce.

---

## LED Behavior Logic
- **Red solid:** Device is charging.
- **Green solid:** Device is full.
- **Off:** No device detected.
- **Dark mode:** All zone LEDs are forced off until the button or app toggles them back on.

The firmware implementation for this behavior lives in:
- `firmware/led_controller.h`
- `firmware/led_controller.cpp`

The controller exposes:
- `setZoneStatus(int zone, ZoneStatus status)`
- `toggleDarkMode()`
- `isDarkMode()`
- `updateLEDs()`
- ISR-driven dark mode button handling with debounce

---

## Key ICs

### CH224K — USB-C PD Trigger
- Negotiates input voltage from PD adapter
- Set resistors on CFG pins to select 20V input
- Datasheet: search LCSC part C2988369

### INA219 — Current/Voltage Monitor
- I2C interface to ESP32
- Measures per-zone current draw and voltage
- Address pins (A0/A1) set unique I2C addresses per zone
- Typical shunt resistor: 0.1 ohm

### ESP32-WROOM-32
- Main MCU
- WiFi 802.11 b/g/n + Bluetooth 4.2
- Flash: 4MB minimum
- Power via 3.3V LDO from main rail

---

## Safety Wiring Notes
- Add **polyfuse or resettable fuse** on each zone output
- Add **TVS diode** on USB-C output for surge protection
- Thermistors connected to ESP32 ADC pins with voltage divider (10K + NTC 10K)
- ESP32 triggers zone shutoff via GPIO if temp exceeds threshold (set in firmware at ~45°C)
- Add **bulk capacitor** (470–1000uF) on main rail for stability

---

## PCB Notes
- Single 4-layer PCB recommended for clean power planes
- Keep Qi coil traces wide (2mm minimum for coil supply)
- Separate analog ground (sensors) from power ground
- Use JLCPCB standard 4-layer stackup
- Place INA219s close to their respective load zones
- ESP32 antenna must be near board edge with no copper pour underneath
