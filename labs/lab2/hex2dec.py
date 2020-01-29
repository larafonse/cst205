#dictionary
hexdict = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}

#functions that takes in hex variables and returns the decimal
def hex2dec(var1,var2):
	#if statement that checks if the variables is in the hexdict and adds  it to dec value
	if var1 in hexdict:
		dec = hexdict[var1]*16
	else:
		dec= int(var1)*16

	if var2 in hexdict:
		dec = dec + hexdict[var2]
	else:
		dec = dec + int(var2)
	return dec

#user input 
hex = input("Enter Hexadecimal: ")

#variable assignment
red = hex2dec(hex[1],hex[2])
green = hex2dec(hex[3],hex[4])
blue = hex2dec(hex[5],hex[6])

#final output
print(str(red) + " " +str(green) + " " + str(blue))