# CUBAN PRIMES

# It follows that n * (n+p)**(1/3) / n**(1/3) = m
# for some positive integer m. If we assume that
# n is not a perfect cube itself, then n**(1/3)
# will be irrational and (n+p)**(1/3) will either not
# be irrational or be an irrational such that its
# irrational part does not cancel against irrational
# part of n**(1/3). In either of these, n and m won't
# be integers. Hence n must be a perfect cube and
# consequently n+p should also be. Let n = x**3 and
# n+p = y**3, then p = y**3-x**3 = (y-x)*(y**2+y*x+x**2).
# Since p is prime, y-x=1, i.e., p=(x+1)**3-x**3.
# Such primes are called Cuban Primes (OEIS A002407).
# OEIS also has sequence for number of Cuban Primes
# below 10**k (OEIS A113478).

import math

def bsa_asc(a, n1, n2, b):
    if b > a[n2 - 1]:
        return False
    if b < a[n1]:
        return False
    nd = n2 - n1
    nm = n1 + nd // 2
    while nd > 1:
        if a[nm] > b:
            n2 = nm
        else:
            n1 = nm
        nd = n2 - n1
        nm = n1 + nd // 2
    if a[n1] == b:
        return True
    elif a[n2] == b:
        return True
    else:
        return False

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

prms = primes_soe(1000000)
np = len(prms)

i = 1
p = 7
c = 0
while p < 1000000:
    if bsa_asc(prms, 0, np, p):
        c += 1
    i += 1
    p = (i + 1) ** 3 - i ** 3
print(c)
