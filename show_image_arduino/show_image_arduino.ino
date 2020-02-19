#include <Adafruit_GFX.h>
#include <Adafruit_NeoMatrix.h>
#include <Adafruit_NeoPixel.h>
#include "mapping.h"

#define PIN 6

#define BRIGHTNESS 96


#define mw 30
#define mh 22


//Adafruit_NeoMatrix *matrix = new Adafruit_NeoMatrix(mw, mh, PIN,
//  NEO_MATRIX_TOP     + NEO_MATRIX_LEFT +
//  NEO_MATRIX_ROWS + NEO_MATRIX_ZIGZAG,
//  NEO_GRB            + NEO_KHZ800);


Adafruit_NeoPixel pixels = Adafruit_NeoPixel(mw*mh, 6, NEO_MATRIX_TOP + NEO_MATRIX_LEFT + NEO_MATRIX_ROWS + NEO_GRB+ NEO_KHZ800);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
  pixels.begin();
  pixels.setBrightness(100);

  for(int i = 0; i < mw*mh; i++){
    pixels.setPixelColor(i, pixels.Color(bitmap24[i][0], bitmap24[i][1], bitmap24[i][2]));
  }

  pixels.show();
  
  Serial.println("Done");

}

void loop() {
  // put your main code here, to run repeatedly:

}
