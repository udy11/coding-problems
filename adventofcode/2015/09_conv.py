# To generate input files for part-2 of day-15 puzzles

import csv

for m in range(0, 2):
    dt = []
    csvreader = csv.reader(open('day-15_in' + str(m) + '.txt', 'r'))
    for row in csvreader:
        nr = len(row)
        rw = [int(r) for r in row]
        r1 = list(rw)
        for k in range(1, 5):
            r1 += [((r-1+k)%9)+1 for r in rw]
        dt.append(r1)
    dt0 = list(dt)
    for k in range(1, 5):
        for rw in dt0:
            r1 = [((r-1+k)%9)+1 for r in rw]
            dt.append(r1)
    ofl = open('day-15_in' + str(m+2) + '.txt', 'w')
    for d0 in dt:
        d1 = [str(d) for d in d0]
        ofl.write(','.join(d1) + '\n')
    ofl.close()
