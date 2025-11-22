# Multile parents have 1 child
class employee:         #BASE CLASS
    company="ITC"
    name="saujas"
    def show(self):
        print(f"name={self.name} lang={self.company}")

class coder:            #BASE 2
    lang="python"
    def showlang(self):
        print(f"your language is {self.lang}")

class programmer(employee,coder):    #CHIld class 
    company="ITC INFOTECH"
    def showlanguage(self):
        print(f"lang={self.lang}")

a=employee()
b=programmer()

print(a.company,b.company)
a.show()
b.showlang()
b.showlanguage()
