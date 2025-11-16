# Writea a program to mine a log file and find out whwther it contains "python"

with open('6.6.2_log.txt') as f:
    a=f.read()

if ("python" in a):
    print("YES")

else:
    print("NO")