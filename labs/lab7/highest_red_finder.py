#
# highest_red_finder.py
# Created by Nicolas Lara Fonseca and Rodrigo Andrade
# 17 February 2020
#

from PIL import Image

im = Image.open('images/Emilie_Preyer.jpg')

width,length = im.size

max = 0

for x in range(width):
	for y in range(length):
		pixel = im.getpixel((x,y))
		if pixel[0] > max:
			max=pixel[0]
			cordinate=(x,y)
			final=pixel
			
print(f'Biggest : {max} at {cordinate} and its tuple is {final}')
