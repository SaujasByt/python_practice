# noun-> class -> employee
#adjective-> attributes -> name,age,salary
#verbs -> methods -> getsalary(),increment()
class employee:
             
    language="python"#↩ these 2 are class attributes
    salary=1000000   #↩


harry = employee()
print(harry.salary, harry.language)

rohan = employee()
rohan.name="roronoa rohan" #↩ THis is a instance attribute
print(rohan.name,rohan.salary, rohan.language)


# here "salary" and "language" are class attributes and name is an instance att.
# The instance att. is prioritized over class att. 