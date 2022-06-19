# ALGORITHM

# The aim is to identify each scanner's orientation and shift.
# The basic idea behind my algorithm is to match triangles
# of small areas formed by beacons' locations for both scanners.

# This idea is not robust enough to work in any scenario,
# however it should work in most practical cases and it indeed
# solves the given problems.

# All data of beacons is stored in beacons dict, where
# beacons[k] will give a list of tuple of all beacons
# position for scanner k.

# Next is the generation of some small area triangles using
# mts() function. This function takes all beacons location
# as input. It iterates over all positions and finds the 2
# closest points to each point. Then area of the triangle
# formed by these 3 points is stored in ts array's first
# entry. The next 3 entries of ts array consists of triangle's
# vertices. These vertices are put in a unique order in array ps.
# The first vertex is opposite of shortest side of triangle.
# The third vertex is opposite of largest side of triangle.
# This ordering of vertices and area of triangle should be
# invariant to any scanner's orientation or shift, this is the
# core idea behind this algorithm. A unique ordering cannot be
# obtained in a line and that is why triangles were chosen, though
# some other workaround should work for lines. The reason for
# working with small area triangles is because 2 scanners are
# likely to have overlapping close beacons rather than distant
# beacons. All the ts are stored in tss. Duplicates are removed
# and tss is sorted by triangle areas.

# In solv() function, results of mts() are generated
# for each scanner and stored in mintrgs dict. beacons[0]
# acts as the main list of all beacons, in which newly found
# beacons are added. ks represents the scanners list that is to
# matched with scanner-0's evolving beacons[0] list. For scanner-k,
# indices of matching triangle areas in mintrgs[0] and mintrgs[k]
# are found and stored in ijs. This step might fail if areas match
# but vertices aren't actually same, this should be fixable though
# I haven't thought about it. Also, it's possible that no match is
# found, in which case, working on scanner-k is postponed to last,
# by when we are expected to have larger beacons[0]. For the 
# triangles with matching area first vertex is oriented in all
# possible 24 ways and a shift r is found. This orientation and
# calculated shift should match the other two vertices. If they
# match the correct orientation and shift of the scanner have been
# found. Using this orientation and shift of the scanner-k, the
# positions of all beacons[k] is found relative to scanner-0
# and new beacon positions are added to beacons[0]. Scanner
# positions are also stored in rs to find Manhattan distance
# for second part of the problem.

# The list of all 24 right-handed orientations mentioned in
# orientation() function can be printed using
# print_right_handed_orientations() function.
# Note that orientations() function applies orientation
# number n to all points in list xs with an optional
# shift of rr.

import sys
import numpy as np

def print_right_handed_orientations():
    def prnt(a, b, c, n):
        s = ''
        for d in (a, b, c):
            if d < 0:
                s += '-x[{}], '.format(abs(d)-1)
            else:
                s += 'x[{}], '.format(d-1)
        print('    if n == {}:'.format(n))
        print('        return (' + s[:-2] + ')')
    def orp(a, b, c, n):
        prnt(a, b, c, n)
        n += 1
        prnt(b, -a, c, n)
        n += 1
        prnt(-a, -b, c, n)
        n += 1
        prnt(-b, a, c, n)
        n += 1
        prnt(a, -b, -c, n)
        n += 1
        prnt(-b, -a, -c, n)
        n += 1        
        prnt(-a, b, -c, n)
        n += 1
        prnt(b, a, -c, n)
        n += 1
    n = 0
    orp(1, 2, 3, n)
    n = 8
    orp(1, 3, -2, n)
    n = 16
    orp(3, 2, -1, n)

def orientation(n, x):
    if n == 0:
        return (x[0], x[1], x[2])
    if n == 1:
        return (x[1], -x[0], x[2])
    if n == 2:
        return (-x[0], -x[1], x[2])
    if n == 3:
        return (-x[1], x[0], x[2])
    if n == 4:
        return (x[0], -x[1], -x[2])
    if n == 5:
        return (-x[1], -x[0], -x[2])
    if n == 6:
        return (-x[0], x[1], -x[2])
    if n == 7:
        return (x[1], x[0], -x[2])
    if n == 8:
        return (x[0], x[2], -x[1])
    if n == 9:
        return (x[2], -x[0], -x[1])
    if n == 10:
        return (-x[0], -x[2], -x[1])
    if n == 11:
        return (-x[2], x[0], -x[1])
    if n == 12:
        return (x[0], -x[2], x[1])
    if n == 13:
        return (-x[2], -x[0], x[1])
    if n == 14:
        return (-x[0], x[2], x[1])
    if n == 15:
        return (x[2], x[0], x[1])
    if n == 16:
        return (x[2], x[1], -x[0])
    if n == 17:
        return (x[1], -x[2], -x[0])
    if n == 18:
        return (-x[2], -x[1], -x[0])
    if n == 19:
        return (-x[1], x[2], -x[0])
    if n == 20:
        return (x[2], -x[1], x[0])
    if n == 21:
        return (-x[1], -x[2], x[0])
    if n == 22:
        return (-x[2], x[1], x[0])
    if n == 23:
        return (x[1], x[2], x[0])

