# MATH

# For last 8 digits, it repeats after every 1250000
# multiplications. So to speed things up, store all
# powers up to that and use them to calculate the
# hyperexponentiation from top to bottom

r = 1250000
n = (1777 ** 1777) % r
k = 2
pw = [1 for i in range(r)]

for i in range(1, r):
    pw[i] = (pw[i - 1] * 1777) % 10 ** 8

while k < 1884:
    n = pw[n] % r
    k += 1

print(pw[n])
