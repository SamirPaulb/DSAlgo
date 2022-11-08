__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1311/A

Solution: The solution can be broken down in set of condition for the difference b and a. 

if zero i.e. b == a, no action needed

if positive i.e. b > a:
    if even:
        add the odd number (a+1) and then reduce by 1: hence 2 operations
    if odd:
        add the odd number (a): hence 1 operation

if negative i.e. b < a:
    if even:
        reduce by even number a: hence 1 operation
    if odd:
        increase by 1 and then reduce by a+1: hence 2 operation
'''


def solve(a, b):

    diff = b - a

    if diff == 0:
        return diff
    elif diff > 0:
        if diff % 2 == 0:
            return 2
        else:
            return 1
    else:
        if diff % 2 == 0:
            return 1
        else:
            return 2


if __name__ == "__main__":

    t = int(raw_input())
    for _ in xrange(0, t):
        a, b = map(int, raw_input().split(" "))
        print solve(a, b)
