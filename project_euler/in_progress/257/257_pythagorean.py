# Last updated: 21-Oct-2015
# Udaya Maurya (udaya_cbscients@yahoo.com)
# Functions to generate Pythagorean Triplets
# using Euclid's Formula

# Euclid's Formula is that for any positive integers m and n (m>n):
# the triplet (m**2 - n**2, 2*m*n, m**2 + n**2) is a
# Pythagorean Triplet. However, this formula does not produce
# all triplets for all values of m and n.
# To get all "primitive" triplets, we need that
# m>n, gcd(m,n)=1, m-n is odd
# and from these primitive triplets, one can get
# rest of the triplets by multiplying a factor k

# ALL YOU NEED TO DO:
# Call one of the pgts functions with required inputs:
#   Call pgts_p(pmx, ip) where pmx is limit on perimeter,
#     this limit is not inclusive (as python's convention),
#     and ip is (optional) logical variable, set it True if you
#     only want primitive triplets

# NOTE:
# The output is not sorted
# int() is used on floats to determine some limits within
#   function, so it is possible limits to be incorrectly
#   calculated due to roundoff error; such an error occurs
#   in pgts_a() for amx = 31; if required, one can get rid
#   of such errors by checking difference between the
#   calculated float and its rounded integer, if difference
#   is very low (< 1.e-13 or so), then one can take rounded
#   number as limit instead of its int() value

import math

def bgcd(a, b):
    ''' (int, int) -> int
        Computes GCD or HCF using Binary GCD/Stein's Algorithm
    '''
    if a == 0:
        return b
    if b == 0:
        return a
    k = 0
    while (a | b) & 1 == 0:
        a >>= 1
        b >>= 1
        k += 1
    while a & 1 == 0:
        a >>= 1
    while b != 0:
        while b & 1 == 0:
            b >>= 1
        if a > b:
            t = b
            b = a
            a = t
        b -= a
    return a << k

def pgts_p(pmx, ip = False):
    ''' (int, [bool]) -> list of tuples
        Generates all Pythagorean Triplets using
        Euclid's Formula upto given limit of perimeter
    '''
    ptp = []
    mmx = int(0.5 * (math.sqrt(2 * pmx - 1) - 1)) + 1
    for m in range(1, mmx, 2):
        for n in range(2, min(m, 1 + int(0.5 * (pmx - 1) / m - m)), 2):
            if bgcd(n, m) == 1:
                m2 = m * m
                n2 = n * n
                ptp.append((m2 - n2, 2 * m * n, m2 + n2))
    for m in range(2, mmx, 2):
        for n in range(1, min(m, 1 + int(0.5 * (pmx - 1) / m - m)), 2):
            if bgcd(n, m) == 1:
                m2 = m * m
                n2 = n * n
                ptp.append((m2 - n2, 2 * m * n, m2 + n2))
    if ip:
        return ptp
    ptl = []
    for pt in ptp:
        k = 2
        pp = k * sum(pt)
        while pp < pmx:
            ptl.append((k * pt[0], k * pt[1], k * pt[2]))
            k += 1
            pp = k * sum(pt)
    return ptp + ptl

# Pythagorean Triplets with limit in perimeter
n = 500
count = 0
pgs = pgts_p(n+1, ip = True)
for p in pgs:
    y = p[2]
    if p[0] < p[1]:
        x = p[0]
        z = p[1]
    else:
        x = p[1]
        z = p[0]
##    if 3 * x > y + z:
##        count += n * 2 // (x + y + z)
##        print((x + y + z) // 2, (x - y + z) // 2, (x + y - z) // 2, (-x + y + z) // 2, '::', p)
    q = 2 * (x + y + z)
##    if 4 * x > y + z:
##        count += 1
##        print(q, 2 * (x - y + z), x + 2 * (y - z), -x + y + z, '::', p, sum(p))
##    if 2 * z > x + y:
##        count += 1
##        print(q, x - y + 2 * z, -x + 2 * (y + z), 2 * (x + y) + z, '::', p, sum(p))
    a = x - y + 2 * z; b = 2 * (x + y) - z; c = -x + y + z
    if c > b or (b > c and x + y > 2 * z):
        count += 1
        print(q, a, b, c, '::', p, sum(p))
print(count)
