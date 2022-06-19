# BRUTE-FORCE

# First problem which used all my three
# nobel-prize-winning combinatorial functions

import math

def is_int(n):
    if n - int(n) == 0:
        return True
    return False

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
                cm.append(ct + [a[k]])
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

def ntpsl(a, r):
    ''' (list/tuple, int) -> list of list
        Returns r-tuples of list/tuple a

        >>> a = [1, 2]; r = 2
        >>> ntpsl(a, r)
        [[1, 1], [1, 2], [2, 1], [2, 2]]
    '''
    if r == 1:
        return [[i] for i in a]
    n = len(a)
    if r < 1 or r > n:
        return []
    ct = []
    nt = []
    m = 0
    def ntps():
        nonlocal m, ct, nt
        if m == 0:
            for k in range(n):
                ct = [a[k]]
                m = 1
                ntps()
        elif m == r-1:
            for k in range(n):
                nt.append(ct + [a[k]])
        else:
            for k in range(n):
                ct.append(a[k])
                m += 1
                ntps()
                ct = ct[:-1]
                m -= 1
    ntps()
    return nt

def prmsl(a, r):
    ''' (list/tuple, int) -> list of list
        Returns r permutations of list/tuple a

        >>> a = [1, 2, 3]; r = 2
        >>> prmsl(a, r)
        [[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]
    '''
    if r == 1:
        return [[i] for i in a]
    n = len(a)
    if r < 1 or r > n:
        return []
    pt = []
    pts = []
    ss = set([i for i in range(n)])
    sr = set()
    m = 0
    def prms():
        nonlocal pt, pts, ss, sr, m
        if m == 0:
            for k in ss:
                pt = [a[k]]
                m = 1
                sr = set([k])
                prms()
        elif m == r-1:
            for k in ss - sr:
                pts.append(pt + [a[k]])
        else:
            for k in ss - sr:
                pt.append(a[k])
                m += 1
                sr = sr.union(set([k]))
                prms()
                sr = sr - set([k])
                m -= 1
                pt = pt[:-1]
    prms()
    return pts

aldg = cmbsl(['1', '2', '3', '4', '5', '6', '7', '8', '9'], 4)

psn = ntpsl(['+', '-', '*', '/'], 3)
br1 = ([0, 1], [1, 2], [2, 3], [0, 2], [1, 3])
br2 = ([[0, 1], [0, 2]], [[0, 2], [1, 2]], [[1, 2], [1, 3]],
       [[1, 3], [2, 3]], [[0, 1], [2, 3]])

mxa = 0
mxd = []
for dgts in aldg:
    pdg = prmsl(dgts, 4)
    nev = []
    for ps in psn:
        for pd in pdg:
            st = pd[0] + ps[0] + pd[1] + ps[1] + pd[2] + ps[2] + pd[3]
            n = eval(st)
            if n > 0 and is_int(n) and not n in nev:
                nev.append(int(n))
            for b1 in br1:
                pd1 = list(pd)
                pd1[b1[0]] = '(' + pd1[b1[0]]
                pd1[b1[1]] += ')'
                st = pd1[0] + ps[0] + pd1[1] + ps[1] + pd1[2] + ps[2] + pd1[3]
                if st[1] == '/' and st[2] == '(' and st[-1] == ')' and eval(st[2:]) == 0:
                    continue
                n = eval(st)
                if n > 0 and is_int(n) and not n in nev:
                    nev.append(int(n))
            for b2 in br2:
                pd1 = list(pd)
                pd1[b2[0][0]] = '(' + pd1[b2[0][0]]
                pd1[b2[1][0]] = '(' + pd1[b2[1][0]]
                pd1[b2[0][1]] += ')'
                pd1[b2[1][1]] += ')'
                st = pd1[0] + ps[0] + pd1[1] + ps[1] + pd1[2] + ps[2] + pd1[3]
                if st[1] == '/' and st[2] == '(' and eval(st[2:]) == 0:
                    continue
                n = eval(st)
                if n > 0 and is_int(n) and not n in nev:
                    nev.append(int(n))
    nev.sort()
    k = 0
    nml = 1
    nmx = 0
    while k < len(nev)-1:
        if nev[k+1] - nev[k] == 1:
            nml += 1
        else:
            if nml > nmx:
                nmx = nml
            nml = 1
        k += 1
    print(dgts, nmx)
    if nmx > mxa:
        mxa = nmx
        mxd = dgts

print('Max for',mxd)
