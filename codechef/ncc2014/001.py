def nm(s):
    s = s.strip()
    n = len(s)
    si = []
    i = 0
    while i < n:
        if s[i] == ' ':
            si.append(i)
        i += 1
    m = [int(s[:si[0]])]
    for j in range(len(si)-1):
        m.append(int(s[si[j]+1:si[j+1]]))
    m.append(int(s[si[-1]+1:]))
    return m

t = int(input())
for k in range(t):
    t0 = nm(input())
    n = t0[0]; k = t0[1]; m = t0[2]

    for i in range(m):
        if n % k == 0:
            n = n // k
        else:
            n = n * k
    print(n)
