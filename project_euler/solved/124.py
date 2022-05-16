# SIEVE

# Basic idea is to generate radical using Sieve method

# I used an inbuilt sort, but that much is ok

import math
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

n = 100000

prms = primes_soe(n)

rad = [[1, i] for i in range(1, n+1)]
for p in prms:
    for j in range(p, n+1, p):
        rad[j-1][0] *= p

rad.sort()
print(rad[9999][1])
