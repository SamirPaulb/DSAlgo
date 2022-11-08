__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1365/A

Solution: We first capture the rows and columns which are already occupied. This is done via two sets (one 
for each dimension). Now the leftover rows to be played for are n - len(row_tracker) and similarly for 
columns. Since the smaller of that value will the one determining the free cells, we use that to calculate
the minimum possible moves. If those moves count is odd, Ashish will play the last move and hence he wins.
Otherwise the winner is Vivek.
'''


def solve(n, m, grid):

    # how many rows are already occupied
    row_tracker = set()
    # how many columns are already occupied
    col_tracker = set()

    for i in xrange(0, n):

        for j in xrange(0, m):

            if grid[i][j] == '1':

                row_tracker.add(i)
                col_tracker.add(j)

    min_moves_possible = min(n - len(row_tracker), m - len(col_tracker))

    # Ashish will play all odd moves and Vivek will even moves
    return "Ashish" if min_moves_possible % 2 == 1 else "Vivek"


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        n, m = map(int, raw_input().split(" "))

        grid = list()
        for _n in xrange(0, n):
            row = raw_input().split(" ")
            grid.append(row)
        results.append(solve(n, m, grid))

    for result in results:
        print result
