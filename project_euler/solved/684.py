# MATH

# Easy to see that s(n) will go like
# 1,2,3,...,8,9,19,29,...,89,99,199,299,...
# Now if q and r are quotient and remainder
# when n is divided by 9, then one can write
# s(n) = (r + 1) * 10**q - 1
# To find sum of s(n), note that q increases
# by 1 when n increases by 9, and r keeps cycling
# between 0 and 8. Thus one can find sum of s(n) as
# ss(n) = SUM(s(i),{r,0,8},{q,0,qq-1}) + SUM(s(i),{r,0,rr})
# where qq and rr are quotients and remainders of n/9
# and also put value of qq in second SUM
# Simplify in Mathematica to get:
# ss(n) = -6 - 9*q - r + (10**q) * (12 + 3*r + r**2) / 2
# (notation changed to rr -> r, qq -> q)
# Because answer is desired in modulo m
# One can calculate 9*q and 10**q modulo m beforehand
# Turns out calculating 9*q % m and finding q,r
# using divmod() are sufficiently fast but
# calculating 10**q % m is pretty slow for high q
# To find 10**q % m fast enough, one can use
# properties of mod that (a*a)%m = ((a%m)*(a%m))%m
# This is implemented in function p10m()
# In Mathematica, PowerMod[] function can be used

import sys
import math

def p10m(q, m):
    ''' Calculates (10 ** q) % m '''
    if q == 0:
        return 1
    # b2 basically contains binary expansion of q
    # q = SUM(2**i, (i in b2))
    b2 = []
    for i in range(1 + math.floor(math.log(q, 2))):
        if q & 2 ** i:
            b2.append(i)
    k = 0
    j = 0
    b = 10 % m
    bs = []
    if b2[j] == k:
        bs.append(b)
        j += 1    
    while k < b2[-1]:
        k += 1
        b = (b * b) % m
        if b2[j] == k:
            bs.append(b)
            j += 1
    return math.prod(bs) % m

def s(n):
    q, r = divmod(n ,9)
    return (10 ** q) * (r + 1) - 1

def ss(n):
    q, r = divmod(n ,9)
    return (10**q) * (r * r + 3 * r + 12) // 2 - r - 6 - 9*q

def ssm(n, m):
    q, r = divmod(n ,9)
    tqm = p10m(q, m)
    qm = (9 * q) % m
    return (tqm * (r * r + 3 * r + 12) // 2 - r - 6 - qm) % m

n = 91
m = 1000000007

t = 0
fib = [0 for i in range(n)]
fib[1] = 1
for i in range(2, n):
    fib[i] = fib[i - 1] + fib[i - 2]
    t += ssm(fib[i], m)
print(t % m)
