import sys

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
    act, ins = inpreader(ifln)
    if m == 'all':
        m = len(act)
    # all interested 3D regions can be found from these xx, yy, zz
    xx = sorted(list(set([ins[k][i] for i in range(0, 2) for k in range(m)])))
    yy = sorted(list(set([ins[k][i] for i in range(2, 4) for k in range(m)])))
    zz = sorted(list(set([ins[k][i] for i in range(4, 6) for k in range(m)])))
    nx = len(xx)
    ny = len(yy)
    nz = len(zz)
    print(xx)
    sys.exit()

    # q arrays will store whether each region is set to on or off
    # it can be box (qbx), face (qfc), line (qln) and vertex (qvt)
    qbx = [[[False for iz in range(nz-1)] for iy in range(ny-1)] for ix in range(nx-1)]
    qfcx = [[[False for iz in range(nz-1)] for iy in range(ny-1)] for ix in range(nx)]
    qfcy = [[[False for iz in range(nz-1)] for iy in range(ny)] for ix in range(nx-1)]
    qfcz = [[[False for iz in range(nz)] for iy in range(ny-1)] for ix in range(nx-1)]
    qlnx = [[[False for iz in range(nz)] for iy in range(ny)] for ix in range(nx-1)]
    qlny = [[[False for iz in range(nz)] for iy in range(ny-1)] for ix in range(nx)]
    qlnz = [[[False for iz in range(nz-1)] for iy in range(ny)] for ix in range(nx)]
    qvt = [[[False for iz in range(nz)] for iy in range(ny)] for ix in range(nx)]

    # for each rule in ins, every region is checked if it satisfies the condition
    for k in range(m):
        # checking condition for box
        for ix in range(nx-1):
            for iy in range(ny-1):
                for iz in range(nz-1):
                    if ins[k][0] <= xx[ix] and ins[k][1] >= xx[ix+1] and ins[k][2] <= yy[iy] and ins[k][3] >= yy[iy+1] and ins[k][4] <= zz[iz] and ins[k][5] >= zz[iz+1]:
                        qbx[ix][iy][iz] = act[k]
                        qfcx[ix][iy][iz] = act[k]
                        qfcx[ix+1][iy][iz] = act[k]
                        qfcy[ix][iy][iz] = act[k]
                        qfcy[ix][iy+1][iz] = act[k]
                        qfcz[ix][iy][iz] = act[k]
                        qfcz[ix][iy][iz+1] = act[k]
                        qlnx[ix][iy][iz] = act[k]
                        qlnx[ix][iy+1][iz] = act[k]
                        qlnx[ix][iy][iz+1] = act[k]
                        qlnx[ix][iy+1][iz+1] = act[k]
                        qlny[ix][iy][iz] = act[k]
                        qlny[ix+1][iy][iz] = act[k]
                        qlny[ix][iy][iz+1] = act[k]
                        qlny[ix+1][iy][iz+1] = act[k]
                        qlnz[ix][iy][iz] = act[k]
                        qlnz[ix+1][iy][iz] = act[k]
                        qlnz[ix][iy+1][iz] = act[k]
                        qlnz[ix+1][iy+1][iz] = act[k]
                        qvt[ix][iy][iz] = act[k]
                        qvt[ix][iy][iz+1] = act[k]
                        qvt[ix][iy+1][iz] = act[k]
                        qvt[ix+1][iy][iz] = act[k]
                        qvt[ix][iy+1][iz+1] = act[k]
                        qvt[ix+1][iy][iz+1] = act[k]
                        qvt[ix+1][iy+1][iz] = act[k]
                        qvt[ix+1][iy+1][iz+1] = act[k]
        # checking condition for faces in y-z plane
        for ix in range(nx):
            for iy in range(ny-1):
                for iz in range(nz-1):
                    if ins[k][0] == xx[ix] == ins[k][1] and ins[k][2] <= yy[iy] and ins[k][3] >= yy[iy+1] and ins[k][4] <= zz[iz] and ins[k][5] >= zz[iz+1]:
                        qfcx[ix][iy][iz] = act[k]
                        qlny[ix][iy][iz] = act[k]
                        qlny[ix][iy][iz+1] = act[k]
                        qlnz[ix][iy][iz] = act[k]
                        qlnz[ix][iy+1][iz] = act[k]
                        qvt[ix][iy][iz] = act[k]
                        qvt[ix][iy][iz+1] = act[k]
                        qvt[ix][iy+1][iz] = act[k]
                        qvt[ix][iy+1][iz+1] = act[k]
        # checking condition for faces in x-z plane
        for ix in range(nx-1):
            for iy in range(ny):
                for iz in range(nz-1):
                    if ins[k][0] <= xx[ix] and ins[k][1] >= xx[ix+1] and ins[k][2] == yy[iy] == ins[k][3] and ins[k][4] <= zz[iz] and ins[k][5] >= zz[iz+1]:
                        qfcy[ix][iy][iz] = act[k]
                        qlnx[ix][iy][iz] = act[k]
                        qlnx[ix][iy][iz+1] = act[k]
                        qlnz[ix][iy][iz] = act[k]
                        qlnz[ix+1][iy][iz] = act[k]
                        qvt[ix][iy][iz] = act[k]
                        qvt[ix][iy][iz+1] = act[k]
                        qvt[ix+1][iy][iz] = act[k]
                        qvt[ix+1][iy][iz+1] = act[k]
        # checking condition for faces in x-y plane
        for ix in range(nx-1):
            for iy in range(ny-1):
                for iz in range(nz):
                    if ins[k][0] <= xx[ix] and ins[k][1] >= xx[ix+1] and ins[k][2] <= yy[iy] and ins[k][3] >= yy[iy+1] and ins[k][4] == zz[iz] == ins[k][5]:
                        qfcz[ix][iy][iz] = act[k]
                        qlnx[ix][iy][iz] = act[k]
                        qlnx[ix][iy+1][iz] = act[k]
                        qlny[ix][iy][iz] = act[k]
                        qlny[ix+1][iy][iz] = act[k]
                        qvt[ix][iy][iz] = act[k]
                        qvt[ix][iy+1][iz] = act[k]
                        qvt[ix+1][iy][iz] = act[k]
                        qvt[ix+1][iy+1][iz] = act[k]
        # checking condition for lines in x direction
        for ix in range(nx-1):
            for iy in range(ny):
                for iz in range(nz):
                    if ins[k][0] <= xx[ix] and ins[k][1] >= xx[ix+1] and ins[k][2] == yy[iy] == ins[k][3] and ins[k][4] == zz[iz] == ins[k][5]:
                        qlnx[ix][iy][iz] = act[k]
                        qvt[ix][iy][iz] = act[k]
                        qvt[ix+1][iy][iz] = act[k]
        # checking condition for lines in y direction
        for ix in range(nx):
            for iy in range(ny-1):
                for iz in range(nz):
                    if ins[k][0] == xx[ix] == ins[k][1] and ins[k][2] <= yy[iy] and ins[k][3] >= yy[iy+1] and ins[k][4] == zz[iz] == ins[k][5]:
                        qlny[ix][iy][iz] = act[k]
                        qvt[ix][iy][iz] = act[k]
                        qvt[ix][iy+1][iz] = act[k]
        # checking condition for lines in z direction
        for ix in range(nx):
            for iy in range(ny):
                for iz in range(nz-1):
                    if ins[k][0] == xx[ix] == ins[k][1] and ins[k][2] == yy[iy] == ins[k][3] and ins[k][4] <= zz[iz] and ins[k][5] >= zz[iz+1]:
                        qlnz[ix][iy][iz] = act[k]
                        qvt[ix][iy][iz] = act[k]
                        qvt[ix][iy][iz+1] = act[k]
        # checking condition for vertices
        for ix in range(nx):
            for iy in range(ny):
                for iz in range(nz):
                    if ins[k][0] == xx[ix] == ins[k][1] and ins[k][2] == yy[iy] == ins[k][3] and ins[k][4] == zz[iz] == ins[k][5]:
                        qvt[ix][iy][iz] = act[k]
    c = 0
    # counting points in boxes
    for ix in range(nx-1):
        for iy in range(ny-1):
            for iz in range(nz-1):
                if qbx[ix][iy][iz]:
                    c += (xx[ix+1] - xx[ix] - 1) * (yy[iy+1] - yy[iy] - 1) * (zz[iz+1] - zz[iz] - 1)
    # counting points in faces in y-z plane
    for ix in range(nx):
        for iy in range(ny-1):
            for iz in range(nz-1):
                if qfcx[ix][iy][iz]:
                    c += (yy[iy+1] - yy[iy] - 1) * (zz[iz+1] - zz[iz] - 1)
    # counting points in faces in x-z plane
    for ix in range(nx-1):
        for iy in range(ny):
            for iz in range(nz-1):
                if qfcy[ix][iy][iz]:
                    c += (xx[ix+1] - xx[ix] - 1) * (zz[iz+1] - zz[iz] - 1)
    # counting points in faces in x-y plane
    for ix in range(nx-1):
        for iy in range(ny-1):
            for iz in range(nz):
                if qfcz[ix][iy][iz]:
                    c += (xx[ix+1] - xx[ix] - 1) * (yy[iy+1] - yy[iy] - 1)
    # counting points in lines along x direction
    for ix in range(nx-1):
        for iy in range(ny):
            for iz in range(nz):
                if qlnx[ix][iy][iz]:
                    c += xx[ix+1] - xx[ix] - 1
    # counting points in lines along y direction
    for ix in range(nx):
        for iy in range(ny-1):
            for iz in range(nz):
                if qlny[ix][iy][iz]:
                    c += yy[iy+1] - yy[iy] - 1
    # counting points in lines along z direction
    for ix in range(nx):
        for iy in range(ny):
            for iz in range(nz-1):
                if qlnz[ix][iy][iz]:
                    c += zz[iz+1] - zz[iz] - 1
    # counting vertices
    for ix in range(nx):
        for iy in range(ny):
            for iz in range(nz):
                if qvt[ix][iy][iz]:
                    c += 1
    return c

#print('Solution of Test-0 Puzzle 1:', p1('day-22_in0.txt', m = 'all'))
print('Solution of Test-1 Puzzle 1:', p1('day-22_in1.txt', m = 20))
#print('Solution of Puzzle 1:', p1('day-22_in2.txt', m = 20))
#print('Solution of Test-2 Puzzle 1:', p1('day-22_in3.txt', m = 10))
#print('Solution of Test-1 Puzzle 2:', p1('day-22_in1.txt', m = 'all'))
#print('Solution of Puzzle 2:', p1('day-22_in2.txt', m = 'all'))    # Memory Overflow (for 8GB RAM)
#print('Solution of Test-2 Puzzle 2:', p1('day-22_in3.txt', m = 'all'))
