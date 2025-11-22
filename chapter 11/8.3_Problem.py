# create a class employee and add salary and increment property to it.
#write a method with as salaryafterincrement using @property with a setter which changes 
# the value of increment based on salary

class employee:
    salary=12345
    increment=10

    @property
    def salafterinc(self):
        return (self.salary+(self.salary*(self.increment/100)))
    
    @salafterinc.setter
    def salafterinc(self,salary):
        self.inc=((salary/self.salary)-1) * 100


e=employee()
# print(e.salafterinc)
e.salafterinc=12345
print(e.inc)






