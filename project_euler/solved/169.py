# RECURSIVE ALGORITHM

# Observe that f(2**n) = n+1
# Then, if you break n in binary representation
# as xy such that y has a leading and only one 1
# then, f(n) = f(x) + f(x0) * (f(y) - 1)
# where x0 means 0 appended to x or x multiplied by 2

def tbit(n):
    c = 0
    h = True
    k = 0
    while n > 0:
        if n % 2 == 0:
            n = n >> 1
        else:
            n = (n - 1) >> 1
            if h:
                d = k
                h = False
            c += 1
        k += 1
    return (c, d)

def cb(n0):
    n = n0
    k = 0
    q = tbit(n)
    if q[0] == 0:
        return 0
    elif q[0] == 1:
        return q[1] + 1
    else:
        n = n >> q[1] + 1
        return cb(n) + cb(n << 1) * q[1]

print(cb(10**25))

