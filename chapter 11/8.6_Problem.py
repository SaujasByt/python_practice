# override the __len__() method on vector of problem 5 to display the dimension of vector

class vector:
    def __init__(self,l):
        self.l=l

    def __len__(self):
        return len(self.l)
    
v= vector([1,2,3,5])
print(len(v))
