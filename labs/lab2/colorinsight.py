#Task 5
red = int(input())
green = int(input())
blue = int(input())


# Task 1
if red > green and red > blue:
	print("The color is reddish.")
elif green > red and green > blue:
	print("The color is greenish.")
elif blue > red and blue > green:
	print("The color is blueish.")

# Task 2
elif blue == red:
	print("The color is a shade of magenta.")
elif blue == green:
	print("The color is a shade of cyan.")
elif red == green:
	print("The color is a shade of yellow.")