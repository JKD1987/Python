x=int(input("Enter year: "))

if(x%100 == 0):
    if(x%400 == 0):
        print(x, "is a Leap year.")
    else:
        print(x, "is not a leap year")
elif(x%4 == 0):
    print(x, "is a Leap year.")
else:
    print(x, "is not a leap year")

if((x%400 ==0) or (x%100!=0 and x%4 == 0)):
    print("Leap year")
else:
    print("Not Leap year")
