# RECIPROCAL DIOPHANTINE EQUATION

# On the similar lines of 108 and 110,
# Since p*a,p*b>10**n, we put p*a=10**n+x, p*b=10**n+y.
# Solving, it gives 100**n=x*y.
# The number of (p*a,p*b) will be distinct pairs of (x,y).
# However, we want solutions in distinct (a,b,p).
# So we need to look at all pairs (x,y) and count divisors
# of gcd(x,y), which will give total number of triplets (a,b,p)

# Implementation is quite poor:
# Most of the time goes in generating 70 million
#   primes needed to count number of divisors.
#   This can be improved with a better algorithm for
#   counting divisors.
# Next, one can directly generate factors of 100**n and need
#   not apply a factorization algorithm for it.

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

def fctrs_tdm(n):
    ''' (int) -> list

        Function to get all factors of n using Trial Division method
        Resulting list is ascendingly sorted and also contains 1 and n
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
    return fc2

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

def ndvsrs(n):
    ''' (int) -> tuple
        To get all prime divisors of a positive integer
        It accounts for multiplicity of a divisor

        It needs prms list containing list of primes at least
        up to n, use prm_ert_upto_n_lst(n) for that before
        calling this function

        >>> pdvsrs(360)
        (2, 2, 2, 3, 3, 5)
    '''
    k = 0
    dvs = []
    while prms[k] <= n:
        if n % prms[k] == 0:
            dvs.append(prms[k])
            n //= prms[k]
        else:
            k += 1
    nd = 1
    i = 1
    for m in range(len(dvs) - 1):
        if dvs[m] != dvs[m + 1]:
            nd *= (i + 1)
            i = 0
        i += 1
    nd *= (i + 1)
    return nd

prms = primes_soe(70000000)

s = 0
for n in range(1, 10):
    fcs = fctrs_tdm(10 ** (2 * n))
    nf = len(fcs)
    for i in range(nf >> 1):
        s += ndvsrs(gcd(fcs[i] + 10 ** n, fcs[nf - i - 1] + 10 ** n))
    s += ndvsrs(2 * 10 ** n)
print(s)
