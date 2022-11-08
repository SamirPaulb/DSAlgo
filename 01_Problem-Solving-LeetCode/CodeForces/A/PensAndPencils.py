__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1244/A

Solution: If we have to take m notes and one stationary item can write n notes, the no. of those stationary items needed
is ceil(m/n) = (m + n - 1) / n. This way we calculate the minimum pens and pencils needed. If their sum is <= k, we return
that as the answer, else it is -1. Note that the question doesn't require minimization but it seems straightforward for
calculation purposes. 
'''


def solve(a, b, c, d, k):

    pens = (a + c - 1) / c
    pencils = (b + d - 1) / d

    return -1 if pens + pencils > k else str(pens) + " " + str(pencils)


if __name__ == "__main__":

    t = int(raw_input())

    for _ in xrange(0, t):
        a, b, c, d, k = map(int, raw_input().split(" "))
        print solve(a, b, c, d, k)
