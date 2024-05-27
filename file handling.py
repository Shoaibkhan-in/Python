#s="shoaib khan pathan"

#writing to a file
#with open("shoaib.txt","w") as f:
#    f.write(s)

'''fp=open("test.txt","w")
fp.write(s)
fp.close()'''

#reading a file

'''with open("123.txt","r") as f:
    s=f.read()
    print(s)'''

#apppend 

with open("test.txt","a") as f:
    f.write("this is append where the data get added to to file")