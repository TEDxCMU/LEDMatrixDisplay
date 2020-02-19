from __future__ import division
from PIL import Image

# origim = Image.open( './images/256x256bb.jpg')
origim = Image.open( './images/mario.jpg')


# matrixWidth = 30
# matrixHeight = 22

matrixWidth = 30
matrixHeight = 22


im = origim.resize((matrixWidth, matrixHeight))

imgWidth = im.width
imgHeight = im.height

print "imgSize", imgWidth, " x ", imgHeight

im.save('images/resizedImage.jpg', "JPEG", optimize=True)



# wBuffer = round(imgWidth/matrixWidth)
# hBuffer = round(imgHeight/matrixHeight)

# print "wBuffer:", wBuffer
# print "hBuffer:", hBuffer



pixVals = []


for y in range(0, imgHeight):
    #rowVals = []
    if y % 2 == 0:
        for x in range(0, imgWidth):
            r,g,b = im.getpixel((x,y))
            pixVals.append([r, g, b])
            #pixVals.append(r<<16 | g<<8 | b)
    else:
        for x in range(imgWidth-1, -1, -1):
            r,g,b = im.getpixel((x,y))
            pixVals.append([r, g, b])
            #rowVals.append(r<<16 | g<<8 | b)
    #pixVals.append(rowVals)

print len(pixVals)
print pixVals

mapFile = open('./show_image_arduino/mapping.h', 'w')
mapFile.write("#if defined(__AVR__)\n")
mapFile.write("#include <avr/pgmspace.h>\n")
mapFile.write("#elif defined(__PIC32MX__)\n")
mapFile.write("#define PROGMEM\n")
mapFile.write("#elif defined(__arm__)\n")
mapFile.write("#define PROGMEM\n")
mapFile.write("#endif\n")

mapFile.write("const unsigned short bitmap24["+str(len(pixVals))+"][3] ={\n")

for pixSet in pixVals:
    mapFile.write('{')
    for pixC in pixSet:
        mapFile.write(str(pixC) + ", ")
    mapFile.write('},')

mapFile.write("\n")


mapFile.write("};\n")

    
        