__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/460/A

Solution: Idea is keep two counters, one for days and other for the sock inventory left to wear. Now after m days,
we would have bought socks_left/m more socks, which means Vasya can wear them for socks_left/m days more. That is
how we update the days counter. Now while those socks_left/m days were going on, Vasya procured more socks at 
every mth day in it. But not necessarily socks_left would be completely divisible by m so need to take care of 
remainder as well. That is how we update sock_left counter. Run this till Vasya has socks inventory more than or
equal to m since that is when his stock would be replenished. 
'''


def solve(n, m):

    days = socks_left = n

    while socks_left >= m:

        days += (socks_left/m)
        socks_left = socks_left/m + socks_left % m

    return days


if __name__ == "__main__":

    n, m = map(int, raw_input().split(" "))
    print solve(n, m)
