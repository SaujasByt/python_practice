# write a program to find if a program is prime or not
a=int(input("ENter the no.:"))

for i in range(2,a):
    if(a%i)==0:
        print(a,"is not prime")
        break
else:
    print(a,"is prime")



