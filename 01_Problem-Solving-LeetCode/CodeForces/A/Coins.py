__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1061/A

Solution: Greedily, we start by using the highest denomination coins. If the current coin's denomination is <= required
sum s, we add s/n coins to the total coins used. Further we reduce the the sum s to s % n. We try this calculation from
the highest to lowest denomination coins. 
'''


def solve(n, s):

    coins = 0
    while s > 0:

        if s >= n:
            coins += (s/n)
            s %= n

        n -= 1

    return coins


if __name__ == "__main__":

    n, s = map(int, raw_input().split(" "))
    print solve(n, s)
