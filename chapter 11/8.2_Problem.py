# create a class pets froam a class animals and further create a class dog 
# from pets and add a method "bark" to class dog

class animals:
    pass

class pets(animals):
    pass

class dogs(pets):
    @staticmethod
    def bark():
        print("Bhow bhow!!")

a=dogs()
a.bark()
        