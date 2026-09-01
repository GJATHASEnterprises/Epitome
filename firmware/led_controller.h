/**
 * Epitome Step — LED Controller
 * ATtiny85 firmware for both Walnut and Obsidian models.
 *
 * Select model at compile time:
 *   #define MODEL_WALNUT    — WS2811, warm white, no button
 *   #define MODEL_OBSIDIAN  — WS2812B, RGB modes, rear button on PB4
 *
 * One of the two must be defined. Compile and flash separately for each model.
 */

#ifndef LED_CONTROLLER_H
#define LED_CONTROLLER_H

#include <stdint.h>

// ── Model selection ────────────────────────────────────────────────────────────
// Uncomment exactly ONE of these before flashing:
#define MODEL_WALNUT
// #define MODEL_OBSIDIAN

#if defined(MODEL_WALNUT) && defined(MODEL_OBSIDIAN)
  #error "Define MODEL_WALNUT or MODEL_OBSIDIAN — not both."
#endif
#if !defined(MODEL_WALNUT) && !defined(MODEL_OBSIDIAN)
  #error "Define MODEL_WALNUT or MODEL_OBSIDIAN before compiling."
#endif

// ── Pin assignments ────────────────────────────────────────────────────────────
#define PIN_LED_DATA    0  // PB0 — WS2811 / WS2812B data out
#define PIN_ZONE1       1  // PB1 — Zone 1 detect (HIGH = phone present)
#define PIN_ZONE2       2  // PB2 — Zone 2 detect (HIGH = buds present)
#define PIN_ZONE3       3  // PB3 — Zone 3 detect (HIGH = watch present)
#define PIN_MODE_BTN    4  // PB4 — Obsidian only: RGB mode button (active LOW)

// ── LED strip config ───────────────────────────────────────────────────────────
#define LED_COUNT       8
#define LED_BRIGHTNESS  200  // 0–255 (daytime default)
#define LED_DIM_CAP     80   // brightness when soft power cap active

// ── Night mode ─────────────────────────────────────────────────────────────────
// Timer-based: 1 tick/sec via WDT. Initialises at 12:00 (noon).
// Night = 23:00 – 07:00 (8 hours off). 86400 ticks/day.
#define TICKS_PER_DAY    86400UL
#define NIGHT_START_TICK 39600UL  // 11 * 3600 ticks from noon = 23:00
#define NIGHT_END_TICK   54000UL  // 15 * 3600 ticks from noon = 07:00 next day

// ── Walnut model ───────────────────────────────────────────────────────────────
#ifdef MODEL_WALNUT
  // Warm white only (#FFD6A0)
  #define WARM_R  255
  #define WARM_G  214
  #define WARM_B  160
#endif

// ── Obsidian model ─────────────────────────────────────────────────────────────
#ifdef MODEL_OBSIDIAN
  #define RGB_MODE_COUNT  8
  // Modes: 0=Blue 1=Purple 2=Green 3=Red 4=Cyan 5=Yellow 6=White 7=Off
  // Stored as {R, G, B} triples
  static const uint8_t RGB_MODES[8][3] = {
    {  51, 153, 255},  // 0 Blue
    { 153,  51, 255},  // 1 Purple
    {  51, 204, 102},  // 2 Green
    { 255,  51,  51},  // 3 Red
    {   0, 255, 255},  // 4 Cyan
    { 255, 255,   0},  // 5 Yellow
    { 255, 255, 255},  // 6 White
    {   0,   0,   0},  // 7 Off
  };
#endif

// ── Public API ─────────────────────────────────────────────────────────────────
void led_init(void);
void led_update(void);
void led_pulse_zone(uint8_t zone);   // zone: 1, 2, or 3
void led_tick(void);                 // call once per second from WDT ISR

#ifdef MODEL_OBSIDIAN
void led_next_mode(void);            // cycle to next RGB mode (called from button ISR)
#endif

#endif /* LED_CONTROLLER_H */
