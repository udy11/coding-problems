def ifcb(n):
    ncb = round(n ** (1/3))
    if ncb * ncb * ncb == n:
        return ncb
    else:
        return False

n = 91

n2 = n * n
i = 1
while True:
    ic = ifcb(i * n + 1)
    if ic:
        print(ic)
    i += 1
    if i > n2:
        break
