# IDEA:
# Make a list of all such numbers
# using pretty much a brute force method
# Then count distinct numbers in the list

# The program can have further optimizations

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

prms = primes_soe(7079)

i = 0
nl = []
while i < 24:
    n = 50000000 - prms[i] ** 4
    j1 = 0
    while True:
        if prms[j1] ** 3 - n > 0:
            break
        j1 += 1
    j = 0
    while j < j1:
        k1 = 0
        m = n - prms[j] ** 3
        while True:
            if prms[k1] ** 2 - m > 0:
                break
            k1 += 1
        for kk in range(k1):
            nl.append(prms[i]**4 + prms[j]**3 + prms[kk]**2)
        j += 1
    i += 1
nl.sort()
nl1 = nl[0]
c = 1
for i in range(1, len(nl)):
    nl2 = nl[i]
    if nl2 > nl1:
        c += 1
    nl1 = nl2
print(c)
