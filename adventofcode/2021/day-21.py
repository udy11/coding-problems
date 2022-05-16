import sys
import math

def p1(inp):
    position_0 = inp[0]
    position_1 = inp[1]
    score_0 = 0
    score_1 = 0
    dice = 100
    rolls = 0
    while True:
        rolls += 3
        dice = (dice + 2) % 100 + 1
        position_0 = (position_0 + 3 * (dice - 1) - 1) % 10 + 1
        score_0 += position_0
        if score_0 > 999:
            return rolls * score_1
        rolls += 3 
        dice = (dice + 2) % 100 + 1
        position_1 = (position_1 + 3 * (dice - 1) - 1) % 10 + 1
        score_1 += position_1
        if score_1 > 999:
            return rolls * score_0

def uppos(pos0, pos1):
    for i in range(1, 11):
        s = 0
        s += pos0[(i+2) % 10 + 1]
        s += pos0[(i+3) % 10 + 1] * 3
        s += pos0[(i+4) % 10 + 1] * 6
        s += pos0[(i+5) % 10 + 1] * 6
        s += pos0[(i+6) % 10 + 1] * 5
        s += pos0[(i+7) % 10 + 1] * 3
        s += pos0[(i+8) % 10 + 1] * 2
        s += pos0[(i+9) % 10 + 1]
        pos1[i] = s

def upscr(pos0, scr0, scr1):
    for j in range(1, 21):
        for i in range(1, 11):
            scr1[j+i] += pos0[i]

def p2(inp):
    steps = 1
    positions_0 = [[0 for i in range(11)] for k in range(steps+1)]
    positions_1 = [[0 for i in range(11)] for k in range(steps+1)]
    positions_0[0][inp[0]] = 1
    positions_1[0][inp[1]] = 1
    scores_0 = [[0 for j in range(31)] for k in range(steps+1)]
    scores_1 = [[0 for j in range(31)] for k in range(steps+1)]
    for k in range(1,steps+1):
        uppos(positions_0[k-1], positions_0[k])
        uppos(positions_1[k-1], positions_1[k])
        upscr(positions_0[k], scores_0[k-1], scores_0[k])
        upscr(positions_1[k], scores_1[k-1], scores_1[k])
    print(positions_0)
    print()
    #print(positions_1)
    #print()
    for sc in scores_0:
        print(sc)
    #print()
    #for sc in scores_1:
    #    print(sc)

in0 = (4, 8)
in1 = (6, 1)

#print('Result for Test Puzzle 1:', p1(in0))
#print('Result for Puzzle 1:', p1(in1))
print('Result for Test Puzzle 2:', p2(in0))
#print('Result for Puzzle 2:', p2(in1))

