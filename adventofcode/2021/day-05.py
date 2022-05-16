import sys

def popl(a, b):
    if a < b:
        return tuple([i for i in range(a, b + 1)])
    elif b < a:
        return tuple([i for i in range(a, b - 1, -1)])
    else:
        return (a, )

def p1(ifln):
    ifl = open(ifln, 'r')
    lyn = ifl.readline()
    pnts = {}
    while lyn != '':
        ls = lyn.split()
        p0 = [int(ls[0]), int(ls[1])]
        p1 = [int(ls[3]), int(ls[4])]
        if p0[0] == p1[0]:
            py0, py1 = sorted((p0[1], p1[1]))
            for j in range(py0, py1 + 1):
                if not (p0[0], j) in pnts:
                    pnts[(p0[0], j)] = 1
                else:
                    pnts[(p0[0], j)] += 1
        elif p0[1] == p1[1]:
            px0, px1 = sorted((p0[0], p1[0]))
            for i in range(px0, px1 + 1):
                if not (i, p0[1]) in pnts:
                    pnts[(i, p0[1])] = 1
                else:
                    pnts[(i, p0[1])] += 1
        lyn = ifl.readline()
    cp = 0
    for p in pnts:
        if pnts[p] > 1:
            cp += 1
    return cp

def p2(ifln):
    ifl = open(ifln, 'r')
    lyn = ifl.readline()
    pnts = {}
    while lyn != '':
        ls = lyn.split()
        p0 = [int(ls[0]), int(ls[1])]
        p1 = [int(ls[3]), int(ls[4])]
        if p0[0] == p1[0]:
            py0, py1 = sorted((p0[1], p1[1]))
            for j in range(py0, py1 + 1):
                if not (p0[0], j) in pnts:
                    pnts[(p0[0], j)] = 1
                else:
                    pnts[(p0[0], j)] += 1
        elif p0[1] == p1[1]:
            px0, px1 = sorted((p0[0], p1[0]))
            for i in range(px0, px1 + 1):
                if not (i, p0[1]) in pnts:
                    pnts[(i, p0[1])] = 1
                else:
                    pnts[(i, p0[1])] += 1
        else:
            for i, j in zip(popl(p0[0], p1[0]), popl(p0[1], p1[1])):
                if not (i, j) in pnts:
                    pnts[(i, j)] = 1
                else:
                    pnts[(i, j)] += 1
        lyn = ifl.readline()
    cp = 0
    for p in pnts:
        if pnts[p] > 1:
            cp += 1
    return cp

print('Soltion of Test Puzzle 1:', p1('day-05_in0.txt'))
print('Soltion of Puzzle 1:', p1('day-05_in1.txt'))
print('Soltion of Test Puzzle 2:', p2('day-05_in0.txt'))
print('Soltion of Puzzle 2:', p2('day-05_in1.txt'))
