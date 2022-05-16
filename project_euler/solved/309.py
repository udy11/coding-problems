# PYTHAGOREAN TRIPLETS

# Let a = sqrt(x*x-w*w) and b = sqrt(y*y-w*w), then using
# some geometry, h = a*b/(a+b). a and b should be integers
# for h to be integer. So, generate all pythagorean triplets
# and search for pairs of triplets with one common side (i.e., w).
# Once found, calculate a and b and check if h is integer.

# I think a better implementation of searching for common w can
# greatly reduce run-time because generation of triplets and
# sorting take much less time.

import math

def gcd(a, b):
    ''' (int, int) -> int
        Computes GCD or HCF using Euclidean Algorithm
    '''
    while b != 0:
        c = b
        b = a % c
        a = c
    return a

def pgts_h(hmx, ip = False):
    ''' (int) -> list of tuples
        Generates all Pythagorean Triplets using
        Euclid's Formula upto given limit of hypotenuse
    '''
    ptp = []
    mmx = int(math.sqrt(hmx - 2)) + 1
    for m in range(1, mmx, 2):
        for n in range(2, min(m, 1 + int(math.sqrt(hmx - 1 - m * m))), 2):
            if gcd(n, m) == 1:
                m2 = m * m
                n2 = n * n
                ptp.append((m2 - n2, 2 * m * n, m2 + n2))
    for m in range(2, mmx, 2):
        for n in range(1, min(m, 1 + int(math.sqrt(hmx - 1 - m * m))), 2):
            if gcd(n, m) == 1:
                m2 = m * m
                n2 = n * n
                ptp.append((m2 - n2, 2 * m * n, m2 + n2))
    if ip:
        return ptp
    ptl = []
    for pt in ptp:
        k = 2
        p2 = k * pt[2]
        while p2 < hmx:
            ptl.append((k * pt[0], k * pt[1], p2))
            k += 1
            p2 = k * pt[2]
    return ptp + ptl

pgs = pgts_h(1000000)
np = len(pgs)
cc = 0

k = 0
p1 = sorted(pgs)
while k < np - 1:
    if p1[k][0] == p1[k + 1][0]:
        ps = [p1[k], p1[k+1]]
        m = 2
        while k + m < np:
            if p1[k][0] == p1[k + m][0]:
                ps.append(p1[k + m])
                m += 1
            else:
                break
        ns = len(ps)
        for j1 in range(ns):
            for j2 in range(j1 + 1, ns):
                if ps[j1][1] * ps[j2][1] % (ps[j1][1] + ps[j2][1]) == 0:
                    cc += 1
        k += m
    else:
        k += 1

k = 0
p2 = sorted(p1, key = lambda x: x[1])
while k < np - 1:
    if p2[k][1] == p2[k + 1][1]:
        ps = [p2[k], p2[k+1]]
        m = 2
        while k + m < np:
            if p2[k][1] == p2[k + m][1]:
                ps.append(p2[k + m])
                m += 1
            else:
                break
        ns = len(ps)
        for j1 in range(ns):
            for j2 in range(j1 + 1, ns):
                if ps[j1][0] * ps[j2][0] % (ps[j1][0] + ps[j2][0]) == 0:
                    cc += 1
        k += m
    else:
        k += 1

k1 = 0
k2 = 0
while k1 < np and k2 < np:
    if p1[k1][0] == p2[k2][1]:
        ps = [p1[k1], p2[k2]]
        m = 1
        while k2 + m < np:
            if p1[k1][0] == p2[k2 + m][1]:
                ps.append(p2[k2 + m])
                m += 1
            else:
                break
        ns = len(ps)
        for j in range(1, ns):
            if ps[0][1] * ps[j][0] % (ps[0][1] + ps[j][0]) == 0:
                cc += 1
        k1 += 1
    elif p1[k1][0] > p2[k2][1]:
        k2 += 1
    else:
        k1 += 1

print(cc)
