# word="donkey"
words=["donkey","is"]
with open("6.5.txt","r") as a:
    content=a.read()

for word in words:
    content=content.replace(word,"#"*len(word))

with open ("6.5.txt","w") as a:
    a.write(content)