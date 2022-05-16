import math
import numpy as np
import time

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

def divsum(pdvs):
    s = 1
    for p in pdvs:
        s *= (p ** (pdvs[p] + 1) - 1) // (p - 1)
    return s

def divsum1(pdvs, md):
    s = 1
    for p in pdvs:
        s *= ((p ** (pdvs[p] + 1) - 1) // (p - 1)) % md
    return s

def prime_power_int(prms, n0):
    nprms = len(prms)
    k = 0
    pdvs = {}
    n = n0
    while k < nprms and prms[k] <= n:
        if n % prms[k] == 0:
            n = n // prms[k]
            pc = 1
            while n % prms[k] == 0:
                n = n // prms[k]
                pc += 1
            pdvs[prms[k]] = pc
        k += 1
    if n > 1:
        pdvs[n] = 1
    return pdvs

def merger(a1, b1):
    z = a1.copy()
    for b in b1:
        z[b] += b1[b]
    return z

def merger2(a1, k, b1, c1):
    z = a1.copy()
    for b in b1:
        z[b] += (k - 1) * b1[b]
    for c in c1:
        z[c] -= c1[c]
    return z

n = 11
md = 1000000007
primes = primes_soe(n)
nprimes = len(primes)

# prime divisors of numbers from 2 to n
pdvs = {}
tym0 = time.time()
for k in range(2, n):
    pdvs[k] = prime_power_int(primes, k)

# prime divisors of factorial of numbers from 2 to n
##fpdvs = {2 : pdvs[2].copy()}
##jp = 1
##for k in range(3, n):
##    if jp < nprimes and k == primes[jp]:
##        fpdvs[k] = fpdvs[k-1].copy()
##        fpdvs[k][k] = 1
##        jp += 1
##    else:
##        fpdvs[k] = merger(fpdvs[k-1], pdvs[k])

# sum of divisors of numbers up to n
nsig = [0 for k in range(n)]
nsig[0] = 1
nsig[1] = 1
for k in range(2, n):
    nsig[k] = divsum(pdvs[k])

# sum of divisors of factorials
fsig = [0 for k in range(n)]
fsig[0] = 1
fsig[1] = 1
for k in range(2, n):
    fsig[k] = int(int(nsig[k]) * int(fsig[k-1]))

# sum of divisors of factorials
bsig = [0 for k in range(n)]
bsig[0] = 1
bsig[1] = 1
for k in range(2, n):
    bsig[k] = int(bsig[k-1]) * int(nsig[k])**(k-1) // int(fsig[k-1])

# prime divisors of B(k), k from 2 to n
##bpdvs = {2 : fpdvs[2].copy()}
##jp = 1
##for k in range(3, n):
##    if jp < nprimes and k == primes[jp]:
##        a1 = bpdvs[k-1].copy()
##        a1[k] = 0
##        bpdvs[k] = merger2(a1, k, pdvs[k], fpdvs[k-1])
##        jp += 1
##    else:
##        bpdvs[k] = merger2(bpdvs[k-1], k, pdvs[k], fpdvs[k-1])
##
##s = 4    # including sums for B(1) and B(2)
##for k in range(3, n):
##    nt = divsum(fpdvs[k], md)
##    s = (s + nt) % md
##print(s)
print('time taken:', time.time() - tym0, 's')
