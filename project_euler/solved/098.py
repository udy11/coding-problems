# PROGRAMMING

# Steps are:
#   Make a dict of words with length as key (w98)
#   From that dict, make anagram pairs, again as dict (wa)
#   Make a dict of squares with length as key (s98)
#   For each length and for each anagram pair, check
#     each square if same permutation is followed by another
#     similar square
# In program, check for different values of kc
#   in {9, 8, 6, 5, 4, 3, 2} in order

# Program currently can give wrong answers but will also give
# correct answer, that one can manually filter out or
# one will have to make a better pch() function

import math

def is_anagram(s1, s2):
    for s in s1:
        if s1.count(s) != s2.count(s):
            return False
    return True

def ismsng(s, n):
    c = 0
    k = 0
    while k < 10:
        if not str(k) in s:
            c += 1
        if c > n - 1:
            break
        k += 1
    else:
        return True
    return False

def pch(p1, p2, q1, q2):
    n = len(p1)
    t = [False for i in range(n)]
    for k in range(n):
        pi = p2.index(p1[k])
        while t[pi]:
            pi = p2.index(p1[k], pi+1)
        t[pi] = True
        if q1[k] != q2[pi]:
            return False
    return True

def nsm(s):
    return len(s) - len(set([e for e in s]))

def read98(ifln,sep):
    ifl = open(ifln, 'r')
    d0 = {}
    while True:
        lyn = ifl.readline().strip()
        i = 0
        if lyn == "":
            break
        while i < len(lyn):
            if not lyn[i] in sep:
                k = 1
                while i+k < len(lyn) and not lyn[i+k] in sep:
                    k += 1
                wd = lyn[i+1:i+k-1]
                lg = len(wd)
                if lg in d0:
                    d0[lg].append(wd)
                else:
                    d0[lg] = [wd]
                i += k + 1
            else:
                i += 1
    ifl.close()
    return d0

w98 = read98('098_words.txt',',')
wa = {}

for k in range(2, 15):
    n = len(w98[k])
    for i in range(n):
        for j in range(i+1, n):
            if is_anagram(w98[k][i], w98[k][j]):
                if k in wa:
                    wa[k].append((w98[k][i], w98[k][j]))
                else:
                    wa[k] = [(w98[k][i], w98[k][j])]

s98 = {}
for i in range(4, 99999):
    s = str(i*i)
    u = len(s)
    if u in s98:
        s98[u].append(s)
    else:
        s98[u] = [s]

kc = 5

for wp in wa[kc]:
    spa = []
    for s in s98[kc]:
        if ismsng(s, 11-kc+nsm(wp[0])):
            spa.append(s)
    nspa = len(spa)
    for i in range(nspa):
        for j in range(i+1, nspa):
            if pch(wp[0], wp[1], spa[i], spa[j]):
                print(spa[i], spa[j], wp[0], wp[1])
