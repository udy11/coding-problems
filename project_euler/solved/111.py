# OPTIMIZED BRUTE-FORCE

# Simply generate such numbers and check primality

# Can be further optimized by improving prime number checking
# and pre-storing combinations

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

def ngtr(n, g, c):
    r = len(c) - 1
    r1 = []; r2 = [10 for j in range(r+1)]
    for j in c:
        if j == 0 or j == n-1:
            r1.append(1)
        else:
            r1.append(0)
    t = [i for i in range(n)]
    for j in c:
        t.remove(j)
    if g % 2 == 0 and t[0] == 0:
        return
    elif g == 5 and t[0] == 0:
        return
    d = 0
    m = 0
    for i in range(n-r-1):
        d += g * 10 ** t[i]
    def frc():
        global s
        nonlocal d, m, r, r1, r2
        if r == 0 and m == 0 and c[0] == 0:
            for k in [1, 3, 7, 9]:
                if is_prime(d + k * 10 ** c[m]):
                    s += d + k * 10 ** c[m]
        elif m == 0 and c[0] == 0:
            for k in [1, 3, 7, 9]:
                d += k * 10 ** (c[m])
                m += 1
                frc()
                m -= 1
                d -= k * 10 ** (c[m])
        elif m < r:
            for k in range(r1[m], r2[m]):
                d += k * 10 ** (c[m])
                m += 1
                frc()
                m -= 1
                d -= k * 10 ** (c[m])
        else:
            for k in range(r1[m], r2[m]):
                if is_prime(d + k * 10 ** c[m]):
                    s += d + k * 10 ** c[m]
    frc()

def cmbsl(a, r):
    if r == 1:
        return [[i] for i in a]
    n = len(a)
    if r < 1 or r > n:
        return []
    ct = []
    cm = []
    m = 0
    i = 0
    def cmbs():
        nonlocal m, ct, cm, i
        if m == 0:
            for k in range(n-r+2):
                i = k
                ct = [a[k]]
                m = 1
                cmbs()
        elif m == r-1:
            for k in range(i+1, n):
                cm.append(ct + [a[k]])
        else:
            for k in range(i+1, n):
                i = k
                ct.append(a[k])
                m += 1
                cmbs()
                ct = ct[:-1]
                m -= 1
    cmbs()
    return cm

n = 10

ss = 0
for g in range(10):
    for k in range(1, n):
        s = 0
        if g > 0:
            ck = cmbsl([j for j in range(n)], k)
        elif g == 0:
            ck = cmbsl([j for j in range(n-1)], k)
            for c in ck:
                c += [n-1]
        for c in ck:
            ngtr(n, g, c)
        if s > 0:
##            print(g, k, s)
            ss += s
            break

print(ss)
