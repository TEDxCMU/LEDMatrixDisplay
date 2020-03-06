#include <Adafruit_GFX.h>
#include <Adafruit_NeoMatrix.h>
#include <Adafruit_NeoPixel.h>
#include "mapping.h"

//#define 1STHALF_PIN 6
//#define 2NDHALF_PIN 5

#define BRIGHTNESS 96


#define mw 30
#define mh 22


//Adafruit_NeoMatrix *matrix = new Adafruit_NeoMatrix(mw, mh, PIN,
//  NEO_MATRIX_TOP     + NEO_MATRIX_LEFT +
//  NEO_MATRIX_ROWS + NEO_MATRIX_ZIGZAG,
//  NEO_GRB            + NEO_KHZ800);


Adafruit_NeoPixel firsthalfpixels = Adafruit_NeoPixel(mw*mh, 5, NEO_MATRIX_TOP + NEO_MATRIX_LEFT + NEO_MATRIX_ROWS + NEO_GRB+ NEO_KHZ800);
Adafruit_NeoPixel secondhalfpixels = Adafruit_NeoPixel(mw*mh, 6, NEO_MATRIX_TOP + NEO_MATRIX_LEFT + NEO_MATRIX_ROWS + NEO_GRB+ NEO_KHZ800);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
  firsthalfpixels.begin();
  secondhalfpixels.begin();
  firsthalfpixels.setBrightness(50);
  secondhalfpixels.setBrightness(50);
  

//  for(int i = 0; i < mw*mh; i++){
//    //Serial.println((uint16_t)pgm_read_byte(&bitmapfirsthalf[i][1]));
//    
//    firsthalfpixels.setPixelColor(i, firsthalfpixels.Color((uint16_t)pgm_read_byte(&bitmapfirsthalf[i][0]), (uint16_t)pgm_read_byte(&bitmapfirsthalf[i][1]), (uint16_t)pgm_read_byte(&bitmapfirsthalf[i][2])));
//    secondhalfpixels.setPixelColor(i, secondhalfpixels.Color((uint16_t)pgm_read_byte(&bitmapsecondhalf[i][0]), (uint16_t)pgm_read_byte(&bitmapsecondhalf[i][1]), (uint16_t)pgm_read_byte(&bitmapsecondhalf[i][2])));
//  }
//
//  firsthalfpixels.show();
//  secondhalfpixels.show();
//  
//  Serial.println("Done");

}

void loop() {

  // First frame
  for(int i = 0; i < mw*mh; i++){
    //Serial.println((uint16_t)pgm_read_byte(&bitmapfirsthalf[i][1]));
    
    firsthalfpixels.setPixelColor(i, firsthalfpixels.Color((uint16_t)pgm_read_byte(&frame1firsthalf[i][0]), (uint16_t)pgm_read_byte(&frame1firsthalf[i][1]), (uint16_t)pgm_read_byte(&frame1firsthalf[i][2])));
    secondhalfpixels.setPixelColor(i, secondhalfpixels.Color((uint16_t)pgm_read_byte(&frame1secondhalf[i][0]), (uint16_t)pgm_read_byte(&frame1secondhalf[i][1]), (uint16_t)pgm_read_byte(&frame1secondhalf[i][2])));
  }

  firsthalfpixels.show();
  secondhalfpixels.show();
  
  Serial.println("Done w 1st frame");

  delay(2000);

  // Second frame
  for(int i = 0; i < mw*mh; i++){
    //Serial.println((uint16_t)pgm_read_byte(&bitmapfirsthalf[i][1]));
    
    firsthalfpixels.setPixelColor(i, firsthalfpixels.Color((uint16_t)pgm_read_byte(&frame2firsthalf[i][0]), (uint16_t)pgm_read_byte(&frame2firsthalf[i][1]), (uint16_t)pgm_read_byte(&frame2firsthalf[i][2])));
    secondhalfpixels.setPixelColor(i, secondhalfpixels.Color((uint16_t)pgm_read_byte(&frame2secondhalf[i][0]), (uint16_t)pgm_read_byte(&frame2secondhalf[i][1]), (uint16_t)pgm_read_byte(&frame2secondhalf[i][2])));
  }

  firsthalfpixels.show();
  secondhalfpixels.show();
  
  Serial.println("Done w 1st frame");

  delay(2000);


  // Third frame
  for(int i = 0; i < mw*mh; i++){
    //Serial.println((uint16_t)pgm_read_byte(&bitmapfirsthalf[i][1]));
    
    firsthalfpixels.setPixelColor(i, firsthalfpixels.Color((uint16_t)pgm_read_byte(&frame3firsthalf[i][0]), (uint16_t)pgm_read_byte(&frame3firsthalf[i][1]), (uint16_t)pgm_read_byte(&frame3firsthalf[i][2])));
    secondhalfpixels.setPixelColor(i, secondhalfpixels.Color((uint16_t)pgm_read_byte(&frame3secondhalf[i][0]), (uint16_t)pgm_read_byte(&frame3secondhalf[i][1]), (uint16_t)pgm_read_byte(&frame3secondhalf[i][2])));
  }

  firsthalfpixels.show();
  secondhalfpixels.show();
  
  Serial.println("Done w 1st frame");

  delay(2000);


  // Fourth frame
  for(int i = 0; i < mw*mh; i++){
    //Serial.println((uint16_t)pgm_read_byte(&bitmapfirsthalf[i][1]));
    
    firsthalfpixels.setPixelColor(i, firsthalfpixels.Color((uint16_t)pgm_read_byte(&frame4firsthalf[i][0]), (uint16_t)pgm_read_byte(&frame4firsthalf[i][1]), (uint16_t)pgm_read_byte(&frame4firsthalf[i][2])));
    secondhalfpixels.setPixelColor(i, secondhalfpixels.Color((uint16_t)pgm_read_byte(&frame4secondhalf[i][0]), (uint16_t)pgm_read_byte(&frame4secondhalf[i][1]), (uint16_t)pgm_read_byte(&frame4secondhalf[i][2])));
  }

  firsthalfpixels.show();
  secondhalfpixels.show();
  
  Serial.println("Done w 1st frame");

  delay(2000);


  

}
