import sys
sys.setrecursionlimit(1000)

n = int(input())
m = int(input())
adjList = [[]for i in range(n+1)]
visited = [False] *(n+1)
for i in range(m):
    x,y = map(int,input().split())
    adjList[x].append(y)
    adjList[y].append(x)

num = 0

def dfs(adjList,v,visited):
    visited[v] = True
    global num
    num +=1
    for i in adjList[v]:
        if not visited[i]:
            dfs(adjList,i,visited)

dfs(adjList,1,visited)
print(num-1)