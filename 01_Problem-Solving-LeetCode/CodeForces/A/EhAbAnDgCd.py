__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/contest/1325/problem/A

Solution: We need to make use properties of number 1 here. GCD(1, t) will always be 1 and LCM(1, t)
will always be t. Hence if 1 + t = x, t = x - 1. So a would 1 and b would be x-1.
'''


def solve(x):

    return str(1) + " " + str(x - 1)


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        x = int(raw_input())
        results.append(solve(x))

    for result in results:
        print result
