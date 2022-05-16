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

a = (0, 1, 2)
coefs = ntpsl(a, 9)
for cs in coefs:
    alf = [cs[0], cs[1], cs[2]]
    bet = [cs[3], cs[4], cs[5]]
    gma = [cs[6], cs[7], cs[8]]
    cx2 = -alf[0]**2 + bet[0]**2 - bet[0] * gma[0] + gma[0]**2
    cy2 = -alf[1]**2 + bet[1]**2 - bet[1] * gma[1] + gma[1]**2
    cz2 = -alf[2]**2 + bet[2]**2 - bet[2] * gma[2] + gma[2]**2
    cxy = -2 * alf[0] * alf[1] + 2 * bet[0] * bet[1] - bet[1] * gma[0] - bet[0] * gma[1] + 2 * gma[0] * gma[1]
    cyz = -2 * alf[1] * alf[2] + 2 * bet[1] * bet[2] - bet[2] * gma[1] - bet[1] * gma[2] + 2 * gma[1] * gma[2]
    cxz = -2 * alf[0] * alf[2] + 2 * bet[0] * bet[2] - bet[2] * gma[0] - bet[0] * gma[2] + 2 * gma[0] * gma[2]
    if cxy == cyz == cxz == 0 and cx2 == cy2 == -cz2 and cx2 != 0:
        print(alf, bet, gma)
