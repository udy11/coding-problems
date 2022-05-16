# DYNAMIC PROGRAMMING

# A single and more general function can be defined instead of ms4, ms7, etc..

def read_data_1(ifln,sep):
    ifl = open(ifln, 'r')
    dn = 0
    dt = []
    while True:
        lyn = ifl.readline().strip()
        i = 0; d0 = []
        if lyn == "":
            break
        while i < len(lyn):
            if not lyn[i] in sep:
                k = 1
                while i+k < len(lyn) and not lyn[i+k] in sep:
                    k += 1
                d0.append(int(lyn[i:i+k]))
                i += k + 1
            else:
                i += 1
        dt.append(d0)
        dn += 1
    ifl.close()
    return dt

def cmbsl(a, r):
    ''' (list/tuple, int) -> list of list
        Returns r combinations of list/tuple a

        >>> a = [1, 2, 3, 4]; r = 3
        >>> cmbsl(a, r)
        [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
    '''
    if r == 1:
        return [[i] for i in a]
    n = len(a)
    if r < 1 or r > n:
        return []
    ct = []
    cm = []
    m = 0
    i = 0
    def cmbs():
        nonlocal m, ct, cm, i
        if m == 0:
            for k in range(n-r+2):
                i = k
                ct = [a[k]]
                m = 1
                cmbs()
        elif m == r-1:
            for k in range(i+1, n):
                cm.append(tuple(ct + [a[k]]))
        else:
            for k in range(i+1, n):
                i = k
                ct.append(a[k])
                m += 1
                cmbs()
                ct = ct[:-1]
                m -= 1
    cmbs()
    return cm

def tt(c, n):
    t = []
    for i in range(n):
        if not i in c:
            t.append(i)
    return tuple(t)

def ms2(r1, r2):
    return max(r2[0] + r1[1], r1[0] + r2[1])
        
def ms3(r1, r2, r3):
    return max(r1[0] + ms2(r2[1:], r3[1:]), r2[0] + ms2(r1[1:], r3[1:]), r3[0] + ms2(r1[1:], r2[1:]))

def ms4(r):
    c42 = cmbsl((0,1,2,3), 2)
    d1 = {}
    d2 = {}
    for c in c42:
        d1[c] = ms2(r[c[0]][:2], r[c[1]][:2])
        d2[c] = ms2(r[c[0]][2:], r[c[1]][2:])
    mx = 0
    for c in c42:
        s = d1[c] + d2[tt(c, 4)]
        if s > mx:
            mx = s
    return mx

def ms7(r):
    c73 = cmbsl((0,1,2,3,4,5,6), 3)
    c74 = cmbsl((0,1,2,3,4,5,6), 4)
    d1 = {}
    d2 = {}
    for c in c74:
        d1[c] = ms4([r[c[0]][:4], r[c[1]][:4], r[c[2]][:4], r[c[3]][:4]])
    for c in c73:
        d2[c] = ms3(r[c[0]][4:], r[c[1]][4:], r[c[2]][4:])
    mx = 0
    for c4 in c74:
        s = d1[c4] + d2[tt(c4, 7)]
        if s > mx:
            mx = s
    return mx

def ms8(r):
    c84 = cmbsl((0,1,2,3,4,5,6,7), 4)
    d1 = {}
    d2 = {}
    for c in c84:
        d1[c] = ms4([r[c[0]][:4], r[c[1]][:4], r[c[2]][:4], r[c[3]][:4]])
        d2[c] = ms4([r[c[0]][4:], r[c[1]][4:], r[c[2]][4:], r[c[3]][4:]])
    mx = 0
    for c4 in c84:
        s = d1[c4] + d2[tt(c4, 8)]
        if s > mx:
            mx = s
    return mx

def ms15(r):
    cx7 = cmbsl((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14), 7)
    cx8 = cmbsl((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14), 8)
    d1 = {}
    d2 = {}
    print('Combinations enlisted...')
    for c in cx7:
        d2[c] = ms7([r[c[i]][:7] for i in range(7)])
    print('d2 populated...')
    for c in cx8:
        d1[c] = ms8([r[c[i]][7:] for i in range(8)])
    print('d1 populated...')
    mx = 0
    for c8 in cx8:
        s = d1[c8] + d2[tt(c8, 15)]
        if s > mx:
            mx = s
    return mx

r15 = read_data_1('345_matrix.txt', ' ')
print(ms15(r15))
