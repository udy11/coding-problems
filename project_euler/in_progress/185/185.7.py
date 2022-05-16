# BACKTRACKING?

# First we interpret data using tx2ar() function
# The digits go to to 2d array dgs
# Their correct counts go to array crc
# nr = number of rows or number of constraints
# nc = number of columns or number of digits in a row
# We also sort dgs and crc as per crc, ascendingly
# If any entry in crc==0, meaning there is no match
# in that row, then we can be sure that those digits
# can never appear in the final answer. So we build
# a possn0 array that stores all the digits that
# correspond to crc==0, i.e., digits that cannot be
# in answer. We then also eliminate this constraint
# from dgs and crc and reduce nr accordingly.
# Then we generate all combinations of indices (in cks)
# for all rows, and store their lengths in tkmx.
# We then eliminate those entries in cks that are
# in conflict with possn0.
# We shall iterate over these combinations and choose
# and accordingly check which combination is valid for
# a particular row. The row for which we're currently
# processing is marked with k. tk array stores which number
# of combination of a row is currently under consideration
# A value of -1 in tk represents that that row has not been
# considered yet.
# For each row, we also build 2 arrays possy and possn,
# possy stores that for a given combination of a row,
# which column is empty or filled, -1 represents empty
# here, empty means that any digit can be filled
# in that column and filled means only that digit can
# exist in that column.
# possn stores that for a given combination of a row,
# which column is empty or filled, -2 represents empty
# here, empty means all digits are allowed in that column
# and filled means that digit is not allowed in that column.
# So, basically possy stores digits that are already filled
# for each row and possn stores that which digits are not
# allowed for each row.
# So when we decide for a valid combination of next row,
# we need to check if it conflicts with either
# possy or possn. An entry in new combination conflicts:
# 1. with possy if corresponding entry in possy is non-empty
#     and doesn't match with any entry in all previous possy
# 2. with possn if corresponding entry in possy is non-empty
#    and matches with any entry in all previous possn
# If there's is conflict, we move on to the next tk[k]
# and when tk[k] reaches its limit, we decrease k
# If no conflict is found, we move on to the next k
# and update possy and possn accordingly
# An answer is found if no conflict is found in the last row
# An answer doesn't exist if all possibilities in first
# row are exhausted

# Note that answer may contain empty rows, which need to be
# filled separately (as it happens with 13th column for txin1)

# While the algorithm looks ok, it takes hours to reach the
# answer for txin1 (but runs in about a second for txin0)
# In contrast, the genetic algorithm gives answer
# much faster with right settings, though it is not always
# reliable because of randomness involved

import numpy as np
import sys
import time

def cmbsl(a, r):
    ''' (list/tuple, int) -> list of list
        Returns r combinations of list/tuple a

        >>> a = [1, 2, 3, 4]; r = 3
        >>> cmbsl(a, r)
        [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
    '''
    if r == 1:
        return [[i] for i in a]
    n = len(a)
    if r < 1 or r > n:
        return []
    ct = []
    cm = []
    m = 0
    i = 0
    def cmbs():
        nonlocal m, ct, cm, i
        if m == 0:
            for k in range(n-r+2):
                i = k
                ct = [a[k]]
                m = 1
                cmbs()
        elif m == r-1:
            for k in range(i+1, n):
                cm.append(ct + [a[k]])
        else:
            for k in range(i+1, n):
                i = k
                ct.append(a[k])
                m += 1
                cmbs()
                ct = ct[:-1]
                m -= 1
    cmbs()
    return cm

def tx2ar(tx):
    ''' (str) -> int, int, int numpy array (nr, nc), int numpy array (nr)
        Given raw data in prescribed format, the function returns
        nr = number of rows (int)
        nc = number of columns (int)
        dgs = individual digits (int numpy array of size (nr, nc))
        crc = number of corrects (int numpy array of size nr)
        dgs and crc are sorted ascendingly as per crc
    '''
    nr = tx.count('\n') + 1
    nc = tx.find(';') - 1
    dgs = np.empty((nr, nc), dtype = 'int32')
    crc = np.empty(nr, dtype = 'int32')
    k = 0
    for i in range(nr):
        for j in range(nc):
            dgs[i,j] = int(tx[k + j])
        k = tx.find('\n', k) + 1
    k = 0
    for i in range(nr):
        k = tx.find(';', k) + 1
        crc[i] = tx[k]
    ii = np.argsort(crc)
    dgs = dgs[ii]
    crc = crc[ii]
    return nr, nc, dgs, crc

