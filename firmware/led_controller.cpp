#include "led_controller.h"

namespace {
constexpr uint8_t kRedPins[LedController::kZoneCount] = {
    LedController::ZONE_1_RED_PIN,
    LedController::ZONE_2_RED_PIN,
    LedController::ZONE_3_RED_PIN,
    LedController::ZONE_4_RED_PIN,
};

constexpr uint8_t kGreenPins[LedController::kZoneCount] = {
    LedController::ZONE_1_GREEN_PIN,
    LedController::ZONE_2_GREEN_PIN,
    LedController::ZONE_3_GREEN_PIN,
    LedController::ZONE_4_GREEN_PIN,
};
}  // namespace

LedController* LedController::instance_ = nullptr;
volatile bool LedController::buttonInterruptFlag_ = false;
volatile unsigned long LedController::lastInterruptMs_ = 0;

LedController::LedController() : darkMode_(false), zoneStatuses_{
    ZoneStatus::NO_DEVICE,
    ZoneStatus::NO_DEVICE,
    ZoneStatus::NO_DEVICE,
    ZoneStatus::NO_DEVICE,
} {}

void LedController::begin() {
    instance_ = this;

    for (uint8_t index = 0; index < kZoneCount; ++index) {
        pinMode(kRedPins[index], OUTPUT);
        pinMode(kGreenPins[index], OUTPUT);
        digitalWrite(kRedPins[index], LOW);
        digitalWrite(kGreenPins[index], LOW);
    }

    pinMode(DARK_MODE_BUTTON_PIN, INPUT_PULLUP);
    attachInterrupt(digitalPinToInterrupt(DARK_MODE_BUTTON_PIN), LedController::handleDarkModeButtonISR, FALLING);

    updateLEDs();
}

void LedController::setZoneStatus(int zone, ZoneStatus status) {
    if (zone < 1 || zone > static_cast<int>(kZoneCount)) {
        return;
    }

    zoneStatuses_[zone - 1] = status;
    updateLEDs();
}

ZoneStatus LedController::getZoneStatus(int zone) const {
    if (zone < 1 || zone > static_cast<int>(kZoneCount)) {
        return ZoneStatus::NO_DEVICE;
    }

    return zoneStatuses_[zone - 1];
}

void LedController::toggleDarkMode() {
    darkMode_ = !darkMode_;
    updateLEDs();
}

bool LedController::isDarkMode() const {
    return darkMode_;
}

void LedController::pollButton() {
    if (!buttonInterruptFlag_) {
        return;
    }

    buttonInterruptFlag_ = false;
    toggleDarkMode();
}

void LedController::updateLEDs() {
    for (uint8_t index = 0; index < kZoneCount; ++index) {
        if (darkMode_) {
            setZoneLEDs(index, false, false);
            continue;
        }

        switch (zoneStatuses_[index]) {
            case ZoneStatus::CHARGING:
                setZoneLEDs(index, true, false);
                break;
            case ZoneStatus::FULL:
                setZoneLEDs(index, false, true);
                break;
            case ZoneStatus::NO_DEVICE:
            default:
                setZoneLEDs(index, false, false);
                break;
        }
    }
}

void IRAM_ATTR LedController::handleDarkModeButtonISR() {
    if (instance_ == nullptr) {
        return;
    }

    const unsigned long now = millis();
    if (now - lastInterruptMs_ < kDebounceMs) {
        return;
    }

    lastInterruptMs_ = now;
    buttonInterruptFlag_ = true;
}

void LedController::setZoneLEDs(uint8_t zoneIndex, bool redOn, bool greenOn) {
    digitalWrite(kRedPins[zoneIndex], redOn ? HIGH : LOW);
    digitalWrite(kGreenPins[zoneIndex], greenOn ? HIGH : LOW);
}
