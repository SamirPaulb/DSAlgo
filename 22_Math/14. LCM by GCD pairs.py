# https://codeforces.com/contest/1717/problem/A
'''
How pairs of integers (a,b) exist, where 1 ≤ a, b ≤ n, for which lcm(a,b) / gcd(a,b) ≤ 3.

For n=1 there is exactly one pair of numbers — (1,1) and it fits.
For n=2, there are only 4 pairs — (1,1), (1,2), (2,1), (2,2) and they all fit.
For n=3, all 9 pair are suitable, except (2,3) and (3,2), since their lcm is 6, and gcd is 1, which doesn't fit the condition.
'''


# Intuition: 
''' 
   lcm(a,b) * gcd(a,b) = a*b
=> l * g = a*b
if l/g = x => l = gx
=> gx * g = a*b
=> x = a*b / g*g
=> l/g = a*b / g*g

for a = b => l/g = 1        # count = n
for a = 2b => l/g = 2       # coutn = floor(n / 2)
for a = 3b => l/g = 3       # count = floor(n / 3)
'''

import math

def solve(n):
    return n + (2 * math.floor(n/2)) + (2 * math.floor(n/3))   


n = int(input())
print(solve(n))
