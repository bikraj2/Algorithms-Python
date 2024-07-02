from swap import swap
def insertion_sort(arr):
    for i in range(1,len(arr)) :
        j = i
        key = arr[i]
        while j >0 and arr[j-1] > key :
            arr[j] =arr[j-1]
            j-=1
        arr[j] = key
    return arr
if __name__=="__main__":
    print(insertion_sort([1,3,5,1,123,14,1,414,14,14,14,12,341,234,412,-10,-123]))
        