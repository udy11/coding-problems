# Simple Backtracking

def tx2dg(tx):
    ''' converts raw input to list form '''
    dgs = [[]]
    dcs = []
    chs = tuple([str(i) for i in range(10)])
    i = 0
    while i < len(tx):
        if tx[i] in chs:
            dgs[-1].append(int(tx[i]))
        elif tx[i] == ';':
            i += 1
            dgs.append([])
            dcs.append(int(tx[i]))
        i += 1
    dgs.pop()
    return dgs, dcs

def chk(nd, nc, g, dgs, dcs):
    ii = g.count(-1)
    for i in range(nc):
        ic = 0
        for j in range(nd):
            if dgs[i][j] == g[j]:
                ic += 1
        if ic > dcs[i]:
            return False
        if ii + ic < dcs[i]:
            return False
    return True

def gnxt():
    global gk, gnm
    if gnm[gk] < 9:
        gnm[gk] += 1
        return True
    elif gk < nd-1 and gnm[gk] == 9:
        gnm[gk+1] += 1
        for i in range(gk+1):
            gnm[i] = -1
        gk = 0
        gnm[gk] += 1
    else:
        return False

txin0 = '''903423 ;2 correct
707945 ;0 correct
394587 ;3 correct
341092 ;1 correct
515459 ;2 correct
125310 ;1 correct'''

txin1 = '''5616185650518293 ;2 correct
3847439647293047 ;1 correct
5855462940810587 ;3 correct
9742855507068353 ;3 correct
4296849643607543 ;3 correct
3174248439465858 ;1 correct
4513559094146117 ;2 correct
7890971548908067 ;3 correct
8157356344118483 ;1 correct
2615250744386899 ;2 correct
8690095851526254 ;3 correct
6375711915077050 ;1 correct
6913859173121360 ;1 correct
6442889055042768 ;2 correct
2321386104303845 ;0 correct
2326509471271448 ;2 correct
5251583379644322 ;2 correct
1748270476758276 ;3 correct
4895722652190306 ;1 correct
3041631117224635 ;3 correct
1841236454324589 ;3 correct
2659862637316867 ;2 correct'''

dgs, dcs = tx2dg(txin0)

nd = len(dgs[0])    # number of digits
nc = len(dgs)    # number of constraints

gnm = [-1 for i in range(nd)]
gk = 0
gc = True

while True:
    gc = gnxt()
    ch = chk(nd, nc, gnm, dgs, dcs)
    print(gnm, ch)
    input('')
    if ch and gnm[-1] >= 0:
        print(gnm)
        break
