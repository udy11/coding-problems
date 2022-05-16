# Generate all possible combinations of 0,1,2 and find their divisors

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
    if r < 1:
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

n = 4
t = 101
dv = [0 for i in range(t)]

k = 1
while k < n:
    tps = ntpsl([0, 1, 2], k)
    for t in tps:
        n0 = sum(t[j] * 10 ** j for j in range(k))
        n1 = 10 ** k + n0
        n2 = 2 * 10 ** k + n0
        print(n1, n2)
    k += 1
