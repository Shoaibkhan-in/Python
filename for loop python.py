for i in range (0,5):
    print(i)

print("\n")
# for loop to access list element 
a=[23,1,4,51,14,2,4,1,3]
for items in a:
    print(items)

print("\n")
i=1;
while (i<10):
    print(i)
    i+=1
    if(i==9):
        break
    
for i in range (6):
    if(i==3):
        continue
    print(i)


while (True):
    a=int(input("Enter The Number"))
    print(a)
    if(a==0):
        print("The Program has been ended")
        break
