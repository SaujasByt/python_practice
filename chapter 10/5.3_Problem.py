# create a class with the class attribute a; create an object from it and
# set "a" directly using object a=o. Does this change the class att.??

class demo:
    a=5

o=demo()        #prints classs attribute cuz instance is not preasent
print(o.a)

o.a=0           #prints instance attribute cuz instance is  preasent

print(o.a)      #prints class att.
print(demo.a)

# ANS> no it does not change the class attribute