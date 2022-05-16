# ALGORITHM

# Basically generate all numbers of form 11..1
# in all bases until they cross 10^12

# Set is needed to remove repeated numbers

import math

n = 10**12
rps = []

for k in range(2, int(0.5 * math.sqrt(4 * n - 7) - 0.5) + 1):
    m = k * k + k + 1
    i = 3
    while m < n:
        rps.append(m)
        m += k ** i
        i += 1

print(sum(set(rps)) + 1)
