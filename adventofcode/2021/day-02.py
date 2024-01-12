def hpvp1(ifln):
    hp = 0
    vp = 0
    ifl = open(ifln, 'r')
    lyn = ifl.readline()
    while lyn != '':
        ls = lyn.split()
        if len(ls) == 2:
            if ls[0] == 'forward':
                hp += int(ls[1])
            elif ls[0] == 'down':
                vp += int(ls[1])
            elif ls[0] == 'up':
                vp -= int(ls[1])
        lyn = ifl.readline()
    ifl.close()
    return hp * vp

def hpvp2(ifln):
    hp = 0
    vp = 0
    ap = 0
    ifl = open(ifln, 'r')
    lyn = ifl.readline()
    while lyn != '':
        ls = lyn.split()
        if len(ls) == 2:
            if ls[0] == 'forward':
                hp += int(ls[1])
                vp += ap * int(ls[1])
            elif ls[0] == 'down':
                ap += int(ls[1])
            elif ls[0] == 'up':
                ap -= int(ls[1])
        lyn = ifl.readline()
    ifl.close()
    return hp * vp

print('Result for Test Puzzle 1:', hpvp1('day-02_in0.txt'))
print('Result for Puzzle 1:', hpvp1('day-02_in1.txt'))
print('Result for Test Puzzle 2:', hpvp2('day-02_in0.txt'))
print('Result for Puzzle 2:', hpvp2('day-02_in1.txt'))

