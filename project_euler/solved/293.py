# BRUTE FORCE (pretty much...)

# Simply generate admissible numbers
# Then check for primality of successive numbers

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

n = 10 ** 9
pms = (2, 3, 5, 7, 11, 13, 17, 19, 23)
pd = {p : [] for p in pms}

pd[2] = [2 ** i for i in range(1, 1 + int(math.log(n, 2)))]

for k in range(1, 9):
    for d in pd[pms[k - 1]]:
        pd[pms[k]] += [d * pms[k] ** i for i in range(1, 1 + int(math.log(n // d, pms[k])))]

pfn = []
for p in pms:
    for d in pd[p]:
        j = 3
        while True:
            if is_prime(d + j):
                pfn.append(j)
                break
            else:
                j += 2

print(sum(set(pfn)))
