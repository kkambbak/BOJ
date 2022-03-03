from cmath import inf


n,m= map(int,input().split())
chessBoard = []
for i in range(n):
    chessBoard.append(list(input()))
B = []
W = []
correctB = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]
correctW = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

rangeX = m-7
rangeY = n-7

def chess(x,y):
    compareB = 0
    compareW = 0
    for i in range(8):
        for j in range(8):
            if chessBoard[y+i][x+j] != correctB[i][j]:
                compareB +=1
            if chessBoard[y+i][x+j] != correctW[i][j]:
                compareW +=1
    return min(compareW,compareB)
 
answer = inf
for i in range(rangeY):
    for j in range(rangeX):
        answer = min(answer,chess(j,i))

print(answer)