__author__ = 'Devesh Bajpai'

'''
TODO Not all testcases are passing 
https://codeforces.com/problemset/problem/1373/A

Solution: If the customer wants to buy kb + j amount of donuts (k, j are integers), the retail shop would give him
at (kb + j) * a dollars. While, the wholesale shop would give him at (k+1)*c dollars. 

TODO
'''


def solve(a, b, c):

    # when retail shop is cheaper than whole sale shop
    x_retail = 1 if a < c else -1

    # when whole sale shop is cheaper than retail shop
    x_wholesale = b if a * b > c else -1

    return x_retail, x_wholesale


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        a, b, c = map(int, raw_input().split(" "))
        results.append(solve(a, b, c))

    for result in results:
        print result