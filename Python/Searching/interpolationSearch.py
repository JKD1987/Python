def interpolationSearch(arr, lo, hi, x):
    if(hi>lo):
        pos = lo + int(((x-arr[lo])*(hi-lo))/(arr[hi]-arr[lo]))
        if(pos < len(arr) and arr[pos]==x):
            return int(pos)
        elif(pos < len(arr) and arr[pos] > x):
            return interpolationSearch(arr, lo, pos-1, x)
        else:
            return interpolationSearch(arr, pos+1, hi, x)
    else:
        return -1


arr = [1, 2, 4, 8, 12, 16, 20]
x=0
count = 0
index = interpolationSearch(arr, 0, len(arr)-1, x)
print(index)