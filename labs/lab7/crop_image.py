from PIL import Image


def copy_jeanne():
	 # source image
	 jeanne = Image.open("images/donut.jpg")
	 print(jeanne.size)
	 # destination image
	 canvas = Image.new("RGB", (1000,657), "white")
	 target_x = 0
	 for source_x in range(120,jeanne.width-121,1):
		 target_y = 0
		 for source_y in range(jeanne.height):
			 color = jeanne.getpixel((source_x, source_y)) # get pixels from the source
			 canvas.putpixel((target_x, target_y), color) # put pixels onto target
			 target_y += 1
		 target_x +=1
	 canvas.save("images/cropped_car_greenscreen.png")
	 canvas.show()

copy_jeanne()
jeanne = Image.open("images/donut.png")
print(jeanne.size)