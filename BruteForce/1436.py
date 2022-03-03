#이분탐색으로 하면 O(logn)

a= int(input())
b=[]
i=665
while len(b) < a:
    i += 1
    i = str(i)
    if '666' in i:
        b.append(i)
    i= int(i)

print(b[a-1])
