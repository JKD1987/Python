x=float(input("Enter first number \n"))
y=int(input("Enter second number \n"))

if(x==y):
    print("Same")
elif(x>y):
    print("Greater is", x)
else:
    print("Greater is", y)

if(x is y):
    print("Same")
elif(x is not y):
    if(type(x) != type(y)):
        print("Type Mismatch")
    if(type(x) is float and type(y) is int):
        print("abc")
    else:
        print("def")




