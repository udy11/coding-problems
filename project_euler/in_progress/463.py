ff = [0, 1, 1, 3, 1]

k = 5
while k < 200:
    if k % 2 == 0:
        ff.append(ff[k // 2])
    elif k % 4 == 1:
        m = (k - 1) // 4
        ff.append(2 * ff[2 * m + 1] - ff[m])
    elif k % 4 == 3:
        m = (k - 3) // 4
        ff.append(3 * ff[2 * m + 1] - 2 * ff[m])
    k += 1

for i in range(200):
	print(i, ff[i])
