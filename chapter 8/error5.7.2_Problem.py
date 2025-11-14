def rem(l,w):
    n=[]
    for item in l:
        if not(item == w):
            n.append(item.strip(w))
        return n
        
l=["harry","sonu","monu","bhalu","kalu","lu"]


print(rem(l,"l"))