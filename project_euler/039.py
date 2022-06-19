# Ideas:
# Only even perimeters above 501 would be effective
# because either two of (a,b,c) are odd or all are even
# making perimeter to be even
# also, searching below 502 is useless, as higher answer would
# be given by the multiples of lower ones

# A much faster method would be generate all Pythagorean triplets
# and count for perimeters

# The answer 840 is also the highest composite number below 1000
# that I currently don't know if it's a coincidence

def isrt(t):
    if t[2]**2 == t[1]**2 + t[0]**2:
        return True
    return False

pcm = 0
for p in range(4,200):
    pc = 0
    for a in range(1, p-1):
        for b in range(a, p-1):
            c = p - a - b
            if(c >= b and isrt([a, b, c])):
                pc += 1
    if(pc > pcm):
        pcm = pc
        pm = p

print(pm, pcm)
