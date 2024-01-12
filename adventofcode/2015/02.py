ifl = open('02_input.txt', 'r')

paper = 0
ribbon = 0
lyn = ifl.readline()
while lyn != '':
    sides = sorted([float(x) for x in lyn.split('x')])
    paper += 3 * sides[0] * sides[1] + 2 * (sides[0] + sides[1]) * sides[2]
    ribbon += 2 * (sides[0] + sides[1]) + sides[0] * sides[1] * sides[2]
    lyn = ifl.readline()
print(paper)
print(ribbon)

ifl.close()

