a=int(input("Enter your age:"))
# 1st if statement
if (a%2==0):
     print("even")
     
else:
     print("odd")             #multiple if statements are independent of each other
#end of 1st if statement
# start of 2nd if statement
if (a>=18):
    print("you are above the age of consent")
    print("you may enter")
elif(a<0):
     print("Invalid Age")

else:
     print("you are below the age of consent")
     print("please leave!")
# end of 2nd if statement

     