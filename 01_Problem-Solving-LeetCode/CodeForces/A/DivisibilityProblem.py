__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1328/A

Solution: Direct application of ceil of division. When a/b is evaluated, the quotient may be
a floating point. That means b does not completely divide a. For that, we need to round up
the quotient since we are only allowed addition of 1. Now the ceil factor of the division and
the b are multiplied to get the divisible multiple of a. We need to return the difference of 
this value and current a. 

We employ the ceil equivalent rather than using library function here. 
'''


def solve(a, b):

    ceil_factor = (a + b - 1) / b

    return (b * ceil_factor) - a


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        a, b = map(int, raw_input().split(" "))
        results.append(solve(a, b))

    for result in results:
        print result
