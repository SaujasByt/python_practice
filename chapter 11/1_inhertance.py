class employee:         #BASE CLASS
    company="ITC"
    def show(self):
        print(f"name={self.name} lang={self.lang}")

#   class programmer:
#      company="ITC INFOTECH"
#      def show(self):
#           print(f"name={self.name} lang={self.lang}")
#      def showsalary(self):
#           print(f"Salary={self.salary}")

class programmer(employee):    #CHIld class 
    company="ITC INFOTECH"
    def showsalary(self):
        print(f"salary={self.salary}")

a=employee()
b=programmer()

print(a.company,b.company)