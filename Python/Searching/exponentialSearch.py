def exponentialSearch(arr, x):
    i = 1;
    while(i<len(arr) and arr[i] <= x):
        i = i*2
    return binarySearch(arr, i/2, min(i,len(arr)-1), x)

def binarySearch(arr, l,r,x):
    if(r>l):
        mid = int((l+r-1)/2)
        if(arr[mid]==x):
            return mid
        elif(arr[mid] > x):
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid+1, r, x)
    else:
        return -1

arr = [1, 2, 4, 8, 12, 16, 20]
x=16
index = exponentialSearch(arr, x)
print(index)