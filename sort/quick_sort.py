from swap import swap
# array as 0 indexed and the end is always included when passing in the r

def quick_sort(arr,p,r):
    if r >p :
        pivot = partition(arr,p,r)
        quick_sort(arr,p,pivot-1)
        quick_sort(arr,pivot+1,r)
    return arr
def partition(arr,p,r):
    key = arr[r]
    i = p-1
    for j in range(p,r):
        if arr[j] < key:
            i+=1
            swap(arr,i,j)
    swap(arr,i+1,r)
    return i+1
if __name__=="__main__":
    arr =[1,2,34,123,412,35,125,12,34,1234,123,41,235,1235,123,41,235,123,4]
    new_arr = arr.copy()
    sorted_arry = quick_sort (new_arr,0,len(arr)-1)
    print(sorted_arry)
    new_arr.sort()
    print(arr)
    print(new_arr== sorted_arry)