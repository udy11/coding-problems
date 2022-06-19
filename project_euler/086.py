# IDEA:
# Minimum path for a cuboid (a, b, c) should be such that:
#   It is sqrt(a*a + (b+c)*(b+c))
#   a >= b and a >= c
# So generate all pythagorean triplets upto min(a, b, c) = M
# Except the hypotenuse in triplet, treate others as a and b+c
# So you need to count contributions for all a when a <= M and a >= b+c
# And you also need to add contributions when a <= b+c and b+c <= 2*a and a <= M
# Contributions in each case need to need to be determined separately
# Then to find when the number crosses 1000000, just do a trial and error with M (sd in program)

import math
import fractions

def pt(m, n):
    m2 = m * m
    n2 = n * n
    return (m2 - n2, 2 * m * n)

sd = 1818
c = 0
for n in range(1, sd // 2 + 2):
    for m in range(n + 1, sd // 2 + 2):
        ptr = pt(m, n)
        mxp = max(ptr)
        mnp = min(ptr)
        if fractions.gcd(mxp, mnp) == 1:
            s1 = mnp; s2 = mxp
            while s1 <= sd and s2 < 2 * sd + 1:
                if s2 <= sd:
                    c += s1//2
                if 2 * s1 >= s2 and s1 <= sd:
                    c += (2 * s1 + 2 - s2) // 2
                s1 += mnp; s2 += mxp
print(c)
