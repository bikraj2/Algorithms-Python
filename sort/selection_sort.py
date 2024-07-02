from swap import swap
def selection_sort(arr):
    for i in range(len(arr)-1):
        sml = i
        for j in range(i,len(arr)):
            if arr[j] < arr[sml]:
                sml = j
        swap(arr,i,sml)
    return arr
if __name__=="__main__":
    print(selection_sort([1,3,5,1,123,14,1,414,14,14,14,12,341,234,412,-10,-123]))
    