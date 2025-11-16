# f=open("myfile.txt")

# print(f.read())
# f.close() #using the close() fn is very cliche

# but using the "with" statement we dont have to close the file
with open("chapter 9/myfile.txt") as a:
    print(a.read())