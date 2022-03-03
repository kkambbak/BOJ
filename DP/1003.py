import sys
input = sys.stdin.readline

t = int(input())
Nums = []
for i in range(t):
    Nums.append(int(input()))


countZero =0
countOne = 0
def fibonacci(n):
    global countZero, countOne
    if(n ==0):
        countZero += 1 
        return 0
        
    elif(n == 1):
        countOne += 1
        return 1
        
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fib_arra = [0,1]

def fib_recur_dp(n):
    if n < len(fib_arra):
        return fib_arra[n]
    else:
        fib = fib_recur_dp(n-1) + fib_recur_dp(n-2)
        fib_arra.append(fib)
        return fib

def fib_dp(n):
    if n == 0:
        print(1,0)
        return 0
    elif n == 1:
        print(0,1)
        return 1
    fib_array=[0,1]

    for i in range(2, n+1):
        num = fib_array[i-1] + fib_array[i-2]
        fib_array.append(num)
    print(fib_array[n-1],fib_array[n])
    return fib_array[n]
    
for i in Nums:
    fib_dp(i)