# inside  a class, python doesnot understand mathematical annotations like '+-*/'
# so we use a dunder method called "OPERATOR OVERLOADING"
# OPERATORS:-
# a+b= a.__add__(b)
# a-b= a.__sub__(b)
# a*b= a.__mul__(b)
# a/b= a.__truediv__(b)
# a//b = a.__floordiv__(b)

# OTHER:-
# __str__() = used to set what gets dispalyed upon calling str(obj)
# __len__() = used to set what gets displayed upon calling len(obj)