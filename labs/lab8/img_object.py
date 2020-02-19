#
# img_object.py
# Created by Nicolas Lara Fonseca and Rodrigo Andrade
# 19 February 2020
# 

from PIL import Image

le = Image.open('images/nick_kong.jpg')

# thumbnail() resizes an image according to tuple passed in
# le.thumbnail((100,100))
# le.show()

# creates a histogram containing all 768 color intensities 
# print(le.histogram())

# creates a copy of the image with the number of colors passed in 
le= le.quantize(2) 
le.save('images/quantized_img.png')

le.show()

