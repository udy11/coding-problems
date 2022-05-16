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

for tt in range(t):
    n = int(input())
    a = nm(input())
    a.sort()
    b = ''
    for k in range(n // 2):
        b += str(a[k]) + ' '
        b += str(a[n-k-1]) + ' '
    if n % 2 == 1:
        b += str(a[n//2])
    print(b.strip())
