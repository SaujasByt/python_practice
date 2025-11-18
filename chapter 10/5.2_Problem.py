# write a class 'calculator' capable of finding square,sq. root and cube of a no.

class calculator:
    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"Square={self.n*self.n}")
    def squareroot(self):
        print(f"Square Root={self.n**(1/2)}")
    def cube(self):
        print(f"cube={self.n**3}")

a=calculator(9)
a.square()
a.squareroot()
a.cube()
