def bubbleSort(arr):
    n=len(arr)
    for i in range(0,n-1):
        flag=0
        for j in range(0,n-1-i):
            if(arr[j] >arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1]= temp
                flag =1
        if(flag == 0):
            break
    return arr

arr = [12,5,3,16,1,9] 
arr1 = bubbleSort(arr)
print(arr1)
