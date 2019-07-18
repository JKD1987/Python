x=int(input("StdCode: "))

if(x>=1 and x<=40):
    y=int(input("Zone Ex 1,2,3,4: "))
    if(y==1):
        print("North")
    elif(y==2):
        print("South")
    elif(y==3):
        print("East")
    elif(y==4):
        print("West")
    else:
        print("Unknown Zone")
else:
    print("Invalid StdCode.")
