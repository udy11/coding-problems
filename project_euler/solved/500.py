# SIEVE (pretty much.. perhaps..)

# Number of divisors of p1**n1 * p2**n2 ...
# is (n1+1)*(n2+1)*...
# Hence to have 2**500500 divisors, you need
# only 2**n-1 powers of primes like
# 2**1, 2**3, 2**7, 2**15... like that.
# If you have already multiplied 2**1, then for
# 2**3, you only need to multiply 2**2 and similarly
# for later 2**4, 2**8... like that :P
# Generating such numbers and sorting is one way
# or sieve the natural numbers, which are already sorted
# Then simply count when you have reached the limit

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

n = 500500
pp = 7400000
prms = primes_soe(pp)
np = len(prms)
pl = prms[-1]
sa = [False for i in range(pp)]
for p in prms:
    k = 0
    t = p
    while t < pl:
        sa[t] = True
        k += 1
        t = p ** (2 ** k)

num = 1
c = 0
k = 0
while c < n:
    k += 1
    if sa[k]:
        c += 1
        num *= k
        num = num % 500500507
print(num)
