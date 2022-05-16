def fqs(f, s, n):
    if f == 1:
        return n * (n + 1) // 2
    c = 0
    for i in range(1, n+1):
        for j in range(n-i+1):
            s0 = s[j:j+i]
            c0 = 0
            for k in range(n-i+1):
                if s0 == s[k:k+i]:
                    c0 += 1
            if c0 == f:
                c += 1
    return c

t = int(input())

for tt in range(t):
   s = input()
   n = len(s)
   q = int(input())
   for qq in range(q):
       f = int(input())
       print(fqs(f, s, n))
