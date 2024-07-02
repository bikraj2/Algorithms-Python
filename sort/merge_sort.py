import math
def merge_sort(arr,p,q):
    if q>p :
        r =  (p+q)//2
        merge_sort(arr,p,r)
        merge_sort(arr,r+1,q)
        merge(arr,p,r,q)
    return arr
def merge(arr,p,q,r):
    left_arr =[arr[i] for i in range(p,q+1)]
    right_arr =[arr[i] for i in range(q+1,r+1)]
    left_arr.append(math.inf)
    right_arr.append(math.inf)
    i,j=0,0
    for k in range(p,r+1):
        if left_arr[i]<right_arr[j]:
            arr[k] =left_arr[i]
            i=i+1
        else :
            arr[k] =right_arr[j]
            j+=1

if __name__=="__main__":
    arr =[1,2,34,123,412,35,125,12,34,1234,123,41,235,1235,123,41,235,123,4]
    new_arr = arr.copy()
    sorted_arry = merge_sort(new_arr,0,len(arr)-1)
    print(sorted_arry)
    new_arr.sort()
    print(new_arr== sorted_arry)