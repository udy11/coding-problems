# GENETIC ALGORITHM

# First we interpret data using tx2ar() function
# The digits go to to 2d array dgs
# Their correct counts go to array crc
# nr = number of rows or number of constraints
# nc = number of columns or number of digits in a row
# We also sort dgs and crc as per crc, ascendingly
# If any entry in crc==0, meaning there is no match
# in that row, then we can be sure that those digits
# can never appear in the final answer. So we build
# a poss array that stores only the possible digits,
# this includes all digits that have appeared at least
# once and excludes all digits corresponding to crc==0
# However, if only one digit is missing from possibilities
# (apart from crc==0 case) then it may still appear
# read in more detail in dgposs() function

# Then we generate a random sample ags of size na of
# various random combinations picked from poss
# Then we estimate the score of each of these string
# and choose the best nb of these and merge them
# together, allowing random mutations with chances given
# by nmt and cmt. Also, we only include unique entries in ags
# The remaining ne places are filled with
# best ne scorers from the sample. Then we again have a
# sample of size na, then we repeat the process until
# the optimal score is achieved.

# Found correct answer:
# after 17 generations (setting: nmt=10, cmt=0.5, na=100000, no poss)
# after 6 generations (setting: nmt=5, cmt=0.2, na=50000)
# after 6 generations (setting: nmt=10, cmt=0.2, na=20000)
# after 4 generations (setting: nmt=8, cmt=0.25, na=200000)
# still, can easily get stuck... :(

import numpy as np
import random
import sys
import time

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

def dgposs(dgs, crc, nr, nc):
    ''' Finds possible entries in each column of answer
        For example, because answer is unique, every digit
        in the answer must occur at least once in some row
        (with >0 crc) for every column, thus we can
        eliminate all entries that never occur.
        However, there is a huge flaw in this logic, if
        only one digit is missing then it can still
        occur, but if 2 digits are missing and answer uses
        missing digits then answer couldn't be unique.
        On the other hand, if crc==0, that entry cannot
        occur in that column, so we also eliminate it.
    '''
    poss = [[] for j in range(nc)]
    # Only entering possible entries in poss
    i = nr - 1
    while crc[i] > 0 and i > -1:
        for j in range(nc):
            poss[j].append(dgs[i,j])
        i -= 1
    # Removing repetitive elements and adjusting for "flaw" discussed above
    for j in range(nc):
        poss[j] = list(set(poss[j]))
        if len(poss[j]) == 9:
            poss[j] = [i for i in range(10)]
    # Removing entries that occur in crc==0 row
    i = 0
    while crc[i] == 0:
        for j in range(nc):
            if dgs[i,j] in poss[j]:
                poss[j].remove(dgs[i,j])
        i += 1
    for j in range(nc):
        poss[j] = np.array(poss[j])
    return np.array(poss), i

def chkcor(s, a, nc):
    ''' (1d numpy array, 1d numpy array, int) -> int
        Given two 1d arrays of size nc, finds how many
        entries are matching
    '''
    return nc - np.count_nonzero(s - a)

def score(dgs, crc, a, nr, nc):
    ''' Returns a score of how well all conditions are matched
        for guess number string a. Lower the score the better
    '''
    scr = 0
    for i in range(nr):
        scr += (chkcor(dgs[i], a, nc) - crc[i])**2
    return scr

def merge(a0, a1, poss, ncj, nc, nch, nmt, cmt):
    ''' Merges two guess number strings randomly
        using half elements from both. Also allows mutation
        a0, a1 = input number strings to be merged
        poss = list of possible digits for each column (see dgposs)
        ncj = tuple (0, 1, 2, ..., nc-1)
        nc = number of columns (same as length of ncj)
        nch = half of nc
        nmt = number of maximum mutations to allow
        cmt = chances of a mutation to occur
    '''
    i0 = random.sample(ncj, nch)
    i1 = [i for i in ncj if i not in i0]
    a = np.empty(nc, dtype = 'int32')
    for i in i0:
        a[i] = a0[i]
    for i in i1:
        a[i] = a1[i]
    for k in range(nmt):
        if random.random() < cmt:
            j = random.randrange(0, nc)
            a[j] = random.choice(poss[j])
    return a

def chbest(ags, scs, na, nb, nc):
    ''' Finds nb best entries from ags that have
        lowest scores and are unique
    '''
    iscs = np.argsort(scs)
    bgs = []
    k = 0
    for i in range(na):
        #if not ags[iscs[i]] in bgs:
        if not any([(b == ags[iscs[i]]).all() for b in bgs]):
            bgs.append(ags[iscs[i]])
            k += 1
        if k == nb:
            break
    if k < nb:
        for i in range(k, nb):
            bgs.append(np.array([random.choice(poss[j]) for j in range(nc)]))
    return np.array(bgs), scs[iscs[0]]

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

# Number of mutations to allow and chance of each mutation (used in merge() function)
nmt = 8
cmt = 0.25

# Reading data, setting digits and correct answers in dgs and crc. nr = number of rows or constraints, nc = number of columns or entries in each row. Also finding possible digits in each column and eliminating rows with crc==0
nr, nc, dgs, crc = tx2ar(txin1)
nch = nc // 2
ncj = tuple([j for j in range(nc)])
poss, ic0 = dgposs(dgs, crc, nr, nc)
nr -= ic0
dgs = dgs[ic0:]
crc = crc[ic0:]

na = 200000
nb = int(np.floor(0.5 * (1.0 + np.sqrt(1.0 + 8.0 * na))))
ne = na - nb * (nb-1) // 2
# Generating random sample ags of size na from poss for 0th generation and scores will be stored in scs
ags = np.array([np.array([random.choice(poss[j]) for j in range(nc)], dtype = 'int32') for j in range(na)])
scs = np.empty(na, dtype = 'int32')
ng = 0
tym0 = time.time()

while True:
    # Finding scores of all entries in ags and checking for 0 score
    for j in range(na):
        scs[j] = score(dgs, crc, ags[j], nr, nc)
        if scs[j] == 0:
            s = ''
            for m in ags[j]:
                s += str(m)
            print(s)
            print('Time taken:', time.time() - tym0, 's')
            sys.exit()
    # Finding best nb scorers of ags and storing in bgs, best score in scs0
    bgs, scs0 = chbest(ags, scs, na, nb, nc)
    print('generation:', ng, 'best:', bgs[0], scs0)
    j = 0
    # Making new generation by merging entries in bgs, remaining ne are filled with best from ags (to maintain size of sample in each generation)
    ags1 = []
    for j0 in range(nb-1):
        for j1 in range(j0+1, nb):
            ags1.append(merge(bgs[j0], bgs[j1], poss, ncj, nc, nch, nmt, cmt))
            j += 1
    for j in range(ne):
        ags1.append(bgs[j])
    ags = np.array(ags1)
    ng += 1
