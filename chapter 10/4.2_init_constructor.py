class employee:
    language="python"
    salary=1000000  

    def __init__(self,name,salary,language): 
        self.name=name
        self.salary=salary
        self.language=language

    
    def getinfo(self):
        print(f"language:{self.language}. salary:{self.salary}")


    def greet(self):
        print("hello") 


harry = employee("harry","C++",999999,)
print(harry.name,harry.language,harry.salary)


