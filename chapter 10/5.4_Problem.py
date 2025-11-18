# add a static method in problem 2 to greet "hello"

class greet():

    def __init__(self,name):
        self.name=name

    @staticmethod
    def hello():
        print(f"hello")

saujas=greet("saujas")
print(saujas.name)
greet.hello()


