import math

a,b,c = map(int,input().split())
if b<c:
    answer = math.ceil(a/(c-b))
    if answer == a/(c-b):
        answer += 1
if b >= c:
    answer = -1
print(answer)