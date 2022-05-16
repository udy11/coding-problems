# MODULAR MULTIPLICATIVE INVERSE

# Note that S(p) = 9 * (p - 5)! (mod p)
# To get (p - 5)! (mod p), use modular inverse, i.e.
# (p-5)! (mod p) = - [(p-4)(p-3)(p-2)(p-1)]^(-1) (mod p),
# which can be calculated using Extended Euclidean Algorithm

# Lucy_Hedgehog in forums has suggested a simple form of S(p),
# which I think comes from this:
# 9*(p-5)! (mod p) = 3*(p-1)!/8 (mod p)
# and (p-1)! (mod p) = (p-1) by Wilson's Theorem
# But I could not figure out how it could be implemented

# It takes quite some time in python, but a c++
# implementation should run faster
# And Linear Diophantine Equation solver can be optimized
# for this particular problem

import math

def fct(n):
    ''' (int) -> int
        To calculate factorial defined as:
        F(n) = 1*2*3* ... *n (for n>0)
        F(0) = 1
    '''
    if(n < 2):
        return 1
    f = n
    for i in range(2, n):
        f *= i
    return f

def lindioeq(a, b, c, nn):
    ''' (int, int, int, list/tuple) -> list of (int, int)
        Solves the Linear Diophantine Equation for (x, y):
        a * x + b * y == c, all integers
        Using Extended Euclidean Algorithm
    '''
    g = a
    b0 = b
    qq = []
    while b0 != 0:
        t = b0
        b0 = g // t
        qq.append(b0)
        b0 = g - b0 * t
        g = t
    if c % g != 0:
        return []
    s0 = 1; s1 = 0
    t0 = 0; t1 = 1
    for q in qq:
        t = s1
        s1 = s0 - q * t
        s0 = t
        t = t1
        t1 = t0 - q * t
        t0 = t
    a0 = a // g
    b0 = b // g
    c0 = c // g
    xy = []
    for n in nn:
        xy.append((c0 * s0 - n * b0, c0 * t0 + n * a0))
    return xy

def primes_soe(n):
    ''' (int) -> list of int
        Function to generate list of prime numbers
        using the sieve of Eratosthenes
        n = upto which primes are needed (inclusive)
    '''
    if n < 2:
        return []
    n2 = (n - 1) // 2
    prms = [2] * (n2 + 1)
    ip = [True for i in range(n2)]
    k = 3
    nsq = round(math.sqrt(n))
    while k <= nsq:
        for i in range(k * k // 2 - 1, n2, k):
            ip[i] = False
        while k <= nsq:
            k += 2
            if ip[k // 2 - 1]:
                break
    m = 1
    for i in range(n2):
        if ip[i]:
            prms[m] = 2 * i + 3
            m += 1
    return prms[:m]

n = 99999999
prms = primes_soe(n)
prms.pop(0)
prms.pop(0)

s = 0
for p in prms:
    t = lindioeq((p - 4) * (p - 3) * (p - 2) * (p - 1), -p, 1, [0])
    s += (-9 * t[0][0]) % p

print('Sum:', s)
