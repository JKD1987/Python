def getMax(a):
    max = a[0]
    n= len(a)
    for i in range (0,n-1):
        if(a[i] > max):
            max = a[i]
    return max
        

def countingSort(a):
    n=len(a)
    maxnum = getMax(a)
    count = [0]*(maxnum+1)
    for i in range(0, n):
        count[a[i]]+=1
    print(count)
    for j in range(1,len(count)):
        count[j] = count[j]+count[j-1]
    print(count)
    k=len(a)-1
    b=[0]*n
    while(k>=0):
        count[a[k]] -=1
        b[count[a[k]]] = a[k] 
        k-=1
    print(a)
    print(b)

arr = [1,2,5,3,4,2,6,1,2,7,9,1,3,2,5]
countingSort(arr)