class Color:
	"""docstring for Contact"""
	def __init__(self,name, red, green, blue):
		self.name = name
		self.red = red
		self.green =green
		self.blue =blue
	def luminosity(self):
		return (self.red + self.green + self.blue)/3

blue = Color("boring blue", 0, 0, 255)
green = Color("normal green", 0, 255, 0)


print(f"{blue.name}'s luminosity is ", blue.luminosity())



		