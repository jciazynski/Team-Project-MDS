from PIL import Image
import numpy as np

im = Image.open('zjedzony_dlugopis.jpg')
picture = im.load()

all_pixels = np.empty(shape=(im.size[0], im.size[1]), dtype=object)

for row in range(0,im.size[0]):
    for column in range(0,im.size[1]):
        all_pixels[row][column] = (picture[row,column][0],picture[row,column][1],picture[row,column][2])
