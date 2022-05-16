# ALGORITHM
# Store all ways to partition any k-digit number in a deque p
# Skip the combinations that will not satisfy the condition
# Such invalid partitions are:
# For even k, all partitions that don't have k//2 entry
# For odd k, all partitions that don't have 1+k//2 entry or their max entry is k//2
# Maybe in odd k, there might be further restriction that if max entry is k//2, it should occur twice, but i don't have any proof
# Then simply loop over all squares upto 10**12 and check over valid partitions if sum matches

# Another optimization was suggested by ecnerwala in forums:
# Only those numbers need to be checked whose %9 is 0 or 1
# Though I couldn't understand the reason but it makes the code much faster

# Python version takes a lot of time, refer to c++ version that runs much faster

import sys
import time
import math

# p will contain all ordered partitions of integers upto 12
n = 13
p = {1 : [(1,)]}
for k in range(2, n):
    p[k] = [(k,)]
    for m in range(1, k):
        for p0 in p[m]:
            for p1 in p[k-m]:
                p[k].append(p0 + p1)
    p[k] = list(set(p[k]))

# excluding entries in p[k] that cannot give sum as sqrt(num)
# for odd-digit numbers of len n, there must be at least either 1 entry for n//2+1 digits or 2 entries for n//2 digits
# for even-digit numbers of len n, there must be at least 1 entry for n//2 digits
for k in range(2, n):
    if k & 1 == 0:
        m = k // 2
        pk = []
        for q in p[k]:
            if m in q:
                pk.append(q)
        p[k] = pk
    else:
        m = 1 + k // 2
        pk = []
        for q in p[k]:
            if m in q:
                pk.append(q)
            elif m-1 == max(q): # one can also check for q.count(m-1) == 2, but I could not find any logic behind this
                pk.append(q)
        p[k] = pk

tym0 = time.time()

kf = 1000000
t = kf * kf
for k in range(9, kf, 9):
    k2 = k * k
    nk = math.floor(math.log10(k2)) + 1
    for q in p[nk]:
        s = 0
        kq = k2
        for j in q:    # should be reversed(q), but this also works because all mirrored version of each entry also exists in p[k]
            # check this for optimized implementation of the following: https://stackoverflow.com/questions/14939953/sum-the-digits-of-a-number-python
            kq, r = divmod(kq, 10**j)
            s += r
            #s, kq = s + kq % 10**j, kq // 10**j
        if s == k:
            #print(k, k2, q)
            t += k2
            break
for k in range(10, kf, 9):
    k2 = k * k
    nk = math.floor(math.log10(k2)) + 1
    for q in p[nk]:
        s = 0
        kq = k2
        for j in q:    # should be reversed(q), but this also works because all mirrored version of each entry also exists in p[k]
            kq, r = divmod(kq, 10**j)
            s += r
            #s, kq = s + kq % 10**j, kq // 10**j
        if s == k:
            #print(k, k2, q)
            t += k2
            break
print(t)
print('Time taken (s):', time.time() - tym0)
