# ROOT-FINDING AND NUMERICAL INTEGRATION

# First find the 2 intersection points of circle and blancmange curve
# One can be efficiently found using bisection method, let it be x0
# Other is simply x1 = 0.5 (because blancmange(0.5) = 0.5)
# Then find area below circle (lower part) between x0 and x1, this
# can be accurately found using its analytical formula (in function circle14_area)
# To calculate blancmange curve points, note that sum need not be
# considered till infinite, because s(2**n * x) will be <= 0.5 but 2**n in
# denominator will increase exponentially
# So choose limit of sum so that it is accurate within double precision
# Then find area below blancmange curve between x0 and x1 using Simpson's rule
# Subtract the area below circle from area below blancmange curve to find the answer

# The problem turned out be simple but I think there's a lot of interesting math that
# goes unnoticed in this simple solution
# Check https://en.wikipedia.org/wiki/Blancmange_curve for details

import numpy as np
import scipy.integrate

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

def blancmange(x):
    s = 0
    for i in range(50):
        ti = 2**i
        s += np.abs(np.round(x * ti) - x * ti) / ti
    return s

def circle14(x):
    return 0.5 - np.sqrt(0.5 * x * (1 - 2.0 * x))

def circle14_area(x0, x1):
    sq2 = np.sqrt(2.0)
    fx0 = np.sqrt(2.0 * x0 - 4.0 * x0**2)
    fx1 = np.sqrt(2.0 * x1 - 4.0 * x1**2)
    return 0.0625 * (-8.0 * x0 - fx0 + 4.0 * x0 * fx0 + 8.0 * x1 + fx1 - 4.0 * x1 * fx1 + np.arcsin(np.sqrt(2.0 * x0)) - np.arcsin(np.sqrt(2.0 * x1)))

def cbrt(x):
    return circle14(x) - blancmange(x)

### To check the plot of blancmange curve
##x = np.linspace(0, 1, 10001)
##y = blancmange(x)
##import matplotlib.pyplot as plt
##plt.plot(x, y)
##plt.show()

# x0, x1 are 2 points where circle cuts blancmange curve
bserr, x0 = bsctn(cbrt, 0.05, 0.3, 1.0e-15)
x1 = 0.5

x = np.linspace(x0, x1, 100001)
y = blancmange(x)
print(scipy.integrate.simps(y, x) - circle14_area(x0, x1))
