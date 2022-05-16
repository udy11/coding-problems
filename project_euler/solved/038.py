def is_pdg(s):
    ''' Checks if it is a 9-digit palindrome '''
    if(len(s)) != 9:
        return False
    for i in range(1,10):
        if(s.count(str(i))) != 1:
            return False
    return True

def swaps(a, ac):
    ''' (list, list) -> list
        Performs swap of list a based on list ac.
        The nth entry of ac decides where to swap
        the nth entry of list a. '''
    b = list(a)
    j = 0
    for i in ac:
        if i:
            t = b[j]
            b[j] = b[j + i]
            b[j + i] = t
        j += 1
    return b

def fctrl(n):
    ''' (int) -> int
        Function to calculate Factorial.
        Assumes non-negative input. '''
    if n<2:
        return 1
    fc = 2
    for i in range(3,n+1):
        fc *= i
    return fc

def perms(aa):
    ''' (str, list) -> int
        Returns all permutations of objects in the list aa.
        Repeated entries in list aa are treated as distinct.'''
    n = len(aa) - 1
    a = [i for i in range(n+1)]
    nf = [1]
    for i in range(2, n + 1):
        nf = [fctrl(i)] + nf
    ac = [0 for j in range(n)]
    n1f = nf[0] * (n+1)
    ap = [aa]
    for m in range(1, n1f):
        for j in range(n):
            mq = m // nf[j]
            ac[j] = mq
            m -= mq * nf[j]
        ap.append(swaps(aa, ac))
    return ap

def combs(a,n):
    na = len(a)
    al = [True for i in range(n)] + [False for i in range(na-n)]
    alp = perms(al)
    ald = {}
    for i in alp:
        ald[tuple(i)] = 0
    alp = list(ald)
    ac = []
    for i in alp:
        at = []
        for j in range(na):
            if i[j]:
                at.append(a[j])
        ac.append(at)
    return sorted(ac)

def perm(a,n):
    ''' Returns permutations.'''
    ac = combs(a, n)
    ap = []
    for c in ac:
        ap += perms(c)
    return ap

def ltn(a):
    ''' List of Digits -> Number.'''
    n = len(a)
    s = a[n-1]
    for i in range(n-1):
        s += a[i] * 10 ** (n-i-1)
    return s

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for j in range(1,5):
    print('For',j)
    acj = perm(a,j)
    for k in acj:
        n = ltn(k)
        s = str(n)
        m = 2
        while True:
            s += str(n * m)
            m += 1
            if len(s) > 8:
                break
        if is_pdg(s):
            print(s)
