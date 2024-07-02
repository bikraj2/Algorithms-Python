
def NQueens(arr,k,n):
    for i in range(n):
        if place(arr,k,i):
            arr[k] =i
            if k==n-1:
                print(arr)
            else:
                NQueens(arr,k+1,n)
def place(arr,k,i):
    for j in range(k):
        if arr[j] == i or (abs(arr[j] -i) == abs(j-k)):
            return False
    return True
if __name__ == "__main__":
    NQueens([None]*4,0,4)