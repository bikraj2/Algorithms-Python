def counting_sort(arr):
    count_arr =[0 for i in range(max(arr)+1)]
    sorted_array =[0 for i in range(len(arr))]
    for j in range(len(arr)):
        count_arr[arr[j]]+=1
    for j in range(1,len(count_arr)):
        count_arr[j] = count_arr[j] + count_arr[j-1]
    for j in range(len(arr)):
        sorted_array[count_arr[arr[j]]-1] = arr[j]
        count_arr[arr[j]] -=1
    return sorted_array
if __name__=="__main__":
    arr =[1,2,34,123,412,35,125,12,34,1234,123,41,235,1235,123,41,235,123,4]
    new_arr = arr.copy()
    sorted_arry = counting_sort(new_arr)
    print(sorted_arry)
    arr.sort()
    print(arr)
    print(arr== sorted_arry)