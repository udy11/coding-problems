# BRUTE-FORCE

# The given "rule" in problem gives the starting point
# for first number in required array. One can still check
# nearby options with this program and see that others don't
# give better results. Then a search is made
# by all combinations that automatically satisfy property (ii).
# Such combinations are then tested for property (i). One can keep
# printing them and manually check for minimum sum.

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

def test1(st, ns):
    ''' Tests property (i) in the problem
        assuming property (ii) is satisfied. '''
    for c1 in dc:
        sm = []
        for c2 in c1:
            sm.append(sum([st[j] for j in c2]))
        sm.sort()
        for j in range(len(sm) - 1):
            if sm[j] == sm[j + 1]:
                return False
    return True

n = 7
dc = []
for k in range(1, n // 2 + 1):
    dc.append(cmbsl([i for i in range(n)], k))

# To get from 4 to 5 (set n = 5):
##k0 = 6
##k1 = k0 + 1
##while True:
##    for k4 in range(k1 + 3, k0 + k1):
##        for k2 in range(k1 + 1, k4 - 1):
##            for k3 in range(k2 + 1, min(k0 + k1 + k2 - k4, k4)):
##                a = [k0, k1, k2, k3, k4]
##                if test1(a, n):
##                    print(a, sum(a))
##    k1 += 1
##    input('Update k1...')

# To get from 6 to 7 (set n = 7):
k0 = 20
k1 = k0 + 1
while True:
    for k6 in range(k1 + 5, k0 + k1):
        for k2 in range(k1 + 1, k6 - 3):
            for k5 in range(k2 + 3, min(k0 + k1 + k2 - k6, k6)):
                for k3 in range(k2 + 1, k5 - 1):
                    for k4 in range(k3 + 1, min(k0 + k1 + k2 + k3 - k5 - k6, k5)):
                        a = [k0, k1, k2, k3, k4, k5, k6]
                        if test1(a, n):
                            print(a, sum(a))
    k1 += 1
    input('Update k1...')
