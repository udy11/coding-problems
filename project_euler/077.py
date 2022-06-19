# DYNAMIC PROGRAMMING

# Let P be a table as shown below, whose (n, i) entry
# shows number of ways to write n using numbers upto i
# with i used at least once.
# With this, it is easy to see that
# P(n, i) = sum(P(n-i, j)) j=1,i

#     2 3 5 7
# - - - - - -
# 2 | 1
# 3 | 0 1
# 4 | 1 0
# 5 | 0 1 1
# 6 | 1 1 0
# 7 | 0 1 1 1
# Take blank entries as 0
# Also, take P(0) = 1 and P(1) = 0

# OEIS A000607

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

prms = primes_soe(10000)
np = len(prms)

n = 80
pf = []
pq = []
i = 0
k = 1
for j in range(n+1):
    if j >= prms[i]:
        i += 1
    pf.append([0 for i in range(i)])
    pq.append(i)

pf[0] = [1]
pf[2][0] = 1
ps = [0 for j in range(n+1)]
ps[0] = 1
ps[2] = 1
for j in range(3, n+1):
    for i in range(pq[j]):
        k = j - prms[i]
        if k <= prms[i]:
            pf[j][i] = ps[k]
        else:
            pf[j][i] = sum(pf[k][:i+1])
    ps[j] = sum(pf[j])
    if ps[j] > 5000:
        if j in prms:
            if ps[j] > 5001:
                print(j)
                break
        else:
            print(j)
            break
