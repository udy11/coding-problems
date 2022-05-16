# MATH

# Riffle Shuffle will revert to original if any of its index
# reverts to original position. Riffle Shuffle basically changes
# index i to j such that:
# j = (2 * i) % (n - 1)
# if n is the size of pack and indices start from 0.
# So, index 1 reverts back in m steps when:
# (2**m) % (n-1) == 1
# Equivalently,
# 2**m == p * (n-1) + 1, or
# n = (2**m - 1) / p
# So, for a given m, n & p are the divisors of (2**m - 1)
# However, if a riffle shuffle repeats in 30 turns, it will repeat
# in 60 turns as well. Thus to find the uniques solutions for 60,
# we will have to eliminate solutions for divisors of 60.

# Check out "Multiplicative Order"

import math

# Riffle Shuffle for an array
# not actually used in finding problem's solution
# but can be used to play with small cases
def rfsf(a):
    n = len(a)
    if n & 1:
        "ERROR: length of input array should be even..."
        return
    b = [0 for i in range(n)]
    for i in range(n // 2):
        b[2 * i] = a[i]
        b[2 * i + 1] = a[n // 2 + i]
    return b

def prm_ert_upto_n_lst(n):
    ''' (int) -> list of int
        Function to generate list of prime numbers
        using Sieves of Eratosthenes
        n = upto which primes are needed (inclusive)
    '''
    np = [2 for i in range(n)]
    ip = [True for i in range(n)]
    ip[0] = False
    ip[1] = True
    for i in range(3, n, 2):
        ip[i] = False
    k = 3
    nsq = math.sqrt(n)
    while k < nsq:
        for j in range(k*k - 1, n, k):
            ip[j] = False
        while k < nsq:
            k += 2
            if ip[k - 1]:
                break
    m = 1
    np[0] = 2
    for i in range(2, n, 2):
        if ip[i]:
            np[m] = i + 1
            m += 1
    return np[:m]

def prdc(aa):
    ''' Returns Product of all elements in input array aa '''
    p = 1
    for a in aa:
        p *= a
    return p

def fctrs_fpf(n0):
    ''' (int) -> tuple
        To get all factors of a positive integer

        It needs prms list containing list of primes at least
        up to sqrt(n) and sometimes one more than that,
        use prm_ert_upto_n_lst() for that before calling this function

        >>> fctrs_fpf(36)
        [1, 2, 3, 4, 6, 9, 12, 18, 36]
    '''
    def ntps():
        nonlocal m, ct, nt
        if m == 0:
            for k in range(ne[0]):
                ct = [es[0][k]]
                m = 1
                ntps()
        elif m == r-1:
            for k in range(ne[r-1]):
                nt.append(prdc(ct + [es[r-1][k]]))
        else:
            for k in range(ne[m]):
                ct.append(es[m][k])
                m += 1
                ntps()
                ct = ct[:-1]
                m -= 1
    k = 0
    pdvs = []
    n = n0
    while prms[k] <= n:
        if prms[k] > round(math.sqrt(n)):
            pdvs.append((n, 1))
            break
        if n % prms[k] == 0:
            n = n // prms[k]
            pc = 1
            while n % prms[k] == 0:
                n = n // prms[k]
                pc += 1
            pdvs.append((prms[k], pc))
        k += 1
    r = len(pdvs)
    if r == 1:
        return [pdvs[0][0] ** i for i in range(pdvs[0][1] + 1)]
    elif r == 0:
        return [1]
    es = [[p[0] ** i for i in range(p[1] + 1)] for p in pdvs]
    ne = [len(e) for e in es]
    ct = []
    nt = []
    m = 0
    ntps()
    return sorted(nt)

m = 60
m21 = 2 ** m - 1
mh21 = 2 ** (m / 2) - 1
# Ideally, one should use m21 below instead of mh21 (mh21 works for m=60 but might not work in general)
prms = prm_ert_upto_n_lst(round(math.sqrt(mh21))+1)

md = fctrs_fpf(m)[:-1]
m21d = fctrs_fpf(m21)
for k in md:
    k21d = fctrs_fpf(2**k-1)
    for j in k21d:
        if j in m21d:
            m21d.remove(j)
print(sum(m21d) + len(m21d))
