import hashlib

def fh(s, n):
    z = '0' * n
    i = 1
    while True:
        si = s + str(i)
        if hashlib.md5(si.encode('ascii')).hexdigest()[:n] == z:
            return i
        i += 1

s0 = 'abcdef'
s1 = 'pqrstuv'
s2 = 'iwrupvqb'

print(s0, fh(s0, 5))
print(s1, fh(s1, 5))
print(s2, fh(s2, 5))
print(s2, fh(s2, 6))

