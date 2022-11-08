__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/935/A

Solution: To have equal division of the workers in teams, we need to employ division. At the
minimum, we can have 1 team having n-1 worker, and at the max, we can have n/2 teams each of
1 worker. In the middle of those extremes, we need to find what other ways can we obtain equal
division. Hence, we need to find the factors of n. 
'''


def solve(n):

    factors = 1

    for f in xrange(2, (n/2)+1):

        if n % f == 0:
            factors += 1

    return factors


if __name__ == "__main__":

    n = int(raw_input())
    print solve(n)
