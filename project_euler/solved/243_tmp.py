import fractions
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

##for i in range(2, 10000):
##    cc = 0
##    for j in range(1, i):
##        if fractions.gcd(i, j) == 1:
##            cc += 1
##    rs = cc / (i-1)
##    if rs < 0.22:
##        print(i, cc)

pms = primes_soe(20000000)
print('primes generated...')

def ngcd(n):
    i = 0
    pf = []
    while pms[i] <= n // 2:
        if n % pms[i] == 0:
            pf.append(pms[i])
        i += 1
    nt = [True for j in range(n-2)]
    for p in pf:
        pk = p
        while pk < n:
            nt[pk-2] = False
            pk += p
    cc = 1
    for j in range(n-2):
        if nt[j]:
            cc += 1
    return cc

def ngcd2(n):
    i = 0
    pf = []
    while pms[i] <= n // 2:
        if n % pms[i] == 0:
            pf.append(pms[i])
        i += 1
    tf = n
    for p in pf:
        tf *= (1 - 1/p)
    return tf

for i in range(223092870, 923092870, 2):
    tt = ngcd2(i)/(i-1)
    if tt < 0.2:
        print(i, tt)

##def ngcd1(n, pf):
##    nt = [True for j in range(n-2)]
##    for p in pf:
##        pk = p
##        while pk < n:
##            nt[pk-2] = False
##            pk += p
##    cc = 1
##    for j in range(n-2):
##        if nt[j]:
##            cc += 1
##    return cc
##
##def ttnf(n, pf):
##    tf = n
##    for p in pf:
##        tf *= (1 - 1/p)
##    return tf
##
##for i in range(1, 10):
##    n = 1
##    pf = []
##    for j in range(i+1):
##        n *= pms[j]
##        pf.append(pms[j])
##    print(n, ttnf(n, pf), ttnf(n, pf)/(n-1))
##
