n=int(input("enter the no to find the sum of its digit"))
sum=0;
while(n>0):
    rem=n%10
    sum=sum+rem
    n=int(n/10)

print("the sum of digit is ", sum)
