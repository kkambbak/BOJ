import sys
input = sys.stdin.readline

tri = []
n = int(input())
for i in range(n):
    tri.append(list(map(int,input().split())))


def Sum(n):
    if n == 1:
        print(tri[0][0])
        return
    if n == 2:
        print(max(tri[0][0]+tri[1][0],tri[0][0]+tri[1][1]))
        return

    tri[1][0] +=tri[0][0]
    tri[1][1] +=tri[0][0]
    for i in range(2,n):
        for j in range(i+1):
            if j == 0:
                tri[i][j] += tri[i-1][j]
            elif j == i:
                tri[i][j] += tri[i-1][j-1]
            else:
                tri[i][j] = max(tri[i-1][j]+tri[i][j] , tri[i-1][j-1]+tri[i][j])
    tri[n-1].sort(reverse=True)
    print(tri[n-1][0])

Sum(n)

