# MATH

# Basically try all base-exponent combinations under
# some limit (z). The limit for base can be
# what is commented out in bs, however, one can notice
# that one can actually lower it to something around 200

import math

def dgs(m):
    s = str(m)
    d = 0
    for c in s:
        d += int(c)
    return d

z = 3000000000000000

bs = 200 # math.floor(math.sqrt(z)) + 1

n = []
for b in range(2, bs):
    es = math.floor(math.log(z, b)) + 1
    for e in range(2, es):
        m = b**e
        if dgs(m) == b:
            n.append(m)

n.sort()

print(len(n))
print(n)
