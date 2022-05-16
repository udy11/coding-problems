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

a = (-2, 1, -1, 2)
coefs = ntpsl(a, 12)
print(len(coefs))
for cs in coefs:
    alf = [cs[0], cs[1], cs[2], cs[3]]
    bet = [cs[4], cs[5], cs[6], cs[7]]
    gma = [cs[8], cs[9], cs[10], cs[11]]
    c1 = -1 + alf[0]**2 + bet[0]**2 - gma[0]**2
    cx2 = alf[1]**2 + bet[1]**2 - gma[1]**2
    cy2 = alf[2]**2 + bet[2]**2 - gma[2]**2
    cz2 = alf[3]**2 + bet[3]**2 - gma[3]**2
    cx = 2*alf[0]*alf[1] + 2*bet[0]*bet[1] - 2*gma[0]*gma[1]
    cy = 2*alf[0]*alf[2] + 2*bet[0]*bet[2] - 2*gma[0]*gma[2]
    cz = 2*alf[0]*alf[3] + 2*bet[0]*bet[3] - 2*gma[0]*gma[3]
    cxy = 2*alf[1]*alf[2] + 2*bet[1]*bet[2] - 2*gma[1]*gma[2]
    cxz = 2*alf[1]*alf[3] + 2*bet[1]*bet[3] - 2*gma[1]*gma[3]
    cyz = 2*alf[2]*alf[3] + 2*bet[2]*bet[3] - 2*gma[2]*gma[3]
    if cxy == cyz == cxz == cx == cy == cz == c1 == 0 and cx2 == cy2 == -cz2 and cx2 != 0:
        print(alf, bet, gma)
