__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1303/A

Solution: Remove the leading and trailing zeroes in the string. The remaining string should only contain 1s and the 0s
present should be removed. Hence we count the zeroes in it and return as the answer. 
'''


def solve(s):

    s_stripped = s.strip('0')
    n = len(s_stripped)

    count = 0
    for i in xrange(0, n):
        if s_stripped[i] == '0':
            count += 1

    return count


if __name__ == "__main__":

    t = int(raw_input())

    for _ in xrange(0, t):
        s = raw_input()
        print solve(s)
