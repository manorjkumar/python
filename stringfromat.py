def print_format(number):
    w=len(str(bin(number))[2:])
    #print("decimal","octal","Hexadecimal","binary",end="")
    for i in range(1,number+1):
        print(str(i).rjust(w," "),oct(i)[2:].rjust(w," "),hex(i)[2:].upper().rjust(w," "),bin(i)[2:].rjust(w," "))
print(print_format(17))
