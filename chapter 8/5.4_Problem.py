# write a recursive program to print the sum of first n natural nos.

def sum(n):
    if(n==1):  #base condition #↩  if these  2 lines are not present then the loop will run             
        return 1                    #↩ infinitely in -ve direction, Hence giving an error
    
        
    return sum(n-1) + n
 






n= int(input("Enter your no.: "))
print (sum(n))