def swap(arr,i,j):
    temp = arr[i]
    arr[i]=arr[j]
    arr[j] = temp

def test_swap():
    arr =[1,2,3,4,5,6]
    swap(arr,0,-1)
    print(arr)
if __name__ == "__main__":
    test_swap()