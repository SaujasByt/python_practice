# write a  program to find the greates to 3 nos. using functions
def gn():             
    a=int(input("Enter the no.:"))
    b=int(input("Enter the no.:"))
    c=int(input("Enter the no.:"))
    if (a>b and a>c):
        print(a,"is the greatest no.")
    
    elif(b>a and b>c):
        print(b,"is the greatest no.")
    else:
        print(c,"is the greatest no.")

gn()
print(type(gn))