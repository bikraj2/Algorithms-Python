memo = None
def fib(n):
    if n <=1:
        return n 
    else :
        if memo[n] !=None:
            return memo[n]
        else :
            memo[n]=fib(n-1) + fib(n-2)
            return memo[n]


if __name__ == "__main__":
    n=30
    memo = [None] * (n+1)
    print(fib(n))