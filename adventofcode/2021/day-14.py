import sys

def count(cs):
    cc = {c : 0 for c in set([c1 for c1 in ''.join([q for q in cs])])}
    for q in cs:
        cc[q[0]] += cs[q]
        cc[q[1]] += cs[q]
    for c in cc:
        cc[c] = (cc[c] + 1) // 2    # why though????
    return max(cc.values()) - min(cc.values())

def p1(ifln, steps):
    ifl = open(ifln, 'r')
    s0 = ifl.readline()[:-1]
    n = len(s0)
    cs0 = {}
    for i in range(n-1):
        if s0[i] + s0[i+1] in cs0:
            cs0[s0[i] + s0[i+1]] += 1
        else:
            cs0[s0[i] + s0[i+1]] = 1
    lyn = ifl.readline()
    rls = {}
    while lyn != '':
        ls = lyn[:-1].split(' -> ')
        if len(ls) == 2:
            rls[ls[0]] = (ls[0][0] + ls[1], ls[1] + ls[0][1])
        lyn = ifl.readline()
    for k in range(steps):
        cs1 = dict(cs0)
        for c in cs0:
            if c in rls:
                if rls[c][0] in cs1:
                    cs1[rls[c][0]] += cs0[c]
                else:
                    cs1[rls[c][0]] = cs0[c]
                if rls[c][1] in cs1:
                    cs1[rls[c][1]] += cs0[c]
                else:
                    cs1[rls[c][1]] = cs0[c]
                cs1[c] -= cs0[c]
        cs0 = dict(cs1)
    return count(cs0)

print('Result for Test Puzzle 1:', p1('day-14_in0.txt', 10))
print('Result for Puzzle 1:', p1('day-14_in1.txt', 10))
print('Result for Test Puzzle 2:', p1('day-14_in0.txt', 40))
print('Result for Puzzle 2:', p1('day-14_in1.txt', 40))

