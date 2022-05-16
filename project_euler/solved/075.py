# MATH

# Generate all Pythagorean Triplets
# using Euclid's formula
# Rest is straight forward

import math

def gcd(a, b):
    ''' (int, int) -> int
        Computes GCD or HCF using Euclidean Algorithm
    '''
    while b != 0:
        c = b
        b = a % c
        a = c
    return a

ps = 1500001

nps = int(math.sqrt(ps)) + 1
pd = {}
for n in range(1, nps):
    for m in range(n+1, nps, 2):
        if gcd(n, m) == 1:
            k = 1
            while True:
                m2 = m * m
                n2 = n * n
                pl = [k * (m2 - n2), 2 * k * m * n, k * (m2 + n2)]
                psm = sum(pl)
                if psm > ps:
                    break
                else:
                    k += 1
                    if psm in pd:
                        pd[psm] += 1
                    else:
                        pd[psm] = 1
cn=0
for p in pd:
    if pd[p] == 1:
        cn += 1
print(cn)
