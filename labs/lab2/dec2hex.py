#dictionary
hexdict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

#function to have more condense and readable code
def dectohex(var):
    var1 = var//16
    var2 = var%16
    
    if var1 in hexdict:
        var1 = hexdict[var1]
    if var2 in hexdict:
        var2 = hexdict[var2]
    return str(var1)+str(var2)

#user input
red = int(input())
green = int(input())
blue = int(input())

#final output
print('#'+dectohex(red)+dectohex(green)+dectohex(blue))

