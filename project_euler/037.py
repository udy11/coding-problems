import math
def is_prime(n):
    if(n<2):
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            return False
    return True

# To generate left-to-right truncatable primes
# of digits 2 to cn
def lrtp(cn):
    c = 0
    fd = ['3', '7']
    fl = list(fd)
    md = ['1', '3', '7', '9']
    nd = 1
    tpn = []
    while (nd < cn):
        ft = []
        for i in fl:
            for j in md:
                if(is_prime(int(j+i))):
                    ft.append(j+i)
        fl = list(ft)
        tpn += ft
        nd += 1
    return tpn

# To check if number is right-to-left truncatable prime
def is_rltp(s):
    for i in range(len(s)):
        if not is_prime(int(s)):
            return False
        s = s[:-1]
    return True

lrtpl = lrtp(9)
sm = 23 + 53     # Noticing that 23 and 53 are the only left out there
print(23)
print(53)
for i in lrtpl:
    if(is_rltp(i)):
        print(i)
        sm += int(i)
print("Sum:",sm)
