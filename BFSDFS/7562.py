from collections import deque

dx = [1,1,-1,-1,2,2,-2,-2]
dy = [2,-2,2,-2,1,-1,1,-1]

def bfs(ChessBoard, nowX, nowY, targetY, targetX):
    queue = deque()
    queue.clear()
    queue.append((nowX, nowY, 0))
    if nowY == targetY and nowX == targetX:
        return 0
    while queue:
        x, y, num = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0<=ny < l and ChessBoard[ny][nx] == 0:
                ChessBoard[ny][nx] = num + 1
                if ny == targetY and nx == targetX:
                    return ChessBoard[ny][nx]
                queue.append((nx,ny,num+1))

n = int(input())
for i in range(n):
    l = int(input())
    ChessBoard = [[0 for i in range(l)]for i in range(l)]
    nowY, nowX = map(int,input().split())
    targetY, targetX = map(int,input().split())
    print(bfs(ChessBoard, nowX, nowY, targetY, targetX))
