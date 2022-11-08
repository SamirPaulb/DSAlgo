__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/contest/1324/problem/C

Solution: The frog jumps from the outside of the array (from left) and aims to reach the outside
of the array (on the right). Any of the 'L' cells disrupt the movement towards the goal since they
bring the frog back. Instead, the frog should try to get to the 'R' cells. In order to make the best
use of them, we calculate the difference between consecutive 'R' cells and consider the maximum of it.
That seems easy but there are test cases where we need to handle special cases when there are no 'R'
cells, or only 1 'R' cell; to cleanly handle that, we add a 'S' (source) and 'D' (destination) cells
to the string.  
'''


def solve(s):

    max_diff = 0
    prev_idx = -1

    s = s + 'D' # destination
    s = 'S' + s  # source

    n = len(s)

    for i in xrange(0, n):

        if s[i] == 'S':
            prev_idx = i
        elif s[i] == 'R':
            max_diff = max(max_diff, i - prev_idx)
            prev_idx = i
        elif s[i] == 'D':
            max_diff = max(max_diff, i - prev_idx)

    return max_diff


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        s = raw_input()
        results.append(solve(s))

    for result in results:
        print result
