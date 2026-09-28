import math

def binomial_probability(n: int, k: int, p: float) -> float:
    
    # the formula is n! /(n-r)!r! *p**r *(1-p)**n-r

    ncr =0
    total=1
    for i in range(1,n+1):
        total*=i
    rtotal=1
    for i in range(1,k+1):
        rtotal*=i
    
    subtotal =1
    x=n-k
    for i in range(1,x+1):
        subtotal*=i
    
    ncr = (total)/(rtotal*subtotal)

    second = p**k
    third = (1-p) **x

    return ncr * second* third