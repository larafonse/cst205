#
# chroma_key.py
# Created by Nicolas Lara Fonseca and Rodrigo Andrade
# 17 February 2020
#
import math
from PIL import Image

def distance(color1, color2):
    """returns color distance"""
    red_diff = math.pow((color1[0] - color2[0]), 2)
    green_diff = math.pow((color1[1] - color2[1]), 2)
    blue_diff = math.pow((color1[2] - color2[2]), 2)
    return math.sqrt(red_diff + green_diff + blue_diff)

def chromakey(background, greenscreen, new_image):
    """creates a new image with the target green changed to background image"""
    for x in range(new_image.width):
            for y in range(new_image.height):

                background_pixel = background.getpixel((x,y))
                new_pixel = background_pixel

                green = (0, 190, 60)


                if (y < greenscreen.height and x < greenscreen.width):
                    greenscreen_pixel = greenscreen.getpixel((x,y)) 
                    if distance(greenscreen_pixel, green) > 128:
                        new_pixel = greenscreen_pixel;
                new_image.putpixel((x,y), new_pixel)

    new_image.save('images/chromakeyed.png')
    return new_image



background = Image.open("images/hartnell_planetarium.jpg")
greenscreen = Image.open("images/car_greenscreen.png")
new_image = Image.new("RGB", (background.width,background.height), "white")

our_new_image = chromakey(background, greenscreen, new_image)
our_new_image.show()