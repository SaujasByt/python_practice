#create a class (2D-vector) and use it represent another class (3D-vector)

class twoDvector:
    def __init__(self, i, j):
        self.i= i
        self.j= j

    def show(self):
        print(f'vector={self.i} + {self.j}')
        

class threeDvector(twoDvector):
    def __init__(self, i, j, k):
        super().__init__(i,j)
        self.k= k

    def show(self):
        print(f'vector={self.i}i + {self.j}j + {self.k}k')


a= twoDvector(1,2)
a.show()
b= threeDvector(7, 8, 9)
b.show()
