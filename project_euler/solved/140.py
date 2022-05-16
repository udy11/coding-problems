# Generalized Pell's Equation

# AG(x) is (x + 3*x*x) / (1 - x - x**2)
# which can be derived by rules to manipulate
# generating functions, see section 12.5 in
# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/readings/MIT6_042JF10_chap12.pdf
# Finding when this is integral means
# finding all N such that
# x + 3*x*x = N * (1 - x - x**2)
# for this quadratic equation to have
# rational solutions, 5 * N**2 + 14 * N + 1
# should be perfect square or
# 5 * N**2 + 14 * N + 1 = B**2
# again solving this quadratic equation,
# 5 * B**2 + 44 should be perfect square
# so, 5 * B**2 + 44 = A**2
# so one needs to solve the generalized
# Pell's Equation:
# A**2 - 5 * B**2 = 44
# then only select A that'll give integral N

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

def pfp(x, y, D):
    ''' (int, int, int) -> logical
        Returns true if parameters satisfy positive Pell's Equation
    '''
    return x * x - D * y * y == 1

def pfg(x, y, D, N):
    ''' (int, int, int, int) -> logical
        Returns true if parameters satisfy generalized Pell's Equation
    '''
    return x * x - D * y * y == N

def pellfp(m):
    ''' Returns the fundamental solution of the positive Pell's Equation '''
    b = cfsq(m)
    n = len(b[1])
    x = [b[0], 0, 0]
    y = [1, 0, 0]
    if pfp(x[0], y[0], m):
        xfp = x[0]
        yfp = y[0]
    elif n > 0:
        x[1] = b[0] * b[1][0] + 1
        y[1] = b[1][0]
        if pfp(x[1], y[1], m):
            xfp = x[1]
            yfp = y[1]
        elif n > 1:
            k = 1
            while True:
                kk = k % n
                x[2] = b[1][kk] * x[1] + x[0]
                y[2] = b[1][kk] * y[1] + y[0]
                if pfp(x[2], y[2], m):
                    xfp = x[2]
                    yfp = y[2]
                    break
                else:
                    x[0] = x[1]; x[1] = x[2]
                    y[0] = y[1]; y[1] = y[2]
                    k += 1
    return (xfp, yfp)

def pellgeq(m, q, z):
    ''' (int, int, int) -> list of tuple
        Solves Generalized Pell's Equation x**2 - D * y**2 = N
        using Convergents of ContinuedbFractions. Returns
        list of tuple of first z solutions of the equation
        (sorted by ascending x)
    '''
    if is_sqrn(m):
        if q == 0:
            return [(j * round(math.sqrt(m)), j) for j in range(z)]
        else:
            print("No solution exists...")
            return []
    if q == 0:
        return [(0, 0)]
    else:
        xf, yf = pellfp(m)
    sf = []
    sqm = math.sqrt(m)
    uf = xf + sqm * yf
    for i in range(1 + math.ceil(math.sqrt(abs(q) * uf))):
        for j in range(1 + math.ceil(math.sqrt(abs(q) * uf) / sqm)):
            if pfg(i, j, m, q):
                sf.append((i, j))
                if i > sqm * j:
                    sf.append((i, -j))
                else:
                    sf.append((-i, j))
    sf = sorted(set(sf))
    if len(sf) == 0:
        print("No solution exists...")
        return []
    sol = []
    sfc = [0 for i in range(len(sf))]
    ns = 0
    while ns < z:
        s = min(sf)
        k = sf.index(s)
        if (s[0] >= 0 and s[1] >= 0) and (ns == 0 or (ns > 0 and s != sol[-1])):
            sol.append(s)
            ns += 1
        sf[k] = (xf * sf[k][0] + m * yf * sf[k][1], xf * sf[k][1] + yf * sf[k][0])
        sfc[k] += 1
    return sol

D = 5
N = 44
sln = pellgeq(D, N, 61)
sg = 0
c = -1
for s in sln:
    if (s[0] - 7) % 5 == 0:
        print((s[0] - 7) // 5)
        c += 1
        sg += (s[0] - 7) // 5
print("Sum of", c, "golden nuggets:", sg)
