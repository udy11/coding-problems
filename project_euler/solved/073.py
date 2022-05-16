# (Pretty much) BRUTE-FORCE

# See how many coprimes are there in (1/3,1/2) of an integer

import math

def gcd(a, b):
    while b != 0:
        c = b
        b = a % c
        a = c
    return a

def ndvs(n):
    ndv = []
    n1 = math.floor(n/3)+1
    n2 = math.ceil(n/2)
    for i in range(n1, n2):
        if gcd(i, n) == 1:
            ndv.append(i)
    return ndv

def cndvs(n):
    cndv = 0
    n1 = math.floor(n/3)+1
    n2 = math.ceil(n/2)
    for i in range(n1, n2):
        if gcd(i, n) == 1:
            cndv += 1
    return cndv

s = 0
for i in range(4, 12001):
    s += cndvs(i)
print(s)
