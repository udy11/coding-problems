# DYNAMIC PROGRAMMING (FAILED IDEA)

# This implementation assumes unordered picks and indistinguishable balls other than their different colors
# Choosing 20 balls with 3 different colors is same as finding
# number of ways 20 can be written with 3 numbers 0<p,q,r<11
# Let number of ways to write n using k numbers, where each number is >0 and <11,
# be denoted as S(n,k)
# We first find S(n,1). Then we realize that S(n,2) is sum of S(m,1) for all m=n-1 to n-10 (or 0 if it goes negative)
# That means S(4,2) = S(3,1) + S(2,1) + S(1,1)
# and S(15,2) = sum of S(m,1) for 4<m<15
# We can expect this kind of table for S(n,k):
# S |  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20
# ----------------------------------------------------------------
# 1 |  1  1  1  1  1  1  1  1  1  1  0  0  0  0  0  0  0  0  0  0
# 2 |  0  1  2  3  4  5  6  7  8  9  10 9  8  7  6  5  4  3  2  1
# 3 |  0  0  1  3  6  10 15 21 28 36 45 55 63 69 73 75 75 73 69 63
# ...
# (horizontal n, vertical k)
# Finally we collect S(20,k) and to find total number of ways we multiply by
# C(7,k) to count for all color combinations
# Then expected value is sum(S(20,k) * C(7,k) * k) / sum(S(20,k) * C(7,k))
# where sum is over 0<k<8
# However, answer turns out to be wrong.

# If we let maximum number of balls be 20 (which is same as infinite balls) instead of 10 for each color
# then we can apply the formula for combinations with repitition C(20+7-1,20)=230230
# and if we find total number of ways using our dynamic programming algorithm,
# we get the same result. This suggests that our code is correct, but for unordered and undistinguishable balls

# Also check the generating function for "Compositions with summands bounded in number and size", which is
# number of ways to compose 20 such that its parts are bounded by 10 and with given number of parts
# Its generating function is given in I.15 of Analytic Combinatorics by Flajolet & Sedgewick
# One can check that the table we obtain from our method is same as obtained by this
# generating function, which is given as:
# (x * (1 - x**10) / (1 - x))**k, where k is number of distinct balls
# One can find required values by checking coefficients of x**20 in its series expansion

# If we run a simple Monte-Carlo test
# we can see that expected number is much higher
# Perhaps we also need to account for order and/or distinguishability

# nc = number of colors
# nb = number of balls for each color
# nd = number of draws

def cmb(n, r):
    ''' (int, int) -> int
        To calculate combination defined as:
        C(n,r) = n!/((n-r)! * r!)
    '''
    if(r > n - r):
        r = n - r
    c = 1
    for i in range(r):
        c = c * (n - i) // (i + 1)
    return c

def prm(n, r):
    ''' (int, int) -> int
        To calculate permutation defined as:
        P(n,r) = n!/(n-r)!
    '''
    if(r == 0):
        return 1
    p = n
    for i in range(n - r + 1, n):
        p *= i
    return p

nc = 7
nb = 10
nd = 20

dw = {}
dw[1] = [0] + [1] * nb + [0] * (nd - nb)

for k in range(2, nc + 1):
    dw[k] = []
    for i in range(nd + 1):
        dw[k].append(sum(dw[k-1][max(0, i-nb) : 1 + max(0, i-1)]))

tw = 0
mw = 0
for k in range(1, nc + 1):
    c = cmb(nc, k)
    tw += c * dw[k][nd]
    mw += k * c * dw[k][nd]
print(mw / tw)
