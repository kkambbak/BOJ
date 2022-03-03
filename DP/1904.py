import sys
from collections import deque
n = int(sys.stdin.readline())

def fib(n):
    if n == 1:
        return 1
    arr = deque([0,1])

    for i in range(2, n+2):
        num = arr[0]+arr[1]
        arr.append(num%15746)
        arr.popleft()
    return arr[1]

print(fib(n)) 