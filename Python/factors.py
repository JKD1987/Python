def getFactors(x):
        fact = []
        for indx in range(1,x+1):
                if(x%indx == 0):
                        fact.append(indx)
        return fact

x=int(input("Enter a number: "))
l=getFactors(x)
print("factors of ", x, " are ", l)
print("Number of factors of ", x, "are: ", len(l))