

def fib(n):
    memo=[0 for i in range(n+2)]
    memo[1] =1
    for i in range(2,n+2):
        memo[i] =memo[i-1] +memo[i-2]
    return memo[n]
if __name__ == "__main__":
    n=30
    memo = [None] * (n+1)
    print(fib(n))