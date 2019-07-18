name = input("Enter Name")
print(name)

a= int(input("First Number"))
b= int(input("Second Number"))
#a= int(input("First Number"), 2) take binary numbers. Print statement still prints in decimal format.
#b= int(input("Second Number"), 2) 
#print(int(a) + int(b))
print("Sum of numbers " + str(a+b)) #str converts numeric to string
c=a+b
print("First=%d Second=%d" %(a,b))
print("Sum of numbers = %d Done" %(c))