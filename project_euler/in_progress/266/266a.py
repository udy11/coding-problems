# FAILED IDEA
# KNAPSACK 0-1 with DYNAMIC PROGRAMMING

# The problem is to get nearest possible to
# sqrt(prod(primes upto 190)) using those primes
# This can thus be translated into Knapsack 0-1
# Problem. However, looks like Dynamic Programming
# is not sufficient to solve this

import math

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

def cmbsl(a, r):
    ''' (list/tuple, int) -> list of list
        Returns r combinations of list/tuple a

        >>> a = [1, 2, 3, 4]; r = 3
        >>> cmbsl(a, r)
        [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
    '''
    if r == 1:
        return [[i] for i in a]
    n = len(a)
    if r < 1 or r > n:
        return []
    ct = []
    cm = []
    m = 0
    i = 0
    def cmbs():
        nonlocal m, ct, cm, i
        if m == 0:
            for k in range(n-r+2):
                i = k
                ct = [a[k]]
                m = 1
                cmbs()
        elif m == r-1:
            for k in range(i+1, n):
                cm.append(ct + [a[k]])
        else:
            for k in range(i+1, n):
                i = k
                ct.append(a[k])
                m += 1
                cmbs()
                ct = ct[:-1]
                m -= 1
    cmbs()
    return cm

def prm_ert_upto_n_lst(n):
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
    np[0] = 2
    for i in range(2, n, 2):
        if ip[i]:
            np[m] = i + 1
            m += 1
    return np[:m]

prms = prm_ert_upto_n_lst(190)

ps = 2323218950681478446587180516177954548

cl = []
np = len(prms)
for i in range(1, np+1):
    cmb = cmbsl(prms, i)
    for cm in cmb:
        p = 1
        for c in cm:
            p *= c
        if not p in cl:
            cl.append(p)
cl.sort()
print("cl created...")

b = ps
nd = bsan_asc(cl, 0, len(cl), b)
nd += 1
dpa = [[prms[0] for j in range(nd)] for i in range(np)]
for k in range(1, np):
    for d1 in range(nd):
        dd = 0
        for d0 in range(d1+1):
            if dpa[k-1][d0] * prms[k] > cl[d1]:
                break
            dd = dpa[k-1][d0] * prms[k]
        if cl[d1] < prms[k]:
            de = 0
        else:
            de = prms[k]
        dpa[k][d1] = max(dd, de, dpa[k-1][d1])

for i in range(nd):
    print(cl[i], dpa[-1][i])
