def printdots(dxy):
    n = len(dxy)
    mxx = dxy[0][0]
    mxy = dxy[0][1]
    for i in range(1, n):
        if dxy[i][0] > mxx:
            mxx = dxy[i][0]
        if dxy[i][1] > mxy:
            mxy = dxy[i][1]
    dots = [[False for i in range(mxx+1)] for j in range(mxy+1)]
    for i in range(n):
        dots[dxy[i][1]][dxy[i][0]] = True
    for j in range(len(dots)):
        for i in range(len(dots[0])):
            if dots[j][i]:
                print('#', end = '')
            else:
                print('∙', end = '')
        print()

def p1(ifln):
    ifl = open(ifln, 'r')
    lyn = ifl.readline()
    folds = []
    dxy = []
    while lyn != '':
        if 'fold' in lyn:
            ls = lyn[:-1].split('=')
            folds.append([ls[0][-1], int(ls[1])])
        else:
            ls = lyn.split(',')
            if len(ls) == 2:
                dxy.append([int(ls[0]), int(ls[1])])
        lyn = ifl.readline()
    for f in folds:
        dxyt = []
        n = len(dxy)
        if f[0] == 'x':
            for i in range(n):
                if dxy[i][0] < f[1]:
                    dxyt.append(dxy[i])
                elif dxy[i][0] > f[1]:
                    if not [2 * f[1] - dxy[i][0], dxy[i][1]] in dxy:
                        dxyt.append([2 * f[1] - dxy[i][0], dxy[i][1]])
        elif f[0] == 'y':
            for i in range(n):
                if dxy[i][1] < f[1]:
                    dxyt.append(dxy[i])
                elif dxy[i][1] > f[1]:
                    if not [dxy[i][0], 2 * f[1] - dxy[i][1]] in dxy:
                        dxyt.append([dxy[i][0], 2 * f[1] - dxy[i][1]])
        dxy = list(dxyt)
        return len(dxy)

def p2(ifln):
    ifl = open(ifln, 'r')
    lyn = ifl.readline()
    folds = []
    dxy = []
    while lyn != '':
        if 'fold' in lyn:
            ls = lyn[:-1].split('=')
            folds.append([ls[0][-1], int(ls[1])])
        else:
            ls = lyn.split(',')
            if len(ls) == 2:
                dxy.append([int(ls[0]), int(ls[1])])
        lyn = ifl.readline()
    for f in folds:
        dxyt = []
        n = len(dxy)
        if f[0] == 'x':
            for i in range(n):
                if dxy[i][0] < f[1]:
                    dxyt.append(dxy[i])
                elif dxy[i][0] > f[1]:
                    if not [2 * f[1] - dxy[i][0], dxy[i][1]] in dxy:
                        dxyt.append([2 * f[1] - dxy[i][0], dxy[i][1]])
        elif f[0] == 'y':
            for i in range(n):
                if dxy[i][1] < f[1]:
                    dxyt.append(dxy[i])
                elif dxy[i][1] > f[1]:
                    if not [dxy[i][0], 2 * f[1] - dxy[i][1]] in dxy:
                        dxyt.append([dxy[i][0], 2 * f[1] - dxy[i][1]])
        dxy = list(dxyt)
    printdots(dxy)

print('Soltion of Test Puzzle 1:', p1('day-13_in0.txt'))
print('Soltion of Puzzle 1:', p1('day-13_in1.txt'))
print('Soltion of Test Puzzle 2:')
p2('day-13_in0.txt')
print('Soltion of Puzzle 2:')
p2('day-13_in1.txt')
