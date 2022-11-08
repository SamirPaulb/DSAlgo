__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1093/A

Solution: Since we can output an number of moves that can provide the required n, we do thinking we get all 7s till the
required remaining number is < 7. So that requires ceil(n/7) moves. 
'''


def solve(n):

    return (n + 6) / 7


if __name__ == "__main__":

    t = int(raw_input())

    for _ in xrange(0, t):
        n = int(raw_input())
        print solve(n)
