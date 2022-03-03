import sys
input = sys.stdin.readline

array = [[[None for i in range(21)]for i in range(21)] for i in range(21)]

def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20,20,20)
    if a < b and b < c:
        return w(a,b,c-1)+ w(a,b-1,c-1) - w(a,b-1,c)
    else:
        return w(a-1,b,c)+ w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)

def w_dp(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w_dp(20,20,20)
    if array[a][b][c] != None:
        return array[a][b][c]

    if a<b and b<c:
        array[a][b][c] = w_dp(a,b,c-1)+ w_dp(a,b-1,c-1) - w_dp(a,b-1,c)
        return array[a][b][c]
    else:
        array[a][b][c] = w_dp(a-1,b,c)+ w_dp(a-1,b-1,c) + w_dp(a-1,b,c-1) - w_dp(a-1,b-1,c-1)
        return array[a][b][c]
    

while True:
    a, b, c = map(int,input().split())
    if a == -1 and b == -1 and c == -1 : 
        break
    print("w(%d, %d, %d) = %d" % (a, b, c, w_dp(a,b,c)))