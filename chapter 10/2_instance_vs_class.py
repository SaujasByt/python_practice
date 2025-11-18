# The instance att. is prioritized over class att. 

class employee: 
    language="python"#↩ these 2 are class attributes
    salary=1000000   #↩


harry = employee()
harry.salary=2000000
print(harry.salary, harry.language)


rohan = employee()
print(rohan.salary, rohan.language)
