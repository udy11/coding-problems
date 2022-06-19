# Read wiki article on Pell Number
# One gets the recurrence relation to generate these fractions

p0n = 2; p1n = 2
p0d = 0; p1d = 1

c = 0
for i in range(2, 1001):
    pd = 2 * p1d + p0d
    pn = 2 * p1n + p0n
    if len(str(pn // 2)) > len(str(pd)):
        c += 1
    p0d = p1d
    p0n = p1n
    p1d = pd
    p1n = pn
print(c)
