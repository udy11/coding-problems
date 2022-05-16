# TRANSFER MATRIX METHOD

# Construct a matrix a which decides which two digits go to
# which two digits by adding a last digit to it, for example
# 00 -> 09 by adding 9, such that the tiplet (e.g. 009) is valid
# Then get the starting number of doublets, i.e. how many 00,
# 01, etc. are there
# Then simply multiply a^17 to b (if you started with triplets)
# and finally add all elements of b to get the answer

import numpy as np

def d111_sum(n):
    m = n % 100
    return m % 10 + m // 10 + n // 100

a = np.uint64(np.array([ [0 for i in range(100)] for i in range(100) ]))

for i in range(1000):
    if d111_sum(i) < 10:
        a[i//10][i%100] = 1

b = np.uint64(np.array([0 for i in range(100)]))

for i in range(100, 1000):
    if d111_sum(i) < 10:
        b[i % 100] += 1

for i in range(17):
    b = np.uint64(np.dot(a, b))

print(np.sum(b))
