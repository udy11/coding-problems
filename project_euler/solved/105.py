# BRUTE-FORCE (OPTIMIZED)

# OPTIMIZATIONS:
# To check property ii, sort the array and test if first i+1 elements
# are getting sum <= last i elements.
# For property i, assume property ii is satisfied, then only equal
# size subsets need to be checked. A combination table can be generated,
# which need to be only till half the size of set.

def read_data_1(ifln, sep):
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

def test1(st):
    ''' Tests property (i) in the problem
        assuming property (ii) is satisfied. '''
    ns = len(st)
    for c1 in dc[ns]:
        sm = []
        for c2 in c1:
            sm.append(sum([st[j] for j in c2]))
        sm.sort()
        for j in range(len(sm) - 1):
            if sm[j] == sm[j + 1]:
                return False
    return True

def test2(st):
    ''' Tests property (ii) in the problem.
        Only need to test if first i are getting <=
        than last i-1 in a sorted set. '''
    s1 = sorted(st)
    ns = len(s1)
    for i in range(2, (ns + 3) // 2):
        if sum(s1[:i]) <= sum(s1[ns-i+1:]):
            return False
    return True

sts = read_data_1('105_sets.txt', ',')

dc = {}
for n in range(7, 13):
    a = [i for i in range(n)]
    dc[n] = []
    for k in range(1, n // 2 + 1):
        dc[n].append(cmbsl(a, k))

s = 0
for st in sts:
    if test2(st) and test1(st):
        s += sum(st)
print(s)
