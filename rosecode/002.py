def dgsm(n):
    " Digital Sum "
    s = str(n)
    sm = 0
    for st in s:
        sm += int(st)
    return sm

f1 = 1
f2 = 1
for i in range(1000):
    f3 = f1 + f2
    if dgsm(f3) > 100:
        print(f3)
        break
    f1 = f2
    f2 = f3
