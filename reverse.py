x=int(input("enter the no to reverse"))
rev=0;
while(x>0):
    rem=x%10
    rev=rev*10+rem
    x=int(x/10)

print("the reverse of string is ", rev)
