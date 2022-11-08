__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/978/B

Solution: Take all groups of xxx and remove 1 from the group. Count these removals and return as the final answer. 
'''


def solve(n, s):

    removals = 0
    for i in xrange(0, n-2):

        if s[i] == 'x' and s[i+1] == 'x' and s[i+2] == 'x':
            removals += 1

    return removals


if __name__ == "__main__":

    n = int(raw_input())
    s = raw_input()
    print solve(n, s)
