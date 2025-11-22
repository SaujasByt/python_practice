
class employee:
    a=1
    @classmethod
    def show2(cls):
        print(f"class att.={cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]


e= employee()
e.a=34335353
e.name="saujas das"
print(e.fname,e.lname)
e.show2()

