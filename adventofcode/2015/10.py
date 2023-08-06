import itertools

i0 = '3113322113'

for m in range(50):
    i1 = ''.join([str(len(''.join(g))) + k for k, g in itertools.groupby(i0)])
    i0 = i1
    if m == 39 or m == 49:
        print(len(i1))

