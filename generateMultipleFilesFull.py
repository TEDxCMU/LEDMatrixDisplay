from __future__ import division
from PIL import Image

# Loops through 4 images
origim1 = Image.open( './images/rainbow.png')
origim2 = Image.open( './images/halfgreenhalfpink.jpeg')
origim3 = Image.open( './images/tedx.jpg')
origim4 = Image.open( './images/google.jpg')

# matrixWidth = 30
# matrixHeight = 22

matrixWidth = 60
matrixHeight = 22


im1 = origim1.resize((matrixWidth, matrixHeight))
im2 = origim2.resize((matrixWidth, matrixHeight))
im3 = origim3.resize((matrixWidth, matrixHeight))
im4 = origim4.resize((matrixWidth, matrixHeight))

imgWidth = im1.width
imgHeight = im1.height

print "imgSize", imgWidth, " x ", imgHeight

im1.save('images/resizedframe1.jpg', "JPEG", optimize=True)
im2.save('images/resizedframe2.jpg', "JPEG", optimize=True)
im3.save('images/resizedframe3.jpg', "JPEG", optimize=True)
im4.save('images/resizedframe4.jpg', "JPEG", optimize=True)


frame1pixVals1 = []
frame2pixVals1 = []
frame3pixVals1 = []
frame4pixVals1 = []
# Populate first half array
for y in range(0, im1.height):
    #rowVals = []
    if y % 2 == 0:
        for x in range(0, int(im1.width/2)):
            r1,g1,b1 = im1.getpixel((x,y))
            frame1pixVals1.append([r1, g1, b1])
            r2,g2,b2 = im2.getpixel((x,y))
            frame2pixVals1.append([r2, g2, b2])
            r3,g3,b3 = im3.getpixel((x,y))
            frame3pixVals1.append([r3, g3, b3])
            r4,g4,b4 = im4.getpixel((x,y))
            frame4pixVals1.append([r4, g4, b4])
    else:
        for x in range((int(im1.width/2))-1, -1, -1):
            r1,g1,b1 = im1.getpixel((x,y))
            frame1pixVals1.append([r1, g1, b1])
            r2,g2,b2 = im2.getpixel((x,y))
            frame2pixVals1.append([r2, g2, b2])
            r3,g3,b3 = im3.getpixel((x,y))
            frame3pixVals1.append([r3, g3, b3])
            r4,g4,b4 = im4.getpixel((x,y))
            frame4pixVals1.append([r4, g4, b4])


frame1pixVals2 = []
frame2pixVals2 = []
frame3pixVals2 = []
frame4pixVals2 = []
# Populate second half array
for y in range(0, imgHeight):
    #rowVals = []
    if y % 2 == 0:
        #counter = 0
        for x in range(int(imgWidth/2), imgWidth):
            r1,g1,b1 = im1.getpixel((x,y))
            frame1pixVals2.append([r1, g1, b1])
            r2,g2,b2 = im2.getpixel((x,y))
            frame2pixVals2.append([r2, g2, b2])
            r3,g3,b3 = im3.getpixel((x,y))
            frame3pixVals2.append([r3, g3, b3])
            r4,g4,b4 = im4.getpixel((x,y))
            frame4pixVals2.append([r4, g4, b4])
            #counter+=1
        #print"!!!!!!!!!!!", counter
    else:
        #counter = 0
        for x in range(imgWidth-1, int(imgWidth/2) - 1, -1):
            r1,g1,b1 = im1.getpixel((x,y))
            frame1pixVals2.append([r1, g1, b1])
            r2,g2,b2 = im2.getpixel((x,y))
            frame2pixVals2.append([r2, g2, b2])
            r3,g3,b3 = im3.getpixel((x,y))
            frame3pixVals2.append([r3, g3, b3])
            r4,g4,b4 = im4.getpixel((x,y))
            frame4pixVals2.append([r4, g4, b4])
            #counter+=1
        #print"!!!!!!!!!!!", counter

# print "Len of pixVals1:", len(pixVals1)
# print "Len of pixVals2:", len(pixVals2)
# print pixVals1
# print "****************************"
# print pixVals2

mapFile = open('./show_frames_arduino/mapping.h', 'w')
mapFile.write("#include <avr/pgmspace.h>\n")
mapFile.write("#if defined(__AVR__)\n")
mapFile.write("#elif defined(__PIC32MX__)\n")
mapFile.write("#define PROGMEM\n")
mapFile.write("#elif defined(__arm__)\n")
mapFile.write("#define PROGMEM\n")
mapFile.write("#endif\n")

mapFile.write("const byte frame1firsthalf["+str(len(frame1pixVals1))+"][3] PROGMEM={\n")

for pixSet in frame1pixVals1:
    mapFile.write('{')
    for pixC in pixSet:
        mapFile.write(str(pixC) + ", ")
    mapFile.write('},')

mapFile.write("\n")
mapFile.write("};\n")

mapFile.write("const byte frame1secondhalf["+str(len(frame1pixVals2))+"][3] PROGMEM={\n")

for pixSet in frame1pixVals2:
    mapFile.write('{')
    for pixC in pixSet:
        mapFile.write(str(pixC) + ", ")
    mapFile.write('},')

mapFile.write("\n")
mapFile.write("};\n")

mapFile.write("const byte frame2firsthalf["+str(len(frame1pixVals1))+"][3] PROGMEM={\n")

for pixSet in frame2pixVals1:
    mapFile.write('{')
    for pixC in pixSet:
        mapFile.write(str(pixC) + ", ")
    mapFile.write('},')

mapFile.write("\n")
mapFile.write("};\n")

mapFile.write("const byte frame2secondhalf["+str(len(frame1pixVals2))+"][3] PROGMEM={\n")

for pixSet in frame2pixVals2:
    mapFile.write('{')
    for pixC in pixSet:
        mapFile.write(str(pixC) + ", ")
    mapFile.write('},')

mapFile.write("\n")
mapFile.write("};\n")

mapFile.write("const byte frame3firsthalf["+str(len(frame1pixVals1))+"][3] PROGMEM={\n")

for pixSet in frame3pixVals1:
    mapFile.write('{')
    for pixC in pixSet:
        mapFile.write(str(pixC) + ", ")
    mapFile.write('},')

mapFile.write("\n")
mapFile.write("};\n")

mapFile.write("const byte frame3secondhalf["+str(len(frame1pixVals2))+"][3] PROGMEM={\n")

for pixSet in frame3pixVals2:
    mapFile.write('{')
    for pixC in pixSet:
        mapFile.write(str(pixC) + ", ")
    mapFile.write('},')

mapFile.write("\n")
mapFile.write("};\n")

mapFile.write("const byte frame4firsthalf["+str(len(frame1pixVals1))+"][3] PROGMEM={\n")

for pixSet in frame4pixVals1:
    mapFile.write('{')
    for pixC in pixSet:
        mapFile.write(str(pixC) + ", ")
    mapFile.write('},')

mapFile.write("\n")
mapFile.write("};\n")

mapFile.write("const byte frame4secondhalf["+str(len(frame1pixVals2))+"][3] PROGMEM={\n")

for pixSet in frame4pixVals2:
    mapFile.write('{')
    for pixC in pixSet:
        mapFile.write(str(pixC) + ", ")
    mapFile.write('},')

mapFile.write("\n")
mapFile.write("};\n")