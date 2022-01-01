memo = []
for i in range(20):
    memo.append(-1)

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if memo[n] != -1:
        return memo[n]
    
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

print(fib(6))

# output: 8









# We can also display the series up to a specific range using a for loop —

memo = []
for i in range(20):
    memo.append(-1)

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if memo[n] != -1:
        return memo[n]
    
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

for i in range(10):
    print(fib(i))

# output:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34