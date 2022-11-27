# From all the mentioned ranges in rules, there are only some chunks
# consisting of areas, lines and points that can be turned on/off.
# Idea is to store these chunks and modify as per rules.

# xs = all key x values between which regions are turned on/off
# ys = all key y values similar to xs
# xys = (x0, y0, x1, y1) defining a region (all inclusive)
# grid = dictionary that contains the chunks and their state

# For a simple example, let's say there are several rules that
# define xs and ys as [2, 5, 6, ...] and [8, 9, 17, ...]
# And the first rule says to turn on region with x=[2,6]
# and y=[8,17]. Then the grid dictionary will be updated to
# contain the following as on:
# POINTS: (2,8), (2,9), (2,17), (5,8), (5,9), (5,17), (6,8), (6,9), (6,17)
# LINES: (2,10-16), (5,10-16), (6,10-16), (3-4,8), (3-4,9), (3-4,17)
# AREAS: (3-4,10-16)

import sys
import re

def bsa_asc(a, n1, n2, b):
    if b > a[n2 - 1]:
        return  # Not Found
    if b < a[n1]:
        return  # Not Found
    nd = n2 - n1
    nm = n1 + nd // 2
    while nd > 1:
        if a[nm] > b:
            n2 = nm
        else:
            n1 = nm
        nd = n2 - n1
        nm = n1 + nd // 2
    if a[n1] == b:
        return n1
    elif a[n2] == b:
        return n2
    else:
        return  # Not Found

def count(grid):
    c = 0
    for xys in grid:
        c += ((xys[2] - xys[0] + 1) * (xys[3] - xys[1] + 1)) * grid[xys]
    return c

def upgrid(x0, y0, x1, y1, action, act):
    i0 = bsa_asc(xs, 0, nxs, x0)
    j0 = bsa_asc(ys, 0, nys, y0)
    i1 = bsa_asc(xs, 0, nxs, x1)
    j1 = bsa_asc(ys, 0, nys, y1)
    i0, i1 = sorted([i0, i1])
    j0, j1 = sorted([j0, j1])
    for i in range(i0, i1):
        chx = xs[i+1] - xs[i] > 1
        act((xs[i], ys[j1], xs[i], ys[j1]), action)    # setting points: top except top-right
        if chx:
            act((xs[i] + 1, ys[j1], xs[i+1] - 1, ys[j1]), action)    # setting horizontal lines: top
        for j in range(j0, j1):
            chy = ys[j+1] - ys[j] > 1
            act((xs[i], ys[j], xs[i], ys[j]), action)    # setting points: all except top and right
            if chx:
                act((xs[i] + 1, ys[j], xs[i+1] - 1, ys[j]), action)    # setting horizontal lines: all except top
                if chy:
                    act((xs[i] + 1, ys[j] + 1, xs[i+1] - 1, ys[j+1] - 1), action)    # setting areas: all
            if chy:
                act((xs[i], ys[j] + 1, xs[i], ys[j+1] - 1), action)    # setting vertical lines: all except right
    for j in range(j0, j1):
        act((xs[i1], ys[j], xs[i1], ys[j]), action)    # setting points: right except top-right
        if ys[j+1] - ys[j] > 1:
            act((xs[i1], ys[j] + 1, xs[i1], ys[j+1] - 1), action)    # setting vertical lines: right
    act((xs[i1], ys[j1], xs[i1], ys[j1]), action)    # setting point: top-right

ifl = open('06_input.txt', 'r')
lyn = ifl.readline()
xs = []
ys = []
rs = []
while lyn != '':
    rs.append([int(i) for i in re.findall(r'[0-9]+', lyn)] + [re.search(r'(on|off|toggle)', lyn).group()])
    xs.append(rs[-1][0])
    xs.append(rs[-1][2])
    ys.append(rs[-1][1])
    ys.append(rs[-1][3])
    lyn = ifl.readline()
ifl.close()
xs = sorted(list(set(xs)))
ys = sorted(list(set(ys)))
nxs = len(xs)
nys = len(ys)

# Part 1
def act1(xys, action):
    if action == 'toggle':
        grid[xys] = not grid.get(xys, False)
    elif action == 'on':
        grid[xys] = True
    elif action == 'off':
        if xys in grid:
            grid[xys] = False
grid = {}
for r in rs:
    upgrid(r[0], r[1], r[2], r[3], r[4], act1)
print(count(grid))

# Part 2
def act2(xys, action):
    if action == 'toggle':
        grid[xys] = grid.get(xys, 0) + 2
    elif action == 'on':
        grid[xys] = grid.get(xys, 0) + 1
    elif action == 'off':
        if xys in grid:
            grid[xys] = max(0, grid[xys] - 1)
grid = {}
for r in rs:
    upgrid(r[0], r[1], r[2], r[3], r[4], act2)
print(count(grid))

iplot = False
if iplot:
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.patches import Rectangle
    clrmap = plt.get_cmap('brg')
    bss = sorted(set(list(grid.values())))    # values needed for colormap
    colors = [clrmap(k) for k in np.linspace(1, 0, len(bss))]
    fig, ax = plt.subplots()
    for xys in grid:
        if xys[2] - xys[0] > 1 and xys[3] - xys[1] > 1:    # only plots areas, to plot everything ignore this check
            rect = Rectangle((xys[0], xys[1]), xys[2] - xys[0] + 0.01, xys[3] - xys[1] + 0.01, color = colors[grid[xys]])
            ax.add_patch(rect)
    ax.set_aspect('equal')
    plt.xlim([min(xs), max(xs)])
    plt.ylim([min(ys), max(ys)])
    plt.show()
