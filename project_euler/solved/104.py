# IDEA:
# Checking for last 10 digits is via % 10**9
# Checking for first 10 digits can cause overflow
#   even while considering floating point arithmetic.
#   So, to avoid that, simply keep on levelling
#   numbers by keep on dividing them

def ipd1(n):
    s = str(n)
    ds = '123456789'
    for d in ds:
        if not d in s:
            return False
    return True

def ipd2(n):
    s = str(n)[:10]
    ds = '123456789'
    for d in ds:
        if not d in s:
            return False
    return True

f1r = 5.9425114757512643212875125
f2r = 9.6151855463018422468774568
f1n = 212875125
f2n = 468774568
i = 127
while True:
    f3r = f2r + f1r
    f3n = (f1n + f2n) % 10**9
    if ipd1(f3n) and ipd2(f3r):
        print(i)
        break
    i += 1
    if f1r > 100:
        f1r = f2r / 10
        f2r = f3r / 10
    else:
        f1r = f2r
        f2r = f3r
    f1n = f2n
    f2n = f3n
