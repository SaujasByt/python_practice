# write a program to print invalid Uname if any blank spaces are found

name = input("ENTER:")
if not name.strip():
    print("Invalid Uname")
else:
    print("OK")