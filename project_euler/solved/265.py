# ALGORITHM

# It is perhaps dynamic programming.
# For N=4 (m in program), All strings will be of form:
# 00001xxxxxxxxxx1
# To get x's, simply keep checking possibilities while
# maintaining what subsequences have been covered, this
# lets you easily decide the values of further x

# May be one can reduce the space requirement
# by fininshing one possible sequence first and then
# going to next, thus not requiring data of previous
# sequence.

# chk() is an optional function that checks a
# sequence of length n and subsequences of length m
# for required consistency

def chk(a1, n, m):
    a0 = [a1[:m]]
    for i in range(1, n - m + 1):
        if not a1[i : i + m] in a0:
            a0.append(a1[i : i + m])
        else:
            return False
    for k in range(1, m):
        if not a1[n - m + k :] + [0 for i in range(k)] in a0:
            a0.append(a1[n - m + k :] + [0 for i in range(k)])
        else:
            return False
    return True

m = 5
n = 2 ** m

a = [2 for i in range(n)]
a[:m] = [0 for i in range(m)]
a[m] = 1
a[-1] = 1

a1 = [a]
ap = [[[0 for i in range(m)], [0 for i in range(m - 1)] + [1], [1] + [0 for i in range(m - 1)]]]

for i in range(m + 1, n - 2):
    a2 = []
    ap2 = []
    n1 = len(a1)
    for j in range(n1):
        if not a1[j][i - m + 1 : i] + [0] in ap[j]:
            a2.append(a1[j][: i] + [0] + a1[j][i + 1:])
            ap2.append(ap[j] + [a1[j][i - m + 1 : i] + [0]])
        if not a1[j][i - m + 1 : i] + [1] in ap[j]:
            a2.append(a1[j][: i] + [1] + a1[j][i + 1:])
            ap2.append(ap[j] + [a1[j][i - m + 1 : i] + [1]])
    a1 = a2
    ap = ap2

i = n - 2
a2 = []
n1 = len(a1)
q = [0, 1] + [0 for i in range(m - 2)]
for j in range(n1):
    app = list(ap[j])
    q[0] = 0
    for k in range(1, m + 1):
        if not a1[j][i - m + k : i] + q[:k] in ap[j]:
            ap[j].append(a1[j][i - m + k : i] + q[:k])
        else:
            break
    else:
        a2.append(a1[j][: i] + [0] + a1[j][i + 1:])
    q[0] = 1
    for k in range(1, m + 1):
        if not a1[j][i - m + k : i] + q[:k] in app:
            app.append(a1[j][i - m + k : i] + q[:k])
        else:
            break
    else:
        a2.append(a1[j][: i] + [1] + a1[j][i + 1:])

s = 0
for a0 in a2:
    s2 = 0
    for i in range(n):
        s2 += a0[i] * 2 ** (n - 1 - i)
    s += s2
print(s)
