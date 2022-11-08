__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1294/A

Solution: Since we can only add coins, we will firstly try to equalize the three sets to be equal to the max initial 
value of coins with one person. Hence n should have enough coins to provide that. The remaining coins in n should be
divided equally and hence should be divisble by 3. Validate these two conditions and return the result accordingly. 
'''


def solve(a, b, c, n):

    initial_max = max(a, b, c)

    needed_to_equalize = (initial_max - a) + (initial_max - b) + (initial_max - c)

    n -= needed_to_equalize

    return "YES" if n >= 0 and n % 3 == 0 else "NO"


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        a, b, c, n = map(int, raw_input().split(" "))
        results.append(solve(a, b, c, n))

    for result in results:
        print result
