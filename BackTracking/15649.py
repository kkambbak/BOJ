n,m = map(int,input().split())
Input = [i+1 for i in range(n)]

Stack=[]
Stack.append(Input)

def bt(nums,length):
    a= Stack[n-length].copy()
    if len(a)== n-m:
        print(nums)
        Stack.pop()
        return 0
    
    for i in range(length):
        a = Stack[n-length].copy()
        x = nums + str(a[i]) + ' '
        del a[i]
        Stack.append(a.copy())
        bt(x,length-1)
    Stack.pop()

bt('',n)