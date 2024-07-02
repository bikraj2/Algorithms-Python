from swap import swap
heap_size =0
def heap_sort(arr):
    global heap_size
    build_heap(arr)
    for i in range(len(arr)-1,0,-1):
        swap(arr,0,i)
        heap_size -=1
        max_heapify(arr,0)
    return arr
def max_heapify(arr,i):
    l = 2*i + 1
    r = 2*i + 2
    largest =i
    if l<= heap_size and arr[l] > arr[i]:
        largest = l
    else :
        largest =i
    if r <=heap_size and arr[r] > arr[largest]:
        largest =r
    if largest !=i :
        swap(arr,i,largest)
        max_heapify(arr,largest)

def build_heap(arr):
    global heap_size
    heap_size = len(arr)-1
    for i in range(len(arr)//2-1 , -1,-1):
        max_heapify(arr,i)
    
if __name__=="__main__":
    arr =[1,2,34,123,412,35,125,12,34,1234,123]
    new_arr = arr.copy()
    
    print(heap_sort(new_arr))
    # print(sorted_arry)
    # new_arr.sort()
    # print(new_arr== sorted_arry)