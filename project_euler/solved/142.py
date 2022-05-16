# ALGEBRA

# Let x+y=a**2, x-y=b**2, x-z=c**2
# We get: x+z=a**2+b**2-c**2, y+z=a**2-c**2, y-z=c**2-b**2
# So, we need a, b and c such that x+z, y+z and y-z are squares
# Look at y+z and y-z, they can be found as pythagorean triplets
# such that c is common in both triplets
# Then, just check if x+z is also square

import math
from operator import itemgetter

# For ascendingly sorted array
def srch(a, n1, n2, b):
    k = n1
    while k < n2:
        if a[k][0] == b:
            return k
        k += 1
    return

def is_sqrn(n):
    ''' (int) -> logical
        To check if a non-negative integer n is a square number
        Sq(n) = n * n
    '''
    if n % 4 == 0 or n % 8 == 1:
        r = round(math.sqrt(n))
        if r * r == n:
            return True
    return False

def gcd(a, b):
    ''' (int, int) -> int
        Computes GCD or HCF using Euclidean Algorithm
    '''
    while b != 0:
        c = b
        b = a % c
        a = c
    return a

def pgts(m1, n1, k1):
    ''' (int, int, int) -> list of tuples
        Generates all Pythagorean Triplets using
        Euclid's Formula upto some limit
    '''
    ptl = []
    for n in range(1, n1):
        for m in range(n+1, m1, 2):
            if gcd(n, m) == 1:
                k = 1
                for k in range(1, k1):
                    m2 = m * m
                    n2 = n * n
                    pl = (k * (m2 - n2), 2 * k * m * n, k * (m2 + n2))
                    ptl.append(pl)
    return ptl

def fx(a, b, c):
    return a * a + b * b - c * c

def sxyz(a, b, c):
    x = (a * a + b * b) / 2
    y = (a * a - b * b) / 2
    z = x - c * c
    return x + y + abs(z)

pgs = pgts(100, 100, 10)
pgs.sort(key = itemgetter(0))
np = len(pgs)

cc = True
k = 0
while cc:
    na = srch(pgs, 0, np, pgs[k][2])
    if na:
        m = 0
        b1 = pgs[k][0]
        b2 = pgs[k][1]
        c = pgs[k][2]
        while pgs[na + m][0] == c:
            a = pgs[na + m][2]
            if is_sqrn(fx(a, b1, c)):
                print(sxyz(a, b1, c))
                cc = False
            if is_sqrn(fx(a, b2, c)):
                print(sxyz(a, b2, c))
                cc = False
            m += 1
    k += 1
