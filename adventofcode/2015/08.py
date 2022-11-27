import re

ifl = open('08_input.txt', 'r')

lyn = ifl.readline().strip()
c1 = 0
c2 = 0
while lyn != '':
    c1 += len(lyn) - len(lyn.encode('utf-8').decode('unicode-escape')) + 2
    c2 += lyn.count('\\') + lyn.count(r'"') + 2
    lyn = ifl.readline().strip()
ifl.close()
print(c1)
print(c2)
