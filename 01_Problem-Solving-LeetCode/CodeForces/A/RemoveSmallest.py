__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1399/A

Solution: Pretty straightforward question. Sort the array and check if any pair of adjacent elements differ
by more than 1. If so return NO. If all the elements check out, return YES.  
'''


def solve(n, arr):

    arr.sort()

    for i in xrange(1, n):

        if arr[i] - arr[i-1] > 1:
            return "NO"

    return "YES"


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        n = int(raw_input())
        arr = map(int, raw_input().split(" "))
        results.append(solve(n, arr))

    for result in results:
        print result
