from __future__ import division
from PIL import Image

origim = Image.open( './images/doge.jpg')


# matrixWidth = 30
# matrixHeight = 22

matrixWidth = 60
matrixHeight = 22


im = origim.resize((matrixWidth, matrixHeight))

imgWidth = im.width
imgHeight = im.height

print "imgSize", imgWidth, " x ", imgHeight

im.save('images/resizedImage.jpg', "JPEG", optimize=True)


pixVals1 = []
# Populate first half array
for y in range(0, imgHeight):
    #rowVals = []
    if y % 2 == 0:
        for x in range(0, int(imgWidth/2)):
            r,g,b = im.getpixel((x,y))
            pixVals1.append([r, g, b])
    else:
        for x in range((int(imgWidth/2))-1, -1, -1):
            r,g,b = im.getpixel((x,y))
            pixVals1.append([r, g, b])


pixVals2 = []
# Populate second half array
for y in range(0, imgHeight):
    #rowVals = []
    if y % 2 == 0:
        counter = 0
        for x in range(int(imgWidth/2), imgWidth):
            r,g,b = im.getpixel((x,y))
            pixVals2.append([r, g, b])
            counter+=1
        print"!!!!!!!!!!!", counter
    else:
        counter = 0
        for x in range(imgWidth-1, int(imgWidth/2) - 1, -1):
            r,g,b = im.getpixel((x,y))
            pixVals2.append([r, g, b])
            counter+=1
        print"!!!!!!!!!!!", counter

print "Len of pixVals1:", len(pixVals1)
print "Len of pixVals2:", len(pixVals2)
print pixVals1
print "****************************"
print pixVals2

mapFile = open('./show_image_arduino/mapping.h', 'w')
mapFile.write("#include <avr/pgmspace.h>\n")
mapFile.write("#if defined(__AVR__)\n")
mapFile.write("#elif defined(__PIC32MX__)\n")
mapFile.write("#define PROGMEM\n")
mapFile.write("#elif defined(__arm__)\n")
mapFile.write("#define PROGMEM\n")
mapFile.write("#endif\n")

mapFile.write("const byte bitmapfirsthalf["+str(len(pixVals1))+"][3] PROGMEM={\n")

for pixSet in pixVals1:
    mapFile.write('{')
    for pixC in pixSet:
        mapFile.write(str(pixC) + ", ")
    mapFile.write('},')

mapFile.write("\n")
mapFile.write("};\n")

mapFile.write("const byte bitmapsecondhalf["+str(len(pixVals2))+"][3] PROGMEM={\n")

for pixSet in pixVals2:
    mapFile.write('{')
    for pixC in pixSet:
        mapFile.write(str(pixC) + ", ")
    mapFile.write('},')

mapFile.write("\n")
mapFile.write("};\n")