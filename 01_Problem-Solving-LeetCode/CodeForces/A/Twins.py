__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/160/A

Solution: Find the total of all coins so that we know the half of the total value which you need to exceed. Now sort the
coins in reverse order and iterate over them. In each round, add the coin to your total and break the iteration if your
total is greater than the half. 
'''


def solve(n, coins):

    total = 0
    for coin in coins:
        total += coin

    coins.sort(reverse=True)

    yourTotal = 0
    yourCoinsCount = 0
    halfTotal = total/2
    for coin in coins:

        if yourTotal > halfTotal:
            break

        yourTotal += coin
        yourCoinsCount += 1

    return yourCoinsCount


if __name__ == "__main__":

    n = int(raw_input())
    coins = map(int, raw_input().split(" "))
    print solve(n, coins)
