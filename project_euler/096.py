# BACKTRACKING

class sudoku():
    def __init__(self, grid0, nr):
        self.grid0 = grid0
        self.n = len(grid0)
        self.nr = nr
        self.nc = self.n // self.nr
        self.n1 = self.n + 1

    def solve(self):
        def ipt(r, c, k):
            for j in range(c):
                if grid[r][j] == k:
                    return False
            for j in range(c+1, self.n):
                if grid[r][j] == k:
                    return False
            for i in range(r):
                if grid[i][c] == k:
                    return False
            for i in range(r+1, self.n):
                if grid[i][c] == k:
                    return False
            r0 = (r // self.nr) * self.nr
            c0 = (c // self.nc) * self.nc
            for i in range(r0, r):
                for j in range(c0, c):
                    if grid[i][j] == k:
                        return False
            c1 = c0 + self.nc
            for i in range(r0, r):
                for j in range(c+1, c1):
                    if grid[i][j] == k:
                        return False
            r1 = r0 + self.nr
            for i in range(r+1, r1):
                for j in range(c0, c):
                    if grid[i][j] == k:
                        return False
            for i in range(r+1, r1):
                for j in range(c+1, c1):
                    if grid[i][j] == k:
                        return False
            return True
        def uas():
            for i in range(self.n):
                for j in range(self.n):
                    if emp[i][j]:
                        return (i, j)
            return False
        def slv():
            tt = uas()
            if tt:
                r, c = tt
                for k in range(1, self.n1):
                    if ipt(r, c, k):
                        grid[r][c] = k
                        emp[r][c] = False
                        if slv():
                            return True
                        grid[r][c] = 0
                        emp[r][c] = True
            else:
                return True
        grid = [list(g) for g in self.grid0]
        emp = [[False for i in range(self.n)] for j in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                if grid[i][j] == 0:
                    emp[i][j] = True
        slv()
        return grid

ifl = open('096_sudoku.txt', 'r')
lyn = ifl.readline()
sdks = []
while True:
    if lyn[0] == 'G':
        sdks.append([])
    else:
        sdks[-1].append([int(lyn[i]) for i in range(len(lyn) - 1)])
    lyn = ifl.readline()
    if lyn == '':
        break
ifl.close()

n = 0
for sdk in sdks:
    s = sudoku(sdk, 3)
    ss = s.solve()
    n += ss[0][0] * 100 + ss[0][1] * 10 + ss[0][2]
print(n)
