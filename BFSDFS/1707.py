import sys
k = int(input())
graphs = []
Visited = []
vNum = []
sys.setrecursionlimit(20000)
input = sys.stdin.readline

for i in range(k):
    v, e = map(int,input().split())
    graph = [[]for _ in range(v+1)]
    Visited.append([False]*(v+1))
    vNum.append(v)
    for j in range(e):
        u, v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    graphs.append(graph)

def dfs(graph,v,visited,color):
    global count
    if visited[v] == False:
        visited[v] = color
        if color == 'W':
            newColor = 'B'
        else:
            newColor = 'W'
        for i in graph[v]:
            dfs(graph,i,visited,newColor)
    elif visited[v] == 'W':
        if color == 'W':
            
            return 0
        elif color == 'B':
            count +=1
            visited[v] = 'W'
            newColor = 'B'
    elif visited[v] == 'B':
        if color == 'B':
            

            
            return 0
        elif color == 'W':
            count +=1
            visited[v] = 'B'
            newColor = 'W'
    return 1


for i in range(k):
    count = 0
    for j in range(1, vNum[i]+1):
        if Visited[i][j] == False:
            dfs(graphs[i],j,Visited[i],'W')
    if count == 0:
        print('YES')
    else:
        print('NO')