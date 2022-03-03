from collections import deque

n = int(input())
stairs = []
for i in range(n):
    stairs.append(int(input()))
answer = 0
cnt= False
t = n

def stairs(n):
    if n == 0:
        return 0
    if n == 1:
        return

    
    costs = [0,0]

    for i in range(3,)
    cost = costs[]
    return


"""
answer+=stairs[t-1]
t-=2
while t>=0:
    if cnt == True:
        answer += stairs[t-1]
        t-=2
        cnt = False
    else:
        if stairs[t] < stairs[t-1]:
            answer += stairs[t-1]
            t -=2
            if t == 0:
                answer+= stairs[t]
                t-=1
                
        else:
            answer += stairs[t]
            t-=1
            cnt = True
print(answer)

"""