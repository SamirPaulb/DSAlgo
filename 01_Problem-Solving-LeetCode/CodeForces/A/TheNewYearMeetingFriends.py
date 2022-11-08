__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/723/A

Solution: Since the movements are in 1D, the options are only to move left or right. We could move to the nearest
spot and hence, moving the left friend to center friend, and right friend to center friend is the optimal strategy.
'''


def solve(arr):

    arr.sort()
    return (arr[1] - arr[0]) + (arr[2] - arr[1])


if __name__ == "__main__":

    arr = map(int, raw_input().split(" "))
    print solve(arr)
