from PIL import Image

im = Image.open( './images/256x256bb.jpg')

width = 30
height = 22
pixVals = []


for y in range(0, height):
    for x in range(0, width):
        r,g,b = im.getpixel((x,y));
        pixVals.append(r<<16 | g<<8 | b)

print(pixVals)