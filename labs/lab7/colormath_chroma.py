from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
from PIL import Image

target_green = (0, 190, 60)
color_distance = 40

def distance(color_1, color_2):
	color1_rgb = sRGBColor(color_1[0],color_1[1],color_1[2],True);
	color2_rgb = sRGBColor(color_2[0],color_2[1],color_2[2],True);
	color1_lab = convert_color(color1_rgb, LabColor);
	color2_lab = convert_color(color2_rgb, LabColor);
	return delta_e_cie2000(color1_lab, color2_lab);

def chromakey(background, greenscreen):
    new_image = Image.new("RGB", (greenscreen.width,greenscreen.height), "black")
    for x in range(background.width):
            for y in range(background.height):
                background_pixel = background.getpixel((x,y))
                new_pixel = background_pixel
                if (y < greenscreen.height and x < greenscreen.width):
                    greenscreen_pixel = greenscreen.getpixel((x,y)) 
                    if distance(greenscreen_pixel, target_green) > color_distance:
                        new_pixel = greenscreen_pixel;
                new_image.putpixel((x,y), new_pixel)

    new_image.save('images/chromakeyed.png')
    return new_image


greenscreen= Image.open("images/hartnell_planetarium.jpg")

background = Image.open("images/car_greenscreen.png")

our_new_image = chromakey(background, greenscreen)
our_new_image.show()