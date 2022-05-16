def nm(s):
    s = s.strip()
    n = len(s)
    si = []
    i = 0
    while i < n:
        if s[i] == ' ':
            si.append(i)
        i += 1
    m = [float(s[:si[0]])]
    for j in range(len(si)-1):
        m.append(float(s[si[j]+1:si[j+1]]))
    m.append(float(s[si[-1]+1:]))
    return m

t = nm(input())
