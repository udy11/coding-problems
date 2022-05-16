# ALGORITHM

# Keep saving what other products you get
# while checking product for n**k. using that
# keep expanding the possible products you
# can get with just one more multiplication
# then save those also along with other products.
# then when you advance to next k, first only
# save its minimum products paths and only then
# expand

def dcexpn(m):
    global kmx
    for pr in dcm[m]:
        n = len(pr)
        for i in range(n):
            for j in range(i, n):
                sij = pr[i] + pr[j]
                if sij > m and sij <= kmx:
                    if not sij in dcm:
                        dcm[sij] = [pr + [sij]]
                    else:
                        dcm[sij].append(pr + [sij])

def dcmnmz(m):
    z = len(dcm[m][0])
    y = []
    for pr in dcm[m]:
        zpr = len(pr)
        if zpr < z:
            z = zpr
            y = [pr]
        elif zpr == z:
            y.append(pr)
    dcm[m] = y
    return z

dcm = {2 : [[1, 2]]}

k = 2
kmx = 200
zf = 0

while k <= kmx:
    zf += dcmnmz(k) - 1
    dcexpn(k)
    k += 1

print(zf)
