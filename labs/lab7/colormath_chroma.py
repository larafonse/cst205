from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
from PIL import Image


#solution from professor modes' slides
def distance(color1, color2):
    """returns color distance"""
    color1_rgb = sRGBColor(color1[0],color1[1],color1[2], True);
    color2_rgb = sRGBColor(color2[0],color2[1],color2[2], True);
    # convert the colors to LabColor
    color1_lab = convert_color(color1_rgb, LabColor);
    color2_lab = convert_color(color2_rgb, LabColor);
    # get the distance
    return delta_e_cie2000(color1_lab, color2_lab) 

#solution from professor modes' slides
def chromakey(background, greenscreen, new_image):
    """creates a new image with the target green changed to background image"""
    for x in range(new_image.width):
            for y in range(new_image.height):

                background_pixel = background.getpixel((x,y))
                new_pixel = background_pixel

                green = (0, 190, 60)


                if (y < greenscreen.height and x < greenscreen.width):
                    greenscreen_pixel = greenscreen.getpixel((x,y)) 
                    if distance(greenscreen_pixel, green) > 20:
                        new_pixel = greenscreen_pixel;
                new_image.putpixel((x,y), new_pixel)

    new_image.save('images/chromakeyed.png')
    return new_image



background = Image.open("images/hartnell_planetarium.jpg")
greenscreen = Image.open("images/car_greenscreen.png")
new_image = Image.new("RGB", (background.width,background.height), "white")

our_new_image = chromakey(background, greenscreen, new_image)
our_new_image.show()