# INCLUSION-EXCLUSION PRINCIPLE

# Given N, the numbers divisible by 6 below N are floor(N/6)
# We need to find all the numbers below N that are divisible by
# all 4-combinations of primes below 100. There are 25 primes below
# 100 and C(25,4)=12650. So we need to count multiples of these
# 12650 numbers below N.
# In counting these, there will be overcounting, so we need to apply
# inclusion-exclusion principle.

# To get a formula for what to include and what to exclude, we take
# an analogy of four sets A,B,C,D and find the count of all
# 2 combinations: count(AB,AC,AD,BC,BD,CD)
# where AB denotes intersection of A and B
# Let small letters denote the count of exclusive sets, meaning:
# a = only those elements from set A that don't belong to B, C or D
# ab = only those elements that belong to both A and B but not to C or D
# With this, we can see that:
# A = a + ab + ac + ad + abc + abd + acd + abcd
# B = b + ab + bc + bd + abc + abd + bcd + abcd
# C = c + ac + bc + cd + abc + acd + bcd + abcd
# D = d + ad + bd + cd + abd + acd + bcd + abcd
# AB = ab + abc + abd + abcd
# AC = ac + abc + acd + abcd
# AD = ad + abd + acd + abcd
# BC = bc + abc + bcd + abcd
# BD = bd + abd + bcd + abcd
# CD = cd + acd + bcd + abcd
# ABC = abc + abcd
# ABD = abd + abcd
# ACD = acd + abcd
# BCD = bcd + abcd
# ABCD = abcd
# We want to calculate ab+ac+ad+bc+bd+cd+abc+abd+acd+bcd+abcd
# which is same as
# AB+AC+AD+BC+BD+CD-2*ABC-2*ABD-2*ACD-2*BCD+3*ABCD
# To find these coefficients, we note that we subtract ABC
# 3 times because it is counted C(3,2)=3 times in AB,AC,BC
# And we add back it one time because we need one count of these.
# So total times ABC needs to be added is 1-C(3,2) = -2 = f(3)
# As for ABCD, we subtract it C(4,2) times because it was overcounted
# in AB,AC,AD,BC,BD,CD but it was over-subtracted f(3) * C(4,3) times
# in ABC,ABD,ACD,BCD, which we need to add back. Finally we need it
# one more time because we want one copy of it in counting.
# This makes the formula for it as:
# 1 - f(3) * C(4,3) - C(4,2)
# So for given number of combinations np, the coefficient for m-combinations
# for inclusion-exclusion principle is:
# f(m) = 1 - sum(f(k) * C(m, k), (k, np, m-1))
# where f(np) = 1

# The code is somewhat slow but a C++ implementation will be much faster.
# Long ago I had used an alternate formula for f that also works,
# but I don't remember how I found that, it's commented in the code below.

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

def cmb(n, r):
    ''' (int, int) -> int
        To calculate combination defined as:
        C(n,r) = n!/((n-r)! * r!)
    '''
    if(r == 0 or r == n):
        return 1
    if(r > n // 2):
        r = n - r
    n1 = n + 1
    cn = n
    cd = 1
    for i in range(2, r + 1):
        cd *= i
        cn *= n1 - i
    return cn // cd

def cmbsl(N, a, r):
    ''' Returns total numbers of multiples below N
        for all r-combinations from a
        This code is modified version to find all combinations. '''
    sc = 0
    if r == 1:
        for i in a:
            sc += N // i
        return sc
    n = len(a)
    if r < 1 or r > n:
        return sc
    ct = []
    m = 0
    i = 0
    def cmbs():
        nonlocal m, ct, i, sc
        if m == 0:
            for k in range(n-r+2):
                i = k
                ct = [a[k]]
                m = 1
                cmbs()
        elif m == r-1:
            for k in range(i+1, n):
                p = a[k]
                for c in ct:
                    p *= c
                sc += N // p
        else:
            for k in range(i+1, n):
                i = k
                ct.append(a[k])
                m += 1
                cmbs()
                ct = ct[:-1]
                m -= 1
    cmbs()
    return sc

prms = primes_soe(100)
nprms = len(prms)
N = 10**16
np = 4

# Calculating upto how many combinations need to be considered
# because after certain numbers, the minimum combination will
# be above given N. For example, if N=1000, then 2*3*5*7 is below 1000
# but 2*3*5*7*11 is above 1000, so it's useless to count for
# 5-combinations and above
q = 0
p = N
while p > 1:
    p /= prms[q]
    q += 1

t = 0
fs = {np : 1}
for i in range(np, q):
    print('calculating for', i, 'combinations...')
    s = cmbsl(N, prms, i)
    f = 1
    m = 0
### This also works for f, though I don't know why
##    for j in range(i-1, np-1, -1):
##        f -= (-1)**m * cmb(i, j)
##        m += 1
    for m in range(np, i):
        f -= fs[m] * cmb(i, m)
    fs[i] = f
    t += f * s
print(t)
