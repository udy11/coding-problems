# Backtracking

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

def nextpos(nd, c, ps):
    ''' finds next valid trying combination

        won't work with incorrect inputs
        
        INPUT:
        nd = total number of digits in a constraint
        c = correct numbers in that constraint
        ps = current position

        OUTPUT:
        st = if valid next position is available
        ps1 = new position
    '''
    if len(ps) == 0:
        return True, [i for i in range(c)]
    elif all([ps[i] == nd - c + i for i in range(c)]):
        return False, ps
    else:
        i = -1
        ps1 = ps[:]
        while i > -(c + 1):
            if ps1[i] < nd + i:
                ps1[i] += 1
                for j in range(i + 1, 0):
                    ps1[j] = ps1[i] - i + j
                return True, ps1
            i -= 1

def validpos(m, ps):
    for p in ps:
        if not itf[p][dgs[m][p]]:
            return False
    return True

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

dps = [[] for i in range(nc)]    # will hold current position of constraints
itf = [[True for i in range(10)] for j in range(nd)]    # will hold which digits are possible at any time

m = 0    # current constraint number
gnm = []    # contains current guess

while True:
    
