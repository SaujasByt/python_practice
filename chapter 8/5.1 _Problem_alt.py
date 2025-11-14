def gn(a,b,c):             
   
    if (a>b and a>c):
        return a
    
    elif(b>a and b>c):
        return b
    else:
        return c
    

a=int(input("Enter the no.:"))
b=int(input("Enter the no.:"))
c=int(input("Enter the no.:"))
print(gn(a,b,c))