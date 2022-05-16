# Sort of Sieve Method
# If a multiple of a number is not containing
# the same digits, just move on..

def dgc(dg, n):
    st = str(n)
    for s in st:
        if not s in dg:
            return False
    return True

for i in range(100001,166667):
    dg = [s for s in str(i)]
    for j in range(2, 7):
        if not dgc(dg, i * j):
            break
    else:
        print(i)
