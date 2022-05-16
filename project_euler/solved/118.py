# Brute Force (pretty much)

# Get all primes and separate valid ones by digits
# Store them by number of digits in them
# Then work out for each kind of combinations possible

# This method lists out all possible sets as well, so you can
# even print them out
# This method works fast enough, most of the time goes into
# getting the prime numbers
# The implementation is rather poor, could have been made better
# by writing some general functions

import math

def vldp(p):
    dg = []
    while p > 0:
        r = p % 10
        if r in dg or r == 0:
            return False
        else:
            dg.append(r)
        p = p // 10
    return sorted(dg)

def dsjnt(d1, d2):
    for d in d1:
        if d in d2:
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

n = 98765432
prms = primes_soe(n)
pdgs = {i : [] for i in range(1, 9)}
k = 0
for p in prms:
    if p > 10 ** k:
        k += 1
    q = vldp(p)
    if q:
        pdgs[k].append(q)
del prms

# For 8-digit prime numbers
c8 = 0
for d8 in pdgs[8]:
    if (not 2 in d8) or (not 3 in d8) or (not 5 in d8) or (not 7 in d8):
        c8 += 1

# For 7-digit prime numbers
t2 = list(pdgs[2])
for i in range(len(pdgs[1])):
    for j in range(i):
        t2.append(pdgs[1][j] + pdgs[1][i])
c7 = 0
for d7 in pdgs[7]:
    d19 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for d in d7:
        d19.remove(d)
    c7 += t2.count(d19)
del t2

# For 6-digit prime numbers
t32 = []
for i in range(len(pdgs[1])):
    for j in range(i):
        for k in range(j):
            t32.append(pdgs[1][k] + pdgs[1][j] + pdgs[1][i])
    for d2 in pdgs[2]:
        if not pdgs[1][i][0] in d2:
            t32.append(sorted(d2 + pdgs[1][i]))
t31 = t32 + pdgs[3]
c6 = 0
for d6 in pdgs[6]:
    d19 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for d in d6:
        d19.remove(d)
    c6 += t31.count(d19)
del t31

# For 5-digit prime numbers
t4 = list(pdgs[4])
t4 += [[2, 3, 5, 7]]
for i in range(len(pdgs[1])):
    for j in range(i):
        for d2 in pdgs[2]:
            d11 = pdgs[1][j] + pdgs[1][i]
            if dsjnt(d11, d2):
                t4.append(sorted(d2 + d11))
    for d3 in pdgs[3]:
        if not pdgs[1][i][0] in d3:
            t4.append(sorted(d3 + pdgs[1][i]))
for i in range(len(pdgs[2])):
    for j in range(i):
        if dsjnt(pdgs[2][i], pdgs[2][j]):
            t4.append(sorted(pdgs[2][i] + pdgs[2][j]))
c5 = 0
for d5 in pdgs[5]:
    d19 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for d in d5:
        d19.remove(d)
    c5 += t4.count(d19)
del t4

# For double 4-digit prime numbers
c44 = 0
for i in range(len(pdgs[4])):
    for j in range(i):
        if dsjnt(pdgs[4][j], pdgs[4][i]):
            d4 = pdgs[4][j] + pdgs[4][i]
            if (not 2 in d4) or (not 3 in d4) or (not 5 in d4) or (not 7 in d4):
                c44 += 1

# For single 4-digit prime numbers
t5 = []
for i in range(len(pdgs[1])):
    for j in range(i):
        for k in range(j):
            d111 = pdgs[1][k] + pdgs[1][j] + pdgs[1][i]
            for d2 in pdgs[2]:
                if dsjnt(d2, d111):
                    t5.append(sorted(d111 + d2))
        for d3 in pdgs[3]:
            d11 = pdgs[1][j] + pdgs[1][i]
            if dsjnt(d11, d3):
                t5.append(sorted(d3 + d11))
    for j in range(len(pdgs[2])):
        if not pdgs[1][i][0] in pdgs[2][j]:
            d211 = pdgs[2][j] + pdgs[1][i]
            for k in range(j):
                if dsjnt(pdgs[2][k], d211):
                    t5.append(sorted(pdgs[2][k] + d211))
for d3 in pdgs[3]:
    for d2 in pdgs[2]:
        if dsjnt(d2, d3):
            t5.append(sorted(d2 + d3))
c4 = 0
for d4 in pdgs[4]:
    d19 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for d in d4:
        d19.remove(d)
    c4 += t5.count(d19)
del t5

# For 3-digit prime numbers
t6 = []
for i in range(len(pdgs[2])):
    for j in range(i):
        if dsjnt(pdgs[2][i], pdgs[2][j]):
            d21 = pdgs[2][i] + pdgs[2][j]
            for k in range(j):
                if dsjnt(d21, pdgs[2][k]):
                    t6.append(sorted(d21 + pdgs[2][k]))
            for m in range(len(pdgs[1])):
                for n in range(m):
                    d1 = pdgs[1][n] + pdgs[1][m]
                    if dsjnt(d1, d21):
                        t6.append(sorted(d1 + d21))
    if dsjnt([2, 3, 5, 7], pdgs[2][i]):
        t6.append(sorted([2, 3, 5, 7] + pdgs[2][i]))
c3 = 0
for i in range(len(pdgs[3])):
    d19 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for d in pdgs[3][i]:
        d19.remove(d)
    c3 += t6.count(d19)
    for j in range(i):
        if dsjnt(pdgs[3][i], pdgs[3][j]):
            d31 = pdgs[3][i] + pdgs[3][j]
            d19 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for d in d31:
                d19.remove(d)
            c3 += t32.count(d19)
            for k in range(j):
                if dsjnt(pdgs[3][k], d31):
                    c3 += 1
del t32, t6

# For 2-digit prime numbers
c2 = len([[5, 23, 89, 41, 67], [5, 23, 89, 47, 61], [5, 29, 83, 41, 67], [5, 29, 83, 47, 61]])
c2+= len([[2, 53, 89, 41, 67], [2, 53, 89, 47, 61], [2, 59, 83, 41, 67], [2, 59, 83, 47, 61]])
for d1 in [[2, 3, 5], [2, 3, 7], [2, 5, 7], [3, 5, 7]]:
    for i in range(len(pdgs[2])):
        if dsjnt(pdgs[2][i], d1):
            d2a = pdgs[2][i] + d1
            for j in range(i):
                if dsjnt(pdgs[2][j], d2a):
                    d2b = d2a + pdgs[2][j]
                    for k in range(j):
                        if dsjnt(pdgs[2][k], d2b):
                            c2 += 1

print(sum([c8 ,c7, c6, c5, c44, c4, c3, c2]))
