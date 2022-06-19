# Idea is to generate a list of 2 * squares
# Keep on subtracting this from all
# odd-composites (i.e. non-prime odds)
# and check if a prime appears

import math

def is_prm(n):
    ''' (int) -> logical
        Checks if a number (>1) is prime
    '''
    for i in range(2,round(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

n0 = 10001
ts = [0 for i in range(n0)]
for i in range(1, n0):
    ts[i - 1] = 2 * i * i

i = 15
while True:
    if not is_prm(i):
        j = 0
        df = i - ts[j]
        while df > 0:
            p = False
            if is_prm(df):
                break
            p = True
            j += 1
            df = i - ts[j]
        if p:
            print(i)
            break
    i += 2
