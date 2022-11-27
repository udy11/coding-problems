ifl = open('01_input.txt', 'r')
dt = ifl.read()
ifl.close()

# Part 1
print(dt.count('(') - dt.count(')'))

# Part 2
f = 0
for i in range(len(dt)):
    if dt[i] == '(':
        f += 1
    elif dt[i] == ')':
        f -= 1
    if f < 0:
        print(i + 1)
        break

