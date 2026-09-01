/**
 * Epitome Step — LED Controller Implementation
 * ATtiny85, FastLED library.
 *
 * Compile-time model selection via led_controller.h.
 * Flash MODEL_WALNUT binary to Walnut units.
 * Flash MODEL_OBSIDIAN binary to Obsidian units.
 */

#include "led_controller.h"
#include <FastLED.h>
#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/wdt.h>

// ── LED array ──────────────────────────────────────────────────────────────────
static CRGB leds[LED_COUNT];

// ── State ──────────────────────────────────────────────────────────────────────
static uint32_t tick_counter = 0;          // seconds since power-on (noon reference)
static uint8_t  current_brightness = LED_BRIGHTNESS;
static uint8_t  is_night = 0;
static uint8_t  pulse_active = 0;
static uint8_t  pulse_ticks = 0;

#ifdef MODEL_OBSIDIAN
static volatile uint8_t mode_index = 0;   // current RGB mode (0–7)
static volatile uint8_t mode_changed = 0; // set in ISR, cleared in led_update
#endif

// ── Forward declarations ───────────────────────────────────────────────────────
static void apply_colour(void);
static void check_soft_cap(void);
static void check_night_mode(void);

// ── Watchdog ISR (1 Hz tick) ───────────────────────────────────────────────────
ISR(WDT_vect) {
    led_tick();
}

// ── INT0 ISR — Obsidian mode button (PB4 → INT0 not directly, use PCINT) ───────
#ifdef MODEL_OBSIDIAN
ISR(PCINT0_vect) {
    // Only act on falling edge (button press, active LOW)
    if (!(PINB & (1 << PIN_MODE_BTN))) {
        led_next_mode();
    }
}
#endif

// ── Initialisation ─────────────────────────────────────────────────────────────
void led_init(void) {
    // Configure zone detect pins as inputs with pull-up
    DDRB  &= ~((1 << PIN_ZONE1) | (1 << PIN_ZONE2) | (1 << PIN_ZONE3));
    PORTB |=  ((1 << PIN_ZONE1) | (1 << PIN_ZONE2) | (1 << PIN_ZONE3));

#ifdef MODEL_WALNUT
    // No button on Walnut
    FastLED.addLeds<WS2811, PIN_LED_DATA, RGB>(leds, LED_COUNT);
#endif

#ifdef MODEL_OBSIDIAN
    // Mode button input with pull-up
    DDRB  &= ~(1 << PIN_MODE_BTN);
    PORTB |=  (1 << PIN_MODE_BTN);

    // Pin change interrupt on PB4 for mode button
    GIMSK  |= (1 << PCIE);
    PCMSK  |= (1 << PCINT4);

    FastLED.addLeds<WS2812B, PIN_LED_DATA, GRB>(leds, LED_COUNT);
#endif

    FastLED.setBrightness(LED_BRIGHTNESS);

    // Watchdog timer for 1-second ticks
    cli();
    MCUSR  &= ~(1 << WDRF);
    WDTCR  |=  (1 << WDCE) | (1 << WDE);
    WDTCR   =  (1 << WDIE) | (1 << WDP2) | (1 << WDP1); // ~1 second
    sei();

    apply_colour();
    FastLED.show();
}

// ── Tick handler (called from WDT ISR, once per second) ───────────────────────
void led_tick(void) {
    tick_counter++;
    if (tick_counter >= TICKS_PER_DAY) {
        tick_counter = 0;  // roll over at midnight+12h
    }
    check_night_mode();
    check_soft_cap();

    if (pulse_active && pulse_ticks > 0) {
        pulse_ticks--;
        if (pulse_ticks == 0) {
            pulse_active = 0;
            current_brightness = is_night ? 0 : LED_BRIGHTNESS;
        }
    }
}

