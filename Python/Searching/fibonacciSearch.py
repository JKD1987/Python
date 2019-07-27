def fibonacciGenerator(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    else: 
        return fibonacciGenerator(n-1) + fibonacciGenerator(n-2) 

def fibonacciSearch(arr, x):
    m=0
    while(fibonacciGenerator(m) < len(arr)):
        m = m+1
    print(m)
    offset=-1

    while(m>1):
        i=min(offset+fibonacciGenerator(m-2), len(arr)-1)
        if(arr[i] < x):
            m=m-1
            offset = i
        elif(arr[i]>x):
            m=m-2
        else:
            return i
    return -1

arr = [2,3,5,7,9,13,15,24,31]
x=13
index = fibonacciSearch(arr, x)
print(index)

