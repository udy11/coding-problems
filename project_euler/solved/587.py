import cmath
import math

def bsctn(f, a, b, er):
    ''' (function, float, float, float) -> (int, float)

        Function to find a root of f(x) using Bisection Method
    '''
    fa = f(a)
    fb = f(b)
    if abs(fa) < er:
        return (2, a)
    if abs(fb) < er:
        return (3, b)
    eps = 4.4408920985006262e-16
    ifa = False
    ifb = False
    c = 0.5 * (a + b)
    if abs(c - 1.0) < eps:
        c0 = 2.0
    else:
        c0 = 1.0
    while True:
        fc = f(c)
        if abs(fc) < er:
            return (1, c)
        elif c0 == 0.0 and c == 0.0:
            return (-1, c)
        elif c0 != 0.0 and abs(1 - c / c0) < eps:
            return (-1, c)
        else:
            if ifa:
                fa = f(a)
            elif ifb:
                fb = f(b)
            if fa * fc < 0.0:
                b = c
                ifa = False
                ifb = True
            elif fb * fc < 0.0:
                a = c
                ifa = True
                ifb = False
            elif abs(fa) < abs(fb):
                b = c
                ifa = False
                ifb = True
            else:
                a = c
                ifa = True
                ifb = False
        c0 = c
        c = 0.5 * (a + b)

def int_smpsn(f, a, b, n):
    """ (num, num, int) -> float
    Returns Integration of function f(x) in range a to b
    using total n points and Simpson's 1/3rd Rule
    Truncation Error = -(b-a)(h**4)f''''(z)/180, a<z<b """
    if n & 1 == 0:
        m = n - 1
        print('changed')
    else:
        m = n
    h = (b - a) / (m - 1)
    sm = h * (f(a) + f(b) + 4 * f(b - h)) / 3
    for i in range(1, m // 2):
        sm += h * (4 * f(a + (2 * i - 1) * h) + 2 * f(a + 2 * i * h)) / 3
    return sm

def qdreqn(a):
    ''' (array) -> tuple

    Returns the roots of the quadratic equation
    a[0] + a[1] * x + a[2] * x**2 == 0
    a[i] and x are complex numbers '''
    if len(a) != 3:
        return tuple([])
    if a[2] == 0:
        if a[1] == 0:
            return tuple([])
        else:
            return (-a[0] / a[1], )
    else:
        a1 = a[1] * 0.5
        ds = cmath.sqrt(a1 * a1 - a[2] * a[0])
        return ((-a1 + ds) / a[2], (-a1 - ds) / a[2])

def crc(x):
    return 0.5 - math.sqrt(x - x * x)

def afrc(n):
    a1 = (1 - math.pi * 0.25) * 0.25
    y = qdreqn([1, -4 * (n + 1), 4 * (n * n + 1)])
    y = min(y[0].real, y[1].real)
    x = y * n
    a2 = 0.5 * x * y + int_smpsn(crc, x, 0.5, 10001)
    return a2 / a1 - 0.001

print(bsctn(afrc, 2, 10000, 1.e-10))
