# MODULAR INVERSE, POWERMOD

# Roots can be explicitly calculated or found using Mathematica
# One can also use Vieta's Formulas to find (a+b)*(b+c)*(c+a)
# Turns out (a+b)*(b+c)*(c+a) = (1-k*k)
# Thus we need to find Σ_p Σ_k (1-k*k)**p % m (sums are from 1 to n)
# Sum over p is simply a geometric progression
# This simplifies to Σ_k ((k*k - 1)*((1 - k*k)**n - 1)) / (k*k) % m
# This can be computed by using PowerMod algorithm for
# (1 - k*k)**n % m, using Python's inbuilt function pow()
# And using Inverse Modulo for 1/(k*k) % m using Extended
# Euclidean Algorithm

# Later I got to know that Mod Inverse can also be calculated
# using same pow() function, the relevant line is commented in code
# and results in faster computation

def modinverse_eea(a, b):
    ''' (int, int) -> int
        Finds Modular Inverse a**-1 (mod b) using Extended
        Euclidean Algorithm. Assumes a and b to be co-prime
    '''
    g = a
    b0 = b
    qq = []
    while b0 != 0:
        t = b0
        b0 = g // t
        qq.append(b0)
        b0 = g - b0 * t
        g = t
    s0 = 1; s1 = 0
    t0 = 0; t1 = 1
    for q in qq:
        t = s1
        s1 = s0 - q * t
        s0 = t
        t = t1
        t1 = t0 - q * t
        t0 = t
    return s0 % b

n = 10**6
m = 10**9 + 7

s = 0
for k in range(1, n+1):
    k2 = k * k
    q = (k2 - 1) % m
    q *= (-1 + pow(1 - k2, n, mod = m)) % m
    q *= modinverse_eea(k2, m)
    #q *= pow(k2, -1, mod = m)
    s += q
    s = s % m
print(s)
