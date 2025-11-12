# write a  program to print the following star pattern
'''    *
      ***
     *****       ''' #for n=3

a=int(input("ENter the no.:"))
for i in range(1,a+1):
    print(" " * (a-i), end="")#spaces for centering
    print("*" * (2*i-1), end="")#stars for pyramid
    print("")#for new line


