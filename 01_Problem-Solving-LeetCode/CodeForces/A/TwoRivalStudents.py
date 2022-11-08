__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1257/A

Solution: Firstly, the distance between the 2 rival students cannot be more than n-1. That is when they
are on 2 opposite ends of the array. Secondly, to calculate their legit distance after x swaps, we can
get it by getting their current distance abs(a-b) and add x to it which would come from the swaps. 
'''


def solve(n, x, a, b):

    return min(n-1, abs(a - b) + x)


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        n, x, a, b = map(int, raw_input().split(" "))
        results.append(solve(n, x, a, b))

    for result in results:
        print result
