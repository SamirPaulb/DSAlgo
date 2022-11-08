__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1307/A

Solution: We iterate till we have enough days and piles to work on. For a given pile, 
if it doesn't have any hayes, we omit it and move to the next pile. If not, we use i days 
to transfer 1 hay from it to first pile, also updating the source and destination piles.

Time Complexity: O(max(d, n))  
'''


def solve(n, d, arr):

    i = 1
    while d > 0 and i < n:

        if arr[i] <= 0 or d < i:
            i += 1
        elif d >= i:
            d -= i
            arr[0] += 1
            arr[i] -= 1

    return arr[0]


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        n, d = map(int, raw_input().split(" "))
        arr = map(int, raw_input().split(" "))
        results.append(solve(n, d, arr))

    for result in results:
        print result
