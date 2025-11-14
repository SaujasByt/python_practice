# Recursion is fn which calls itself
# it is used to use a mathematical formula directly as a fn.
def fact(n):
    if(n==1 or n==0):
        return 1
    return n*fact(n-1)
    
n= int(input("Enter your no.: "))
print (fact(n))

# EXPLANATION:-

''' this creates a type of loop as showns
        
        5 X 4!
        5 X 4 x 3!
        5 X 4 X 3 X 2!.....'''