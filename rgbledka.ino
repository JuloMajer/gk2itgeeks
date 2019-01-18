// NeoPixel Ring simple sketch (c) 2013 Shae Erisson
// released under the GPLv3 license to match the rest of the AdaFruit NeoPixel library

#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
  #include <avr/power.h>
#endif

#define PIN            14
#define NUMPIXELS      1

Adafruit_NeoPixel pixels = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

int delayval = 500; // delay for half a second

void setup() {
  pixels.begin(); // This initializes the NeoPixel library.
}

void loop() {
    pixels.setPixelColor(0, pixels.Color(0,150,0));
    pixels.show();
    delay(delayval);
    pixels.setPixelColor(0,pixels.Color(150,0,0));
    pixels.show();
    delay(delayval);
    pixels.setPixelColor(0,pixels.Color(0,0,150));
    pixels.show();
    delay(delayval);
}
