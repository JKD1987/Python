def merge(a, l, r):
    i=j=k=0
    while(i<len(l) and j<len(r)):
        if(l[i]<r[j]):
            a[k] = l[i]
            i = i+1
        else:
            a[k]=r[j]
            j=j+1
        k=k+1
    if(i<len(l)):
        while(i<len(l)):
            a[k]=l[i]
            i=i+1
            k=k+1
    elif(j<len(r)):
        while(j<len(r)):
            a[k]=r[j]
            j=j+1
            k=k+1
    return a


def mergeSort(a):
    if(len(a)>1):
        mid = int(len(a)/2)
        l = a[:mid]
        r = a[mid:]
        print(l)
        print(r)
        mergeSort(l)
        mergeSort(r)
        return(merge(a, l, r))

arr = [12,5,3,16,1,9] 
arr1 = mergeSort(arr)
print(arr1)