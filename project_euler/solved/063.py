# MATH

# For n, 10**n will always have n+1 digits,
# so checking base above 9 will be useless
# One also finds that 22 ** 9 has 21 digits
# and that for all n > 22 number of digits
# will be less than n
# so it is also useless for exponent to be above 21

s = []
for i in range(1, 22):
    ml = 1
    for m in range(1, 10):
        mi = m ** i
        ml = len(str(mi))
        if ml == i:
            s.append(mi)
print(len(s))
