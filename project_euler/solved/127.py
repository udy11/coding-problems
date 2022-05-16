# MATH

# Note that if gcd(c, b)=1 then gcd(c, c-b)=1
# c cannot be of form p0*p1*...*pn (p are primes)
# rad(a*b*c) < c is equivalent to rad(a)*rad(b)*rad(c) < c for coprimes a,b,c
# Use sieve to get all primes, prime divisors and rad upto n
# Use prime divisors of c to get coprimes

# In forums, people have further suggested that gcd(b, c) and gcd(a, c) need not be checked if gcd(a, b)=1
# People have also found limits on a or b using rad(a*b*c) < c condition

# C++ version of the algorithm takes about 2.2 seconds but
# its Python-3 version takes about 10 minutes

# Relevant resources:
# abc Conjecture
# OEIS A130510, A120498, A007947
# http://www.phfactor.net/abc/index.php

import math
import time

def bgcd(a, b):
    ''' (int, int) -> int
        Computes GCD or HCF using Binary GCD/Stein's Algorithm
    '''
    if a == 0:
        return b
    if b == 0:
        return a
    k = 0
    while (a | b) & 1 == 0:
        a >>= 1
        b >>= 1
        k += 1
    while a & 1 == 0:
        a >>= 1
    while b != 0:
        while b & 1 == 0:
            b >>= 1
        if a > b:
            t = b
            b = a
            a = t
        b -= a
    return a << k

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

n = 120000
prms = primes_soe(n)
nprms = len(prms)

# store all prime divisors, their counts and rad in pdvs, cpdvs and rad
pdvs = [[] for k in range(n)]
cpdvs = [[] for k in range(n)]
rad = [1 for k in range(n)]
for p in prms:
    for j in range(p, n, p):
        rad[j] *= p
        pdvs[j].append(p)
for k in range(n):
    for d in pdvs[k]:
        k0 = k
        i = 0
        while k0 % d == 0:
            k0 //= d
            i += 1
        cpdvs[k].append(i)
pdvs[0].append(1)
pdvs[1].append(1)
cpdvs[0].append(1)
cpdvs[1].append(1)

start = time.process_time()

# c should not be of form p0*p1*...*pk
cs = []
for k in range(n):
    if any([i > 1 for i in cpdvs[k]]):
        cs.append(k)

tc = 0
for c in cs:
    c2 = (c + 1) // 2
    cc = [True for i in range(c2)]    # cc will define coprimes of c
    for p in pdvs[c]:
        for j in range(p, c2, p):
            cc[j] = False
    for i in range(1, c2):
        if cc[i] and rad[i] * rad[c-i] * rad[c] < c and bgcd(i, c-i) == 1:
            tc += c
print(tc)
print(time.process_time() - start)
# 456, 18407904
