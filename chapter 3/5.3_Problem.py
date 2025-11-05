# write a program to detect double spaces in a string
a=("write a program to detect  double spaces in a string")
print(a.find("  "))

# ALT METHOD FOR USER INPUT
a=input("enter")

if a.find("  ") != -1:#if double space is not found the value of a.find is -1 so using 
    print("double space") #!=-1 means print(double space) only if value is not equal to -1

else:
    print("OK")