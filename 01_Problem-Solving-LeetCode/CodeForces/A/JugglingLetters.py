__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1397/A

Solution: Build a joint character frequency map of the strings. The frequency of each character must be divisible by n
to make sure the moving of characters amongst them can eventually equalize them.
'''


def solve(n, s_arr):

    char_freq = {}

    for s in s_arr:
        for c in s:
            if c in char_freq:
                char_freq[c] += 1
            else:
                char_freq[c] = 1

    for f in char_freq.values():
        if f % n != 0:
            return "NO"

    return "YES"


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        n = int(raw_input())
        s_arr = list()
        for __ in xrange(0, n):
            s = raw_input()
            s_arr.append(s)
        results.append(solve(n, s_arr))

    for result in results:
        print result
