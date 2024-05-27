n=int(input("enter the no "))
temp=n
rev=0
while(temp!=0):
    rev=(rev*10)+(temp%10)
    temp=temp//10
if n==rev:
    print("no is pallindrome")
else:
    print("no is not pallindrome")
