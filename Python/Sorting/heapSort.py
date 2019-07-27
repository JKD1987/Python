
def max_heapify(a, heap_size, i):
    l = 2*i+1
    r=2*i+2
    if(l<heap_size and a[l]>a[i]):
        largest = l
    else:
        largest = i
    if(r<heap_size and a[r] >a[largest]):
        largest = r
    if(largest != i):
        temp = a[largest]
        a[largest] = a[i]
        a[i] = temp
        max_heapify(a, heap_size, largest)


def build_max_heap(a):
    heap_size = len(a)
    print("Originl Array: ",a)
    i=int(len(a)/2)-1
    while(i>=0):
        max_heapify(a, heap_size, i)
        i-=1

def heapSort(a):
    build_max_heap(a)
    print("Max_heapified_array: ", a)
    heap_size = len(a)
    i= len(a)-1
    while(i>0):
        temp = a[i]
        a[i] = a[0]
        a[0] = temp
        heap_size= heap_size -1
        max_heapify(a, heap_size, 0)
        i-=1
    print("Sorted Array: ",a)


arr = [12,4,1,10,5,8,13,2,6,3,17,7,15,20,11,16,19,14,9,18]
heapSort(arr)
#arr1 = heapSort(arr)
#print(arr1)