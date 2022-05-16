# IDEA:
# Pretty much brute force
# The difference in transitions between Sam's and Max's Clocks
#   will be as much taken by AND of digits changing while taking
#   digital root. This is represented by dsm(n) function below

# The method can further be optimized by storing transitions
# between different pairs of digits

# Prime Number generation is done by Sieves of Eratosthenes
# For 2e7, it takes ~ 5 seconds, however on Fortran it takes < 1 second

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

def dgrt(n):
    " One Step of Digital Root "
    s = str(n)
    sm = 0
    for st in s:
        sm += int(st)
    return sm

def sam(n):
    " Transitions taken by n for Sam's Clock "
    dr = n
    t = 0
    while True:
        for d in str(dr):
            t += bin(i2b[d]).count('1')
        if dr < 10:
            break
        dr = dgrt(dr)
    return 2 * t

def mx(n):
    " Transitions taken by n for Max's Clock "
    d1 = str(n)
    t = 0
    for d in d1:
        t += bin(i2b[d]).count('1')
    while True:
        d2 = str(dgrt(d1))
        if int(d1) < 10:
            break
        for d in d2:
            t += bin(i2b[d]).count('1')
        for i in range(-len(d2), 0):
            t -= bin(i2b[d1[i]] & i2b[d2[i]]).count('1')
        d1 = d2
    return 2 * t

def dsm(n):
    " Difference in transitions taken by n between Sam's and Max's Clocks "
    d1 = str(n)
    t = 0
    while True:
        d2 = str(dgrt(d1))
        if int(d1) < 10:
            break
        for i in range(-len(d2), 0):
            t += bin(i2b[d1[i]] & i2b[d2[i]]).count('1')
        d1 = d2
    return 2 * t

i2b = {' ' : 0b0000000}
i2b['0'] = 0b1110111
i2b['1'] = 0b0010010
i2b['2'] = 0b1011101
i2b['3'] = 0b1011011
i2b['4'] = 0b0111010
i2b['5'] = 0b1101011
i2b['6'] = 0b1101111
i2b['7'] = 0b1110010
i2b['8'] = 0b1111111
i2b['9'] = 0b1111011

prms = primes_soe(20000000)[664579:]
print('Listed Primes')

tsv = 0
for p in prms:
    tsv += dsm(p)
print(tsv)
