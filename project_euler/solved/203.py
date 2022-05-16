# ALGORITHM

# Sieve to get prime factors of factorials of numbers
# See which pair of combination would be squarefree
# Add their combination to a list
# Add distinct combinations

def cmb(n, r):
    ''' (int, int) -> int
        To calculate combination defined as:
        C(n,r) = n!/((n-r)! * r!)
    '''
    if(r == 0 or r == n):
        return 1
    if(r > n // 2):
        r = n - r
    n1 = n + 1
    cn = n
    cd = 1
    for i in range(2, r + 1):
        cd *= i
        cn *= n1 - i
    return cn // cd

def icsf(n, k):
    dc = {}
    for p in prms:
        dc[p] = nffd[n][p] - nffd[k][p] - nffd[n-k][p]
        if dc[p] > 1:
            return False
    return True

prms = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

nffd = {}
nffd[1] = {p : 0 for p in prms}
nffd[0] = {p : 0 for p in prms}
for i in range(2, 51):
    nffd[i] = dict(nffd[i-1])
    j = i
    for p in prms:
        pf = 0
        while j % p == 0:
            nffd[i][p] += 1
            j //= p

cs = []
for j in range(1, 51):
    for i in range(j//2+1):
        if icsf(j, i):
            cs.append(cmb(j, i))

print(sum(set(cs)))
