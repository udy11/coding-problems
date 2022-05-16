# RECIPROCAL DIOPHANTINE EQUATION

# Do some coordinate geometry to get a relation between
# ra, rb and rc. Take contact point of L and A as origin
# and L as x-axis. Then after some simple math, one obtains:
# 1 / sqrt(ra) + 1 / sqrt(rb) = 1 / sqrt(rc)
# which is similar to a reciprocal diophantine equation
# One may also get to this equation from geometry, but i
# don't know how.
# Anyways, now to solve this, simply put:
# sqrt(ra) = sqrt(rc) + x and sqrt(rb) = sqrt(rc) + y
# which gives: x*y = rc
# All that one needs is to get divisors of rc and for every
# coprime x and y, one will get an appropriate (ra, rb, rc)
# Note that since we need rc to be perfect square, one
# can iterate directly on squares only
# Also, one will need to add all multiples of obtained
# (ra, rb, rc) triplets upto the required limit of rb,
# which is given as 10**9

# Implementation is rather poor.
# Once can have a much better divisors function
# One also need not go upto 10**9 for rc, its limit
# should be smaller than this
# And a sieve approach for divisors may be faster, not
# sure though
# One may also think of directly producing coprime
# divisor pairs for rc rather than checking gcd
# every time

import math

def gcd(a, b):
    ''' (int, int) -> int
        Computes GCD or HCF using Euclidean Algorithm
    '''
    while b != 0:
        c = b
        b = a % c
        a = c
    return a

def fctrs2_tdm(n):
    ''' (int) -> list

        Function to get all factors of n**2 using Trial Division method
        Resulting list is ascendingly sorted and also contains 1 and n**2
    '''
    if n < 1:
        return []
    ch = n == (n >> 1) << 1
    c2 = 1
    while ch:
        c2 += 1
        n = n >> 1
        ch = n == (n >> 1) << 1
    fc = [1, n]
    for i in range(2, 1 + math.ceil(math.sqrt(n))):
        if n % i == 0:
            fc.append(i)
            fc.append(n // i)
    if fc[-1] * fc[-1] == n:
        fc.pop()
    fc2 = list(fc)
    for i in range(1, c2):
        fc2 += [2 ** i * f for f in fc]
    fc2.sort()
    fc = list(fc2)
    for k1 in range(len(fc)):
        for k2 in range(1, k1 + 1):
            if not fc[k1] * fc[k2] in fc2:
                fc2.append(fc[k1] * fc[k2])
    fc2.sort()
    return fc2

n = 10**9
ss = 0
for c in range(1, math.floor(math.sqrt(n)) + 1):
    dv = fctrs2_tdm(c)
    m = len(dv)
    for i in range(m // 2 + 1):
        if gcd(dv[i], dv[m - i - 1]) == 1:
            a = c + dv[i]
            b = c + dv[m - i - 1]
            mm = math.floor(n / b / b)
            ss += (a * a + b * b + c * c) * (mm + 1) * mm // 2
print(ss)
