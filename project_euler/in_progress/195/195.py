import math

count = 0
for m in range(1, 1000):
    for n in range(m):
        a = m**2 + m * n + n**2
        b = m * (m + 2 * n)
        c = m**2 - n**2
        s = (a + b + c) // 2
        r = math.sqrt((s - a) * (s - b) * (s - c) / s)
        if r <= 100:
            count += 1
            #print(m, n, a, b, c, r)
print(count)
