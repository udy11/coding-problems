n = 100
s = 0

for z in range(n + 1):
    for y in range(z + 1):
        for x in range(y + 1):
            if x ^ y ^ z == 0:
                s += x + y + z

print(s)
