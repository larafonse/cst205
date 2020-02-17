# sunset_filter.py
# This program will prompt the user to slect an image and create a new image 
# with Green and Blue values fixed
# Created by Nicolas Lara Fonseca and Rodrigo Andrade

from PIL import Image

im = Image.open('Emilie_Preyer.jpg')

width, length = im.size()

print(width)
# im.putdata(list(new_list))
# im.save('new_landscape.jpg')
im.show()