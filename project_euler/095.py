# BRUTE FORCE

# Only optimization is sieving and not considering primes
# Speed can be increased by making dvsr_sum() faster

# One can also sieve to get the divisor sums first,
#   it would be much faster then

import math

def nprm_ert_upto_n_lst(n):
    ''' (int) -> list of int
        Function to generate list of prime numbers
        using Sieves of Eratosthenes
        n = upto which primes are needed
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
    np = {1:False}
    for i in range(2, n):
        if not ip[i]:
            np[i + 1] = True
            m += 1
    return np

def dvsr_sum(n):
    s = round(math.sqrt(n))
    dv = [1]
    for i in range(2, s+1):
        if n % i == 0:
            dv.append(i)
            dv.append(n//i)
    return sum(set(dv))

dc = nprm_ert_upto_n_lst(1000000)

im = 1
km = 1
for i in range(1, 1000001):
    if i in dc and dc[i]:
        dc[i] = False
        s = dvsr_sum(i)
        k = 1
        sl = [i]
        while True:
            j = 0
            ch = False
            for j in range(k):
                if sl[j] == s and k - j > km:
                    km = k - j
                    im = s
                    ch = True
                    break
            if ch:
                break
            if (not s in dc) or (not dc[s]):
                break
            else:
                k += 1
                sl.append(s)
                dc[s] = False
                s = dvsr_sum(s)

print(km, im)
