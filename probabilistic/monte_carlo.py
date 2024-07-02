import random
import math
def fermat_primality_test(n,k):
    for i in range(k):
        a = random.randint(2,n-2)
        if pow(a,n-1) %n != 1:
            return False
    return True
def miller_rabin_test(n,k):
    s=0
    d=0
    i=0
    while pow(2,i) < n:
        if (n -1) % pow(2,i) !=0:
            s = i - 1
            d = int((n-1) / pow(2,i-1))
            break
        i+=1
    for i in range(k):
        a  = random.randint(2,n-1)
        x = pow(a,d,n) 
        if x==1 or x == n-1:
            continue
        for i in range(s-1):
            x = pow(x,2,n)
            if x==n-1:
                break
            elif x ==1:
                return False
    return True


        
if __name__== "__main__":
    print(fermat_primality_test(567,1))
    print(miller_rabin_test(22,10))
