__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/476/A

Solution: The minimum number of moves to reach the top of the stairs is to use 2 step-policy, which would 
require n/2 moves. But if n is odd, we would need one more move of 1 step-policy. Hence we can calculate 
the minimum moves needed as (n+1)/2. Let that be saved in min_moves_needed

To find the nearest value >= min_moves_needed which is divisible by m would be:

ceil(min_moves_needed / m) * m 

This is because min_moves_needed/m would give the quotient that when multiplied by m should give you a m
divisible value. But since min_moves_needed may not be completely divisible by m, we need to use ceil 
function. 

We further employ a shortcut to avoid using ceil() function directly. 


~ Tidbit ~

1) We can find ceil() without using the function. The shortcut is as follows:
 ceil(a/b) = (a+b-1) / b

2) Find nearest value >= a which is divisible by b:
 ceil(a/b) * b
 
3) Find nearest value <= a which is divisible by b:
 floor(a/b) * b or just (a/b) * b when integer division is employed
'''


def solve(n, m):

    min_moves_needed = (n+1)/2
    ceil_val = (min_moves_needed + m - 1) / m
    moves_needed = ceil_val * m
    return -1 if moves_needed > n else moves_needed


if __name__ == "__main__":

    n, m = map(int, raw_input().split(" "))
    print solve(n, m)
