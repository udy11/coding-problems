# MONTE-CARLO (BRUTE-FORCE, ONLY FOR TESTING)

# A brute force test to see what kind of answer should we be expecting

import random

bag = []
for i in range(7):
    for j in range(10):
        bag.append(i)

count = [0] * 8
n = 100000
for k in range(n):
    rs = random.sample(bag, 20)
    count[len(set(rs))] += 1

ev = 0
for i in range(8):
    ev += i * count[i]
ev /= n
print(ev)
