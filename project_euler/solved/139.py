# PELL's EQUATION

# Let b = a + d, then for primitive pythagorean
# triplet, gcd(a, b) = 1 and gcd(a, d) = 1
# a**2 + (a+d)**2 = c**2
# 2*a**2 + d**2 + 2*a*d = c**2
# If we want b-a = d to divide c**2, we want it to divide
# 2*a**2 + d**2 + 2*a*d, which is not possible unless d=1
# because gcd(a, d) = 1.
# Hence, what we are looking for are primitive pythagorean
# triplets such that |a - b| = 1.
# Euclid's Formula says a = m**2 - n**2 and b = 2*m*n
# so we want, |m**2 - n**2 - 2*m*n| = 1
# or |(m-n)**2 - 2*n**2| = 1, which is to solve
# two Pell's equations

import math

def is_sqrn(n):
    ''' (int) -> logical
        To check if a non-negative integer n is a square number
        Sq(n) = n * n
    '''
    if n % 4 == 0 or n % 8 == 1:
        r = round(math.sqrt(n))
        if r * r == n:
            return True
    return False

def cfsq(r):
    ''' (int) -> tuple
    Returns Continued Fractions of sqrt(r)
    Assumes input to be positive integer
    '''
    ss = math.sqrt(r)
    n = int(ss)
    m1 = 1
    p1 = n
    m = p1
    p = r - m * m
    c1 = [n]
    w = []
    while True:
        if [m1, p1] in w:
            break
        else:
            w.append([m1, p1])
        s = (ss + m) / p
        n = int(s)
        m1 = p
        p1 = (p * n - m)
        m = p1
        p = (r - m * m) // m1
        c1.append(n)
    return (c1[0], c1[1:])

def pf(x, y, D):
    ''' (int, int, int) -> logical
        Returns true if parameters satisfy Pell's Equation
    '''
    return x * x - D * y * y == 1

def pelleq(m, j):
    ''' (int, int) -> list of tuple
        Solves Pell's Equation using Convergents of Continued Fractions
        Returns list of tuple of first j solutions of the equation
    '''
    if is_sqrn(m):
        return
    b = cfsq(m)
    n = len(b[1])
    x = [b[0], 0, 0]
    y = [1, 0, 0]
    if pf(x[0], y[0], m):
        xf = x[0]
        yf = y[0]
    elif n > 0:
        x[1] = b[0] * b[1][0] + 1
        y[1] = b[1][0]
        if pf(x[1], y[1], m):
            xf = x[1]
            yf = y[1]
        elif n > 1:
            k = 1
            while True:
                kk = k % n
                x[2] = b[1][kk] * x[1] + x[0]
                y[2] = b[1][kk] * y[1] + y[0]
                if pf(x[2], y[2], m):
                    xf = x[2]
                    yf = y[2]
                    break
                else:
                    x[0] = x[1]; x[1] = x[2]
                    y[0] = y[1]; y[1] = y[2]
                    k += 1
    sol = []
    for i in range(1, j+1):
        t1 = xf ** i
        xa = t1
        ya = 0
        k = 0
        while k < i + 1:
            t1 = t1 * (i - k) * yf // (k + 1) // xf
            ya += t1
            k += 1
            if k > i:
                break
            t1 = t1 * (i - k) * yf * m // (k + 1) // xf
            xa += t1
            k += 1
        sol.append((xa, ya))
    return sol

def npf(x, y, D):
    ''' (int, int, int) -> logical
        Returns true if parameters satisfy Negative Pell's Equation
    '''
    return D * y * y - x * x == 1

def npelleq(m, j):
    ''' (int, int) -> list of tuple
        Solves Negative Pell's Equation using
        Convergents of Continued Fractions
        Returns list of tuple of first j solutions of the equation
    '''
    if is_sqrn(m):
        return
    b = cfsq(m)
    n = len(b[1])
    if n % 2 == 0:
        return
    x = [b[0], 0, 0]
    y = [1, 0, 0]
    if npf(x[0], y[0], m):
        xf = x[0]
        yf = y[0]
    elif n > 0:
        x[1] = b[0] * b[1][0] + 1
        y[1] = b[1][0]
        if npf(x[1], y[1], m):
            xf = x[1]
            yf = y[1]
        elif n > 1:
            k = 1
            while True:
                kk = k % n
                x[2] = b[1][kk] * x[1] + x[0]
                y[2] = b[1][kk] * y[1] + y[0]
                if npf(x[2], y[2], m):
                    xf = x[2]
                    yf = y[2]
                    break
                else:
                    x[0] = x[1]; x[1] = x[2]
                    y[0] = y[1]; y[1] = y[2]
                    k += 1
    sol = []
    for i in range(1, 2*j+1, 2):
        t1 = xf ** i
        xa = t1
        ya = 0
        k = 0
        while k < i + 1:
            t1 = t1 * (i - k) * yf // (k + 1) // xf
            ya += t1
            k += 1
            if k > i:
                break
            t1 = t1 * (i - k) * yf * m // (k + 1) // xf
            xa += t1
            k += 1
        sol.append((xa, ya))
    return sol

mnp = pelleq(2, 12)
mnp += npelleq(2, 12)

s = 0
for mn in mnp:
    p = 2 * (mn[1] + mn[0]) * (2 * mn[1] + mn[0])
    s += 99999999 // p
print(s)
