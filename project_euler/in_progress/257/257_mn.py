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

# Pythagorean Triplets with limit in perimeter
pmx = 10**2
count = pmx // 3
##m = 2
##while 4 * m * m / 3 <= pmx:
##    n = max(m // 3 + 1, 1)
##    if (m - n) & 1 == 0:
##        n += 1
##    p = m * (m + n)
##    while p <= pmx and n < m / 2:
##        if bgcd(m, n) != 1:
##            n += 2
##            p = m * (m + n)
##            continue
####        for k in range(1, 2):#1 + pmx // p):
####            print(k * p, (k * n * (m - n), k * m * (m - n), k * n * (m + n)))
##        count += pmx // p
##        n += 2
##        p = m * (m + n)
##    m += 1

##m = 2
##while 3 * m * m <= pmx:
##    n = max(m // 2 + 1, 1)
##    while n & 1 == 0 or bgcd(2 * m - n, m + n) > 1:
##        n += 1
##    p = 2 * m * (m + n)
##    while p <= pmx and n < m:
####        for k in range(1, 2):#1 + pmx // p):
####            print(m, n, k * p, (k * n * (2 * m - n), k * m * (2 * m - n), k * n * (m + n)), end = '  ')
####            print(math.gcd(math.gcd(n * (2 * m - n), m * (2 * m - n)), n * (m + n)))
##        count += pmx // p
##        n += 2
##        while bgcd(2 * m - n, m + n) > 1:
##            n += 2
##        p = 2 * m * (m + n)
##    m += 1

m = 3
while 3 * m * m / 2 <= pmx:
    n = max(m // 4 + 1, 1)
    while bgcd(m, n) > 1 or bgcd(m + 2 * n, m - n) > 1:
        n += 1
    p = m * (m + 2 * n)
    while p <= pmx and n < m / 2:
##        for k in range(1, 2):#1 + pmx // p):
##            print(m, n, k * p, (k * 2 * n * (m - n), k * m * (m - n), k * n * (m + 2 * n)), end = '  ')
##            print(math.gcd(math.gcd(2 * n * (m - n), m * (m - n)), n * (m + 2 * n)))
        count += pmx // p
        print(m, n)
        n += 1
        while bgcd(m, n) > 1 or bgcd(m + 2 * n, m - n) > 1:
            n += 1
        p = m * (m + 2 * n)
    m += 2

print('total:', count)
