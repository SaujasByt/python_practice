# Write a program to generate multiplication table from 2-20 and write 
# it in different files and palce it in a folder for a 13yo

def t(n):
    table=""
    for i in range(1,11):
        table+=(f"{n}X{i}={n*i}\n")

    with open(f"chapter 9/tables/table_{n}.txt","w") as f:
        f.write(table)

for a in range(2,21):
    t(a)