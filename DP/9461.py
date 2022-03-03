import sys
input = sys.stdin.readline
from collections import deque

def tri(n):
    a = deque([1,1,1,2,2])
    if n<6:
        print(a[n-1])
    else:
        for i in range(6, n+1):
            num = a[0]+a[4]
            a.append(num)
            a.popleft()
        print(a[4])

t= int(input())
for i in range(t):
    n = int(input())
    tri(n)