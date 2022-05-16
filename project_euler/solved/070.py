# MATH (with some REASONABLE TRIAL-AND-ERROR)

# From the known formula of Totient Function
# our best possibility is that the number we are
# looking for is composed of two primes which are
# as near to sqrt(10**7) as possible

import math

def is_perm(s1, s2):
    """ (str, str) -> bool
    """
    for s in s1:
        if s1.count(s) != s2.count(s):
            return False
    return True

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

prms = primes_soe(10000)
np = len(prms)
print('Primes generated...')

pl = []
for i in range(np):
    for j in range(i+1, np):
        p = prms[i] * prms[j]
        if p < 10000000:
            phi = p-prms[i]-prms[j]+1
            if is_perm(str(p), str(phi)):
                pl.append([p/phi, p, phi])
pl.sort()
print(pl[0])
