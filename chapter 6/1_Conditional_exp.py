a=int(input("Enter your age:"))

if (a>=18):
    print("you are above the age of consent")
    print("you may enter")

elif(a<0):
     print("Invalid Age")

elif(a==0):
     print("Not valid")

else:
     print("you are below the age of consent")
     print("please leave!")