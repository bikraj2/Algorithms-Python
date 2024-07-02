from swap import swap
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)-1):
            if arr[j] > arr [j+1]:
                swap(arr,j,j+1)
    return arr


if __name__=="__main__":
    arr =[1,2,34,123,412,35,125,12,34,1234,123,41,235,1235,123,41,235,123,4]
    new_arr = arr.copy()
    sorted_arry = bubble_sort(new_arr)
    print(sorted_arry)
    new_arr.sort()
    print(arr)
    print(new_arr== sorted_arry)