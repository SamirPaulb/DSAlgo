__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1213/B

Solution: Move from right to left. Keep track of the smallest element seen so far. If the current array's price
is greater than that smaller price, the current price is bad and hence increase the bad prices counter. If not,
update the smallest element value. 
'''


def solve(n, arr):

    min_price_on_right = arr[n-1]
    bad_prices = 0

    for i in xrange(n-2, -1, -1):

        if arr[i] > min_price_on_right:
            bad_prices += 1
        else:
            min_price_on_right = arr[i]

    return bad_prices


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        n = int(raw_input())
        arr = map(int, raw_input().split(" "))
        results.append(solve(n, arr))

    for result in results:
        print result
