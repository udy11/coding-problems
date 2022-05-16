import sys

def ans(brdk, bchkk, drw):
    bsum = 0
    for i in range(5):
        for j in range(5):
            if not bchkk[i][j]:
                bsum += brdk[i][j]
    return bsum * drw

def p1(ifln):
    ifl = open(ifln, 'r')
    lyn = ifl.readline()
    boards = []
    while lyn != '':
        ls = lyn.split()
        if len(ls) > 5:
            draws = [int(l) for l in ls]
        if len(ls) == 5:
            boards.append([])
            for i in range(5):
                boards[-1].append([int(l) for l in ls])
                lyn = ifl.readline()
                ls = lyn.split()
        lyn = ifl.readline()
    nd = len(draws)
    nb = len(boards)
    bchk = [[[False for i in range(5)] for j in range(5)] for k in range(nb)]
    bfound = False
    for m in range(nd):
        for k in range(nb):
            for i in range(5):
                for j in range(5):
                    if boards[k][i][j] == draws[m]:
                        bchk[k][i][j] = True
        for k in range(nb):
            for i in range(5):
                if all(bchk[k][i]):
                    return ans(boards[k], bchk[k], draws[m])
        for k in range(nb):
            for j in range(5):
                bchkj = [bchk[k][i][j] for i in range(5)]
                if all(bchkj):
                    return ans(boards[k], bchk[k], draws[m])

def p2(ifln):
    ifl = open(ifln, 'r')
    lyn = ifl.readline()
    boards = []
    while lyn != '':
        ls = lyn.split()
        if len(ls) > 5:
            draws = [int(l) for l in ls]
        if len(ls) == 5:
            boards.append([])
            for i in range(5):
                boards[-1].append([int(l) for l in ls])
                lyn = ifl.readline()
                ls = lyn.split()
        lyn = ifl.readline()
    nd = len(draws)
    nb = len(boards)
    bchk = [[[False for i in range(5)] for j in range(5)] for k in range(nb)]
    bfound = False
    kc = [True for i in range(nb)]
    for m in range(nd):
        for k in range(nb):
            for i in range(5):
                for j in range(5):
                    if boards[k][i][j] == draws[m]:
                        bchk[k][i][j] = True
        for k in range(nb):
            for i in range(5):
                if all(bchk[k][i]):
                    kc[k] = False
                    if kc.count(True) == 1:
                        k1 = kc.index(True)
                    if kc.count(True) == 0:
                        return ans(boards[k1], bchk[k1], draws[m])
        for k in range(nb):
            for j in range(5):
                bchkj = [bchk[k][i][j] for i in range(5)]
                if all(bchkj):
                    kc[k] = False
                    if kc.count(True) == 1:
                        k1 = kc.index(True)
                    if kc.count(True) == 0:
                        return ans(boards[k1], bchk[k1], draws[m])

print('Soltion of Test Puzzle 1:', p1('day-04_in0.txt'))
print('Soltion of Puzzle 1:', p1('day-04_in1.txt'))
print('Soltion of Test Puzzle 2:', p2('day-04_in0.txt'))
print('Soltion of Puzzle 2:', p2('day-04_in1.txt'))
