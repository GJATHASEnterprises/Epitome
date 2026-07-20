#include "led_controller.h"

#ifdef ARDUINO
#include <FastLED.h>
#else
// Provide the FastLED global stub for non-Arduino builds.
_CFastLEDStub FastLED;
#endif

LedController::LedController()
    : darkMode_(false),
      zoneStatuses_{ZoneStatus::NO_DEVICE, ZoneStatus::NO_DEVICE,
                    ZoneStatus::NO_DEVICE, ZoneStatus::NO_DEVICE},
      currentBrightness_(kMaxBrightness),
      pulseTheta_(0),
      lastPulseMs_(0),
      lastBrightnessPollMs_(0),
      leds_{} {}

void LedController::begin() {
#ifdef ARDUINO
    FastLED.addLeds<WS2812B, LED_DATA_PIN, GRB>(leds_, kTotalLeds)
           .setCorrection(TypicalLEDStrip);
#endif
    updateBrightness();
    applyColors();
}

void LedController::setZoneStatus(int zone, ZoneStatus status) {
    if (zone < 1 || zone > static_cast<int>(kZoneCount)) {
        return;
    }
    zoneStatuses_[zone - 1] = status;
    applyColors();
}

ZoneStatus LedController::getZoneStatus(int zone) const {
    if (zone < 1 || zone > static_cast<int>(kZoneCount)) {
        return ZoneStatus::NO_DEVICE;
    }
    return zoneStatuses_[zone - 1];
}

void LedController::setDarkMode(bool enable) {
    darkMode_ = enable;
    applyColors();
}

bool LedController::isDarkMode() const {
    return darkMode_;
}

void LedController::update() {
    const unsigned long now = millis();

    if (now - lastBrightnessPollMs_ >= kBrightnessPollMs) {
        lastBrightnessPollMs_ = now;
        updateBrightness();
    }

    // Advance the breathing animation only when all zones are full and LEDs are on.
    if (allZonesFull() && !darkMode_) {
        if (now - lastPulseMs_ >= kPulseStepMs) {
            lastPulseMs_ = now;
            pulseTheta_ += 3u;  // Full cycle ~1.71 s at 20 ms steps ((256 / 3) * 20 ms)
            applyColors();
        }
    }
}

bool LedController::allZonesFull() const {
    for (uint8_t i = 0; i < kZoneCount; ++i) {
        if (zoneStatuses_[i] != ZoneStatus::FULL) {
            return false;
        }
    }
    return true;
}

void LedController::applyColors() {
    if (darkMode_) {
        for (uint8_t i = 0; i < kTotalLeds; ++i) {
            leds_[i] = CRGB(0, 0, 0);
        }
#ifdef ARDUINO
        FastLED.show();
#endif
        return;
    }

    if (allZonesFull()) {
        // All zones fully charged: breathe the entire strip green.
        const uint8_t wave   = sin8(pulseTheta_);
        // Keep the green channel between 50 and 255 so the strip never goes fully dark.
        const uint8_t green  = static_cast<uint8_t>(50u + (static_cast<uint32_t>(wave) * 205u) / 255u);
        for (uint8_t i = 0; i < kTotalLeds; ++i) {
            leds_[i] = CRGB(0, green, 0);
        }
    } else {
        for (uint8_t zone = 0; zone < kZoneCount; ++zone) {
            CRGB color;
            switch (zoneStatuses_[zone]) {
                case ZoneStatus::CHARGING:
                    color = CRGB(255, 0, 0);    // Red — actively charging
                    break;
                case ZoneStatus::FULL:
                    color = CRGB(0, 255, 0);    // Green — fully charged
                    break;
                case ZoneStatus::NO_DEVICE:
                default:
                    color = CRGB(0, 0, 0);      // Off — no device detected
                    break;
            }
            for (uint8_t led = 0; led < kLedsPerZone; ++led) {
                leds_[zone * kLedsPerZone + led] = color;
            }
        }
    }

#ifdef ARDUINO
    FastLED.show();
#endif
}

void LedController::updateBrightness() {
    const int raw = analogRead(AMBIENT_LIGHT_PIN);
    uint8_t target;
    if (raw <= static_cast<int>(kAmbientDarkThreshold)) {
        target = kMinBrightness;
    } else if (raw >= static_cast<int>(kAmbientBrightThreshold)) {
        target = kMaxBrightness;
    } else {
        // Linear map: dark threshold → min brightness, bright threshold → max brightness.
        const int      span   = static_cast<int>(kAmbientBrightThreshold - kAmbientDarkThreshold);
        const int      offset = raw - static_cast<int>(kAmbientDarkThreshold);
        const uint32_t range  = kMaxBrightness - kMinBrightness;
        target = static_cast<uint8_t>(
            kMinBrightness + static_cast<uint8_t>((static_cast<uint32_t>(offset) * range) / static_cast<uint32_t>(span))
        );
    }
    if (target != currentBrightness_) {
        currentBrightness_ = target;
#ifdef ARDUINO
        FastLED.setBrightness(currentBrightness_);
#endif
    }
}
