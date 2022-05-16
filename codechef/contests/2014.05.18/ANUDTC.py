def case1(n):
    if 360 % n == 0:
        return 'y'
    else:
        return 'n'

def case2(n):
    if n < 361:
        return 'y'
    else:
        return 'n'

def case3(n):
    if n < 27:
        return 'y'
    else:
        return 'n'

t = int(input())
for i in range(t):
    n = int(input())
    print(case1(n), end=' ')
    print(case2(n), end=' ')
    print(case3(n))
