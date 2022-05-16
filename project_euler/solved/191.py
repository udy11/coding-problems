import numpy as np

aom = np.int64(np.array([[1,1,0,0],[0,0,1,1],[1,1,0,0],[0,0,1,0]]))

aoi = np.int64(np.array([1,1,1,1]))

dc = {0:1, 1:2, 2:4}

n = 30

for i in range(3, n+1):
    aoi = np.dot(aom, aoi)
    dc[i] = np.sum(aoi)

s = dc[n]

for i in range(1, n+1):
    s += dc[i-1] * dc[n-i]

print(s)
