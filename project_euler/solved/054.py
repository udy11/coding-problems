# IDEA:
# BRUTE FORCE

# On the other hand, I wanted to devise a formula which will
# generate some sort of score or a given hand

# Though the function score() returns a score, it's ultimately a brute force method

vl = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
for i in range(1,10):
    vl[str(i)] = i

def score(s):
    ifpr = False
    pcl = [[0, ''] for i in range(5)]
    for i in range(5):
        pcl[i][0] = vl[s[i * 3]]
        pcl[i][1] = s[1 + i * 3]
    pcl.sort()
    cnsctv = False
    if pcl[4][0] == pcl[3][0] + 1 == pcl[2][0] + 2 == pcl[1][0] + 3 == pcl[0][0] + 4:
        cnsctv = True
    if pcl[0][1] == pcl[1][1] == pcl[2][1] == pcl[3][1] == pcl[4][1]:
        if cnsctv:
            if pcl[0][0] == 10:
                if ifpr:
                    print('Royal Flush')
                return 18000
            if ifpr:
                print('Straight Flush')
            return 16000 + pcl[1][0] * 100
        if ifpr:
            print('Flush')
        return 10000 + pcl[4][0] * 100
    if cnsctv:
        if ifpr:
            print('Straight')
        return 8000 + 100 * pcl[0][0]
    for i in range(4):
        if pcl[i][0] == pcl[i+1][0]:
            if i < 3 and pcl[i+1][0] == pcl[i+2][0]:
                if i < 2 and pcl[i+2][0] == pcl[i+3][0]:
                    if ifpr:
                        print("Four of a Kind")
                    if i == 0:
                        return 14000 + 100 * pcl[0][0] + 10 * pcl[4][0]
                    else:
                        return 14000 + 100 * pcl[4][0] + 10 * pcl[0][0]
                if i == 0:
                    if pcl[3][0] == pcl[4][0]:
                        if ifpr:
                            print("Full House")
                        return 12000 + pcl[0][0] * 100 + pcl[3][0] * 10
                    else:
                        if ifpr:
                            print("Three of a Kind")
                        return 6000 + 100 * pcl[0][0] + 10 * pcl[4][0] + pcl[3][0]
                if i == 1:
                    if ifpr:
                        print("Three of a Kind")
                    return 6000 + 100 * pcl[1][0] + 10 * pcl[4][0] + pcl[0][0]
                if i == 2:
                    if ifpr:
                        print("Three of a Kind")
                    return 6000 + 100 * pcl[2][0] + 10 * pcl[1][0] + pcl[0][0]
            if i == 0:
                if pcl[2][0] == pcl[3][0] == pcl[4][0]:
                    if ifpr:
                        print("Full House")
                    return 12000 + pcl[2][0] * 100 + pcl[0][0] * 10
                elif pcl[2][0] == pcl[3][0]:
                    if ifpr:
                        print("Two Pairs")
                    return 4000 + 100 * pcl[2][0] + 10 * pcl[0][0] + pcl[4][0]
                elif pcl[3][0] == pcl[4][0]:
                    if ifpr:
                        print("Two Pairs")
                    return 4000 + 100 * pcl[3][0] + 10 * pcl[0][0] + pcl[2][0]
                else:
                    if ifpr:
                        print("One Pair")
                    return 2000 + 100 * pcl[0][0] + 10 * pcl[4][0] + pcl[3][0] + 0.1 * pcl[2][0]
            if i == 1:
                if pcl[3][0] == pcl[4][0]:
                    if ifpr:
                        print("Two Pairs")
                    return 4000 + 100 * pcl[3][0] + 10 * pcl[1][0] + pcl[0][0]
                else:
                    if ifpr:
                        print("One Pair")
                    return 2000 + 100 * pcl[1][0] + 10 * pcl[4][0] + pcl[3][0] + 0.1 * pcl[0][0]
            if i == 2:
                if ifpr:
                    print("One Pair")
                return 2000 + 100 * pcl[2][0] + 10 * pcl[4][0] + pcl[1][0] + 0.1 * pcl[0][0]
            if i == 3:
                if ifpr:
                    print("One Pair")
                return 2000 + 100 * pcl[3][0] + 10 * pcl[2][0] + pcl[1][0] + 0.1 * pcl[0][0]
    if ifpr:
        print('High Card')
    return sum(pcl[i][0] * 10 ** (i-3) for i in range(5))

ifl = open('054_poker.txt','r')
lyn = ifl.readline()
i = 1
w1 = 0
while lyn != '':
    s1 = lyn[0:14]
    s2 = lyn[15:31]
#    print(i, score(s1), score(s2))
    if(score(s1) > score(s2)):
        w1 += 1
    lyn = ifl.readline()
    i += 1
ifl.close()
print(w1)
