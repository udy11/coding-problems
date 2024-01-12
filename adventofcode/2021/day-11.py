import sys

in0 = '''5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526'''

in1 = '''4134384626
7114585257
1582536488
4865715538
5733423513
8532144181
1288614583
2248711141
6415871681
7881531438'''

def octoprint(octos, nr, nc):
    for i in range(nr):
        for j in range(nc):
            print(octos[(i, j)], end = '')
        print()
    print()

def countzeros(octos, nr, nc):
    c0 = 0
    for i in range(nr):
        for j in range(nc):
            if octos[(i, j)] == 0:
                c0 += 1
    return c0

def nbrs(i, j, nr, nc):
    i1 = [i]
    j1 = [j]
    if i > 0:
        i1.append(i-1)
    if i < nr-1:
        i1.append(i+1)
    if j > 0:
        j1.append(j-1)
    if j < nc-1:
        j1.append(j+1)
    nbs = [(i0, j0) for j0 in j1 for i0 in i1]
    nbs.remove((i,j))
    return nbs

def flash(octos, i, j, nr, nc):
    if octos[(i, j)] > 9:
        octos[(i, j)] = 0
        nbs = nbrs(i, j, nr, nc)
        for nb in nbs:
            if octos[(nb[0], nb[1])] > 0:
                octos[(nb[0], nb[1])] += 1
                if octos[(nb[0], nb[1])] > 9:
                    flash(octos, nb[0], nb[1], nr, nc)

def p1(inp):
    octos = {}
    nr = 0
    for lyn in inp.split('\n'):
        nc = 0
        for l in lyn:
            octos[(nr, nc)] = int(l)
            nc += 1
        nr += 1
    c0s = 0
    for k in range(1, 101):
        for i in range(nr):
            for j in range(nc):
                octos[(i, j)] += 1
        for i in range(nr):
            for j in range(nc):
                flash(octos, i, j, nr, nc)
        c0s += countzeros(octos, nr, nc)
        #octoprint(octos, nr, nc)
    return c0s

def p2(inp):
    octos = {}
    nr = 0
    for lyn in inp.split('\n'):
        nc = 0
        for l in lyn:
            octos[(nr, nc)] = int(l)
            nc += 1
        nr += 1
    k = 0
    while True:
        k += 1
        for i in range(nr):
            for j in range(nc):
                octos[(i, j)] += 1
        for i in range(nr):
            for j in range(nc):
                flash(octos, i, j, nr, nc)
        if countzeros(octos, nr, nc) == nr * nc:
            return k

print('Soltion of Test Puzzle 1:', p1(in0))
print('Soltion of Puzzle 1:', p1(in1))
print('Soltion of Test Puzzle 2:', p2(in0))
print('Soltion of Puzzle 2:', p2(in1))
