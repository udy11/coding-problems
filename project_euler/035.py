# to check if a positive number is prime
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

# Generating primes till m (inclusive)
def prms(n):
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

# To generate all cyclic permutations of a non-negative integer
def cy_prmts(n):
    s = str(n)
    l = len(s)
    cp = []
    for i in range(l):
        st = ''
        for j in range(-i,l-i):
            st += s[j%l]
        cp.append(int(st))
    return cp

# To check if a digit in n is even or 5
def chk_25(n):
    s = str(n)
    for d in s:
        m = int(d)
        if m==5 or m%2==0:
            return True
    return False

prml = prms(1000000)
c = 2       # Already including 2 and 5
print(2)
print(5)
for p in prml:
    if not chk_25(p):
        cp = cy_prmts(p)
        icp = True
        for n in cp:
            if not is_prime(n):
                icp = False
                break
        if icp:
            c += 1
            print(p)
print('Total: '+str(c))
