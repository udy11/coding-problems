# (Sort of) BRUTE FORCE

# Method:
# Ignore last two digits since they must be 00
# For remaning, check all integers between 101010100,138902600
# such that last digits end in one of
# (3, 33, 43, 53, 83, 93, 7, 17, 47, 57, 67, 97)
# because the number formed by digits preceding 9 must ...
# ... be divisible by 4

# NUMBER IS: 1929374254627488900
# ITS SQRT:  1389019170

# Instead of str method, one can also check digits of number
# that might be faster
def chk(n):
    s = str(n)
    for i in range(9):
        if s[2*i] != str(i+1):
            return False
    return True

dl = [3, 33, 43, 53, 83, 93, 7, 17, 47, 57, 67, 97]
for i in range(101010100,138902601,100):
    for j in dl:
        n = i + j
        if chk(n*n):
            print(n)
