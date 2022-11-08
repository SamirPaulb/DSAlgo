__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1167/A

Solution: From the first occurrence of 8 in the given string s, we should have at least 10 characters. Say that 8 exists
on ith index. Then n - 1 - i + 1 = n - i would give the length of the longest string starting with 8. That should be
at least 11 characters. The extra ones (>11) can be deleted by the operations.
'''


def solve(n, s):

    i = 0
    while i < n:
        if s[i] == '8':
            break
        i += 1

    return "YES" if n - i >= 11 else "NO"


if __name__ == "__main__":

    t = int(raw_input())

    for _ in xrange(0, t):
        n = int(raw_input())
        s = raw_input()
        print solve(n, s)
