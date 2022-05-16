import math

dc = {2:[[0, 1], [2, 1], [1, 0], [3, 2]]}

k = 3

while k < 22:
    k2 = 2 ** k
    k0 = k2 // 4
    dc[k] = [[0, 0] for i in range(k2)]
    for i in range(k0):
        i2 = 2 * i
        dc[k][4 * i] = dc[k-1][i2]
        dc[k][4 * i + 1][0] = 2 * dc[k-1][i2+1][0] - dc[k-1][i2][0]
        dc[k][4 * i + 1][1] = 2 * dc[k-1][i2+1][1] - dc[k-1][i2][1]
        dc[k][4 * i + 2] = dc[k-1][i2+1]
        dc[k][4 * i + 3][0] = 3 * dc[k-1][i2+1][0] - 2 * dc[k-1][i2][0]
        dc[k][4 * i + 3][1] = 3 * dc[k-1][i2+1][1] - 2 * dc[k-1][i2][1]
    k += 1

s0 = 0
s1 = 0
for i in range(2097152):
    s0 += dc[21][i][0]
    s1 += dc[21][i][1]

