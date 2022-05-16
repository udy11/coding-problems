# BRUE FORCE

# Since any polygon number can be after any other, one needs to check
# on all permutations of these polygon numbers
# Thus first generate a list of permutaions of indices from 0 to 5
# Then iterate over all these permutations and check the required

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

p6 = perms_list([0, 1, 2, 3, 4, 5])

nl = [[] for i in range(6)]
nl[0] = [n * (3 * n - 2) for n in range(19, 59)]
nl[1] = [n * (5 * n - 3) // 2 for n in range(21, 64)]
nl[2] = [n * (2 * n - 1) for n in range(23, 71)]
nl[3] = [n * (3 * n - 1) // 2 for n in range(26, 82)]
nl[4] = [n * n for n in range(32, 101)]
nl[5] = [n * (n + 1) // 2 for n in range(45, 141)]

for p in p6:
    mm = [[i] for i in nl[p[5]]]
    for n in range(4, -1, -1):
        nn = []
        for i in mm:
            for j in nl[p[n]]:
                if str(i[0])[:2] == str(j)[2:]:
                    nn.append([j] + i)
        mm = nn
    for m in mm:
        if str(m[0])[:2] == str(m[5])[2:]:
            print(m)
