def insertionSort(a):
    n= len(a)
    for i in range(1,n):
        temp = a[i]
        j=i-1
        while(j>=0 and a[j] > temp):
            a[j+1] = a[j]
            j = j-1
        a[j+1] = temp
    return arr
    
arr = [12,5,3,16,1,9] 
arr1 = insertionSort(arr)
print(arr1)