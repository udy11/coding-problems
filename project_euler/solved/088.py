# ALGORITHM

# The method is to check all combinations possible
# which may give k upto 12000
# However, algorithm part was difficult.
# I had to use my arbitrary-nested-for-loops algorithm
# which allowed me to check all the combinations

import math

def s88(a):
    p = 1
    s = 0
    for ae in a:
        p *= ae
        s += ae
    return (p, p - s + len(a))

def ffor():
    m = 0
    i = 0
    ls = []
    nr = nn
    def frc():
        nonlocal m, ls, i, nr
        if m == 0:
            for k in range(2, r0):
                nr = nn // k
                ls = [k]
                i = k
                m += 1
                frc()
                m -= 1
        elif m < r:
            for k in range(2, nr):
                ls.append(k)
                nr1 = nr
                nr //= k
                i = k
                m += 1
                frc()
                m -= 1
                nr = nr1
                ls.remove(k)
        else:
            for k in range(2, nr):
                lst = ls + [k]
                kk = s88(lst)
                if kk[1] < 12001:
                    if not kk[1] in kd:
                        kd[kk[1]] = kk[0]
                    elif kd[kk[1]] > kk[0]:
                        kd[kk[1]] = kk[0]
    frc()

nn = 15001
nnr = [int(nn ** (1/i)) for i in range(2, 14)]
kd = {}

for r in range(1, 13):
    r0 = nnr[r-1]+1
    ffor()

ssl=[]
for k in range(2, 12001):
    if not kd[k] in ssl:
        ssl.append(kd[k])
print(sum(ssl))
