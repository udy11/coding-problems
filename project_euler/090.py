# BRUTE FORCE

# Had originally thought of various optimizations like
# 2 and 5 can be counted logically since both need to
# there in distinct sets. Also the duo of 6 and 9 can
# be handled with logic too.
# However, brute force works quick as well.

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

def qq(a, b, n1, n2):
    if (n1 in a and n2 in b) or (n1 in b and n2 in a):
        return True
    else:
        return False

def q6(a, b, n):
    na = n in a
    nb = n in b
    a6 = 6 in a or 9 in a
    b6 = 6 in b or 9 in b
    if na and (not nb):
        if not b6:
            return False
    elif (not na) and nb:
        if not a6:
            return False
    elif na and nb:
        if (not a6) and (not b6):
            return False
    return True

def ps(a, b):

    dd = [0, 1, 2, 3, 4, 5, 8]
    for d in dd:
        if (not d in a) and (not d in b):
            return False

    if ((not 6 in a) and (not 6 in b)) and ((not 9 in a) and (not 9 in b)):
        return False

    if not qq(a, b, 0, 1):
        return False

    if not qq(a, b, 0, 4):
        return False

    if not q6(a, b, 0):
        return False

    if not q6(a, b, 1):
        return False

    if not qq(a, b, 2, 5):
        return False

    if not q6(a, b, 3):
        return False

    if not q6(a, b, 4):
        return False

    if not qq(a, b, 8, 1):
        return False

    return True

c = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

c6 = cmbsl(c, 6)
cn = len(c6)

cc = 0
for i in range(cn):
    for j in range(i+1, cn):
        if ps(c6[i], c6[j]):
            # print(c6[i], c6[j])
            cc += 1

print(cc)
