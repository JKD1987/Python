def partition(a, lb, ub):
    pivot = a[lb]
    start = lb
    end = ub

    while(start<end):
        while(a[start] <= pivot):
            start = start+1
        while(a[end]> pivot):
            end = end -1
        if(start < end):
            temp = a[start]
            a[start] = a[end]
            a[end] = temp
    a[lb] = a[end]
    a[end]=pivot
    return end

def quickSort(a, lb, ub):
    if(lb<ub):
        loc = partition(a, lb, ub)
        quickSort(a, lb, loc-1)
        quickSort(a, loc+1, ub)
    return a




arr = [12,5,3,16,1,9] 
arr1 = quickSort(arr, 0, len(arr)-1)
print(arr1)