__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1285/A

Solution: Let the count of Ls and Rs be a and b respectively. Hence the possible final positions lie in the range 
[-a, b]. That range has a + b + 1 values. a + b = n since the string only comprises of Ls and Rs. Hence the answer will
always be n+1. 
'''


def solve(n):

    return n + 1


if __name__ == "__main__":

    n = int(raw_input())
    raw_input() # ignore the string
    print solve(n)
