# ALGORTIHM

# Use the commented part of the code separately to verify the
# analytical formula ncubes() of the number of cubes in a layer

# I originally guessed it with some experimenting, trial and error
# and some drawing of 2D and 3D cases

# Then what follows is a search of cases under some limit (smx)
# Store all counts (in ss) and then easily find required count (cc)

##a = 3
##b = 2
##c = 1
##vs = [set([(0, 0, 0), (1, 0, 0), (2, 0, 0), (0, 1, 0), (1, 1, 0), (2, 1, 0)])]
##
##m = 0
##while True:
##    vn = []
##    v = vs[-1]
##    for p in v:
##        vn.append((p[0] - 1, p[1], p[2]))
##        vn.append((p[0] + 1, p[1], p[2]))
##        vn.append((p[0], p[1] - 1, p[2]))
##        vn.append((p[0], p[1] + 1, p[2]))
##        vn.append((p[0], p[1], p[2] - 1))
##        vn.append((p[0], p[1], p[2] + 1))
##    vn = set(vn)
##    for k in range(len(vs)):
##        vn = vn - vs[k]
##    vs.append(vn)
##    #print(vn)
##    print(len(vn), ncubes(a, b, c, m+1))
##    input('')
##    m += 1

def ncubes(a, b, c, n):
    m = n - 1
    return 2 * (a*b + b*c + c*a) + 4 * m * (a + b + c) + 4 * m * (m-1)

smx = 20000
ss = {}
s = 0

i = 1
while True:
    j = i
    while True:
        k = j
        while True:
            m = 0
            s = 0
            while s <= smx:
                m += 1
                s = ncubes(i, j, k, m)
                if s > smx:
                    break
                if not s in ss:
                    ss[s] = 1
                else:
                    ss[s] += 1
            k += 1
            if ncubes(i, j, k, 1) > smx:
                break
        j += 1
        if ncubes(i, j, j, 1) > smx:
            break
    i += 1
    if ncubes(i, i, i, 1) > smx:
        break

cc = 1000
s1 = max(ss)
for s in ss:
    if ss[s] == cc and s < s1:
        s1 = s
print(s1)
