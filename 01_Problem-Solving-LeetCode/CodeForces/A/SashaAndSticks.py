__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/832/A

Solution: We need to calculate the number of rounds of game that happen. That is n / k. If that is even, Sasha's opponent
will win, otherwise he wins.
'''


def solve(n, k):

    rounds = n / k

    if rounds % 2 != 0:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":

    n, k = map(int, raw_input().split(" "))
    print solve(n, k)
