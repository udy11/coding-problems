def upxy(d, x, y):
    if d == 'v':
        y -= 1
    elif d == '^':
        y += 1
    elif d == '<':
        x -= 1
    elif d == '>':
        x += 1
    return x, y

ifl = open('03_input.txt')
ds = ifl.read().strip()
ifl.close()

# Part 1
x = 0
y = 0
h = {(x, y) : 1}
for d in ds:
    x, y = upxy(d, x, y)
    h[(x, y)] = h.get((x, y), 0) + 1
print(len(h))

# Part 2
x = [0, 0]
y = [0, 0]
h = {(0, 0) : 2}
i = 0
for d in ds:
    x[i], y[i] = upxy(d, x[i], y[i]) 
    h[(x[i], y[i])] = h.get((x[i], y[i]), 0) + 1
    i = (i + 1) & 1
print(len(h))

