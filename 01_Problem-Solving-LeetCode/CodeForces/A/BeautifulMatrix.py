__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/263/A

Solution: Idea is to find the cell containing 1 and then find the Manhattan distance from the center of the grid (that
would be 2,2 cell).
'''


def solve(matrix):

    i = r = c = 0
    isOneFound = False
    # find the cell containing 1
    while i < 5 and not isOneFound:
        j = 0
        while j < 5 and not isOneFound:

            if matrix[i][j] == '1':
                r = i
                c = j
                isOneFound = True

            j += 1

        i += 1

    # find Manhattan distance of (r,c) from (0,0)
    return abs(r - 2) + abs(c - 2)


if __name__ == "__main__":

    matrix = list()
    for _ in xrange(0, 5):
        matrix.append(raw_input().split(" "))

    print solve(matrix)
