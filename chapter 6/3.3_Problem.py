# Write  a program to detect spam from the keywords
#"make a lot of money","subcribe me,"buy now","click this"
co=input("Comment:")
a="make a lot of money"
b="subcribe me"
c="buy now"
d="click this"

if (a in co or b in co or c in co or d in co):
    print("SPAM!!")

else:
    print("Thank you for the comment!!")
