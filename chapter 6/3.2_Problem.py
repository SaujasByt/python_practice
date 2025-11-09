# Write a program to find if a student has passed or failed as a min. of 40% is req. 
# and 33% aggregate is req. all 3 subjects
a1=int(input("Enter your marks in hindi:"))
a2=int(input("Enter your marks in english:"))
a3=int(input("Enter your marks in maths:"))
c=(a1+a2+a3)/3
if(a1>=33 and a2>=33 and a3>=33 and c>=40):
    print("Pass",c,"%")

else:
    print("Fail",c,"%")


    
