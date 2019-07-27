def selectionSort(a):
    n = len(a)
    for i in range(0,n):
        min = i
        for j in range(i+1,n):
            if(a[j] < a[min]):
                min = j
        if(min != i):
            temp = a[min]
            a[min] = a[i]
            a[i] = temp
    return a

arr = [12,5,3,16,1,9] 
arr1 = selectionSort(arr)
print(arr1)