a={1,23,454,34}
b={23,65,76,64}
print(a.union(b))
print(a.intersection(b))
print(a-b)  #  this will print all values of a that is not present in b (a-b=a-anb)
print({1}.issubset(a))
print(a.issuperset({1,23,454,34,2}))