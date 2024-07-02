def binary(arr,val,s,e):
    if e >= s :
        mid = (s+e)//2
        if arr[mid]==val:
            return mid
        elif arr[mid] > val:
            return binary(arr,val,s,mid -1 )
        else:
            return binary(arr,val,mid+1,e)
    return -1
if __name__ =="__main__":
    arr = [1,2,3,4,5,6,7,8,9,10]
    print(binary(arr,10,0,len(arr)))
