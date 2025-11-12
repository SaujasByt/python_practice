""" *** 
    * *
    ***   """
a=int(input("ENter the no.:"))
for i in range(1,a+1):
    if (i==1 or i==a):
        print("*"*a,end="")
    else:
        print("*",end="")#prints the first * of the row
        print(" "*(a-2),end="")#prints the hollow spaces b/w *'s
        print("*",end="")#prints the last * of the row
    print("")#moves to next line