__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/996/A

Solution: This the popular coin change problem. We can use the standard quadratic DP solution, but since the coins
are less, we just iterate over them and compute the bills. Since we are minimizing the bills used, we go over the 
coins in decreasing order so that we use the higher dollar value bills to reduce their counts. 
'''


def solve(n):

    coins = [100, 20, 10, 5, 1]

    total_coin_count = 0

    for coin in coins:

        if n >= coin:

            this_coin_count = n/coin
            total_coin_count += this_coin_count
            n -= (this_coin_count * coin)

    return total_coin_count


if __name__ == "__main__":

    n = int(raw_input())
    print solve(n)
