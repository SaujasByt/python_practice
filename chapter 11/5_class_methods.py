# Classmethod is a way to overwrite the instance attribute as class attribute
# as we know that instance att. is prioriotized over class att.

class employee:
    a=1

    def show1(self):
        print(f"default(instance)={self.a}")

    @classmethod
    def show2(cls):
        print(f"class att.={cls.a}")

e= employee()
e.a=34335353
e.show1()
e.show2()






