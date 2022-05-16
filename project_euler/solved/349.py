# PATTERN

# Simulate the system to about 11000 moves and see the results.
# If you simulate any more, it becomes evident that ant starts
# making a pattern in a particular direction. One can save images
# from below program in some range and observe that pattern 
# repeats after every 104 moves. Over these moves, the ant adds
# 12 more black squares in the grid. One can start from a move
# so that after some 104*n moves, 10**18 moves have been executed.
# Let's start from move number 10544, so after 104*9615384615384514
# steps, the ant would have executed 10**18 moves. Number of black
# squares after 10544 move is 784, so one can get the total black
# squares after 10**18 moves.

import matplotlib.pyplot as plt

bx = []
by = []
nb = 0

pd = 0
px = 0
py = 0

def move(pd, px, py):
    if pd == 0:
        return [px, py + 1]
    elif pd == 1:
        return [px - 1, py]
    elif pd == 2:
        return [px, py - 1]
    elif pd == 3:
        return [px + 1, py]
    else:
        return [px, py]

for k in range(1, 11000):
    for i in range(nb):
        if bx[i] == px and by[i] == py:
            bx.pop(i)
            by.pop(i)
            pd = (pd + 1) % 4
            [px, py] = move(pd, px, py)
            nb -= 1
            break
    else:
        bx.append(px)
        by.append(py)
        pd = (pd - 1) % 4
        [px, py] = move(pd, px, py)
        nb += 1
    if k == 10544:
        print(nb)
    if False and k > 10500:
        plt.scatter(bx, by)
        plt.axis([-50, 40, -30, 30])
        plt.savefig(str(k) + '.png')
        plt.clf()
