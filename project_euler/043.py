# Idea is to generate all divisible numbers
# for each prime number
# Then starting from list for 17
# start checking which ones from 13 can
# give required numbers
# Keep on iterating till 2

def issm(s):
    n = len(s)
    for i in range(n):
        for j in range(i+1,n):
            if s[i] == s[j]:
                return False
    return True

def mpd(s):
    for i in range(10):
        if(not str(i) in s):
            return str(i) + s

pl = [17, 13, 11, 7, 5, 3, 2]
sp = [[] for i in range(7)]
i = 0
for p in pl:
    for j in range(p,1000,p):
        s = str(j).zfill(3)
        if issm(s):
            sp[i].append(s)
    i += 1

sf = list(sp[0])
pl.remove(17)

i=1
for p in pl:
    st = []
    for s0 in sf:
        for s1 in sp[i]:
            if s1[1:] == s0[:2]:
                ss = s1[0] + s0
                if issm(ss):
                    st.append(s1[0] + s0)
    i += 1
    sf = st

sm = 0
for i in range(len(sf)):
    sf[i] = mpd(sf[i])
    sm += int(sf[i])

print(sm)
