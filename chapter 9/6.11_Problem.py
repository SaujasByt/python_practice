# Write  a program to rrename a file to "renamed_by_python"
with open("hello.txt") as f:
    content=f.read()

with open("renamed_by_python.txt","w") as a:
    a.write(content)

# this will only create a copy of the initial file, it cant rename it
# to rename it we'll have to install some modules 