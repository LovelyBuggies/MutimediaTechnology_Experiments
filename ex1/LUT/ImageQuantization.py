import numpy as np
from PIL import Image, ImageDraw

# Images Input and Properties
img1 = Image.open("pics/redapple.jpg").convert("RGB")
npImage1 = np.array(img1)
width, height = img1.size

# Fuzzier Images
for n in range(3, 8, 1):
    for x in range(0, int(width-1)):
        for y in range(0, int(height-1)):
            npImage1[y][x] = np.floor(npImage1[y][x] / np.power(2,n)) * np.power(2,n)
    Image.fromarray(npImage1).show()

Image.fromarray(npImage1).save('pics/vagueapple.png')
