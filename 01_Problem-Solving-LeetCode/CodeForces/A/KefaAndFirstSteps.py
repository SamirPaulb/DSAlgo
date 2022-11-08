__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/580/A

Solution: Iterate over the list and check for each element if its >= its left neighbor. If so, it is part of a non-
decreasing sub-segment. Therefore, increase the counter of length, otherwise reset it to 1. Keep a variable to track
the max length of that sub-segment seen so far which is the final answer. 
'''


def solve(n , arr):

    length = 1
    max_length = 1

    for i in xrange(1, n):

        if arr[i] >= arr[i-1]:
            length += 1
        else:
            length = 1

        max_length = max(max_length, length)

    return max_length


if __name__ == "__main__":

    n = int(raw_input())
    arr = map(int, raw_input().split(" "))
    print solve(n, arr)
