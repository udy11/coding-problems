# INCLUSION-EXCLUSION PRINCIPLE

# There are 25 primes <= 100. We need to find
# number of ways to arrange these so that exactly
# 22 are not in their place, which means 3 are exactly
# in place.
# First we fix these 3 numbers. Number of ways is C(25,3) = a
# Then we need to find all ways in which remaining 22 primes
# are not in their place. To find this consider:
# b = all arrangements of remaining numbers = 97!
# c = all arrangements in which at least one of the
# remaining primes is in its place
# So what we need is a * (b - c)
# To find c, we count all ways in which one prime is
# in-place and subtract overcounting with
# inclusion-exclusion principle.
# Number of ways to arrange n numbers
# with k entries fixed in their place is (n-k)!
# and to choose such entries is C(22,k)
# So as per inclusion-exclusion principle:
# c = #(1 prime in-place) - #(2 primes in-place) + #(3 primes in-place) + ...
# c = sum((-1)**(k+1) * C(22, k) * (22 - k)!, (k, 1, 22))

import scipy.special

nn = 100
np = 25
mp = 22

nc = nn - np + mp
c = sum([(-1)**(k+1) * scipy.special.comb(mp, k, exact = True) * scipy.special.factorial(nc - k, exact = True) for k in range(1, mp+1)])
print(scipy.special.comb(np, np - mp, exact = True) * (scipy.special.factorial(nc, exact = True) - c) / scipy.special.factorial(nn, exact = True))
