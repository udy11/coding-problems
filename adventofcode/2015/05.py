import re

def p1(s):
    n0 = len(re.findall(r'[aeiou]', s))    # finds all occurences of vowels
    n1 = len(re.findall(r'(\w)\1', s))    # finds occurences of double characters. \w is for any alphanumeric character, () encloses what to output, \1 finds whatever was in first ()
    n2 = len(re.findall(r'ab|cd|pq|xy', s))    # finds all occurences of ab, cd, pq or xy
    return (n0 > 2) and (n1 > 0) and (n2 == 0)

def p2(s):
    n0 = len(re.findall(r'(\w{2})\w*?\1', s))    # finds occurences of a repeated pair of characters, *? to non-greedily include anything between a pair \w{2} and its repeatition \1
    n1 = len(re.findall(r'(\w)\w\1', s))    # finds occurences of format aba
    return (n0 > 0) and (n1 > 0)

ifl = open('05_input.txt', 'r')

s = ifl.readline().strip()
c1 = 0
c2 = 0
while s != '':
    if p1(s):
        c1 += 1
    if p2(s):
        c2 += 1
    s = ifl.readline().strip()
print(c1)
print(c2)
