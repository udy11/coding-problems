import sys

def count1(img):
    c = 0
    for r in img:
        c += r.count('1')
    return c

def imgprint(img):
    for row in img:
        print(''.join(row).replace('0', '∙').replace('1', '#'))

def newimg(img0, b):
    nr = len(img0)
    nc = len(img0[0])
    img1 = []
    for i in range(2):
        img1.append([b for j in range(nc+4)])
    for i in range(nr):
        img1.append([b for j in range(2)] + img0[i] + [b for j in range(2)])
    for i in range(2):
        img1.append([b for j in range(nc+4)])
    return img1

def enhancement(img0, iea):
    nr = len(img0)
    nc = len(img0[0])
    img1 = [list(r) for r in img0]
    if img0[0][0] == '0':
        bc = iea[0]
    if img0[0][0] == '1':
        bc = iea[511]
    for j in range(nc):
        img1[0][j] = bc
        img1[nr-1][j] = bc
    for i in range(1, nr-1):
        img1[i][0] = bc
        img1[i][nc-1] = bc
    for i in range(1, nr-1):
        for j in range(1, nc-1):
            img1[i][j] = iea[int('0b' + ''.join(img0[i-1][j-1:j+2] + img0[i][j-1:j+2] + img0[i+1][j-1:j+2]), 2)]
    return img1

# Image size keeps increasing, it can be reduced for optimization
def p1(ifln, steps):
    ifl = open(ifln, 'r')
    iea = ifl.readline()[:-1].replace('.', '0').replace('#', '1')
    ifl.readline()
    lyn = ifl.readline().replace('.', '0').replace('#', '1')
    img0 = []
    while lyn != '':
        img0.append([c for c in lyn[:-1]])
        lyn = ifl.readline().replace('.', '0').replace('#', '1')
    ifl.close()
    img1 = newimg(img0, '0')
    img1 = enhancement(img1, iea)
    for k in range(1, steps):
        img1 = newimg(img1, img1[0][0])
        img1 = enhancement(img1, iea)
    return count1(img1)

print('Result for Test Puzzle 1:', p1('day-20_in0.txt', 2))
print('Result for Puzzle 1:', p1('day-20_in1.txt', 2))
print('Result for Test Puzzle 2:', p1('day-20_in0.txt', 50))
print('Result for Puzzle 2:', p1('day-20_in1.txt', 50))

