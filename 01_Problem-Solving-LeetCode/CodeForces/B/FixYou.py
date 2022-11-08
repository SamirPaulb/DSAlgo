__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1391/B

Solution: All cells eventually drain the luggage to either last row or last column so as to reach the 
destination counter. Therefore, any 'D' in the last row and any 'R' in the last column will force the
luggage go out of the grid thereby not reaching the counter. We need to count these occurrences and return
it as the answer. 
'''


def solve(n, m, grid):

    to_be_changed = 0

    # count all D in the last row
    for j in xrange(0, m):
        if grid[n-1][j] == 'D':
            to_be_changed += 1

    # count all R in the last column
    for i in xrange(0, n):
        if grid[i][m-1] == 'R':
            to_be_changed += 1

    return to_be_changed


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        n, m = map(int, raw_input().split(" "))
        grid = list()
        for __ in xrange(0, n):
            row = raw_input()
            grid.append(row)
        results.append(solve(n, m, grid))

    for result in results:
        print result
