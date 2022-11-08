__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/939/A

Solution: The problem is the classic DFS traversal problem but the depth should be 3 and should end at
the source. Hence f(f(f(i))) = i for the love triangle to exist. 
'''


def solve(n, arr):

    for i in xrange(0, n):
        # -1 for converting 1 to 0 indexing
        f1 = arr[i]
        f2 = arr[f1-1]
        f3 = arr[f2-1]
        if f3-1 == i:
            return "YES"

    return "NO"


if __name__ == "__main__":

    n = int(raw_input())
    arr = map(int, raw_input().split(" "))
    print solve(n, arr)
