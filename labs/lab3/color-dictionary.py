# color dictionary
color_dictionary = {
"red":{"red":255,"green":0,"blue":0},
"green":{"red":0,"green":128,"blue":0},
"blue":{"red":0,"green":0,"blue":255},
"magenta":{"red":255,"green":0,"blue":255}, 
"cyan":{"red":0,"green":255,"blue":255},
"yellow":{"red":255,"green":255,"blue":0}
}

# color=input("Enter a color: ")
# channel=input("Enter a channel: ")

# # value assignment
# channel_value=color_dictionary[color][channel]

# # final output
# print(f"The {channel} channel of {color} has a value {channel_value}")


# RGB tuples of any colors in color_dictionary whose second letter is "e"
for key in color_dictionary:
	if key[1] == 'e':
		print(key)
		print(color_dictionary[key])