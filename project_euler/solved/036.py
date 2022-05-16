# To check if a string is palindrome
def is_pl(st):
    """ (str) -> bool
    """
    n=len(st)
    for i in range(n // 2):
        if st[i] != st[n-i-1]:
            return False
    return True

# To get m digits of n in b base
def dg(n,m,b):
    d = []
    for i in range(m-1,-1,-1):
        bi = b**i
        p = n // bi
        d.append(p)
        if(bi<=n):
            n -= p * bi
    return d

import math
sm = 0
for i in range(1,1000000,2):   # checking only odd numbers
    if(is_pl(str(i))):
        nib2 = int(math.log(i,2)) + 1
        db2 = dg(i,nib2,2)
        ib2 = ''
        for j in range(nib2):
            ib2 += str(db2[j])
        if(is_pl(ib2)):
            print(i)
            sm += i
print('Sum:',sm)
