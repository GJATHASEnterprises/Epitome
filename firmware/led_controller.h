#pragma once

#include <cstdint>

#ifdef ARDUINO
#include <Arduino.h>
#else
#define IRAM_ATTR
using byte = uint8_t;
extern unsigned long millis();
extern void pinMode(uint8_t pin, uint8_t mode);
extern void digitalWrite(uint8_t pin, uint8_t value);
extern int digitalRead(uint8_t pin);
extern int digitalPinToInterrupt(uint8_t pin);
extern void attachInterrupt(int interruptNumber, void (*userFunc)(), int mode);
constexpr uint8_t OUTPUT = 0x1;
constexpr uint8_t INPUT_PULLUP = 0x2;
constexpr uint8_t HIGH = 0x1;
constexpr uint8_t LOW = 0x0;
constexpr int FALLING = 0x2;
#endif

enum class ZoneStatus {
    CHARGING,
    FULL,
    NO_DEVICE,
};

class LedController {
public:
    static constexpr uint8_t kZoneCount = 4;

    static constexpr uint8_t ZONE_1_RED_PIN = 2;
    static constexpr uint8_t ZONE_1_GREEN_PIN = 4;
    static constexpr uint8_t ZONE_2_RED_PIN = 5;
    static constexpr uint8_t ZONE_2_GREEN_PIN = 18;
    static constexpr uint8_t ZONE_3_RED_PIN = 19;
    static constexpr uint8_t ZONE_3_GREEN_PIN = 23;
    static constexpr uint8_t ZONE_4_RED_PIN = 25;
    static constexpr uint8_t ZONE_4_GREEN_PIN = 26;
    static constexpr uint8_t DARK_MODE_BUTTON_PIN = 27;

    LedController();

    void begin();
    void setZoneStatus(int zone, ZoneStatus status);
    ZoneStatus getZoneStatus(int zone) const;
    void toggleDarkMode();
    bool isDarkMode() const;
    void pollButton();
    void updateLEDs();

    static void IRAM_ATTR handleDarkModeButtonISR();

private:
    static constexpr unsigned long kDebounceMs = 200;

    static LedController* instance_;
    static volatile bool buttonInterruptFlag_;
    static volatile unsigned long lastInterruptMs_;

    bool darkMode_;
    ZoneStatus zoneStatuses_[kZoneCount];

    void applyZoneColor(uint8_t zoneIndex, bool redOn, bool greenOn);
};
