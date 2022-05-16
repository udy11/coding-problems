# MARKOV CHAIN METHOD (or may be TRANSFER MATRIX METHOD)

# Get the probability matrices for transitions
# Keep multiplying them, and you eventually get the
# probabilities

# However, the below program has a slight problem that
# in more than 3 consecutive doubles, the player still goes to jail
# which is not intended by the problem, however, it
# still gives the correct answer

import numpy as np

def nur(y):
    if y == 7:
        return [15, 12]
    elif y == 22:
        return [25, 28]
    elif y == 36:
        return [5, 12]

def ft0(y):
    z = np.array([0.0 for i in range(40)])
    if y in (2, 17, 33):
        z[y] = 14 / 16
        z[0] = 1 / 16
        z[10] = 1 / 16
        return z
    if y in (7, 22, 36):
        [u, r] = nur(y)
        z[y] = 6 / 16
        z[0] = 1 / 16
        z[10] = 1 / 16
        z[11] = 1 / 16
        z[24] = 1 / 16
        z[39] = 1 / 16
        z[5] = 1 / 16
        z[r] += 2 / 16
        z[u] += 1 / 16
        if y == 36:
            z[0] += 1 / 256
            z[10] += 1 / 256
            z[33] += 14 / 256
        else:
            z[y-3] = 1 / 16
        return z
    if y == 30:
        z[10] = 1
        return z
    z[y] = 1
    return z

# For 6-sided die, initial two rolls
def wdc0(w):
    for j in range(40):
        for i in range(2, 8):
            w[(i+j)%40][j] = (i - 1) / 36
        for i in range(8, 13):
            w[(i+j)%40][j] = (13 - i) / 36

# For 6-sided die, after first two rolls
def wdc1(w):
    for j in range(40):
        w[(2+j)%40][j] += (1 / 36) * (1295 / 1296)
        w[10][j] += (1 / 36) * (1 / 1296)
        w[(3+j)%40][j] += 2 / 36
        w[(4+j)%40][j] += (3 / 36) * (2 / 3) + (3 / 36) * (1 / 3) * (1295 / 1296)
        w[10][j] += (3 / 36) * (1 / 3) * (1 / 1296)
        w[(5+j)%40][j] += 4 / 36
        w[(6+j)%40][j] += (5 / 36) * (4 / 5) + (5 / 36) * (1 / 5) * (1295 / 1296)
        w[10][j] += (5 / 36) * (1 / 5) * (1 / 1296)
        w[(7+j)%40][j] += 6 / 36
        w[(8+j)%40][j] += (5 / 36) * (4 / 5) + (5 / 36) * (1 / 5) * (1295 / 1296)
        w[10][j] += (5 / 36) * (1 / 5) * (1 / 1296)
        w[(9+j)%40][j] += 4 / 36
        w[(10+j)%40][j] += (3 / 36) * (2 / 3) + (3 / 36) * (1 / 3) * (1295 / 1296)
        w[10][j] += (3 / 36) * (1 / 3) * (1 / 1296)
        w[(11+j)%40][j] += 2 / 36
        w[(12+j)%40][j] += (1 / 36) * (1295 / 1296)
        w[10][j] += (1 / 36) * (1 / 1296)

# For 4-sided die, initial two rolls
def vdc0(w):
    for j in range(40):
        for i in range(2, 6):
            w[(i+j)%40][j] = (i - 1) / 16
        for i in range(6, 9):
            w[(i+j)%40][j] = (9 - i) / 16

# For 4-sided die, after first two rolls
def vdc1(w):
    for j in range(40):
        w[(2+j)%40][j] += (1 / 16) * (255 / 256)
        w[10][j] += (1 / 16) * (1 / 256)
        w[(3+j)%40][j] += 2 / 16
        w[(4+j)%40][j] += (3 / 16) * (2 / 3) + (3 / 16) * (1 / 3) * (255 / 256)
        w[10][j] += (3 / 16) * (1 / 3) * (1 / 256)
        w[(5+j)%40][j] += 4 / 16
        w[(6+j)%40][j] += (3 / 16) * (2 / 3) + (3 / 16) * (1 / 3) * (255 / 256)
        w[10][j] += (3 / 16) * (1 / 3) * (1 / 256)
        w[(7+j)%40][j] += 2 / 16
        w[(8+j)%40][j] += (1 / 16) * (255 / 256)
        w[10][j] += (1 / 16) * (1 / 256)

a0 = np.array([[0.0 for i in range(40)] for j in range(40)])
a1 = np.array([[0.0 for i in range(40)] for j in range(40)])
w0 = np.array([[0.0 for i in range(40)] for j in range(40)])
w1 = np.array([[0.0 for i in range(40)] for j in range(40)])
x = np.array([0.0 for i in range(40)])
x[0] = 1.0

# Use wdc functions for 6-sided die and
# vdc functions for 4-sided die
vdc0(w0)
vdc1(w1)

for i in range(40):
    z = ft0(i)
    for j in range(40):
        a0[j][i] = z[j]

x = np.dot(a0, np.dot(w0, x))
x = np.dot(a0, np.dot(w0, x))

while True:
    x = np.dot(a0, np.dot(w1, x))
    print(x)
    input()
