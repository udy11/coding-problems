qs = '''5616185650518293 ;2 correct
3847439647293047 ;1 correct
5855462940810587 ;3 correct
9742855507068353 ;3 correct
4296849643607543 ;3 correct
3174248439465858 ;1 correct
4513559094146117 ;2 correct
7890971548908067 ;3 correct
8157356344118483 ;1 correct
2615250744386899 ;2 correct
8690095851526254 ;3 correct
6375711915077050 ;1 correct
6913859173121360 ;1 correct
6442889055042768 ;2 correct
2321386104303845 ;0 correct
2326509471271448 ;2 correct
5251583379644322 ;2 correct
1748270476758276 ;3 correct
4895722652190306 ;1 correct
3041631117224635 ;3 correct
1841236454324589 ;3 correct
2659862637316867 ;2 correct'''

qqs = '''903423 ;2 correct
707945 ;0 correct
394587 ;3 correct
341092 ;1 correct
515459 ;2 correct
125310 ;1 correct'''

qt = [[]]
for c in qs:
    if 47 < ord(c) < 58:
        qt[-1].append(int(c))
    elif ord(c) == 10:
        qt.append([])
qm = len(qt[0]) - 1
qn = len(qt)

ss = [5, 6, 4, 8, 9, 7, 1, 0, 3, 1, 6, 2, 0, 4, 1, 9]

for i in range(qn):
    cc = 0
    wr = []
    for j in range(qm):
        if ss[j] == qt[i][j]:
            wr.append(j)
            cc += 1
    if cc != qt[i][-1]:
        print('wrong for ' + str(i) + ':', qt[i], ', matches at ', wr)
