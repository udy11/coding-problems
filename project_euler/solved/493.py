# COMBINATORICS

# To account for distinct colors, we simply work with only the required colors
# For example, to get all ways to pick 4 distinct colors
# let there be only four colors (i.e., 40 balls) and then we find in how many ways can
# 20 balls be picked from these 40 balls such that at least 1 of each color
# is picked. To ensure the condition of at least one picked, we subtract
# the cases when only 2 colors are picked and when only 3 colors are picked
# so that number of ways to pick 4 colors will be:
# W(4) = P(40,20) - C(4,3) * W(3) - C(4,2) * W(2)
# where W(n) is number of ways to pick exactly n colors and P, C are permutation and combination symbols
# similarly for 5 distinct colors:
# W(5) = P(50,20) - C(5,4) * W(4) - C(5,3) * W(3) - C(5,2) * W(2)
# To find the total ways to pick from 70 balls, we then multiply W(n) with C(7,n)

# In forums, there are some other solutions suggested:
# The probability of not picking a color is p=1-C(60,20)/C(70,20)
# then expected value is simply sum of p for all colors, i.e., 7*p
# Another solution suggested is of Hypergeometric Distribution Function
# print(7*(scipy.stats.hypergeom.sf(0,(70), 10, 20)))

# Another interesting point is to run a simple Monte-Carlo test to
# get an idea of the problem and answer

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

tc = [0, 0] + [prm(k*10, 20) for k in range(2, 8)]
for k in range(3, 8):
    for j in range(2, k):
        tc[k] -= cmb(k, j) * tc[j]
tw = 0
mw = 0
for k in range(2, 8):
    tw += tc[k] * cmb(7, k)
    mw += tc[k] * cmb(7, k) * k
print(mw / tw)
