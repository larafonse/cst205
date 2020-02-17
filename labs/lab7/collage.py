#
# collage.py
# Created by Nicolas Lara Fonseca and Rodrigo Andrade
#

from PIL import Image 

def add_cavas(image,target_x,y):
	"""adds image to canvas"""
	for source_x in range(image.width):
		 target_y = y
		 for source_y in range(image.height):
			 color = image.getpixel((source_x, source_y))
			 canvas.putpixel((target_x, target_y), color)
			 target_y += 1
		 target_x += 1


im = Image.open('images/donkey.jpeg')
im2 = Image.open('images/smartdog.jpg')
im3 = Image.open('images/funny_cat.png')
canvas = Image.new('RGB', (800,800), 'black')

add_cavas(im,100,100)
add_cavas(im2,400,100)
add_cavas(im3,250,400)

canvas.show()
canvas.save("images/emptycanvas.jpg")
