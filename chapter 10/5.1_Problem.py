# create a class "programmer" for storing info of some programmers working at microsoft

class programmer:

    def __init__(self,name,lang,salary):
        self.name=name
        self.lang=lang
        self.salary=salary

harry=programmer("Harry","java",3231244)
print(f"Name={harry.name}\nLang={harry.lang}\nSalary={harry.salary}")
print("")
saujas=programmer("sauajs","java",3231244)
print(f"Name={saujas.name}\nLang={saujas.lang}\nSalary={saujas.salary}")
print("")
bhalu=programmer("bhalu","java",3231244)
print(f"Name={bhalu.name}\nLang={bhalu.lang}\nSalary={bhalu.salary}")
