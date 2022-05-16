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

#a = ['a', 'b', 'c', 'd']
a = ['a', 'b', 'c']
n = len(a)
ap = [b[0] + b[1] + b[2] for b in prmsl(a, n)]
#ap = [b[0] + b[1] + b[2] + b[3] for b in prmsl(a, n)]

t3 = [b[0] + b[1] for b in ntpsl(a, n-1)]
#t3 = [b[0] + b[1] + b[2] for b in ntpsl(a, n-1)]
m3 = [[False for i in t3] for j in t3]
n3 = len(t3)
for i in range(n3):
    for j in range(n3):
        if t3[i][1:] == t3[j][:-1] and not t3[i] + t3[j][-1] in ap: #check conditions
            m3[i][j] = True

for i in range(n3):
    for j in range(n3):
        if m3[i][j]:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()

