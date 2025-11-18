class employee:
    language="python"
    salary=1000000  

    def __init__(self):  #dunder method which is automatically called when class is called
        print("I am creating an object")
    
    def getinfo(self):
        print(f"language:{self.language}. salary:{self.salary}")


    def greet(self):
        print("hello") 


harry = employee()
harry.greet()

harry.getinfo()   

rohan = employee()