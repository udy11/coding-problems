for p in range(50):
    for a in range(1, p // 2):
        for b in range(a, p):
            c = p - a - b
            if a + b > c and a*a + b*b == c*c + 1:
                print(p, a, b, c)
