def fib(a):
    if(a==0):
        return 0;
    if(a==1):
        return 1;
    else:
        return fib(a-1)+fib(a-2)



a=int(input("enter the no which you wanna have of fibbnocio series of"))
for a in range(0,a):
    print(fib(int(a)))


