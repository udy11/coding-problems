def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

st = 'UDD'

if st[0] == 'U':
    a = [3, 1, 1]
elif st[0] == 'd':
    a = [3, 2, 1]
elif st[0] == 'D':
    a = [3, 0, 1]

for i in range(1, len(st)):
    if st[i-1] == 'U':
        if st[i] == 'U':
            a[1] = 4 * a[1] + 2 + 4 * a[0] / 3
            a[0] = 4 * a[0]
        elif st[i] == 'D':
            a[1] = 4 * a[1] + 2
            a[0] = 4 * a[0]
        elif st[i] == 'd':
            a[1] = 4 * a[1] + 2 + 8 * a[0] / 3
            a[0] = 4 * a[0]
    elif st[i-1] == 'D':
        if st[i] == 'U':
            a[1] = a[1] + a[0] / 3
        elif st[i] == 'd':
            a[1] = a[1] + 2 * a[0] / 3
            a[0] = 4 * a[0]
    elif st[i-1] == 'd':
        if st[i] == 'U':
            a[1] = 2 * a[1] - 1 + 2 * a[0] / 3
            a[0] = 2 * a[0]
        elif st[i] == 'D':
            a[1] = 2 * a[1] - 1
            a[0] = 2 * a[0]
        elif st[i] == 'd':
            a[1] = 2 * a[1] - 1 + 4 * a[0] / 3
            a[0] = 2 * a[0]
    print(a)

b = [0, 0, 1]
b[0] = round(a[0])
b[1] = round(a[1])
##for i in range(len(st) - 1, -1, -1):
##    if st[i] == 'U':
##        b[0] = 3 * b[0] / 4
##        b[1] = (3 * b[1] - 2) / 4
##    if st[i] == 'D':
##        b[0] = 3 * b[0]
##        b[1] = 3 * b[1]
##    if st[i] == 'd':
##        b[0] = 3 * b[0] / 2
##        b[1] = (3 * b[1] + 1) / 2

for i in range(len(st) - 1, -1, -1):
    if st[i] == 'U':
        k = 1
        while not (3 * b[0] * k % 4 == 0 and (3 * b[1] - 2) * k % 4 == 0):
            k += 1
        b[0] = 3 * b[0] * k // 4
        b[1] = (3 * b[1] - 2) * k // 4
    if st[i] == 'D':
        b[0] = 3 * b[0]
        b[1] = 3 * b[1]
    if st[i] == 'd':
        k = 1
        while not (3 * b[0] * k % 2 == 0 and (3 * b[1] + 1) * k % 2 == 0):
            k += 1
        b[0] = 3 * b[0] // 2
        b[1] = (3 * b[1] + 1) // 2

print(a, b)
