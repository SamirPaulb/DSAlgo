__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/34/B

Solution: As long as the prices are negative, Bob would be interested to buy. Hence we sort the prices and select
the prices that are negative. That sum is what he needs to have (multiplied by -1). 
'''


def solve(n, m, prices):

    prices.sort()

    total = 0
    for i in xrange(0, min(n, m)):
        if prices[i] >= 0:
            break
        total += prices[i]

    return -total


if __name__ == "__main__":

    n, m = map(int, raw_input().split(" "))
    prices = map(int, raw_input().split(" "))
    print solve(n, m, prices)
