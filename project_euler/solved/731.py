# Bailey-Borwein-Plouffe Formula

# First we find up to what term sum needs to be made
# After certain k, the terms will be less than the
# digits required, this is easily found and stored as k below
# Then we need to find sum(1 / (10**(3**i) * 3**i)) where
# i goes from 1 to k. To calculate contribution of an
# individual term from n digit onwards, we multiply
# it with 10**n and then we only need to check fractional
# part of each term, each term then is:
# {10**(n - 3**i) / 3**i}
# Note that we only want fractional part of this
# term, denoted with {}. To efficiently calculate this
# we note that if we can write 10**(n - 3**i) = 3**i * q + r
# where r is the fractional part then r = 10**(n - 3**i) % 3**i
# Thus we only need to find {(10**(n - 3**i) % 3**i) / 3**i}
# Inner term can be efficiently calculated using inbuilt
# function pow(), which also calculates power mods

# To know more about this algorithm, read more on
# Bailey-Borwein-Plouffe Formula

import math

n = 10**16

# finds till what term sum needs to be considered
k = 1
while 3**k + math.log10(3**k) <= n:
    k += 1

s = 0
for i in range(1, k):
    s += pow(10, n - 1 - 3**i, 3**i) / (3**i)
#print(s)
print(math.floor((s - math.floor(s)) * 10**10))    # this gives first 10 digits from fractional part of s
