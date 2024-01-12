def score1(b):
    bs = {')' : 3, ']' : 57, '}' : 1197, '>' : 25137}
    return bs[b]

def score2(mc):
    bs = {'(' : 1, '[' : 2, '{' : 3, '<' : 4}
    sc = 0
    for i in range(len(mc)-1, -1, -1):
        sc *= 5
        sc += bs[mc[i]]
    return sc

def txusfn(ifl, mprs, meqs):
    def trnsp(mch):
        n = len(mch)
        for i in range(n):
            for j in range(i+1, n):
                if mch[i][0] == mch[j][0]:
                    print('WARNING: Recheck matches, multiple entries found for %s...' % mch[i][0])
                elif mch[i][0] in mch[j][0]:
                    t = mch[i]
                    mch[i] = mch[j]
                    mch[j] = t
        return mch
    def trnse(mch):
        n = len(mch)
        for i in range(n):
            for j in range(i+1, n):
                if mch[i] == mch[j]:
                    print('WARNING: Recheck matches, multiple entries found for %s...' % mch[i][0])
                elif mch[i] in mch[j]:
                    t = mch[i]
                    mch[i] = mch[j]
                    mch[j] = t
        return mch
    fyl = open(ifl, 'r')
    dt = fyl.read()
    fyl.close()
    n = len(dt)
    mprs = trnsp(mprs)
    npr = [(len(m[0]), len(m[1])) for m in mprs]
    np = len(mprs)
    meqs = trnse(meqs)
    neq = [len(m) for m in meqs]
    bs = []
    mpn = {m : [0, 0] for m in mprs}
    men = {m : 0 for m in meqs}
    nn = 1
    k = 0
    eok = True
    lynerr = {}
    while k < n:
        for j in range(np):
            if k+npr[j][0] < n and dt[k:k+npr[j][0]] == mprs[j][0]:
                bs.append((nn, mprs[j][0]))
                mpn[mprs[j]][0] += 1
                k += npr[j][0]
                break
            elif k+npr[j][1] < n and dt[k:k+npr[j][1]] == mprs[j][1]:
                mpn[mprs[j]][1] += 1
                if bs[-1][1] == mprs[j][0]:
                    bs.pop()
                else:
                    eok = False
                    #print('Expecting companion of %s from line %i, but found %s at line %i...' % (bs[-1][1], bs[-1][0], mprs[j][1], nn))
                    if not nn in lynerr:
                        lynerr[nn] = [score1(mprs[j][1])]
                    else:
                        lynerr[nn].append(score1(mprs[j][1]))
                    #input('Press any key to continue searching...')
                k += npr[j][1]
                break
        else:
            if dt[k] == '\n':
                nn += 1
                k += 1
#            elif dt[k] == '%':
#                while k < n and dt[k] != '\n':
#                    k += 1
            else:
                k += 1
    sscore1 = 0
    for lk in lynerr:
        sscore1 += lynerr[lk][0]
    sscore2 = []
    for i in range(1, nn + 1):
        if not i in lynerr:
            mbks = ''
            for bb in bs:
                if i == bb[0]:
                    mbks += bb[1]
            sscore2.append(score2(mbks))
    return sscore1, sorted(sscore2)[len(sscore2)//2]

# INPUTS
mprs = [('(', ')'),
        ('{', '}'),
        ('[', ']'),
        ('<', '>')]
meqs = []

# Make sure input file has no extra blank line at the end
# And last line has extra space at the very end

st1, st2 = txusfn('day-10_in0.txt', mprs, meqs)
s1, s2 = txusfn('day-10_in1.txt', mprs, meqs)
print('Soltion of Test Puzzle 1:', st1)
print('Soltion of Puzzle 1:', s1)
print('Soltion of Test Puzzle 2:', st2)
print('Soltion of Puzzle 2:', s2)
