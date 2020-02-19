from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000

import math
color1=(255,0,0)
color2=(0,0,255)



red_diff = math.pow((color1[0] - color2[0]), 2)
green_diff = math.pow((color1[1] - color2[1]), 2)
blue_diff = math.pow((color1[2] - color2[2]), 2)
print(math.sqrt(red_diff + green_diff + blue_diff))

# define colors as RGB objects
color1_rgb = sRGBColor(255, 0, 0, True);
color2_rgb = sRGBColor(0, 0, 255, True);
# convert the colors to LabColor
color1_lab = convert_color(color1_rgb, LabColor);
color2_lab = convert_color(color2_rgb, LabColor);
# get the distance
delta_e = delta_e_cie2000(color1_lab, color2_lab);
print(f'The difference is {delta_e}.')