# BRUTE FORCE

import math

def is_prime(n):
    if n < 2:
        return False
    if n > 2 and n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

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

def swaps(a, ac):
    ''' (list, list) -> list
        Performs swap of list a based on list ac.
        The nth entry of ac decides where to swap
        the nth entry of list a. '''
    b = list(a)
    j = 0
    for i in ac:
        if i:
            t = b[j]
            b[j] = b[j + i]
            b[j + i] = t
        j += 1
    return b

def fctrl(n):
    ''' (int) -> int
        Function to calculate Factorial.
        Assumes non-negative input. '''
    if n<2:
        return 1
    fc = 2
    for i in range(3,n+1):
        fc *= i
    return fc

def perms_list(aa):
    ''' (list) -> list of lists
        Function returns list of list containing all permutations
        Repeated entries in list aa are treated as distinct.'''
    n = len(aa) - 1
    a = [i for i in range(n+1)]
    nf = [1]
    for i in range(2, n + 1):
        nf = [fctrl(i)] + nf
    an = list(a)
    ac = [0 for j in range(n)]
    n1f = nf[0] * (n+1)
    prms = [aa]
    for m in range(1, n1f):
        for j in range(n):
            mq = m // nf[j]
            ac[j] = mq
            m -= mq * nf[j]
            an = swaps(aa, ac)
        if (int(an[-1]) % 2 > 0) and (not an in prms):
            prms.append(an)
    return prms

prms = primes_soe(10000)[168:]
for p in prms:
    sl = [s for s in str(p)]
    slp = perms_list(sl)
    pp = []
    for ps in slp:
        n = int(ps[0])*1000 + int(ps[1])*100 + int(ps[2])*10 + int(ps[3])
        if is_prime(n):
            pp.append(n)
    if len(pp) > 2:
        for a in pp:
            pp1 = []
            for b in pp:
                ba=b-a
                if -ba in pp1:
                    print(pp)
                else:
                    pp1.append(ba)
