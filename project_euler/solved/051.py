# (Sort of) Brute Froce with Trial and Error

# For divisibility by 2 and 5, last digit has to be 1, 3, 7, 9
# For divisibility by 3, the number of replacements must be multiple of 3

# Rest is brute force
# From printed answers, see which smallest one is a valid answer

import math
def is_prime(n):
    if n < 2:
        return False
    if n > 2 and n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

d2 = (1, 3, 7, 9)

cm = [[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]]
ed = []
for c in cm:
    p = [1, 2, 3, 4, 5]
    p.remove(c[0])
    p.remove(c[1])
    ed.append([10**p[0] + 10**p[1] + 10**p[2], 10**c[0], 10**c[1]])

for ee in ed:
    print('\nFor',ee)
    for a in range(10):
        for d in range(10):
            for e in range(10):
                for b in d2:
                    cc = 0
                    for i in range(10):
                        n = a*10**6 + b + ee[0]*i + d*ee[2] + e*ee[1]
                        if is_prime(n):
                            cc += 1

                    if cc > 7:
                        print(n, cc)
