import sys
import numpy as np

def print_right_handed_orientations():
    def prnt(a, b, c):
        x = [a, b, c]
        s = ''
        for d in x:
            if d < 0:
                s += '-x[{}], '.format(abs(d)-1)
            else:
                s += 'x[{}], '.format(d-1)
        print('[' + s[:-2] + '], ', end = '')
    def orp(a, b, c):
        prnt(a, b, c)
        prnt(b, -a, c)
        prnt(-a, -b, c)
        prnt(-b, a, c)
        prnt(a, -b, -c)
        prnt(-b, -a, -c)
        prnt(-a, b, -c)
        prnt(b, a, -c)
    orp(1, 2, 3)
    orp(1, 3, -2)
    orp(3, 2, -1)

def orientations(x):
    return np.array([[x[0], x[1], x[2]], [x[1], -x[0], x[2]], [-x[0], -x[1], x[2]], [-x[1], x[0], x[2]], [x[0], -x[1], -x[2]], [-x[1], -x[0], -x[2]], [-x[0], x[1], -x[2]], [x[1], x[0], -x[2]], [x[0], x[2], -x[1]], [x[2], -x[0], -x[1]], [-x[0], -x[2], -x[1]], [-x[2], x[0], -x[1]], [x[0], -x[2], x[1]], [-x[2], -x[0], x[1]], [-x[0], x[2], x[1]], [x[2], x[0], x[1]], [x[2], x[1], -x[0]], [x[1], -x[2], -x[0]], [-x[2], -x[1], -x[0]], [-x[1], x[2], -x[0]], [x[2], -x[1], x[0]], [-x[1], -x[2], x[0]], [-x[2], x[1], x[0]], [x[1], x[2], x[0]]], dtype = np.int32)

def p1(ifln):
    ifl = open(ifln, 'r')
    beacons = {}
    lyn = ifl.readline()
    while lyn != '':
        if 'scanner' in lyn:
            m = int(lyn.split()[2])
            beacons[m] = []
        elif len(lyn) > 1:
            ls = lyn.split(',')
            beacons[m].append([int(ls[0]), int(ls[1]), int(ls[2])])
        lyn = ifl.readline()
    for m in beacons:
        beacons[m] = np.array(beacons[m], dtype = np.int32)
    nb = {m : len(beacons[m]) for m in beacons}
    m = 1
    matches = np.zeros((len(beacons[0]), len(beacons[m])), dtype = np.int32)
    osbm = np.array([orientations(beacons[m][im])[2] for im in range(nb[m])], dtype = np.int32)
    for i0 in range(nb[0]):
        for im in range(nb[m]):
            dx = beacons[0][i0] - osbm[im]
            for xt0 in beacons[0]:
                if xt0 - dx in osbm:
                    matches[i0, im] += 1
    print(matches)
    return

print('Result for Test Puzzle 1:', p1('day-19_in0.txt'))
#print('Result for Puzzle 1:', p1('day-19_in1.txt'))
#print('Result for Test Puzzle 2:', p2('day-19_in0.txt'))
#print('Result for Puzzle 2:', p2('day-19_in1.txt'))
