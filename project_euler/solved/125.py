# BRUTE-FORCE

# Main point was that a palindrome could have
# more than one expansions in squares
# thus that was needed to be taken care of

def is_palindrome(st):
    """ (str) -> bool
    """
    n=len(st)
    for i in range(n // 2):
        if st[i] != st[n-i-1]:
            return False
    return True

nn = 100000000
k = 1

ps = set()
while k < 10000:
    i = k
    ss = i * i
    while ss < nn:
        i += 1
        ss += i * i
        if ss < nn and is_palindrome(str(ss)):
            ps = ps.union(set([ss]))
    k += 1

print(sum(ps))
