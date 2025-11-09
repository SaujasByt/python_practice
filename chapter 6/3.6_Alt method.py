# Write a code to find a student's grade 
a=int(input("Enter your marks:"))
if(90<=a<=100):
    g=("Ex")
elif(80<=a<90):
    g=("A")
elif(70<=a<80):
    g=("B")
elif(60<=a<70):
    g=("C")
elif(50<=a<60):
    g=("D") 
else:
    g=("F") 

print("Your Grade:",g)