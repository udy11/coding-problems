def gcd(a, b):
    ''' (int, int) -> int
        Computes GCD or HCF using Euclidean Algorithm
    '''
    while b != 0:
        c = b
        b = a % c
        a = c
    return a

def seq(n, s):
    sq = [n]
    for c in s:
        if c == 'U':
            sq.append((4 * sq[-1] + 2) / 3)
        elif c == 'D':
            sq.append(sq[-1] / 3)
        elif c == 'd':
            sq.append((2 * sq[-1] - 1) / 3)
    return sq

def fabc(a, b):
    return [a[0] * b[0], a[1] * b[2] + b[1] * a[0], a[2] * b[2]]

def rdc(t):
    g1 = gcd(t[0], t[2])
    g2 = gcd(t[1], t[2])
    g = gcd(g1, g2)
    return [t[0] // g, t[1] // g, t[2] // g]

s = 'DdDddUUdDDDdUDUUUdDdUUDDDUdDD'
ns = len(s)
t = [1, 0, 1]

for k in range(ns - 1, -1, -1):
    if s[k] == 'U':
        t = fabc(t, [4, 2, 3])
    elif s[k] == 'D':
        t = fabc(t, [1, 0, 3])
    elif s[k] == 'd':
        t = fabc(t, [2, -1, 3])
if s[0] == 'U':
    t = rdc(fabc(t, [3, 1, 1]))
elif s[0] == 'D':
    t = rdc(fabc(t, [3, 0, 1]))
elif s[0] == 'd':
    t = rdc(fabc(t, [3, 2, 1]))
