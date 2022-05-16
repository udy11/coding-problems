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

def pelleq(m):
    ''' (int) -> tuple
        Solves Pell's Equation using Convergents of Continued Fractions
    '''
    if is_sqrn(m):
        return (None, None)
    b = cfsq(m)
    b0 = b[0]
    b = b[1]
    n = len(b)
    x = [b0, 0, 0]
    y = [1, 0, 0]
    if pf(x[0], y[0], m):
        return (x[0], y[0])
    if n > 0:
        x[1] = b0 * b[0] + 1
        y[1] = b[0]
        if pf(x[1], y[1], m):
            return (x[1], y[1])
        if n > 1:
            k = 1
            while True:
                kk = k % n
                x[2] = b[kk] * x[1] + x[0]
                y[2] = b[kk] * y[1] + y[0]
                if pf(x[2], y[2], m):
                    return (x[2], y[2])
                else:
                    x[0] = x[1]; x[1] = x[2]
                    y[0] = y[1]; y[1] = y[2]
                    k += 1

xmx = 0
for m in range(2, 1001):
    if not is_sqrn(m):
        pm = pelleq(m)
        if pm[0] > xmx:
            xmx = pm[0]
            mmx = m

print(mmx)
