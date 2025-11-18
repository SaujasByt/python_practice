# Self refers to the instance of the class it automaically passed with a fn call from a obj

class employee:
    language="python"
    salary=1000000  
    
    def getinfo(self):
        print(f"language:{self.language}. salary:{self.salary}")

    def greet(self):
        print("hello")

    @staticmethod  
    def greetings():
        print("hello buffalo")

harry = employee()
harry.greet()
harry.greetings()
harry.getinfo()         #↩ these are 2 methods of getting info
employee.getinfo(harry) #↩
