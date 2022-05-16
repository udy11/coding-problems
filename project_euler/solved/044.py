# BRUTE FORCE

# Iterating till 2000 for n and k produces D
# as 5482660
# Now to show that this is minimum, note that
# difference of consecutive pentagonal numbers:
# P(k+1)-P(k) = 6k+2
# Thus there is no point in checking above k
# when 6k+2 > 5482660 ==> k > 913776
# Making this check for k and consecutive pentagonal
# numbers (i.e. n=1), the algo won't yield any results
# Thus 5482660 must be minimum

import math

def ispn(p):
    pd = (math.sqrt(24*p+1)+1)/6
    pr = abs(pd - round(pd))
    if pr < 1e-8:
        return True
    return False

def pg(n):
    return n*(3*n-1)//2

# ispn(pndn(k,n))

def pndn(k,n):
    return n*(6*k+3*n-1)//2
def pnsn(k,n):
    return k*(3*k-1) + n*(6*k+3*n-1)//2

for n in range(1,2000):
    for k in range(1,2000):
        if ispn(pndn(k,n)) and ispn(pnsn(k,n)):
            print(pg(k),pg(n+k),pg(k)+pg(n+k),pg(n+k)-pg(k))
