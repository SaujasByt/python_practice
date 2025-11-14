# write a program to remove a given word from a list and strip it at the same time
# this means create a lsit with eg:- "an" and remove this from all elements in that list
def rem(l,w):
    for items in l:
        l.remove(w)
        return l
        print(l)

l=["harry","sonu","monu","bhalu","kalu"]
w=input("enter the name you wanna remove:")


print(rem(l,w))