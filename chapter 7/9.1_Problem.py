# write a program to make a multiplication table of a no. entered by the user
# Using for loop
a=int(input("ENter the no.:"))

for b in range(1,11):
    print(f"{a} X {b} = {a*b}")

# using while loop
# a=int(input("ENter the no.:"))
b=1
while (b<11):
    print(f"{a} X {b} = {a*b}")
    b+=1
