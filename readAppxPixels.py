# Written in Python 2

from __future__ import division
from PIL import Image

im = Image.open( './images/256x256bb.jpg')

matrixWidth = 30
matrixHeight = 22

imgWidth = im.width
imgHeight = im.height 

print "imgSize", imgWidth, " x ", imgHeight

wBuffer = round(imgWidth/matrixWidth)
hBuffer = round(imgHeight/matrixHeight)

print "wBuffer:", wBuffer
print "hBuffer:", hBuffer


pixVals = []

xcounter = 0
ycounter = 0

y = 0
while y < imgHeight:
    x = 0
    xcounter = 0
    while x < imgWidth:
        r,g,b = im.getpixel((x,y))
        pixVals.append(r<<16 | g<<8 | b)
        x += wBuffer
        xcounter += 1
    y += hBuffer
    ycounter += 1

print "x counter: ", xcounter
print "y counter: ", ycounter 

 
print "length: ", len(pixVals)
print(pixVals)

mapFile = open('mapping.h', 'w')
mapFile.write("#if defined(__AVR__)\n")
mapFile.write("#include <avr/pgmspace.h>\n")
mapFile.write("#elif defined(__PIC32MX__)\n")
mapFile.write("#define PROGMEM\n")
mapFile.write("#elif defined(__arm__)\n")
mapFile.write("#define PROGMEM\n")
mapFile.write("#endif\n")

mapFile.write("const unsigned short bitmap24["+str(len(pixVals))+"] PROGMEM={\n")

for val in pixVals:
    mapFile.write(str(val) + ", ")

mapFile.write("\n")


mapFile.write("};\n")


