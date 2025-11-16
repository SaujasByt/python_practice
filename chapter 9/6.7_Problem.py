# Write  a program to find the line n0. where "python" is present in ques.6

with open('6.6.2_log.txt') as f:
    lines=f.readlines()

lineno=1
for line in lines:
    if("python" in line):
        print(f"YES, {lineno}")
        break
    lineno+=1

else:
    print("NO")
