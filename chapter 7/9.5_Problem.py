# Write a program to print factorial of a no. using for loop
a=int(input("ENter the no.:"))
b=1
fact=1
for a in range(1,a+1):
    fact*=b
    b+=1

print(fact)

# Alt method
a=int(input("ENter the no.:"))
fact=1
for b in range(1,a+1):
    fact= fact*b
print(fact)