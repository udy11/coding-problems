'''
We are given x[0] = 0 and y[0] = 0

To find y[t], note that:
y[t+1] = y[t] + vy[t]
vy[t+1] = vy[t] - 1
From this, vy[t] = vy[0] - t
Therefore, y[t+1] = y[t] + vy[0] - t
which implies, y[t+1] = (t+1)*vy[0] - t*(t+1)/2
so, y[t] = t*vy[0] - t*(t-1)/2
Its maximum is y_max = vy[0]*(vy[0]+1)/2

Note that y[t] = 0 if t = 0 or t = 2*vy[0]+1
At t = 2*vy[0]+1, vy[t] = -vy[0]-1 and y[t] = 0
In next step, t = 2*vy[0]+2, vy[t] = -vy[0]-2 and y[t] = -vy[0]-1
Therefore, a particle launched with positive vy[0]
will skip the point y = -vy[0] on return
So when we want to search that when a particle will
remain within a range (y0, y1), where y1 is negative,
vy[0] should be less -y1

Given a height y, a particle will reach it at:
t = 0.5 + vy[0] + 0.5 * sqrt(1 + 4*vy[0] + 4*vy[0]**2 - 8y)
Thus particle will be at y if t is an integer or will
surpass it at integer ceil(t)
Thus to see if a particle will be in range (y0, y1)
we need to find corresponding times t0 and t1
Note that y1 > y0 (if both negative then |y1| < |y0|), so t1 < t0
Then, if there is an integer in the the range [t1, t0]
(both boundaries inclusive), then particle was present in the
range (y0, y1). Equivalently, if ceil(t1) <= floor(t0)
To calculate ceil and floor without any numerical errors,
the quantity inside sqrt, i.e., 1 + 4*vy[0] + 4*vy[0]**2 - 8y,
can be checked to be perfect square. if it is perfect square,
then t could be integer and it is calculated with care

To find x[t], note that:
x[t+1] = x[t] + vx[t]
vx[t+1] = vx[t] - 1 if vx[t] > 0
where we assume vx[0] > 0
From this:
vx[t] = vx[0] - t, if t <  vx[0]
      = 0,         if t >= vx[0]
Thus:
x[t] = t*vx[0] - t*(t-1)/2, if t <  vx[0]
     = vx[0]*(vx[0]+1)/2,   if t >= vx[0]

To reach length x, minimum vx[0] needed is:
0.5 * (-1 + sqrt(1 + 8*x))
And maximum vx[0] possible will be x itself, beyond
which particle will overshoot x in first step itself

Given a length x, a particle will reach it at:
t = 0.5 + vx[0] - 0.5 * sqrt(1 + 4*vx[0] + 4*vx[0]**2 - 8x)
Note the difference in sign before sqrt term in t for x and y
It's because we assume negative values for y and positive
values for x, because that's how problem inputs are
Following same procedure as y, any vx[0] can be found if
it reaches any given range and for how long it stays there
In addition, there will be a preliminary range of vx[0], where
particle will forever stay in range xr, this range is dealt
separately in code
'''

import sys
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def is_sqrn(n):
    ''' (int) -> logical
        To check if a non-negative integer n is a square number
        Sq(n) = n * n
    '''
    if n % 4 == 0 or n % 8 == 1:
        r = round(math.sqrt(n))
        if r * r == n:
            return True
    return False

def sign(a):
    if a != 0:
        return a // abs(a)
    else:
        return 0

def plotter(trajx, trajy, xr, yr):
    ''' Plots trajectory of projectile
        and range box '''
    fig, ax = plt.subplots()
    rect = patches.Rectangle((xr[0], yr[0]), xr[1] - xr[0], yr[1] - yr[0], linewidth=1, edgecolor='red', facecolor='none')
    ax.add_patch(rect)
    ax.scatter(trajx, trajy, marker = '*')
    plt.show()

def sim(vx, vy, xr, yr):
    ''' Simulates projectile motion with initial
        vx and vy, until either target xr, yr is reached
        or it is out of target's range '''
    x = 0
    y = 0
    ymax = 0
    trajx = [x]
    trajy = [y]
    hit = False
    while True:
        x += vx
        y += vy
        vx -= sign(vx)
        vy -= 1
        if y > ymax:
            ymax = y
        trajx.append(x)
        trajy.append(y)
        if (xr[0] <= x <= xr[1]) and (yr[0] <= y <= yr[1]):
            hit = True
            break
        if (vx > 0 and x > xr[1]) or (vy < 0 and y < yr[1]):
            break
    plotter(trajx, trajy, xr, yr)
    return ymax

