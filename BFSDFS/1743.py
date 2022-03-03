import sys
sys.setrecursionlimit(100000)

n,m,k = map(int,input().split())
Map = [[0]*m for _ in range(n)]
for i in range(k):
    r,c = map(int,input().split())
    Map[r-1][c-1] = 1

cnt = 0

def dfs(y,x):
    global cnt
    if y<= -1 or y >= n or x <= -1 or x>=m:
        return False
    if Map[y][x] == 1:
        Map[y][x] = 0
        cnt += 1
        dfs(y-1,x)
        dfs(y,x-1)
        dfs(y+1,x)
        dfs(y,x+1)
        return True
    return False
trash = []

for i in range(n):
    for j in range(m):
        if Map[i][j] == 1:
            dfs(i,j)
            if cnt != 0:
                trash.append(cnt)
                cnt = 0

print(max(trash))