# MATH

# This can be done on paper also, though with this method it will
# need many calculations, but still doable on few pages

def clndc(a, r):
    n = len(a)
    ct = []
    m = 0
    def ntps():
        nonlocal m, ct
        if m == 0:
            for k in range(n):
                ct = [a[k]]
                m = 1
                ntps()
        elif m == r-1:
            for k in range(n):
                sm = a[k] + sum(ct)
                cln[sm] += 1
        else:
            for k in range(n):
                ct.append(a[k])
                m += 1
                ntps()
                ct = ct[:-1]
                m -= 1
    ntps()
    return

def ptrdc(a, r):
    n = len(a)
    ct = []
    m = 0
    def ntps():
        nonlocal m, ct
        if m == 0:
            for k in range(n):
                ct = [a[k]]
                m = 1
                ntps()
        elif m == r-1:
            for k in range(n):
                sm = a[k] + sum(ct)
                ptr[sm] += 1
        else:
            for k in range(n):
                ct.append(a[k])
                m += 1
                ntps()
                ct = ct[:-1]
                m -= 1
    ntps()
    return

ptr = {i : 0 for i in range(9, 37)}
cln = {i : 0 for i in range(6, 37)}

ptrdc([1, 2, 3, 4], 9)
clndc([1, 2, 3, 4, 5, 6], 6)

ps = sum([ptr[i] for i in ptr])
cs = sum([cln[i] for i in cln])

wpp = 0
for i in range(9, 37):
    cp = 0
    for j in range(6, i):
        cp += cln[j]
    wpp += cp * ptr[i]

print(wpp / (ps * cs))
