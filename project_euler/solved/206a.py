# BRUTE FORCE

# Only few optmizations:
# Ignore last two digits, as they have to be 0
# the number formed by digits preceding 9 must ...
# ... be divisible by 4

# NUMBER IS: 1929374254627488900
# ITS SQRT:  1389019170

import math

def issqr(n):
    s=math.sqrt(n)
    if abs(s-round(s))<1e-8:
        return True
    return False

n = 10203040506070809
j = [0, 0, 0, 0, 0, 0, 0]
for i in range(0,90,40):
    for k in range(10**7):
        if(k%10**5==0):
            print(k)
        m = k
        for mn in range(7):
            jb = 10 ** (6 - mn)
            j[mn] = m // jb
            m -= j[mn] * jb
        nf = n + i
        for mn in range(7):
            nf += j[mn] * 10 ** (2*mn+3)
        if issqr(nf):
            print(nf)
