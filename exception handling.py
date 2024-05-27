#exception handling 
try:
    a=int(input("Enter your number :"))
    print(a+3)
except Exception as e:
    print("some Erros Occured",e)