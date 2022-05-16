# to check if a number is prime
import math
def is_prime(n):
    if(n<2):
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            return False
    return True

# Generating primes till 1000
# since b only needs to run over primes
pr = []
n=2
for n in range(2,998):
    ch = True
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            ch = False
    if ch:
        pr.append(n)

d=[]
m=1000
nm=0
am=-m
bm=2
for a in range(-m,m+1):
    for b in pr:
        n=1
        ip=True
        while(ip):
            q = n*(a+n)+b
            if(not is_prime(q)):
                ip=False
            n+=1
        if(nm<n):
            nm=n
            am=a
            bm=b
print(am,bm,am*bm)
