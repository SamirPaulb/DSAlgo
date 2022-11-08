__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/822/A

Solution: Say A < B. Then A! = 1*2*3....A-1*A. Then B! = 1*2*3....A-1*A*A+1....B-1*B. Since 1*2*3....A-1*A is a factor
of 1*2*3....A-1*A*A+1....B-1*B, we can deduce that the !A would the answer. Therfore, the smaller of the two value's
factorial would be the required GCD.
'''


def solve(a, b):

    f = 1
    for i in xrange(2, min(a, b)+1):
        f *= i

    return f


if __name__ == "__main__":

    a, b = map(int, raw_input().split(" "))
    print solve(a, b)
