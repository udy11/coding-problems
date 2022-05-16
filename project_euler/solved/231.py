# ALGORITHM

# The function npc() gives number of occurences of a prime
# in (n1, n2], which is all you need. npc() uses simple
# fact that a prime p comes between 1 and n this many times:
# n // p + n // p**2 + n // p**3 + ...
# Rest is straightforward
# Most of the time goes into generation of 20 million
# prime numbers

# This link is worth checking:
# http://www.numbertheory.org/php/binomial.html

import math

def npc(p, n1, n2):
    ''' (int, int) -> int

        Returns number of occurences of prime p
        between n1 (exclusive) and n2 (inclusive)
    '''
    p0 = p
    c1 = n1 // p0
    while p <= n1:
        p *= p0
        c1 += n1 // p
    p = p0
    c2 = n2 // p0
    while p <= n2:
        p *= p0
        c2 += n2 // p
    return c2 - c1

def bsan_asc(a, n1, n2, b):
    if b > a[n2 - 1]:
        return n2 - 1
    if b < a[n1]:
        return n1
    nd = n2 - n1
    nm = n1 + nd // 2
    while nd > 1:
        if a[nm] > b:
            n2 = nm
        else:
            n1 = nm
        nd = n2 - n1
        nm = n1 + nd // 2
    d1 = b - a[n1]
    d2 = a[n2] - b
    if d1 < d2:
        return n1
    else:
        return n2

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

prms = primes_soe(20000000)
mu = len(prms)
su = 0
for i in range(mu):
    su += npc(prms[i], 15000000, 20000000) * prms[i]
md = bsan_asc(prms, 0, mu, 5000000)
sd = 0
if prms[md] > 5000000:
    md -= 1
for i in range(md + 1):
    sd += npc(prms[i], 1, 5000000) * prms[i]
print(su - sd)
