# 
# hw1_task1.py
# Created by Nicolas Lara Fonseca and Rodrigo Andrade
# 24 February 2020
# 

from PIL import Image
from glob import glob
from math import floor

img_list=[]

for filepath in glob('images/*.png'):
	img_list.append(Image.open(filepath))

new_img=Image.new('RGB',(img_list[0].width,img_list[0].height),'white')

median = floor((len(img_list)+1)/2)



for x in range(new_img.width):
	for y in range(new_img.height):
		pixel=[]
		for im in img_list:
			pixel.append(im.getpixel((x,y)))
		pixel.sort()
		new_img.putpixel((x,y),pixel[median])

new_img.save('images/no_obj.png')
new_img.show()