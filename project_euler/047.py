# (Quite a) BRUTE FORCE

# Generate all such 4-prime-factor numbers
# Check for 4 consecutives in the list

# nn specifies till what prime numbers are to be generated
# first set nn to be ~200, one gets the answer 253894, which is
# wrong. so, it's quite natural that it is sufficient to check for
# nn upto 800 only, which gives the correct answer

# a better method could be Sieve. in the logical list, simply
# eliminate elements with prime factors < 4, then search for
# 4 consecutives

import math
def primes_soe(n):
    ''' (int) -> list of int
        Function to generate list of prime numbers
        using the sieve of Eratosthenes
        n = upto which primes are needed (inclusive)
    '''
    if n < 2:
        return []
    n2 = (n - 1) // 2
    prms = [2] * (n2 + 1)
    ip = [True for i in range(n2)]
    k = 3
    nsq = round(math.sqrt(n))
    while k <= nsq:
        for i in range(k * k // 2 - 1, n2, k):
            ip[i] = False
        while k <= nsq:
            k += 2
            if ip[k // 2 - 1]:
                break
    m = 1
    for i in range(n2):
        if ip[i]:
            prms[m] = 2 * i + 3
            m += 1
    return prms[:m]

nn = 800
pms = primes_soe(nn)
a = [1,2,3,4,5]
p = 2
i = 1
pfs = []
for p in pms:
    j = 1
    pp = p ** j
    pf = []
    while pp <= nn:
        pf.append(pp)
        j += 1
        pp = p ** j
    pfs.append(pf)

nf = len(pms)
ppr = []

for n1 in range(nf):
    pl1 = pfs[n1]
    for p1 in pl1:
        for n2 in range(n1+1, nf):
            pl2 = pfs[n2]
            for p2 in pl2:
                for n3 in range(n2+1, nf):
                    pl3 = pfs[n3]
                    for p3 in pl3:
                        for n4 in range(n3+1, nf):
                            pl4 = pfs[n4]
                            for p4 in pl4:
                                ppr.append(p1*p2*p3*p4)

ppr.sort()
npr = len(ppr)
for i in range(npr-3):
    if ppr[i+1]==ppr[i]+1 and ppr[i+2]==ppr[i]+2 and ppr[i+3]==ppr[i]+3:
        print(ppr[i])
        break
