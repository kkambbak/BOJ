import time
from collections import deque


n, m = map(int,input().split())
Map = []
for i in range(n):
    x=list(map(int,input()))
    y =[]
    for j in range(m):
        y.append([x[j],x[j]])
    Map.append(y)

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def printMap():
    for i in range(n):
        print(Map[i])
    print("----------------")

queue = deque()
queue.append((0,0,0,1))
Map[0][0][1] = 2
Map[0][0][0] = 2
def bfs():
    while queue:
        x,y,z,num = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0<= ny < n:
                if z == 0 and Map[ny][nx][0] == 0:
                    Map[ny][nx][0] = num+1
                    Map[ny][nx][1] = num+1
                    if nx == m-1 and ny == n-1:
                        print(Map[ny][nx][0])
                        return
                    queue.append((nx,ny,0,num+1))

                elif z == 0 and Map[ny][nx][0] == 1:
                    Map[ny][nx][1] = num+1
                    if nx == m-1 and ny == n-1:
                        print(Map[ny][nx][1])
                        return
                    queue.append((nx,ny,1,num+1))

                elif z == 1 and Map[ny][nx][1] == 0:
                    Map[ny][nx][1] = num+1
                    if nx == m-1 and ny == n-1:
                        print(Map[ny][nx][1])
                        return
                    queue.append((nx,ny,1,num+1))
    print(-1)

if n==1 and m == 1:
    print(1)
else:
    bfs()



