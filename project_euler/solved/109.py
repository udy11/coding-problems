# BRUTE FORCE (more or less)

# Generate all valid throws and simply count the scores

# Can be optimized in numerous ways but this novice
# implementation also works pretty fast

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

def score(c):
    n = len(c)
    s = 0
    for i in range(n):
        if c[i][0] == 'S':
            s += int(c[i][1:])
        if c[i][0] == 'D':
            s += int(c[i][1:]) * 2
        if c[i][0] == 'T':
            s += int(c[i][1:]) * 3
    return s

hitd = ['D' + str(i) for i in range(1, 21)] + ['D25']
hita = ['S' + str(i) for i in range(1, 21)] + ['S25'] + ['T' + str(i) for i in range(1, 21)] + hitd

cc = [[d] for d in hitd]
cc += ntpsl(hita, 2)
c2 = cmbsl(hita, 2)
for d in hitd:
    for ac in c2:
        cc.append(ac + [d])
    for w in hita:
        cc.append([w, w, d])

v = [0 for k in range(100)]

for c in cc:
    s = score(c)
    if s < 100 and c[-1][0] == 'D':
        v[s] += 1

print(sum(v))
