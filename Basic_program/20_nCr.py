import math

def fact(n):
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial * i
    return factorial

def nCr(n,r):
    numerator = fact(n)
    denominator = fact(r) * fact(n-r)
    return math.floor(numerator/denominator)

ans = nCr(8,2)
print(ans)