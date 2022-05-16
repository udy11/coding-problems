# (Pretty much) BRUTE FORCE

# Make a dict of cubes with their length as keys
# In each element of dict, check each element if there
# are more with same digits

# The process can be made faster by removing the numbers
# with same digits

cbd = {}
j = 1
cbd[j] = []
for i in range(10000):
    i3 = i * i * i
    if len(str(i3)) > j:
        j += 1
        cbd[j] = [i3]
    else:
        cbd[j].append(i3)

def smd(s1, s2):
    for d in '0123456789':
        if s1.count(d) != s2.count(d):
            return False
    return True

for j in range(8, 13):
    nj = len(cbd[j])
    for i1 in range(nj):
        cc = 1
        n1 = cbd[j][i1]
        s1 = str(n1)
        for i2 in range(i1+1, nj):
            n2 = cbd[j][i2]
            s1t = list(s1)
            s2 = str(n2)
            if smd(s1, s2):
                cc += 1
        if cc > 3:
            print(n1, cc)
