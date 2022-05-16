import math
def fctr(n):
    ''' (int) -> list
        Function to get all factors of n
        Resulting list is unsorted and does not contain 1 and n
    '''
    fc = []
    for i in range(2, 1 + math.ceil(math.sqrt(n))):
        if n % i == 0:
            fc += [i, n // i]
    return fc

pqd = []
n = 51
for a in range(1, n):
    for b in range(a, n):
        ab = a * a + b * b
        abf = fctr(ab)
        for p in abf:
            p2 = p * p
            if p2 < ab and not (a % 2 == 1 and b % 2 == 1):
                c = (ab - p2) // (2 * p)
                d = (ab + p2) // (2 * p)
                if d < 51:
                    pqd.append([a, b, c, d])

npqd = []
for qd in pqd:
    if qd[3] < 26:
        k = 2
        while k * qd[3] < 51:
            npqd.append([k * qd[0], k * qd[1], k * qd[2], k * qd[3]])
            k += 1
pqd += npqd

pdc = {}
for qd in pqd:
    if qd[3] in pdc:
        if not sorted([qd[0], qd[1], qd[2]]) in pdc[qd[3]]:
            pdc[qd[3]].append(sorted([qd[0], qd[1], qd[2]]))
    else:
        pdc[qd[3]] = [sorted([qd[0], qd[1], qd[2]])]

for r in pdc:
    print(r, pdc[r])
