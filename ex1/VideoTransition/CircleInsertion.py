import numpy as np
from PIL import Image, ImageDraw

# Images Input and Properties
img1 = Image.open("pics/lena.jpg").convert("L")
npImage1 = np.array(img1)
img2 = Image.open("pics/nobel.jpg").convert("L")
npImage2 = np.array(img2)
height2, width2 = img2.size
centerX = int(width2/2)
centerY = int(height2/2)
radius = int(height2/4);
'''
# Circle Insertion
for y in range(centerY-radius, centerY+radius):
    for x in range(centerX-radius, centerX+radius):
        if np.power((x-centerX),2)+np.power((y-centerY),2) < np.power(radius,2):
            npImage2[y][x] = npImage1[y][x]
Image.fromarray(npImage2).save('pics/circleinsertion.png')
'''
# Image Extension
img3 = Image.new("L", img1.size)
npImage3 = np.array(img3)
height3, width3 = img3.size
for y in range(0, height3-1):
    for x in range(0, width3-1):
            npImage3[y][x] = npImage1[int(3*y/4), int(3*x/4)]
Image.fromarray(npImage3).save('pics/larger.png')

# Circle Extended Insertion
npImage2 = np.array(img2)
radius = int(3*radius/2)
for y in range(centerY-radius, centerY+radius):
    for x in range(centerX-radius, centerX+radius):
        if np.power((x-centerX),2)+np.power((y-centerY),2) < np.power(radius,2):
            npImage2[y][x] = npImage3[y][x]
Image.fromarray(npImage2).save('pics/circleExinsertion.png')
