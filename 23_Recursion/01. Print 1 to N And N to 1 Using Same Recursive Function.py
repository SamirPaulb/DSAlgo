# https://www.youtube.com/watch?v=qDJJBZAIXIw&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=4

# print N to 1 using recursion
def solve(n):
    if n == 1: 
        print(n)
        return
    print(n)  # print before calling the function
    solve(n-1)
    
solve(7)
''' 
stack = [solve(7), solve(6), solve(5), solve(4), solve(3), solve(2), solve(1)]
while returning there are noting so stack got popped and print nothing during returning
'''



print('------------------------------')


# Print 1 to N using recursion
def solve(n):
    if n == 1:
        print(n)
        return
    solve(n-1)
    print(n)  # print after calling the function

solve(7)
''' 
stack = [solve(7), solve(6), solve(5), solve(4), solve(3), solve(2), solve(1)]
while appending there is nothing in to print, while returning there is print function 
so stack got popped and get printted in reversed order
'''

print('------------------------------')


def solve(n):
    if n == 1: 
        print(n)
        return
    print(n)  
    solve(n-1)
    print(n)
    
solve(7)
''' 
stack = [solve(7), solve(6), solve(5), solve(4), solve(3), solve(2), solve(1)]
while appending to the stack print(n) and after returning from 1 stack got popped and print(n)
again
 '''