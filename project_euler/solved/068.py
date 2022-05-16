# LOGIC

# For 16-digit string, of course 10 must lie in
# outer vertices. And for maximum, 6 to 9 should also
# lie in outside vertices, however order is not known.
# So simply try all such permutations of inner and outer
# vertices and check the sums.

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

def perms_list(aa):
    ''' (list) -> list of lists
        Function returns list of list containing all permutations
        Repeated entries in list aa are treated as distinct.'''
    n = len(aa) - 1
    a = [i for i in range(n+1)]
    nf = [1]
    for i in range(2, n + 1):
        nf = [fctrl(i)] + nf
    an = list(a)
    ac = [0 for j in range(n)]
    n1f = nf[0] * (n+1)
    prms = [aa]
    for m in range(1, n1f):
        for j in range(n):
            mq = m // nf[j]
            ac[j] = mq
            m -= mq * nf[j]
        prms.append(swaps(aa, ac))
    return prms

c69 = perms_list([6, 7, 8, 9])
d15 = perms_list([1, 2, 3, 4, 5])

for c in c69:
    for d in d15:
        m1 = [10, d[0], d[1]]
        m2 = [c[0], d[1], d[2]]
        m3 = [c[1], d[2], d[3]]
        m4 = [c[2], d[3], d[4]]
        m5 = [c[3], d[4], d[0]]
        s = sum(m1)
        if s == sum(m2) == sum(m3) == sum(m4) == sum(m5):
            print(s, m1, m2, m3, m4, m5)
