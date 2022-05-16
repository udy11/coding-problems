# MATHEMATICS

# My 75th problem

# Read 128_math.docx for details on algorithm

# Code can be optimized futher by storing the
# sequence generated by function hxn in an array.
# And further optimization is possible by
# converting two loops into one.

import math
def is_prime(n):
    ''' assumes positive n '''
    if n > 2 and n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    if n < 2:
        return False
    return True

# OEIS A077588
def hxn(n):
    return 3*n*n - 3*n + 2

pd3 = [1]
for i in range(3, 100000):
    hr=hxn(i)-1
    if is_prime(hxn(i+1)-2-hr) and is_prime(hr-hxn(i-1)) and is_prime(hr-hxn(i-2)):
        pd3.append(hr)

for i in range(1, 100000):
    hl=hxn(i)
    if is_prime(hxn(i+1)+1-hl) and is_prime(hxn(i+1)-1-hl) and is_prime(hxn(i+2)-1-hl):
        pd3.append(hl)

pd3.sort()
print(pd3[1999])
