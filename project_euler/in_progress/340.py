def f(n, a, b, c):
    if n > b:
        return n - c
    else:
        return f(a + f(a + f(a + f(a + n, a, b, c), a, b, c), a, b, c), a, b, c)

def s(a, b, c):
    ss = 0
    for n in range(0, b + 1):
        ss += f(n, a, b, c)
    return ss
