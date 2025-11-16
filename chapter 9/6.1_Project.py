# write a program to read a file 'poems.txt' and find out if it contains the word twinkle
a=open("chapter 9/6.1.txt")
poem=a.read()
# b=(poem.find("twinkle"))
# if (b!=True):
#     print("TRUE") 
# else:
#     print("FALSE")
# a.close()

# ALT METHOD

if("twinkle" in poem and "little" in poem):
    print("True")

else:
    print("False")

a.close()