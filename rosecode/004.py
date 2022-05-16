import math
def prm_ert_upto_n_lst(n):
    ''' (int) -> list of int
        Function to generate list of prime numbers
        using Sieves of Eratosthenes
        n = upto which primes are needed
    '''
    np = [2 for i in range(n)]
    ip = [True for i in range(n)]
    ip[0] = False
    ip[1] = True
    for i in range(3, n, 2):
        ip[i] = False
    k = 3
    nsq = math.sqrt(n)
    while k < nsq:
        for j in range(k*k - 1, n, k):
            ip[j] = False
        while k < nsq:
            k += 2
            if ip[k - 1]:
                break
    m = 1
    np[0] = 2
    for i in range(2, n, 2):
        if ip[i]:
            np[m] = i + 1
            m += 1
    return np[:m]

n = 1000000
prms = prm_ert_upto_n_lst(n)
pd2 = []
md = 0
p1 = 5
pm = 5
for i in range(1, len(prms)):
    if prms[i] - prms[i-1] == 2:
        if prms[i] - p1 > md:
            md = prms[i] - p1
        p1 = prms[i]

print(md)
