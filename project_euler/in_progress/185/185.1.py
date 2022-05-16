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

def stme():
    ''' sets current empty and matching values of st '''
    global se, sm
    se = 0
    sm = 0
    for i in range(qm):
        if st[i] == -1:
            se += 1
        elif st[i] == qt[r][i]:
            sm += 1

def cccc(r):
    ''' current constraint consistency checker '''
    if sm > qt[r][-1]:
        return False
    elif sm + se < qt[r][-1]:
        return False
    else:
        return True

def pccc(r):
    ''' previous constraints consistency checker '''
    for k in range(r - 1):
        m = 0
        for i in range(qm):
            if st[i] == qt[k][i]:
                m += 1
        if m > qt[k][-1]:
            return False
    return True

def srti():
    if rt[r][0] == -1:
        rt[r][1] = qt[r][-1] - sm
        rt[r][2] = len(qc[rt[r][1]])
        for i in range(rt[r][2]):
            for j in qc[rt[r][1]][i]:
                if st[j] > 0:
                    break
            else:
                break
        rt[r][0] = i
        return True
    elif rt[r][0] == rt[r][2] - 1:
        rt[r] = [-1, 0, 0]
        return False


qs = '''90342 ;2 correct
70794 ;0 correct
39458 ;2 correct
34109 ;1 correct
51545 ;2 correct
12531 ;1 correct'''

qt = [[]]
for c in qs:
    if 47 < ord(c) < 58:
        qt[-1].append(int(c))
    elif ord(c) == 10:
        qt.append([])
qm = len(qt[0]) - 1
qn = len(qt)
qc = {i : cmbsl([k for k in range(qm)], i) for i in range(1, 4)}   # all possible index combinations that need to be checked
qc[0] = [[]]

st = [-1 for i in range(qm)]    # solution string
rt = [[-1, 0, 0] for j in range(qn)]   # parameters of current constraint under processing
r = 0   # the current constraint number (in [0, qn))
cnt = True   # checks if solution is found

while cnt:
    stme()
    print(r)
    print(st)
    print(rt)
    print()
    input()
    if cccc(r):
        if vldi():
            sadv()
        else:
            r -= 1
    else:
        r -= 1
        
