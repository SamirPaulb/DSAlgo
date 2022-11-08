__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1234/A

Solution: The idea is to set the new price of each product as the average price, i.e. sum(prices) / n. Since we may not
the sum to always be divisible by n, we take the ceil division in order to avoid any loss of price due to truncation of
fractional part. We use the equivalent formula for ceil (a/b)
'''


def solve(n, prices):

    return (sum(prices) + n - 1) / n


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        n = int(raw_input())
        prices = map(int, raw_input().split(" "))
        results.append(solve(n, prices))

    for result in results:
        print result