// ── Zone pulse ─────────────────────────────────────────────────────────────────
void led_pulse_zone(uint8_t zone) {
    (void)zone;  // same pulse for all zones
    if (is_night) return;
    pulse_active = 1;
    pulse_ticks  = 2;  // ~200 ms bright pulse (2 ticks at 1Hz — small ATtiny tick)
    current_brightness = 255;
}

// ── Obsidian: cycle mode ───────────────────────────────────────────────────────
#ifdef MODEL_OBSIDIAN
void led_next_mode(void) {
    mode_index = (mode_index + 1) % RGB_MODE_COUNT;
    mode_changed = 1;
}
#endif

// ── Main update loop (call as frequently as possible from main loop) ───────────
void led_update(void) {
    // Check zone detect pins for device presence
    uint8_t z1 = (PINB >> PIN_ZONE1) & 1;
    uint8_t z2 = (PINB >> PIN_ZONE2) & 1;
    uint8_t z3 = (PINB >> PIN_ZONE3) & 1;

    // Pulse on newly detected device (simple edge: could add debounce if needed)
    static uint8_t last_z1 = 0, last_z2 = 0, last_z3 = 0;
    if (z1 && !last_z1) led_pulse_zone(1);
    if (z2 && !last_z2) led_pulse_zone(2);
    if (z3 && !last_z3) led_pulse_zone(3);
    last_z1 = z1; last_z2 = z2; last_z3 = z3;

#ifdef MODEL_OBSIDIAN
    if (mode_changed) {
        mode_changed = 0;
        apply_colour();
    }
#endif

    FastLED.setBrightness(current_brightness);
    FastLED.show();
}

// ── Colour application ─────────────────────────────────────────────────────────
static void apply_colour(void) {
#ifdef MODEL_WALNUT
    for (uint8_t i = 0; i < LED_COUNT; i++) {
        leds[i] = CRGB(WARM_R, WARM_G, WARM_B);
    }
#endif

#ifdef MODEL_OBSIDIAN
    uint8_t r = RGB_MODES[mode_index][0];
    uint8_t g = RGB_MODES[mode_index][1];
    uint8_t b = RGB_MODES[mode_index][2];
    for (uint8_t i = 0; i < LED_COUNT; i++) {
        leds[i] = CRGB(r, g, b);
    }
#endif
}

// ── Night mode check ───────────────────────────────────────────────────────────
static void check_night_mode(void) {
    uint8_t was_night = is_night;

    // Night window: tick_counter [NIGHT_START_TICK, TICKS_PER_DAY) or [0, NIGHT_END_TICK)
    if (tick_counter >= NIGHT_START_TICK || tick_counter < NIGHT_END_TICK) {
        is_night = 1;
    } else {
        is_night = 0;
    }

    if (is_night != was_night) {
        current_brightness = is_night ? 0 : LED_BRIGHTNESS;
        apply_colour();
        FastLED.setBrightness(current_brightness);
        FastLED.show();
    }
}

// ── Soft cap check ─────────────────────────────────────────────────────────────
static void check_soft_cap(void) {
    if (is_night) return;

    uint8_t z1 = (PINB >> PIN_ZONE1) & 1;
    uint8_t z2 = (PINB >> PIN_ZONE2) & 1;
    uint8_t z3 = (PINB >> PIN_ZONE3) & 1;

    // Estimated wireless draw: zone1=20W zone2=5W zone3=5W = 30W max wireless
    // USB-C always assumed present. Dim LEDs if all three zones active (max wireless load).
    uint8_t total_wireless = (z1 * 20) + (z2 * 5) + (z3 * 5);
    if (total_wireless >= 30) {
        current_brightness = LED_DIM_CAP;
    } else {
        if (!pulse_active) {
            current_brightness = LED_BRIGHTNESS;
        }
    }
}

// ── Arduino-style entry points (if building with Arduino IDE) ─────────────────
#ifdef ARDUINO
void setup(void) {
    led_init();
}

void loop(void) {
    led_update();
    // Delay to avoid hammering FastLED.show() — 50 ms (20 Hz)
    delay(50);
}
#endif
