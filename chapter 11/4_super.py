# super() method is used to access the methods of a super class in a derived class

class employee:
    def __init__(self):
        print("Employee")
    a=1

class programmer(employee): 
    def __init__(self):
        super().__init__()
        print("Programmer")
    b=2

class manager(programmer):
    def __init__(self):
        super().__init__()
        print("Manager")
    c=3

# o=employee()
# print(o.a)

# o=programmer()
# print(o.a,o.b)

o=manager()
print(o.a,o.b,o.c)



