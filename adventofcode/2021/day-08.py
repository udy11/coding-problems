import sys

def dc_finder(dps):
    dc = {}
    for i in dps:
        ctf = 0
        for d in dps[i]:
            if dps[i][d]:
                ctf += 1
                dc[d] = str(i)
        if ctf != 1:
            print('Invalid dps', i, dps[i])
            sys.exit()
    return dc

def dgconv(dg):
    dgc = {'012456' : 0,
           '25' : 1,
           '02346' : 2,
           '02356' : 3,
           '1235' : 4,
           '01356' : 5,
           '013456' : 6,
           '025' : 7,
           '0123456' : 8,
           '012356' : 9}
    return dgc[dg]

def p1(ifln):
    ifl = open(ifln, 'r')
    lyn = ifl.readline()
    c = 0
    while lyn != '':
        ls0, ls1 = lyn[:-1].split(' | ')
        for l in ls1.split(' '):
            if len(l) in (2, 3, 4, 7):
                c += 1
        lyn = ifl.readline()
    return c

def p2(ifln):
    ifl = open(ifln, 'r')
    lyn = ifl.readline()
    sumd = 0
    while lyn != '':
        ls0, ls1 = lyn[:-1].split(' | ')
        lds = {2 : '', 3 : '', 4 : '', 5 : [], 6 : []}
        for l in ls0.split() + ls1.split():
            ll = len(l)
            if ll < 5:
                lds[ll] = ''.join(sorted(l))
            elif ll < 7:
                lds[ll].append(''.join(sorted(l)))
        lds[5] = list(set(lds[5]))
        lds[6] = list(set(lds[6]))
        dps = {i : {d : True for d in 'abcdefg'} for i in range(7)}
        if lds[2] != '':
            for c in 'abcdefg':
                if c in lds[2]:
                    dps[0][c] = False
                    dps[1][c] = False
                    dps[3][c] = False
                    dps[4][c] = False
                    dps[6][c] = False
                else:
                    dps[2][c] = False
                    dps[5][c] = False
        if lds[3] != '':
            for c in 'abcdefg':
                if c in lds[3]:
                    dps[1][c] = False
                    dps[3][c] = False
                    dps[4][c] = False
                    dps[6][c] = False
                else:
                    dps[0][c] = False
                    dps[2][c] = False
                    dps[5][c] = False
        if lds[4] != '':
            for c in 'abcdefg':
                if c in lds[4]:
                    dps[0][c] = False
                    dps[4][c] = False
                    dps[6][c] = False
                else:
                    dps[1][c] = False
                    dps[2][c] = False
                    dps[3][c] = False
                    dps[5][c] = False
        if len(lds[5]) == 3:
            lds5 = ''.join(lds[5])
            for c in 'abcdefg':
                cc = lds5.count(c)
                if cc == 1:
                    dps[0][c] = False
                    dps[2][c] = False
                    dps[3][c] = False
                    dps[5][c] = False
                    dps[6][c] = False
                elif cc == 2:
                    dps[0][c] = False
                    dps[1][c] = False
                    dps[3][c] = False
                    dps[4][c] = False
                    dps[6][c] = False
                elif cc == 3:
                    dps[1][c] = False
                    dps[2][c] = False
                    dps[4][c] = False
                    dps[5][c] = False
        if len(lds[6]) == 3:
            lds6 = ''.join(lds[6])
            for c in 'abcdefg':
                cc = lds6.count(c)
                if cc == 2:
                    dps[0][c] = False
                    dps[1][c] = False
                    dps[5][c] = False
                    dps[6][c] = False
                elif cc == 3:
                    dps[2][c] = False
                    dps[3][c] = False
                    dps[4][c] = False
        dc = dc_finder(dps)
        sd = ''
        for l in ls1.split():
            dg = ''
            for d in l:
                dg += dc[d]
            sd += str(dgconv(''.join(sorted(dg))))
        sumd += int(sd)
        lyn = ifl.readline()
    return sumd

print(p1('day-08_in0.txt'))
print(p1('day-08_in1.txt'))
print(p2('day-08_in0.txt'))
print(p2('day-08_in1.txt'))

