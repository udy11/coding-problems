# MATH

# The remainder will be:
# For even n, r = 2
# For odd  n, r = 2 * n * a

# Then make a simple function to get the max remainder

def rm(a, n):
    if n % 2 == 0:
        return 2
    else:
        return (2 * a * n) % (a * a)

def rmmx(a):
    r0 = rm(a, 1)
    r = r0 + 1
    rs = [r0]
    n = 3
    while r != r0:
        r = rm(a, n)
        if r == r0:
            return max(rs)
        else:
            rs.append(r)
            n += 2

s = 0
for a in range(3, 1001):
    s += rmmx(a)

print(s)
