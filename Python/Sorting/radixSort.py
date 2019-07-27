def getMax(a):
    max = a[0]
    n = len(a)
    for i in range(0, n-1):
        if(a[i] > max):
            max = a[i]
    return max

def radixSort(a):
    n = len(a)
    maxnum = getMax(a)
    pos=1
    while(int(maxnum/pos) > 0):
        countingSort(a,pos)
        pos = pos *10
    return a

def countingSort(a, pos):
    n = len(a)
    count = [0]*10
    for i in range(0,n):
        indx = int(a[i]/pos)%10
        count[indx] +=1
    for j in range(1,len(count)):
        count[j] = count[j] + count[j-1]
    k=n-1
    b=[0]*n
    while(k>=0):
        indx1 = int(a[k]/pos)%10
        count[indx1]-=1
        b[count[indx1]]= a[k]
        k-=1
    for i in range (0,n):
        a[i] = b[i]

arr = [8,1,56,33,237, 533, 677, 131]
print("Original Array : " , arr)
arr1 = radixSort(arr)
print("Sorted Array : ", arr1)