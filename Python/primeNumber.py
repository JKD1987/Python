#Function to determine if a number is prime or not
x= int(input("Enter Number"))
factorCount = 0
if(x==1 or  x==2):
    print("Number is prime.")
else:
    for n in range(2,x-1):
        if(x%n == 0):
            print("Number is Composite.")
            break
    else:
        print("Number is Prime.")

##function to print number of Prime Numbers till a given number
y = x
if(y==1):
    print("Only one prime number: 1")
if(y==2):
    print("Available prime numbers are 1 and 2.")
else:
    l=[]
    i=1
    for i in range(1,y+1):
        factorCountNum = 0
        if(i==1 or  i==2):
            l.append(i)
        else:
            for num in range(2,i-1):
                if(i%num == 0):
                    break
            else:
                l.append(i)
    print("Available prime numbers upto ",y, " are: ", l)


    
    

    


    
