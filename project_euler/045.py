# IDEA:
# Any hexagonal number will be a triangle number,
#   so no need to check for triangle-ness
# if P_m = H_n, then sqrt(3)*m ~ 2*n
# so generate such m,n and check if you get them matching

import math

def hx(n):
    return n*(2*n-1)

def pt(n):
    return n*(3*n-1)//2

i = 144
while True:
    j = round(2 * i / math.sqrt(3))
    h = hx(i)
    if pt(j) == h:
        print(i,h)
        break
    i += 1
