# (Pretty much) BRUTE-FORCE

# First divide the list of primes in two categories:
#   those with %3=1 and those with %3=2
#   these are ps1 and ps2 below
#   also include 3 in each list
# Then for ps1 and ps2, create 2 separate dictionaries
#   containing which primes are concatenable
#   then simply keep on checking if dictionary values
#   have common values upto 5

# To prove minimum, one can then check for all primes upto 26000
#   since this is the sum that minimum sum one obtains

# Also, many improvements are possible, since many things are
#   getting checked multiple times

# Further optimization can be done by generating prime numbers
#   instead of checking them each time

# And why ps2 doesn't generate any result.. there may be some reason for that

import math

def is_prime(n):
    for i in range(3, round(math.sqrt(n)), 2):
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

def dgsm(n):
    ds = 0
    for s in str(n):
        ds += int(s)
    return ds

def pp(pl):
    n = len(pl)
    for i in range(n):
        ps1 = str(pl[i])
        for j in range(i+1,n):
            ps2 = str(pl[j])
            if not is_prime(int(ps1+ps2)) or not is_prime(int(ps2+ps1)):
                return False
    return True

pms = primes_soe(10000)
pms.remove(2)
pms.remove(3)
pms.remove(5)
np = len(pms)

ps1 = [3]
ps2 = [3]
for p in pms:
    if p % 3 == 1:
        ps1.append(p)
    else:
        ps2.append(p)
n1 = len(ps1)
n2 = len(ps2)

pd1 = {}
for p in ps1:
    pd1[p] = []
for i1 in range(n1):
    for i2 in range(i1+1, n1):
        pl = [ps1[i1], ps1[i2]]
        if pp(pl):
            pd1[ps1[i1]].append(ps1[i2])
            pd1[ps1[i2]].append(ps1[i1])

pd2 = {}
for p in ps2:
    pd2[p] = []
for i1 in range(n2):
    for i2 in range(i1+1, n2):
        pl = [ps2[i1], ps2[i2]]
        if pp(pl):
            pd2[ps2[i1]].append(ps2[i2])
            pd2[ps2[i2]].append(ps2[i1])

print("Dictionaries generated...")

for p1 in pd1:
    for p2 in pd1[p1]:
        for p3 in pd1[p2]:
            if p1 in pd1[p3]:
                for p4 in pd1[p3]:
                    if p2 in pd1[p4] and p1 in pd1[p4]:
                        for p5 in pd1[p4]:
                            if p2 in pd1[p5] and p1 in pd1[p5] and p3 in pd1[p5]:
                                print([p1, p2, p3, p4, p5], sum([p1, p2, p3, p4, p5]))

print('--------------------------')

for p1 in pd2:
    for p2 in pd2[p1]:
        for p3 in pd2[p2]:
            if p1 in pd2[p3]:
                for p4 in pd2[p3]:
                    if p2 in pd2[p4] and p1 in pd2[p4]:
                        for p5 in pd2[p4]:
                            if p2 in pd2[p5] and p1 in pd2[p5] and p3 in pd2[p5]:
                                print([p1, p2, p3, p4, p5], sum([p1, p2, p3, p4, p5]))
