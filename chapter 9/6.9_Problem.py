# write a program to find if a file is identical and matches the contents of another file

with open('this.txt') as f:
    content1=f.read()

with open("this_copy.txt") as f:
    content2=f.read()

if(content1==content2):
    print("YES, Its same")

else:
    print("NO, its not")
    