import os

ifl = open('01_input.txt', 'r')
dt = ifl.read().strip()
ifl.close()

sdt = sorted([sum([int(d) for d in d1.split(os.linesep)]) for d1 in dt.split(2 * os.linesep)])

print(sdt[-1])

print(sum(sdt[-3:]))

