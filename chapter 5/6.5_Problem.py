# create a empty dict and let 4 friends enter their language
dict={}
a=input("enter your name:")
b=input("enter your language:")
dict.update({a:b})
a=input("enter your name:")             #if 2 friends have the same name then
b=input("enter your language:")             #the lateest entry will be submitted
dict.update({a:b})
a=input("enter your name:")
b=input("enter your language:")
dict.update({a:b})
a=input("enter your name:")
b=input("enter your language:")
dict.update({a:b})
print(dict)

