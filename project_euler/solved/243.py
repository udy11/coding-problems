# REASONABLE TRIAL-AND-ERROR

# The whole game is of Euler's Totient Function
# which will give the numerator of Resilence
# The denominator of Resilence is n-1
# So you need to cross 0.1635881955585578
# with least possible n
# First note that Totient function is given as
# n * (Prod(1-1/p) for all prime factors of n)
# So to keep n at minimum, one can note that, it is
# most effective to have as many as small prime numbers
# as possible, thus it's most effective to include all small prime
# numbers upto a certain limit
# When this limit is 23, one notices that we're pretty close to the target
# but not have crossed it
# And when we also include 29, we have far crossed the target
# The next thing we notice is that to reduce the Resilence further,
# it is possible with multiples of n
# Thus choosing multiples of 223092870
# and looking when it has crossed the target will give the answer

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

pms = primes_soe(10000)

def ngcd2(n):
    ''' Totient Function '''
    i = 0
    pf = []
    while i < 1000:
        if n % pms[i] == 0:
            pf.append(pms[i])
        i += 1
    tf = n
    for p in pf:
        tf *= (1 - 1/p)
    return tf

# TARGET: 0.1635881955585578
# 223092870 = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 23
# Multiples: 223092870, 446185740, 669278610, 892371480, 1115464350

while True:
    n = int(input("Enter number: "))
    t = ngcd2(n)
    print(t, t / (n-1))
