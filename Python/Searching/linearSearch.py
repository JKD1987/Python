def linerSearch(arr, x):
    present = False;
    for i in range(0, len(arr)):
        if(x==arr[i]):
            print(x, "is available in the input array at index", i)
            present = True
    if(present == False):
        print(x, "is not present in the input array");


arr = [2,3,8,6,23,54,32]
x = 23
linerSearch(arr, x)
x=53
linerSearch(arr,x)
