__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1269/A

Solution: Since we need the 2 numbers to be composite, the easiest way is to take 2 consecutive composite
numbers and return the multiple of n of them. Say we chose 14 and 15.

Then 15n - 14n = n and that solves the problem. 
'''


def solve(n):

    return str(15*n) + " " + str(14*n)


if __name__ == "__main__":

    n = int(raw_input())
    print solve(n)
