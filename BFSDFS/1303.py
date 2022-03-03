n,m = map(int,input().split())
Map = []
MapCopy = []
Check = [[0]*n for _ in range(m)]
Wlist = []
Blist = []
for i in range(m):
    Map.append(list(input()))

MapCopy = Map.copy()

playerPos = [0,0]
cnt = 0

def dfs(y,x):
    global cnt
    if y<= -1 or y >= m or x <= -1 or x>=n:
        return False
    if Map[y][x] == 'W':
        Map[y][x] = 'B'
        Check[y][x] = 1
        cnt += 1
        dfs(y-1,x)
        dfs(y,x-1)
        dfs(y+1,x)
        dfs(y,x+1)
        return True
    return False

def dfsB(y,x):
    global cnt
    if y<= -1 or y >= m or x <= -1 or x>=n:
        return False
    if Check[y][x] == 0:
        Check[y][x] = 1
        cnt += 1
        dfsB(y-1,x)
        dfsB(y,x-1)
        dfsB(y+1,x)
        dfsB(y,x+1)
        return True
    return False

for i in range(m):
    for j in range(n):
        if Check[i][j] == 0:
            dfs(i,j)
            if(cnt!=0):
                Wlist.append(cnt)
                cnt = 0

for i in range(m):
    for j in range(n):
        if Check[i][j] == 0:
            dfsB(i,j)
            if(cnt!=0):
                Blist.append(cnt)
                cnt = 0

Wsum = 0
Bsum = 0
for i in Wlist:
    Wsum += (i**2)
for j in Blist:
    Bsum += (j**2)
print(Wsum, Bsum)

