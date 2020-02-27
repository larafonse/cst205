# 
# hw1_task1.py
# Created by Nicolas Lara Fonseca and Rodrigo Andrade
# 24 February 2020
# 

from PIL import Image
from glob import glob
from math import floor

img_list=[]

# extract all imgs using glob module
for filepath in glob('images/*.png'):
	img_list.append(Image.open(filepath))

# blank canvas to for new img
new_img=Image.new('RGB',(img_list[0].width,img_list[0].height),'white')

# 
median = floor((len(img_list)+1)/2)

# for loop that will iterate through new img's pixels 
for x in range(new_img.width):
	for y in range(new_img.height):
		pixel=[]

		# for loop that will iterate through each img to get pixel
		for im in img_list:
			pixel.append(im.getpixel((x,y)))

		# insert median pixel to new img
		pixel.sort()
		new_img.putpixel((x,y),pixel[median])

new_img.save('images/no_obj.png')
new_img.show()