__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1359/B

Solution: Since we can only the tiles in row-wise fashion, there are 2 options if we encounter a white square. 
If it has an adjacent white square, we pick the smaller of twice of 1x1 tile or once of 1x2 tile. If the adjacent
neighbor doesn't exist, there is only one option to pick one 1x1 tile. Keep adding these costs in a variable 
which is the final answer. 
'''


def solve(n, m, x, y, grid):

    cost = 0

    i = 0
    while i < n:

        j = 0
        while j < m:

            if grid[i][j] == '.':

                if j + 1 < m and grid[i][j+1] == '.':
                    cost += min(2*x, y)
                    j += 1 # advance the pointer since adjacent white cell has also been addressed
                else:
                    cost += x

            j += 1
        i += 1

    return cost


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        n, m, x, y = map(int, raw_input().split(" "))
        grid = list()
        for _n in xrange(0, n):
            row = raw_input()
            grid.append(row)
        results.append(solve(n, m, x, y, grid))

    for result in results:
        print result
