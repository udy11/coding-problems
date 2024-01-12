import sys
import time

def bsa_asc(a, n1, n2, b):
    if b > a[n2 - 1]:
        return  # Not Found
    if b < a[n1]:
        return  # Not Found
    nd = n2 - n1
    nm = n1 + nd // 2
    while nd > 1:
        if a[nm] > b:
            n2 = nm
        else:
            n1 = nm
        nd = n2 - n1
        nm = n1 + nd // 2
    if a[n1] == b:
        return n1
    elif a[n2] == b:
        return n2
    else:
        return  # Not Found

def inpreader(ifln):
    ifl = open(ifln, 'r')
    lyn = ifl.readline()
    ins = []
    act = []
    while lyn != '':
        box = []
        l0 = lyn.split()
        act.append(l0[0] == 'on')
        l1 = l0[1].split(',')
        box += l1[0].split('=')[1].split('..')
        box += l1[1].split('=')[1].split('..')
        box += l1[2].split('=')[1].split('..')
        lyn = ifl.readline()
        ins.append([int(b) for b in box])
    return act, ins

def p1(ifln, m = 'all'):
    boxes = []
    qbx = {}
    qfcx = {}
    qfcy = {}
    qfcz = {}
    qlnx = {}
    qlny = {}
    qlnz = {}
    qvt = {}
    act, ins = inpreader(ifln)
    if m == 'all':
        m = len(act)
    xx = sorted(list(set([ins[k][i] for i in range(0, 2) for k in range(m)])))
    yy = sorted(list(set([ins[k][i] for i in range(2, 4) for k in range(m)])))
    zz = sorted(list(set([ins[k][i] for i in range(4, 6) for k in range(m)])))
    nx = len(xx)
    ny = len(yy)
    nz = len(zz)

    for k in range(m):
        kx0 = bsa_asc(xx, 0, nx, ins[k][0])
        kx1 = bsa_asc(xx, 0, nx, ins[k][1])
        ky0 = bsa_asc(yy, 0, ny, ins[k][2])
        ky1 = bsa_asc(yy, 0, ny, ins[k][3])
        kz0 = bsa_asc(zz, 0, nz, ins[k][4])
        kz1 = bsa_asc(zz, 0, nz, ins[k][5])
        for ix in range(kx0, kx1):
            for iy in range(ky0, ky1):
                for iz in range(kz0, kz1):
                    qbx[(xx[ix], xx[ix+1], yy[iy], yy[iy+1], zz[iz], zz[iz+1])] = act[k]
        for ix in range(kx0, kx1+1):
            for iy in range(ky0, ky1):
                for iz in range(kz0, kz1):
                    qfcx[(xx[ix], yy[iy], yy[iy+1], zz[iz], zz[iz+1])] = act[k]
        for ix in range(kx0, kx1):
            for iy in range(ky0, ky1+1):
                for iz in range(kz0, kz1):
                    qfcy[(xx[ix], xx[ix+1], yy[iy], zz[iz], zz[iz+1])] = act[k]
        for ix in range(kx0, kx1):
            for iy in range(ky0, ky1):
                for iz in range(kz0, kz1+1):
                    qfcz[(xx[ix], xx[ix+1], yy[iy], yy[iy+1], zz[iz])] = act[k]
        for ix in range(kx0, kx1):
            for iy in range(ky0, ky1+1):
                for iz in range(kz0, kz1+1):
                    qlnx[(xx[ix], xx[ix+1], yy[iy], zz[iz])] = act[k]
        for ix in range(kx0, kx1+1):
            for iy in range(ky0, ky1):
                for iz in range(kz0, kz1+1):
                    qlny[(xx[ix], yy[iy], yy[iy+1], zz[iz])] = act[k]
        for ix in range(kx0, kx1+1):
            for iy in range(ky0, ky1+1):
                for iz in range(kz0, kz1):
                    qlnz[(xx[ix], yy[iy], zz[iz], zz[iz+1])] = act[k]
        for ix in range(kx0, kx1+1):
            for iy in range(ky0, ky1+1):
                for iz in range(kz0, kz1+1):
                    qvt[(xx[ix], yy[iy], zz[iz])] = act[k]
    c = 0
    for bx in qbx:
        if qbx[bx]:
            c += (bx[1] - bx[0] - 1) * (bx[3] - bx[2] - 1) * (bx[5] - bx[4] - 1)
    for fc in qfcx:
        if qfcx[fc]:
            c += (fc[2] - fc[1] - 1) * (fc[4] - fc[3] - 1)
    for fc in qfcy:
        if qfcy[fc]:
            c += (fc[1] - fc[0] - 1) * (fc[4] - fc[3] - 1)
    for fc in qfcz:
        if qfcz[fc]:
            c += (fc[1] - fc[0] - 1) * (fc[3] - fc[2] - 1)
    for ln in qlnx:
        if qlnx[ln]:
            c += ln[1] - ln[0] - 1
    for ln in qlny:
        if qlny[ln]:
            c += ln[2] - ln[1] - 1
    for ln in qlnz:
        if qlnz[ln]:
            c += ln[3] - ln[2] - 1
    for vt in qvt:
        if qvt[vt]:
            c += 1
    print(len(qbx), len(qfcx), len(qfcy), len(qfcz), len(qlnx), len(qlny), len(qlnz), len(qvt))
    return c

print('Solution of Test-0 Puzzle 1:', p1('day-22_in0.txt', m = 'all'))
print('Solution of Test-1 Puzzle 1:', p1('day-22_in1.txt', m = 20))
print('Solution of Puzzle 1:', p1('day-22_in2.txt', m = 20))
print('Solution of Test-2 Puzzle 1:', p1('day-22_in3.txt', m = 10))
print('Solution of Test-1 Puzzle 2:', p1('day-22_in1.txt', m = 'all'))
t0 = time.time()
print('Solution of Puzzle 2:', p1('day-22_in2.txt', m = 'all'))    # Memory Overflow (for 8GB RAM)
print('time taken:', time.time() - t0)
print('Solution of Test-2 Puzzle 2:', p1('day-22_in3.txt', m = 'all'))
