# Define functions to convert any decimal number to Minimal Roman Number
# And any valid Roman Number to decimal number

def rm(n):
    ''' (int) ->  str
        Converts a decimal number to a valid minimal Roman Number
        The rules for a minimal valid Roman Number are given here:
        http://projecteuler.net/about=roman_numerals
    '''
    rmtr = (('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90), ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1))
    s = ''
    for k in rmtr:
        ss = n // k[1]
        s += k[0] * ss
        n -= ss * k[1]
    return s

def rn(s):
    ''' (str) ->  int
        Converts a valid Roman Number to decimal number
        The rules for a valid Roman Number are given here:
        http://projecteuler.net/about=roman_numerals
    '''
    rmtr = (('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90), ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1))
    n = 0
    for k in rmtr:
        j = 0
        c = 0
        if len(k[0]) == 2:
            while True:
                if(j >= len(s)):
                    break
                if s[j:j+2] == k[0]:
                    c += 1
                    j += 2
                else:
                    break
            s = s[j:]
            n += k[1] * (j//2)
        else:
            while True:
                if(j >= len(s)):
                    break
                if s[j] == k[0]:
                    c += 1
                    j += 1
                else:
                    break
            s = s[j:]
            n += k[1] * j
    return n

ifl = open('089_roman.txt','r')
rmn = ifl.readline().strip()
stl = 0
while rmn != '':
    sl = len(rmn) - len(rm(rn(rmn)))
    print(rm(rn(rmn)),rn(rmn),rmn)
    stl += sl
    rmn = ifl.readline().strip()
ifl.close()
print(stl)
