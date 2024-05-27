
n=int(input("enter the no"))
num=n
sum=0
while(n>0):
    rem=n%10
    sum=sum+rem*rem*rem
    n=int(n/10)

if(num==sum):
    print("no is armstrong")
else:
    print("No is Not armstrong")
