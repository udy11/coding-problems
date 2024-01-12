import re

# For 1st condition; finds increasing straight of 3 letters
sc0s = '(abc' + ''.join(['|' + chr(i) + chr(i+1) + chr(i+2) for i in range(98, 103)])
sc0s += ''.join(['|' + chr(i) + chr(i+1) + chr(i+2) for i in range(109, 121)]) + ')'
def sc0(s):
    return re.findall(sc0s, s)

# For 2nd condition; finds i, l, o
def sc1(s):
    return re.findall(r'[ilo]', s)

# For 3rd condition; finds double letters
def sc2(s):
    return set([m.group() for m in re.finditer(r'(([a-z])\2)+?', s)])

# Checks 1st and 3rd conditions
def schk(s):
    return (len(sc0(s)) > 0) and (len(sc2(s)) > 1)

# Mapping a,b,c... as 0,1,2... in base nc,
# this function converts string s to an integer
def s2m(s):
    ds = [d1[c] for c in s]
    n = len(ds)
    m = ds[-1]
    for i in range(n-2, -1, -1):
        m += ds[i] * (nc ** (n-i-1))
    return m

# Mapping a,b,c... as 0,1,2... in base nc,
# this function converts integer m to s (of length ns)
def m2s(m):
    m1=m
    ds = []
    for i in range(ns):
        ds = [m % nc] + ds
        m = m // nc
    return ''.join([d0[d] for d in ds])

# Finds next valid password
# If i,l,o are in s, it's automatically
# set to next valid string
# Then it converts string s to integer m
# where characters a,b,c,... are mapped to
# 0,1,2... m is then increased and
# converted back to string s and check
# if it's a valid password
def pwdnxt(s):
    n = len(s)
    for i in range(n):
        if s[i] in ('i', 'l', 'o'):
            s = s[:i] + chr(ord(s[i])+1) + 'a' * (n-i-1)
            break
    m = s2m(s)
    while not schk(s):
        m += 1
        s = m2s(m)
    return s

chs = 'abcdefghjkmnpqrstuvwxyz'    # all valid letters, except i,l,o
nc = len(chs)
d0 = {i : chs[i] for i in range(nc)}    # d0, d1 are integer <-> letter mapping dict
d1 = {d0[d] : d for d in d0}

ns = 8    # string length
s0 = 'abcdefgh'
s1 = 'ghijklmn'
s2 = 'cqjxjnds'
s3 = 'cqjxxzaa'    # next string of solution of part 1

print(s0, pwdnxt(s0))
print(s1, pwdnxt(s1))
print(s2, pwdnxt(s2))
print(s3, pwdnxt(s3))
