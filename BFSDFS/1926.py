import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
Map = []
visited = [[False] * m for _ in range(n)]
for i in range(n):
    Map.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    maxq = 1
    queue = deque()
    queue.append((x,y))
    visited[y][x]= True
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if Map[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    maxq += 1
                    queue.append((nx,ny))
    return maxq

cnt ,maxcnt = 0, 0
for i in range(n):
    for j in range(m):
        if Map[i][j] == 1 and not visited[i][j]:
            cnt +=1
            maxcnt = max(maxcnt, bfs(j,i))

print(cnt)
print(maxcnt)
