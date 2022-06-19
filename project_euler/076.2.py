# DYNAMIC PROGRAMMING

# Let P be a table as shown below, whose (n, i) entry
# shows number of ways to write n using numbers upto i
# with i used at least once.
# With this, it is easy to see that
# P(n, i) = sum(P(n-i, j)) j=1,i

#     1 2 3 4 5 6 7 8
# - - - - - - - - - - -
# 1 | 1
# 2 | 1 1
# 3 | 1 1 1
# 4 | 1 2 1 1
# 5 | 1 2 2 1 1
# 6 | 1 3 3 2 1 1
# 7 | 1 3 4 3 2 1 1
# 8 | 1 4 5 5 3 2 1 1
# 9 | . . .
# Take blank entries as 0

# OEIS A000041

n = 100
pf = [[0 for i in range(j+1)] for j in range(n+1)]
ps = [0 for j in range(n+1)]

pf[1][1] = 1
ps[0] = 1
ps[1] = 1
for j in range(2, n+1):
    for i in range(1, j+1):
        x = j - i
        if x <= i:
            pf[j][i] = ps[x]
        else:
            pf[j][i] = sum(pf[x][1:i+1])
    ps[j] = sum(pf[j])

print(ps[100])
