__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1343/A

Solution: If calculate the sum of the wrappers, it forms a GP:

2^0 * x + 2^1 * x + ...... 2^(k-1) * x = n

Applying the GP sum we get:

x * ((2^k - 1) / (2 - 1)) = n

x * (2^k - 1) = n

x  = n / (2^k - 1)

Hence n should be completely divisible by denominator (2^k - 1) to get an integer value of x. We iterate over values of
k starting from 2 and return the value  n / (2^k - 1) when n is divisible by (2^k - 1)
'''

import math


def solve(n):

    k = 2

    while True:

        denominator = math.pow(2, k) - 1

        if n % denominator == 0:
            return int(n / denominator)

        k += 1


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        n = int(raw_input())
        results.append(solve(n))

    for result in results:
        print result

