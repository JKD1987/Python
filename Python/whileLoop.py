response = "Y"

while(response == "Y" or response == "y"):
    x=int(input("Enter year: "))
    if((x%400 ==0) or (x%100!=0 and x%4 == 0)):
        print("Leap year")
    else:
        print("Not Leap year")
    response = input("Do you want to continue (Y/N): ")