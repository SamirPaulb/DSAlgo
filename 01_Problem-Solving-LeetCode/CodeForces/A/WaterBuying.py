__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1118/A

Solution: Since we need to do apples to apples comparison, we calculate the minimum cost of buying 2l of water via two 1l
bottles or a 2l bottle. That when multiplied to n/2 gives the money needed to get the water when n is even. 
In the case when n is odd, we need to accommodate that and add 'a' to the above calculated cost. 
'''


def solve(n, a, b):

    min_cost_2l = min(a * 2, b)
    cost = (n / 2) * min_cost_2l
    if n % 2 != 0:
        cost += a
    return cost


if __name__ == "__main__":

    t = int(raw_input())

    for _ in xrange(0, t):
        n, a, b = map(int, raw_input().split(" "))
        print solve(n, a, b)
