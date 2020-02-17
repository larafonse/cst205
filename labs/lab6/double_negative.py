# double_negative.py
# This program will take and image and return the negative of the image
# Created by Nicolas Lara Fonseca and Rodrigo Andrade

from PIL import Image

im = Image.open(input('what is the name of the image?'))

def negative_image(pixel):
	return tuple(map(lambda a : 255-a, pixel))

negative_list = (map(negative_image, im.getdata()))

im.putdata(list(negative_list))
im.save('new_negative.jpg')
im.show()