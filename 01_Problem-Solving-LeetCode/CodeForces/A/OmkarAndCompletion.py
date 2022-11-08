__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1372/A

Solution: The array composed of same numbers at all indices obeys the constraint. Just that
the number should be <= 1000. So we safely use 1. 
'''


def solve(n):

    result = [1] * n
    return " ".join(str(_) for _ in result)


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        n = int(raw_input())
        results.append(solve(n))

    for result in results:
        print result
