import math

##a = 1504170715041707
##b = 4503599627370517
a = 30
b = 41
d = [a]
m = a
k = 2
while m > 1:
    m = (a * k) % b
    if m < d[-1]:
        d.append(m)
        print(k, m, (a * k) / b)
        k = math.floor(b / m)
    else:
        k += 1
