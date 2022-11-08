__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/266/B

Solution: Perform the swap operation between a B standing in front of G for all such pairs. This is done in the entire
queue for t times. 
'''


def solve(n, t, s):

    for _ in xrange(0, t):

        i = 0
        while i < n-1:

            if s[i] == 'B' and s[i+1] == 'G':
                s[i] = 'G'
                s[i+1] = 'B'
                i += 2
            else:
                i += 1

    return "".join(s)


if __name__ == "__main__":

    n, t = map(int, raw_input().split(" "))
    s = raw_input()
    print solve(n, t, list(s))
