def ucpy(inList):
    ''' Arbitrary depth copy for lists '''
    if isinstance(inList, list):
        return list( map(ucpy, inList) )
    return inList

def pstr(n1):
    ''' To generate Pascal's Triangle '''
    pt = [[1]]
    for n in range(1, n1 + 1):
        cc = [1]
        c = 1
        for r in range(n // 2):
            c = c * (n - r) // (r + 1)
            cc.append(c)
        if n % 2 == 0:
            pt.append(cc + cc[-2:-len(cc)-1:-1])
        else:
            pt.append(cc + cc[-1:-len(cc)-1:-1])
    return pt

def rplc(a, m, n):
    l = len(m)
    for i in range(len(a)):
        for j in range(len(a[i])):
            for k in range(l):
                if a[i][j] == m[k]:
                    a[i][j] = n[k]
                    break
    return a

def cmbsl(a, r):
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

def fqcr():
    global r, qc, qt, qm, ss, st, vrbs
    c2 = qt[r][-1]
    for i in range(qm):
        if ss[i] > -1 and qt[r][i] == ss[i]:
            c2 -= 1
    if c2 < 0 or ss.count(-1) < c2 or (r > qn - 2 and ss.count(-1) > c2):
        return False
    ir = [i for i in range(qm) if qt[r][i] > -1 and ss[i] < 0]
    for j in range(r):
        for k in range(qm):
            if qt[j][k] == qt[r][k] and k in ir and ss[k] < 0:
                ir.remove(k)
    li = len(ir)
    if vrbs > 1:
        print()
        print('------------------------')
        print(r, c2, ir)
        print(qt[r])
        print('------------------------')
        print()
    if li < c2:
        return False
    if c2 > 0:
        qc[r] = rplc(ucpy(tc[c2][:st[li][c2]]), [i for i in range(li)], ir)
    else:
        qc[r] = []
    if vrbs > 1:
        print()
        print('************************')
        if r > 1:
            print(r - 2, qc[r - 2])
        if r > 0:
            print(r - 1, qc[r - 1])
        print(r, qc[r])
        print('************************')
        print()
    return True

def nxti():
    global r, qc, qt, qm, ss, st, vrbs
    

def fssr():
    global ss, qc, qj, r, qn
    if qc[r]:
        for k in qc[r][qj[r]]:
            ss[k] = qt[r][k]

def ufssr():
    global ss, qc, qj, r, qn
    if qc[r]:
        for k in qc[r][qj[r]]:
            ss[k] = -1

qs = '''903423 ;2 correct
707945 ;0 correct
394587 ;3 correct
341092 ;1 correct
515459 ;2 correct
125310 ;1 correct'''

qqs = '''5616185650518293 ;2 correct
3847439647293047 ;1 correct
5855462940810587 ;3 correct
9742855507068353 ;3 correct
4296849643607543 ;3 correct
3174248439465858 ;1 correct
4513559094146117 ;2 correct
7890971548908067 ;3 correct
8157356344118483 ;1 correct
2615250744386899 ;2 correct
8690095851526254 ;3 correct
6375711915077050 ;1 correct
6913859173121360 ;1 correct
6442889055042768 ;2 correct
2321386104303845 ;0 correct
2326509471271448 ;2 correct
5251583379644322 ;2 correct
1748270476758276 ;3 correct
4895722652190306 ;1 correct
3041631117224635 ;3 correct
1841236454324589 ;3 correct
2659862637316867 ;2 correct'''

qt = [[]]
for c in qs:
    if 47 < ord(c) < 58:
        qt[-1].append(int(c))
    elif ord(c) == 10:
        qt.append([])
q0 = [q for q in qt if q[-1] == 0]
qt = [q for q in qt if not q[-1] == 0]
qm = len(qt[0]) - 1
qn = len(qt)
for i in range(qn):
    for j in range(qm):
        for q1 in q0:
            if qt[i][j] == q1[j]:
                qt[i][j] = -1
del q0
st = pstr(qm)
tc = {i : cmbsl([k for k in range(qm)], i) for i in set([q[-1] for q in qt])}
tc[0] = []
for t in tc:
    tt = []
    k = 0
    while k < qm:
        for c in tc[t]:
            if k in c and all([c1 <= k for c1 in c]):
                tt.append(c)
        k += 1
    tc[t] = ucpy(tt)
qc = [[] for j in range(qn)]
i0 = [i for i in range(qm) if qt[0][i] > -1]
qc[0] = rplc(ucpy(tc[qt[0][-1]][:st[len(i0)][qt[0][-1]]]), [i for i in range(len(i0))], i0)
ss = [-1 for i in range(qm)]
qj = [-1 for j in range(qn)]
qj[0] = 0
r = 0
vrbs = 2
while not chks():
    if nxti():
        fssr()
