n = int(input())

t = (n-1)/6

y = 1
x = 1
while x < t:
    x = y*(y+1)/2
    y += 1

if 1 < n <= 7:
    print(2)
else:
    print(y)

a,b = map(int,input().split())
print(a-b)