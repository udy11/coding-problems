# IDEA:
# Quite a brute force
# Simply check if for all lines of triangle, the third
# point and origin lie on same side or not

# Some commented lines were the idea that sum of angles
# between lines formed by joining the points with origin
# should total 2*pi if origin lies in the triangle
# however because of error stuff, one cannot check for exact
# 2*pi (though it can still be done if one checks within 1e-10
# of 2*pi)

import math

def read_data_1(ifln, sep):
    ifl = open(ifln, 'r')
    dn = 0
    dt = []
    while True:
        lyn = ifl.readline().strip()
        i = 0; d0 = []
        if lyn == "":
            break
        while i < len(lyn):
            if not lyn[i] in sep:
                k = 1
                while i+k < len(lyn) and not lyn[i+k] in sep:
                    k += 1
                d0.append(float(lyn[i:i+k]))
                i += k + 1
            else:
                i += 1
        dt.append(d0)
        dn += 1
    ifl.close()
    return dt

def dot(x, y):
    return (x[0] * y[0] + x[1] * y[1]) / math.sqrt(x[0] * x[0] + x[1] * x[1]) / math.sqrt(y[0] * y[0] + y[1] * y[1])

def lyn(x0, x1, x):
    if x1[0] != x0[0]:
        return (x1[1] - x0[1]) * (x[0] - x0[0]) / (x1[0] - x0[0]) + x0[1] - x[1]
    else:
        return (x1[0] - x0[0]) * (x[1] - x0[1]) / (x1[1] - x0[1]) + x0[0] - x[0]

ts = read_data_1("102_triangles.txt", ' ')
cc = 0
i = 1
orgn = [0, 0]
for t in ts:
##    th1 = 180 * math.acos(dot(t[:2], t[2:4])) / math.pi
##    th2 = 180 * math.acos(dot(t[2:4], t[4:])) / math.pi
##    th3 = 180 * math.acos(dot(t[4:], t[:2])) / math.pi
##    print(i,th1, th2, th3, th1+th2+th3, th1+th2+th3==360.0)
##    if th1+th2+th3==360.0:
##        cc += 1
    a1 = lyn(t[:2], t[2:4], orgn) * lyn(t[:2], t[2:4], t[4:])
    a2 = lyn(t[2:4], t[4:], orgn) * lyn(t[2:4], t[4:], t[:2])
    a3 = lyn(t[4:], t[:2], orgn) * lyn(t[4:], t[:2], t[2:4])
##    print(i, a1 > 0 and a2 > 0 and a3 > 0)
    if a1 > 0 and a2 > 0 and a3 > 0:
        cc += 1
    i += 1
print(cc)
