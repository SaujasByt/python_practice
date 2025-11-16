f=open("chapter 9/myfile.txt")

'''METHOD 1 = using readline's' '''
# # lines=f.readlines()       #READLINE's' reads everything in a file
# # print(lines)                    
# # print(type(lines)) 
# # f.close()
'''METHOD 2 =using readline'''
# lines1=f.readline()         #READLINE READS ONLY A SPECIFIC LINE
# print(lines1,type(lines1))

# lines2=f.readline()
# print(lines2,type(lines2))

# lines3=f.readline()
# print(lines3,type(lines3))

# lines4=f.readline()
# print(lines4,lines4=="")

# f.close()
'''METHOD 3 = using while loop'''
line=f.readline()
while(line !=""):
    print(line)
    line=f.readline()

f.close()