def chkcor(s, a, nc):
    ''' (1d numpy array, 1d numpy array, int) -> int
        Given two 1d arrays of size nc, finds how many
        entries are matching
    '''
    return nc - np.count_nonzero(s - a)

def poss0(dgs, crc, nr, nc):
    p0 = [[] for j in range(nc)]
    i = 0
    while crc[i] == 0:
        for j in range(nc):
            p0[j].append(dgs[i,j])
        i += 1
    for j in range(nc):
        p0[j] = np.array(list(set(p0[j])), dtype = 'int32')
    return np.array(p0), i

txin0 = '''90342 ;2 correct
70794 ;0 correct
39458 ;2 correct
34109 ;1 correct
51545 ;2 correct
12531 ;1 correct'''

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

# Reading data and eliminating entries for crc==0
nr, nc, dgs, crc = tx2ar(txin1)
possn0, ic0 = poss0(dgs, crc, nr, nc)
nr -= ic0
dgs = dgs[ic0:]
crc = crc[ic0:]
ncj = tuple([j for j in range(nc)])

possy = np.array([np.array([-1 for j in range(nc)], dtype = 'int32') for i in range(nr)])
possn = np.array([np.array([-2 for j in range(nc)], dtype = 'int32') for i in range(nr)])
tk = -np.ones(nr, dtype = 'int32')

k = 3
tk[0] = 2
tk[1] = 0
tk[2] = 4
#k = 0
# Finding all combination indices and storing them separately for each row, storing their lengths (also max for tk) in tkmx
tkmx = np.empty(nr, dtype = 'int32')
cks = []
for i in range(nr):
    cs = cmbsl(ncj, crc[i])
    cks.append(cs)
    tkmx[i] = len(cs)

for i in range(3):
    for j in range(nc):
        if j in cks[i][tk[i]]:
            possy[i,j] = dgs[i,j]
            possn[i,j] = -2
        else:
            possy[i,j] = -1
            possn[i,j] = dgs[i,j]

# Removing combinations from cks that are in conflict with possn0
for i in range(nr):
    j = 0
    while j < tkmx[i]:
        for c in cks[i][j]:
            if dgs[i,c] in possn0[c]:
                cks[i].remove(cks[i][j])
                tkmx[i] -= 1
                break
        else:
            j += 1

tym0 = time.time()
chk = False
while not chk:
    #print(k, tk)
    #print(possy)
    #print(possn)
    #print('----')
    tk[k] += 1
    # If tk[k] has reached its limit, it means that we need to reconsider
    # previous row, so we reset current tk[k], its possy and possn, then
    # decrease k and increase its tk. A solution doesn't exist if all
    # possibilities for first row are exhausted
    if tk[k] >= tkmx[k]:
        tk[k] = -1
        for j in range(nc):
            possy[k,j] = -1
            possn[k,j] = -2
        k -= 1
        if k < 6:
            print('-', k, tk[k])
        if k < 0:
            print('k < 0, maybe no solution?')
            sys.exit()
        continue
    chk = True
    # Checking if new combination has any conflict with possy
    for i in range(k):
        for c in cks[k][tk[k]]:
            if not (possy[i,c] < 0 or dgs[k,c] == possy[i,c]):
                chk = False
                break
        if not chk:
            break
    if not chk:
        continue
    # Checking if new combination has any conflict with possn
    for i in range(k):
        for c in cks[k][tk[k]]:
            if not (possn[i,c] < 0 or dgs[k,c] != possn[i,c]):
                chk = False
                break
        if not chk:
            break
    if chk:
        chk = False
        # if no conflict is found we update possy and possn with new valid combination
        for j in range(nc):
            if j in cks[k][tk[k]]:
                possy[k,j] = dgs[k,j]
                possn[k,j] = -2
            else:
                possy[k,j] = -1
                possn[k,j] = dgs[k,j]
        # then we move on to the next row
        k += 1
        if k < 6:
            print('+', k, tk[k])
        # a solution is found if valid combination has been found for the last row
        if k >= nr:
            print('solution found?')
            sol = -np.ones(nc, dtype = 'int32')
            for i in range(nr):
                for j in range(nc):
                    if possy[i,j] >= 0:
                        sol[j] = possy[i,j]
            print(sol)
            print('Time taken:', time.time() - tym0, 's')
            sys.exit()
