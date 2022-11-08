__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/734/A

Solution: Just counters for each of the two people and if checks to return the string appropriately.
'''


def solve(n, s):

    anton = danik = 0

    for i in xrange(0, n):

        if s[i] == 'D':
            danik += 1
        else:
            anton += 1

    return "Anton" if anton > danik else "Danik" if anton < danik  else "Friendship"


if __name__ == "__main__":

    n = int(raw_input())
    s = raw_input()
    print solve(n, s)
