# LINEAR DIOPHANTINE EQUATION

# Basically, you need to solve:
# m * x + p1 = p2 * y
# for positive integers x and y,
# and where m is 10**(number of digits in p1).
# It can be solved using
# extended euclidean algorithm.

import math

def primes_soe(n):
    if n < 2:
        return []
    n2 = (n - 1) // 2
    prms = [2] * (n2 + 1)
    ip = [True for i in range(n2)]
    k = 3
    nsq = round(math.sqrt(n))
    while k <= nsq:
        for i in range(k * k // 2 - 1, n2, k):
            ip[i] = False
        while k <= nsq:
            k += 2
            if ip[k // 2 - 1]:
                break
    m = 1
    for i in range(n2):
        if ip[i]:
            prms[m] = 2 * i + 3
            m += 1
    return prms[:m]

def lindioeq(a, b, c):
    g = a
    b0 = b
    qq = []
    while b0 != 0:
        t = b0
        b0 = g // t
        qq.append(b0)
        b0 = g - b0 * t
        g = t
    if c % g != 0:
        return []
    s0 = 1; s1 = 0
    t0 = 0; t1 = 1
    for q in qq:
        t = s1
        s1 = s0 - q * t
        s0 = t
        t = t1
        t1 = t0 - q * t
        t0 = t
    a0 = a // g
    b0 = b // g
    c0 = c // g
    return (a0, b0, c0, s0, t0)

def ldesol(z, n):
    return (z[2] * z[3] - n * z[1], z[2] * z[4] + n * z[0])

prms = primes_soe(1000003)
np = len(prms)

m = 10
s = 0
for k in range(2, np - 1):
    if prms[k] > m:
        m *= 10
    z = lindioeq(m, -prms[k + 1], -prms[k])
    y = ldesol(z, math.floor(z[2] * z[3] / z[1]))
    s += m * y[0] + prms[k]

print(s)
