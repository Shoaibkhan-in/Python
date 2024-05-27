print("Enter -1 to exit the program");
n=int(input("Enter the No:-"))


fact=1
if n<0:
    print("The Factorial Below Than Zero is Not Possible")
elif n==0:
    print("Factial Of 0 is 1");
else:
    for i in range (1,n+1):
        fact=fact*i;

print("The Factorial is ",fact);
