# BRUTE-FORCE (pretty much)

# Generate the right truncatable Harshad numbers while keep checking
# for strong property. Lastly, generate possible prime
# numbers from generated strong right-truncatable Harshad numbers

# A lot of optimisations still possible like a better primality
# checking and a better digital sum

def dgsm(n):
    s = 0
    for c in str(n):
        s += int(c)
    return s

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

hns = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]

hh = []

for k in range(0, 12):
    t = []
    for h in hns[-1]:
        ht = h * 10
        hds = dgsm(h)
        for i in range(10):
            hti = ht + i
            hq = hti // (hds + i)
            hr = hti - hq * (hds + i)
            if hr == 0:
                t.append(hti)
                if is_prime(hq):
                    hh.append(hti)
    hns.append(t)

hpr = []
for h in hh:
    ht = 10 * h
    for i in (1, 3, 7, 9):
        if is_prime(ht + i):
            hpr.append(ht + i)

print(sum(hpr))
