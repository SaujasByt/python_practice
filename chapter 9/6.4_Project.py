#A file contains the word "Donkey" multiple times. write a program which replaces the
#word with ##### by updating the same file
word="donkey"

with open("6.4.txt","r") as a:
    content=a.read()

contentnew=content.replace(word,"######")

with open ("6.4.txt","w") as a:
    a.write(contentnew)

    