#pragma once

#include <cstdint>

#ifdef ARDUINO
#include <Arduino.h>
#include <FastLED.h>
#else
#define IRAM_ATTR
using byte = uint8_t;
extern unsigned long millis();
extern int analogRead(uint8_t pin);

// Minimal CRGB stub for non-Arduino builds (unit testing)
struct CRGB {
    uint8_t r, g, b;
    constexpr CRGB() : r(0), g(0), b(0) {}
    constexpr CRGB(uint8_t r, uint8_t g, uint8_t b) : r(r), g(g), b(b) {}
};

// Minimal FastLED global stub
struct _CFastLEDStub {
    void setBrightness(uint8_t) {}
    void show() {}
};
extern _CFastLEDStub FastLED;

// sin8: maps 0–255 input angle to 0–255 sinusoidal output.
// Stub uses a triangular approximation sufficient for unit tests.
inline uint8_t sin8(uint8_t theta) {
    return theta < 128u
        ? static_cast<uint8_t>(theta * 2u)
        : static_cast<uint8_t>((255u - theta) * 2u);
}
#endif

enum class ZoneStatus {
    CHARGING,
    FULL,
    NO_DEVICE,
};

class LedController {
public:
    static constexpr uint8_t kZoneCount = 4;
    // Number of WS2812B LEDs allocated per zone on the front-edge strip.
    static constexpr uint8_t kLedsPerZone = 4;
    static constexpr uint8_t kTotalLeds = kZoneCount * kLedsPerZone;

    // WS2812B single-wire data pin connected to the front-edge LED strip.
    static constexpr uint8_t LED_DATA_PIN = 12;
    // TEMT6000 analog output pin (ADC1_CH0 on ESP32, input only, no attenuation needed).
    static constexpr uint8_t AMBIENT_LIGHT_PIN = 36;

    LedController();

    void begin();
    // Public zone numbering is 1–4 to match user-facing zone labels in the dock docs and app.
    void setZoneStatus(int zone, ZoneStatus status);
    ZoneStatus getZoneStatus(int zone) const;
    // Enable or disable dark mode (LEDs forced off). Called by the app over BLE/WiFi.
    // When dark mode is active the ambient light sensor is still read but has no effect.
    void setDarkMode(bool enable);
    bool isDarkMode() const;
    // Must be called from the main loop on every iteration to advance the breathing
    // pulse animation and periodically re-sample the ambient light sensor.
    void update();

private:
    static constexpr uint8_t  kMinBrightness         = 10;
    static constexpr uint8_t  kMaxBrightness          = 200;
    // ESP32 12-bit ADC range: 0–4095.
    // Below kAmbientDarkThreshold the room is considered dark → minimum brightness.
    // Above kAmbientBrightThreshold the room is fully lit → maximum brightness.
    static constexpr uint16_t kAmbientDarkThreshold   = 300;
    static constexpr uint16_t kAmbientBrightThreshold = 2500;
    // How often (ms) to advance the breathing pulse one step.
    static constexpr unsigned long kPulseStepMs       = 20;
    // How often (ms) to re-sample the ambient light sensor.
    static constexpr unsigned long kBrightnessPollMs  = 500;

    bool          darkMode_;
    ZoneStatus    zoneStatuses_[kZoneCount];
    uint8_t       currentBrightness_;
    // Angle (0–255) fed into sin8() to produce the breathing effect.
    uint8_t       pulseTheta_;
    unsigned long lastPulseMs_;
    unsigned long lastBrightnessPollMs_;

    CRGB leds_[kTotalLeds];

    bool allZonesFull() const;
    // Recompute zone colors and push the updated buffer to the WS2812B strip.
    void applyColors();
    // Read the ambient light sensor and update FastLED global brightness accordingly.
    void updateBrightness();
};
