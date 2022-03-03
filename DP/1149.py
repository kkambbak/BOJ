import sys
input= sys.stdin.readline

houses = []

n = int(input())
for i in range(n):
    r,g,b = map(int,input().split())
    houses.append([r,g,b])

print(houses)

def dp(i):
    return