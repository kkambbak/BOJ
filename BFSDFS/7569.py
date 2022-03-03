import sys
from collections import deque
input = sys.stdin.readline


m,n,h = map(int,input().split())
Box = [[] for i in range(h)]
for i in range(h):
    for j in range(n):
        Box[i].append(list(map(int,input().split())))

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]
queue = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if Box[i][j][k] == 1:
                queue.append((k,j,i,0))


def bfs(x,y,z,day):
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0 <= nx < m and 0 <= ny < n and 0 <=nz < h:
            if Box[nz][ny][nx] == 0:
                queue.append((nx,ny,nz,day+1))
                Box[nz][ny][nx] =1
    day += 1
    return day

while queue:
    x,y,z,day = queue.popleft()
    endDay = bfs(x,y,z,day)

cond = True
for i in range(h):
    for j in range(n):
        for k in range(m):
            if Box[i][j][k] == 0:
                cond = False


if cond == True:
    print(endDay - 1)
else:
    print(-1)