def ytym(vy0, y):
    ''' (int, int) -> float
        finds time taken by projectile
        starting from y[0]=0 to reach y
        when thrown with vy[0]=vy0.
        to avoid numerical issues when
        ceil and floor will be taken later,
        the sqrt is calculated by finding if
        its argument is a perfect square, in which
        case its sqrt is found in integer and
        then result is calculated '''
    dsc = 1 + 4 * vy0 * (1 + vy0) - 8 * y
    if is_sqrn(dsc):
        sqdsc = round(math.sqrt(dsc))
        return 0.5 + vy0 + 0.5 * sqdsc
    else:
        sqdsc = math.sqrt(dsc)
        return 0.5 + vy0 + 0.5 * sqdsc

def xtym(vx0, x):
    ''' (int, int) -> float
        finds time taken by projectile
        starting from x[0]=0 to reach x
        when thrown with vx[0]=vx0.
        to avoid numerical issues when
        ceil and floor will be taken later,
        the sqrt is calculated by finding if
        its argument is a perfect square, in which
        case its sqrt is found in integer and
        then result is calculated '''
    dsc = 1 + 4 * vx0 * (1 + vx0) - 8 * x
    if is_sqrn(dsc):
        sqdsc = round(math.sqrt(dsc))
        return 0.5 + vx0 - 0.5 * sqdsc
    else:
        sqdsc = math.sqrt(dsc)
        return 0.5 + vx0 - 0.5 * sqdsc

def vxmin(x):
    ''' finds minimum vx needed to reach x '''
    dsc = 1 + 8 * x
    if is_sqrn(dsc):
        sqdsc = round(math.sqrt(dsc))
        return 0.5 * (-1 + sqdsc)
    else:
        sqdsc = math.sqrt(dsc)
        return 0.5 * (-1 + sqdsc)

def p1(yr):
    dts = []
    for vy0 in range(0, -yr[0]):
        t0 = ytym(vy0, yr[0])
        t1 = ytym(vy0, yr[1])
        dts.append(math.ceil(t1) <= math.floor(t0))    # stores True if particle is inside range
    for i in range(len(dts)-1, -1, -1):
        if dts[i]:
            return i * (i + 1) // 2    # formula for y_max

def p2(xr, yr):
    yts = {}    # this will times t and vy that will make it within range yr for that t
    for vy0 in range(yr[0], -yr[0]):
        t0 = ytym(vy0, yr[0])
        t1 = ytym(vy0, yr[1])
        if math.ceil(t1) <= math.floor(t0):    # checking if range [t0, t1] contains integer
            t = math.ceil(t1)
            while t <= math.floor(t0):
                if not t in yts:
                    yts[t] = [vy0]
                else:
                    yts[t].append(vy0)
                t += 1
    ytmax = max(yts)    # in xts, no entry greater than ytmax will be made
    vx0min = math.ceil(vxmin(xr[0]))
    vx1min = math.ceil(vxmin(xr[1]))
    xts = {}    # this will times t and vx that will make it within range xr for that t
    for vx0 in range(vx0min, vx1min):    # in this range, particle reaches region xr and stays there forever
        t0 = xtym(vx0, xr[0])
        for t in range(math.ceil(t0), ytmax + 1):
            if not t in xts:
                xts[t] = [vx0]
            else:
                xts[t].append(vx0)
    for vx0 in range(vx1min, xr[1]+1):    # in this range, particle reaches region xr and leaves it later
        t0 = xtym(vx0, xr[0])
        t1 = xtym(vx0, xr[1])
        if math.ceil(t0) <= math.floor(t1):    # checking if range [t0, t1] contains integer
            t = math.ceil(t0)
            while t <= math.floor(t1) and t <= ytmax:
                if not t in xts:
                    xts[t] = [vx0]
                else:
                    xts[t].append(vx0)
                t += 1
    pairs = []
    for t in yts:
        if t in xts:
            for x in xts[t]:
                for y in yts[t]:
                    pairs.append((x, y))
    return len(set(pairs))

xr0 = (20, 30)
yr0 = (-10, -5)
xr1 = (235, 259)
yr1 = (-118, -62)

#print(sim(6, 3, xr0, yr0))

print('Result for Test Puzzle 1:', p1(yr0))
print('Result for Puzzle 1:', p1(yr1))
print('Result for Test Puzzle 2:', p2(xr0, yr0))
print('Result for Puzzle 2:', p2(xr1, yr1))
