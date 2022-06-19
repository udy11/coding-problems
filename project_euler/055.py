# BRUTE FORCE
# But perhaps that was intended

# This is an important line in the problem:
# Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.
# As it implies that you should not check for palindrome before adding first reverse

def rvs(n):
    return int(str(n)[::-1])

def is_palindrome(st):
    """ (str) -> bool
    """
    n=len(st)
    for i in range(n // 2):
        if st[i] != st[n-i-1]:
            return False
    return True

c = 0
for i in range(1, 10000):
    m = i
    j = 1
    while j < 55:
        m += rvs(m)
        if is_palindrome(str(m)):
            break
        j += 1
    else:
        c += 1
#        print(i)
print(c)