def orientations(n, xs, rr = (0, 0, 0)):
    xs1 = []
    for x in xs:
        x1 = orientation(n, x)
        xs1.append((x1[0] - rr[0], x1[1] - rr[1], x1[2] - rr[2]))
    return xs1

def mts(bs):
    n = len(bs)
    ts = []
    for i in range(n):
        ds = [[np.linalg.norm([bs[i][k] - bs[j][k] for k in range(3)]), bs[j]] for j in [jj for jj in range(i)] + [jj for jj in range(i+1,n)]]    # distance of bs[i] from all other points in bs
        dss = sorted(ds)
        es = [dss[0][0], dss[1][0], np.linalg.norm([dss[0][1][k] - dss[1][1][k] for k in range(3)])]    # side lengths of triangle formed with 2 closest points
        ps = [p for _, p in sorted(zip(es, [dss[1][1], dss[0][1], bs[i]]))]    # vertices of triangle, put in order of ascending opposite side length
        s = np.sum(es) * 0.5
        a = np.sqrt(s * (s - es[0]) * (s - es[1]) * (s - es[2]))    # area of triangle
        ts.append([a, ps[0], ps[1], ps[2]])
    tss = []
    for t in sorted(ts):
        if not [t[1], t[2], t[3]] in [[tt[1], tt[2], tt[3]] for tt in tss]:    # removing duplicate triangles
            tss.append(t)
    return tss

def solv(ifln):
    ifl = open(ifln, 'r')
    beacons = {}    # will store all becaons data
    lyn = ifl.readline()
    while lyn != '':
        if 'scanner' in lyn:
            m = int(lyn.split()[2])    # scanner number
            beacons[m] = []
        elif len(lyn) > 1:
            ls = lyn.split(',')
            beacons[m].append((int(ls[0]), int(ls[1]), int(ls[2])))
        lyn = ifl.readline()
    nb = len(beacons)    # number of scanners
    mintrgs = {}    # will contain small triangle areas and vertices-in-order
    ks = [k for k in range(1, nb)]    # scanners will be iterated over this
    rs = {0: (0, 0, 0)}    # will store shifts of scanners
    while len(ks) > 0:
        k = ks[0]
        mintrgs[0] = mts(beacons[0])    # recalculated because beacons[0] keeps updating in loop
        mintrgs[k] = mts(beacons[k])

        ijs = []    # will store indices of matching triangles in mintrgs[0] and mintrgs[k]
        for i in range(len(mintrgs[0])):
            for j in range(len(mintrgs[k])):
                if abs(mintrgs[0][i][0] - mintrgs[k][j][0]) < 1.0e-10:    # checking if areas are matching
                    ijs.append((i, j))
        if len(ijs) == 0:    # if no match is found, working on scanner k is postponed to last
            ks = ks[1:] + [ks[0]]
            continue
        nn = -1    # will contain the orientation number of beacons[k]
        for ij in ijs:
            i = ij[0]
            j = ij[1]
            for n in range(24):    # checks over all 24 orientations
                p0 = orientation(n, mintrgs[k][j][1])    # orientation of 1st point of mintrgs[k][j]
                r = (p0[0] - mintrgs[0][i][1][0], p0[1] - mintrgs[0][i][1][1], p0[2] - mintrgs[0][i][1][2])    # shift based on this orientation
                p1 = orientation(n, mintrgs[k][j][2])    # orientation of 2nd point of mintrgs[k][j]
                q1 = (p1[0] - r[0], p1[1] - r[1], p1[2] - r[2])    # orientation+shift of 2nd point of mintrgs[k][j]
                p2 = orientation(n, mintrgs[k][j][3])    # orientation of 3rd point of mintrgs[k][j]
                q2 = (p2[0] - r[0], p2[1] - r[1], p2[2] - r[2])    # orientation+shift of 3rd point of mintrgs[k][j]
                if mintrgs[0][i][2] == q1 and mintrgs[0][i][3] == q2:    # if oriented+shifted 2nd and 3rd points of mintrgs[k][j] match with respective mintrgs[0][i] points, then the correct orientation number n and shift r have been found
                    nn = n
                    break
            if nn > -1:
                break
        for x in orientations(nn, beacons[k], rr = r):    # adding new points to beacons[0]
            if not x in beacons[0]:
                beacons[0].append(x)
        rs[k] = r
        ks = ks[1:]
    mdmax = 0.0    # will store maximum Manhattan distance, for second-part of the problem
    for k0 in range(nb):
        for k1 in [k for k in range(k0)] + [k for k in range(k0+1,nb)]:
            md = sum([abs(rs[k0][i] - rs[k1][i]) for i in range(3)])     # Manhattan distance between scanners k0 and k1
            if md > mdmax:
                mdmax = md
    return len(beacons[0]), mdmax

p1, p2 = solv('day-19_in0.txt')
print('Result for Test Puzzle 1:', p1)
print('Result for Test Puzzle 2:', p2)
p1, p2 = solv('day-19_in1.txt')
print('Result for Puzzle 1:', p1)
print('Result for Puzzle 2:', p2)
