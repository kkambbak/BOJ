x = int(input())
Sum = 1
i = 2
while Sum < x:
    Sum += i
    i += 1

gap = Sum - x
if i%2 == 0:
    x = i-gap-1
    y = i-x
    print(str(y)+"/"+str(x))
else:
    x = i-gap-1
    y = i-x
    print(str(x)+"/"+str(y))