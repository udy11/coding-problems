# DYNAMIC PROGRAMMING

# Let n(m, d) denote number of step numbers of length m
# and ending with digit d. So we get the recurrence relation:
#
#          | n(m-1,d-1) + n(m-1,d+1), 0<d<9
# n(m,d) = | n(m-1,1), d==0
#          | n(m-1,8), d==9
#
# However, we also need to count pandigital numbers
# All we need is to count those numbers that will have
# both 0 and 9 present at least once. This is same as
# (all) - (all without 0) - (all without 9) + (all without 0 and 9)
# where last term is added as per inclusion-exclusion principle, or
# because, we over-subtracted that in the 2 middle terms
# In code below, this is denoted as na - n0 - n9 + n09
# We do this for numbers of all lengths from 1 to 40

# There was another idea of arranging steps +1 and -1
# in empty boxes, whose number of ways would have been 2**m
# but this would have also counted invalid numbers
# when cumulative sum of steps will give digit below 0
# or above 9
# In code, the use of dictionary doesn't seem to be a good idea

def sm(n, m, d0, d1):
    s = 0
    for d in range(d0, d1+1):
        s += n[(m, d)]
    return s

mf = 40

# All step numbers
na = {(1, k) : 1 for k in range(1, 10)}
na[(1, 0)] = 0
for m in range(2, mf+1):
    for d in range(1, 9):
        na[(m, d)] = na[(m-1, d-1)] + na[(m-1, d+1)]
    na[(m, 0)] = na[(m-1, 1)]
    na[(m, 9)] = na[(m-1, 8)]

# All step numbers without 0
n0 = {(1, k) : 1 for k in range(1, 10)}
for m in range(2, mf+1):
    for d in range(2, 9):
        n0[(m, d)] = n0[(m-1, d-1)] + n0[(m-1, d+1)]
    n0[(m, 1)] = n0[(m-1, 2)]
    n0[(m, 9)] = n0[(m-1, 8)]

# All step numbers without 9
n9 = {(1, k) : 1 for k in range(1, 9)}
n9[(1, 0)] = 0
for m in range(2, mf+1):
    for d in range(1, 8):
        n9[(m, d)] = n9[(m-1, d-1)] + n9[(m-1, d+1)]
    n9[(m, 0)] = n9[(m-1, 1)]
    n9[(m, 8)] = n9[(m-1, 7)]

# All step numbers without 0 and 9
n09 = {(1, k) : 1 for k in range(1, 9)}
for m in range(2, mf+1):
    for d in range(2, 8):
        n09[(m, d)] = n09[(m-1, d-1)] + n09[(m-1, d+1)]
    n09[(m, 1)] = n09[(m-1, 2)]
    n09[(m, 8)] = n09[(m-1, 7)]

t = 0
for m in range(1, mf+1):
    t += sm(na, m, 0, 9) - sm(n0, m, 1, 9) - sm(n9, m, 0, 8) + sm(n09, m, 1, 8)
    #print(m, sm(na, m, 0, 9), sm(n0, m, 1, 9), sm(n9, m, 0, 8), sm(n09, m, 1, 8), sm(na, m, 0, 9) - sm(n0, m, 1, 9) - sm(n9, m, 0, 8) + sm(n09, m, 1, 8))
print(t)
